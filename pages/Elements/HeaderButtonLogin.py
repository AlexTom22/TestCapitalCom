"""
-*- coding: utf-8 -*-
@Time    : 2023/04/14 08:30
@Author  : Alexander Tomelo
"""
from datetime import datetime
import pytest
import allure
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.testing_elements_locators import HeaderButtonLoginLocators
from selenium.common.exceptions import ElementClickInterceptedException


class HeaderButtonLogin(BasePage):

    def arrange_(self, d, cur_role, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if cur_role == "Auth":
            pytest.skip('This test not for "Auth" role')

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Is visible BUTTON_LOGIN? =>")
        if self.element_is_visible(HeaderButtonLoginLocators.BUTTON_LOGIN):
            print(f"{datetime.now()}   => BUTTON_LOGIN is visible on the page!")
        else:
            print(f"{datetime.now()}   => BUTTON_LOGIN is not visible on the page!")
            pytest.skip("Checking element is not on this page")

    @allure.step("Click [Log In] button")
    def element_click(self):
        print(f"\n{datetime.now()}   2. Act")
        print(f"{datetime.now()}   Start Click button [Log in] =>")
        button_list = self.browser.find_elements(*HeaderButtonLoginLocators.BUTTON_LOGIN)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_LOGIN is not present on the page!")
            del button_list
            return False

        print(f"{datetime.now()}   BUTTON_LOGIN scroll =>")
        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )

        print(f"{datetime.now()}   Is BUTTON_LOGIN clickable? =>")
        if not self.element_is_clickable(button_list[0], 5):
            print(f"{datetime.now()}   => BUTTON_LOGIN is not clickable")
            return False
        print(f"{datetime.now()}   => BUTTON_LOGIN is clickable")

        print(f"{datetime.now()}   BUTTON_LOGIN click =>")
        try:
            button_list[0].click()
            print(f"{datetime.now()}   => BUTTON_LOGIN is clicked!")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   'Signup' or 'Login' form is automatically opened")

            page_ = SignupLogin(self.browser)
            if page_.close_login_form():
                pass
            else:
                page_.close_login_page()

            del page_
            button_list[0].click()

        del button_list
        return True
