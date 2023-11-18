"""
-*- coding: utf-8 -*-
@Time    : 2023/04/20 22:00
@Author  : Suleyman Alirzaev
"""
from datetime import datetime
import pytest
import allure
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.testing_elements_locators import MainBannerLocators
from selenium.common.exceptions import ElementClickInterceptedException


class MainBannerTryDemo(BasePage):

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v0")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   BUTTON_TRY_DEMO is visible? =>")
        if self.element_is_visible(MainBannerLocators.BUTTON_TRY_DEMO):
            print(f"{datetime.now()}   => BUTTON_TRY_DEMO is visible on the page!")
        else:
            print(f"{datetime.now()}   => BUTTON_TRY_DEMO is not visible on the page!")
            pytest.skip("Checking element is not on this page")

    @allure.step("Click button [Try demo] on Main banner")
    def element_click(self):
        print(f"\n{datetime.now()}   2. Act_v0")
        print(f"{datetime.now()}   BUTTON_TRY_DEMO is present? =>")
        button_list = self.browser.find_elements(*MainBannerLocators.BUTTON_TRY_DEMO)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_TRY_DEMO is not present on the page!")
            del button_list
            return False
        print(f"{datetime.now()}   => BUTTON_TRY_DEMO is present on the page!")

        print(f"{datetime.now()}   BUTTON_TRY_DEMO scroll =>")

        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )

        self.element_is_clickable(button_list[0], 5)

        try:
            # button_list[0].click()
            self.browser.execute_script("arguments[0].click();", button_list[0])
            print(f"{datetime.now()}   => BUTTON_TRY_DEMO clicked!")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => BUTTON_TRY_DEMO NOT CLICKED")
            print(f"{datetime.now()}   'Sign up' form or page is auto opened")

            page_ = SignupLogin(self.browser)
            if page_.close_signup_form():
                pass
            else:
                page_.close_signup_page()

            # button_list[0].click()
            self.browser.execute_script("arguments[0].click();", button_list[0])
            del page_

        del button_list
        return True
