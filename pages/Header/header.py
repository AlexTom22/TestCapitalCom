"""
-*- coding: utf-8 -*-
@Time    : 2023/02/08 10:00
@Author  : Alexander Tomelo
"""

import allure
from selenium.webdriver import ActionChains
# from selenium.common.exceptions import (
#     ElementClickInterceptedException,
#     ElementNotInteractableException
# )
from datetime import datetime
from pages.base_page import BasePage
# from pages.Signup_login.signup_login import SignupLogin
from pages.Header.header_locators import HeaderElementLocators
from pages.My_account.my_account_locators import MyAccountLocator
# from .src.src import HeaderSrc


class Header(BasePage):

    @allure.step("Click button [My account]")
    def header_button_my_account_click(self):
        print(f"{datetime.now()}   1. BUTTON_MY_ACCOUNT is present? =>")
        button_list = self.browser.find_elements(*HeaderElementLocators.BUTTON_MY_ACCOUNT)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_MY_ACCOUNT is not present on this page")
            del button_list
            return False

        print(f"{datetime.now()}   => BUTTON_MY_ACCOUNT is present on this page")
        button_list = self.browser.find_elements(*HeaderElementLocators.BUTTON_MY_ACCOUNT)
        ActionChains(self.browser) \
            .move_to_element(button_list[0]) \
            .pause(0.5) \
            .perform()
        print(f"{datetime.now()}   => Move to BUTTON_MY_ACCOUNT")

        print(f"{datetime.now()}   2. BUTTON_MY_ACCOUNT is clickable? =>")
        button_list = self.browser.find_elements(*HeaderElementLocators.BUTTON_MY_ACCOUNT)
        if not self.element_is_clickable(button_list[0], 10):
            print("Button [My account] is not clickable!")

        print(f"{datetime.now()}   => BUTTON_MY_ACCOUNT is clickable. Click =>")
        button_list = self.browser.find_elements(*HeaderElementLocators.BUTTON_MY_ACCOUNT)
        ActionChains(self.browser) \
            .click(button_list[0]) \
            .perform()

        if not self.element_is_visible(MyAccountLocator.LOGOUT, 10):
            print(f"{datetime.now()}   => User panel [My account] not opened")
            del button_list
            return False
        print(f"{datetime.now()}   => User panel [My account] is opened")

        del button_list
        return True
