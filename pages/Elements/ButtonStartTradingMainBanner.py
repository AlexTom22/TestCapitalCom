"""
-*- coding: utf-8 -*-
@Time    : 2023/04/19 23:50
@Author  : Suleyman Alirzaev
"""
from datetime import datetime
import pytest
import allure
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import MainBannerLocators
from selenium.common.exceptions import ElementClickInterceptedException


class MainBannerStartTrading(BasePage):

    def full_test_with_tpi(self, d, cur_language, cur_country, cur_role, cur_item_link):

        self.arrange_(d, cur_item_link)
        self.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link)

    def full_test(self, d, cur_language, cur_country, cur_role, page_url):

        self.arrange_(d, page_url)

        self.element_click()

        test_element = AssertClass(d, page_url)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(
                    d, cur_language, page_url
                )
            case "Reg/NoAuth":
                test_element.assert_login(
                    d, cur_language, page_url
                )
            case "Auth":
                test_element.assert_trading_platform_v4(
                    d, page_url
                )

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v0")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        button_list = self.browser.find_elements(*MainBannerLocators.BUTTON_START_TRADING)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_START_TRADING is not present on the page!")
            del button_list
            pytest.skip("Checking element 'BUTTON_START_TRADING on the main banner' is not on this page")

        print(f"{datetime.now()}   BUTTON_START_TRADING scroll =>")
        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});', button_list[0]
        )

        print(f"{datetime.now()}   BUTTON_START_TRADING is visible? =>")
        if self.element_is_visible(MainBannerLocators.BUTTON_START_TRADING):
            print(f"{datetime.now()}   => BUTTON_START_TRADING is visible on the page!")
        else:
            print(f"{datetime.now()}   => BUTTON_START_TRADING is not visible on the page!")
            pytest.fail("Bug! Checking element 'BUTTON_START_TRADING on main banner' is present on this page, "
                        "but not visible")

    @allure.step("Click button [Start Trading] on Main banner")
    def element_click(self):
        print(f"\n{datetime.now()}   2. Act_v0")
        print(f"{datetime.now()}   Start Click button [Start Trading] =>")
        button_list = self.browser.find_elements(*MainBannerLocators.BUTTON_START_TRADING)

        print(f"{datetime.now()}   BUTTON_START_TRADING is clickable? =>")
        time_out = 3
        if not self.element_is_clickable(button_list[0], time_out):
            print(f"{datetime.now()}   => BUTTON_START_TRADING is not clickable after {time_out} sec. Stop TC>")
            pytest.fail(f"BUTTON_START_TRADING is not clickable after {time_out} sec.")

        print(f"{datetime.now()}   BUTTON_START_TRADING click =>")
        try:
            button_list[0].click()
            print(f"{datetime.now()}   => BUTTON_START_TRADING clicked")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => BUTTON_START_TRADING not clicked")
            print(f"{datetime.now()}   'Signup' or 'Login' form is automatically opened")

            page_ = SignupLogin(self.browser)
            if page_.close_signup_form():
                pass
            elif page_.close_login_form():
                pass
            elif page_.close_signup_page():
                pass
            else:
                page_.close_login_page()

            del page_
            button_list[0].click()

        del button_list
        return True
