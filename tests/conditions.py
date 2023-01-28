import time
import allure
from datetime import datetime
from capital.base_page import BasePage
from capital.header import Header
from capital.capital_locators import (
    SignupLoginFormLocators,
)


class Conditions:
    """This class used as a base class for other page classes that represent specific pages on a website"""

    def __init__(self, host, end_point=""):
        """Initializes the object.

        Args:
            host: Start page URL
            end_point: End Point
        """
        self.host = host
        self.end_point = end_point
        # self.url_language = "?"
        # self.url_locense = "?"
        self.test_link = "?"
        self.prev_role = "?"
        self.prev_license = "?"
        self.prev_language = "?"

    @allure.step("Set preconditions")
    def preconditions(self, d, login, password, role, language, license):

        url_language = None
        url_license = None

        # устанавливаем Язык, если не соответствует предыдущему
        if language != self.prev_language:
            if language != "":
                url_language = f"{self.host}/{language}{self.end_point}"
            elif language == "":
                url_language = f"{self.host}{self.end_point}"
            self.test_link = url_language
            page = BasePage(d, url_language)
            page.open_page()
            self.prev_language = language

        if license != self.prev_license:
            if language != "":
                url_license = f"{self.host}/{language}{self.end_point}?license={license}"
            elif language == "":
                url_license = f"{self.host}{self.end_point}?license={license}"
            page = BasePage(d, url_license)
            page.open_page()
            self.prev_license = license

        # Настраиваем в соответствии с параметром "Роль"
        if role != self.prev_role:
            if role == "NoReg":
                page = BasePage(d, self.test_link)
                page.open_page()
                time.sleep(1)
                d.delete_all_cookies()
                page.button_reject_all_cookies_click()
                pass
            elif role == "Reg_NoAuth":
                self.to_do_registration(d, login, password)
            elif role == "Auth":
                page = BasePage(d, self.test_link)
                page.open_page()
                time.sleep(1)
                d.delete_all_cookies()
                page.button_accept_all_cookies_click()

                self.to_do_authorization(d, login, password)
                page.check_current_page_is("https://capital.com/trading/platform/")
                self.prev_role = "Auth"
                d.back()
            else:
                print(f"Задан не существующий параметр роли - '{role}'.\nТест будет выполнять с ролью 'NoReg'")
                self.prev_role = "NoReg"

        return self.test_link

    # регистрация пользователя
    def to_do_registration(self, d, login, password):
        """Register user on the login page.

        Args:
            login: username user
            password: password user
        """
        assert login != "", "Регистрация невозможна. Не указан e-mail"
        assert password != "", "Регистрация невозможна. Не указан пароль"
        # нажать в хедере на кнопку "Log in"
        # page = HeaderElement(d, test_link)
        # page.open_page()
        page = Header(d, self.test_link)
        page.click_button_login_on_header()
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
        page.click_button_login_on_header()

        # User's name is passed to the text element on the login page
        page.send_keys(login, *SignupLoginFormLocators.LOGIN_INPUT_USERNAME)
        # Password is passed to the text element on the login page
        page.send_keys(password, *SignupLoginFormLocators.LOGIN_INPUT_PASSWORD)
        page.click_button(*SignupLoginFormLocators.LOGIN_SUBMIT_BTN_LOCATOR)
        time.sleep(2)
