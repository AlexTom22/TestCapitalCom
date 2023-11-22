"""
-*- coding: utf-8 -*-
@Time    : 2023/11/07 18:00
@Author  : Mike Taran
"""
from datetime import datetime
import pytest
import allure
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from selenium.common.exceptions import ElementClickInterceptedException
from pages.Elements.testing_elements_locators import ButtonOnHorizontalBannerLocators, ButtonOnVerticalBannerLocators
from src.src import CapitalComPageSrc


class ButtonOnVerticalBanner(BasePage):

    def arrange_0(self, cur_item_link=CapitalComPageSrc.URL):
        print(f"\n{datetime.now()}   1. Arrange_")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

    def arrange_(self, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   BUTTON_ON_VER_BANNER is visible? =>")
        if self.element_is_visible(ButtonOnVerticalBannerLocators.BUTTON_ON_VER_BANNER):
            print(f"{datetime.now()}   => BUTTON_ON_VER_BANNER is visible on the page!")
            return True
        else:
            print(f"{datetime.now()}   => BUTTON_ON_VER_BANNER is not visible on the page!")
            pytest.skip("Checking element is not present on this page")

    @allure.step("Click button [BUTTON_ON_VER_BANNER]")
    def element_click(self):
        print(f"\n{datetime.now()}   2. Act")
        print(f"{datetime.now()}   BUTTON_ON_VER_BANNER is present? =>")
        button_list = self.browser.find_elements(*ButtonOnVerticalBannerLocators.BUTTON_ON_VER_BANNER)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_ON_VER_BANNER is not present on the page!")
            del button_list
            return False
        print(f"{datetime.now()}   => BUTTON_ON_VER_BANNER is present on the page!")

        print(f"{datetime.now()}   BUTTON_ON_VER_BANNER scroll =>")

        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )

        self.element_is_clickable(button_list[0], 5)

        data_type = button_list[0].get_attribute("data-type")
        data_id = data_type.split('_')[-1]

        try:
            button_list[0].click()
            print(f"{datetime.now()}   => BUTTON_ON_VER_BANNER clicked!")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => BUTTON_ON_VER_BANNER NOT CLICKED")
            print(f"{datetime.now()}   'Sign up' form or page is auto opened")

            page_ = SignupLogin(self.browser)
            if page_.close_signup_form():
                pass
            else:
                page_.close_signup_page()

            button_list[0].click()
            del page_

        del button_list
        return data_id
