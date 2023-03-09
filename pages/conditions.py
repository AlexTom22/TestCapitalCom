import time
import allure
from datetime import datetime

import pytest

from pages.base_page import BasePage
from pages.Header.header import Header
from pages.Signup_login.signup_login_locators import (
    SignupFormLocators,
    LoginFormLocators,
)

url_language = "?"
url_license = "?"
test_link = "?"
prev_role = "?"
prev_license = "?"
prev_language = "?"


class Conditions(BasePage):
    """This class used as a base class for other page classes that represent specific pages on a website"""

    @allure.step("Set preconditions")
    def preconditions(self, d, host, end_point, login, password, cur_role, cur_language, cur_license):

        global url_language
        global url_license
        global test_link
        global prev_language
        global prev_license
        global prev_role

        # устанавливаем Язык, если не соответствует предыдущему
        if cur_language != prev_language:
            d.delete_all_cookies()
            if cur_language != "":
                url_language = f"{host}/{cur_language}{end_point}"
            elif cur_language == "":
                url_language = f"{host}{end_point}"
            test_link = url_language
            self.browser = d
            self.link = url_language
            self.open_page()
            prev_language = cur_language

        if cur_license != prev_license:
            if cur_language != "":
                url_license = f"{host}/{cur_language}{end_point}/?license={cur_license}"
            elif cur_language == "":
                url_license = f"{host}{end_point}/?license={cur_license}"
            self.browser = d
            self.link = url_license
            self.open_page()
            prev_license = cur_license

        # Настраиваем в соответствии с параметром "Роль"
        if cur_role != prev_role:
            if cur_role == "NoReg":
                self.browser = d
                self.link = test_link
                self.open_page()
                self.button_reject_all_cookies_click()
                prev_role = cur_role
            elif cur_role == "Reg_NoAuth":
                pytest.skip("Test for 'Reg_noAuth' role not yet written")
                self.to_do_registration(d, login, password)
                prev_role = cur_role
            elif cur_role == "Auth":
                pytest.skip("Test for 'Auth' role not yet written")
                self.browser = d
                self.link = test_link
                self.open_page()
                time.sleep(1)
                # page.button_accept_all_cookies_click()

                self.to_do_authorization(d, login, password)
                self.check_current_page_is("https://capital.com/trading/platform/")
                prev_role = cur_role
                d.back()
            else:
                print(f"Задан не существующий параметр роли - '{cur_role}'.\nТест будет выполнять с ролью 'NoReg'")
                prev_role = "NoReg"

        return test_link

    # регистрация пользователя
    def to_do_registration(self, d, login, password):
        """Register user on the login page.

        Args:
            d: web_driver
            login: username user
            password: password user
        """
        assert login != "", "Регистрация невозможна. Не указан e-mail"
        assert password != "", "Регистрация невозможна. Не указан пароль"
        # нажать в хедере на кнопку "Log in"
        # page = HeaderElement(d, test_link)
        # page.open_page()
        page = Header(d, test_link)
        page.header_button_login_click()
        # проверить, открылась ли форма "Log in"
        # перейти на форму "Signup", нажав кнопку "SignUp"
        # проверить, открылась ли форма "SignUp"
        # ввести логин, вести пароль, нажать подтвердить

    # авторизация пользователя
    @allure.step(f"{datetime.now()}. Checking if the page has a Header.")
    def to_do_authorization(self, d, link, login, password):

        assert login != "", "Авторизация невозможна. Не указан e-mail"
        assert password != "", "Авторизация невозможна. Не указан пароль"
        # нажать в хедере на кнопку "Log in"
        page = Header(d, link)
        page.header_button_login_click()

        # User's name is passed to the text element on the login page
        page.send_keys(login, *LoginFormLocators.LOGIN_INPUT_EMAIL)
        # Password is passed to the text element on the login page
        page.send_keys(password, *LoginFormLocators.LOGIN_INPUT_PASSWORD)
        page.click_button(*LoginFormLocators.LOGIN_CONTINUE)
        time.sleep(2)
