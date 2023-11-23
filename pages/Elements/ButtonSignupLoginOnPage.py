"""
-*- coding: utf-8 -*-
@Time    : 2023/04/29 00:30
@Author  : Suleyman Alirzaev
"""
from datetime import datetime
import pytest
import allure
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.testing_elements_locators import ButtonsOnPageLocators
from selenium.common.exceptions import (ElementClickInterceptedException,
                                        NoSuchElementException)
from pages.Elements.AssertClass import AssertClass
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


class PageSignUpLogin(BasePage):

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Is visible BUTTON_SIGNUP_LOGIN? =>")
        # if self.element_is_visible(ButtonsOnPageLocators.BUTTON_SIGNUP_LOGIN):
        try:
            if self.browser.find_element(*ButtonsOnPageLocators.BUTTON_SIGNUP_LOGIN):
                print(f"{datetime.now()}   => BUTTON_SIGNUP_LOGIN is visible on the page!")
        except NoSuchElementException:
            print(f"{datetime.now()}   => BUTTON_SIGNUP_LOGIN is not visible on the page!")
            pytest.skip("Checking element is not on this page")

    @allure.step("Click button BUTTON_SIGNUP_LOGIN")
    def element_click(self, cur_item_link, cur_language, cur_role):
        print(f"\n{datetime.now()}   2. Act_v0")
        print(f"{datetime.now()}   Start Click button BUTTON_SIGNUP_LOGIN =>")
        button_list = self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_SIGNUP_LOGIN)
        if len(button_list) >= 1:
            self.click__button(len(button_list), cur_item_link, cur_language, cur_role)
        else:
            print(f"{datetime.now()}   => BUTTON_SIGNUP_LOGIN is not present on the page!")
            del button_list
            pytest.skip("Checking element is not present on this page")

    def click__button(self, times, cur_item_link, cur_language, cur_role):
        # wait = WebDriverWait(self.browser, 30)
        for i in range(times):
            button_list = self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_SIGNUP_LOGIN)
            print(f"{datetime.now()}   BUTTON_SIGNUP_LOGIN#{i + 1} scroll =>")
            # Наводим на тестовый элемент, чтобы кнопка могла корректно отработать нажатие
            # hover = ActionChains(self.browser).move_to_element(button_list[i])

            print(f"{datetime.now()}   BUTTON_SIGNUP_LOGIN#{i + 1} scroll =>")
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                button_list[i]
            )
            print(f"{datetime.now()}   Is BUTTON_SIGNUP_LOGIN#{i + 1} clickable? =>")
            if self.element_is_clickable(button_list[i], 10):
                print(f"{datetime.now()}   => BUTTON_SIGNUP_LOGIN#{i + 1} is clickable")
            # wait.until(EC.element_to_be_clickable(button_list[i]))

            print(f"{datetime.now()}   BUTTON_SIGNUP_LOGIN#{i + 1} click =>")
            try:
                # hover.perform()
                # button_list[i].click()
                self.browser.execute_script("arguments[0].click();", button_list[i])
                print(f"{datetime.now()}   => BUTTON_SIGNUP_LOGIN#{i + 1} clicked!")
                # self.browser.back()
                test_element = AssertClass(self.browser, cur_item_link)
                # test_element.assert_signup(self.browser, cur_language, cur_role, cur_item_link)
                match cur_role:
                    case "NoReg":
                        test_element.assert_signup(self.browser, cur_language, cur_item_link)
                    case "Reg/NoAuth":
                        # test_element.assert_login(self.browser, cur_language, cur_item_link)
                        match i:
                            case 1:
                                test_element.assert_login(self.browser, cur_language, cur_item_link)
                            case 2:
                                test_element.assert_signup(self.browser, cur_language, cur_item_link)
                    case "Auth":
                        test_element.assert_trading_platform_v3(self.browser)
                self.browser.get(cur_item_link)
            # except Exception as e:
            #     print(f"EXC_IS: {e}")
            except ElementClickInterceptedException:
                print(f"{datetime.now()}   'Signup' or 'Login' form is automatically opened")
                page_ = SignupLogin(self.browser)
                if page_.close_signup_page():
                    pass
                else:
                    page_.close_signup_page()
                del page_
            del button_list

        return True
