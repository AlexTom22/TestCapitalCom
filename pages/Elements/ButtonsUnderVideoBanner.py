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
from pages.Elements.testing_elements_locators import ButtonsUnderVideoBannerLocators
from selenium.common.exceptions import ElementClickInterceptedException


class ButtonUnderVideoBanner(BasePage):

    def arrange_(self, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")
        # self.page_glossary = GlossaryPage(d, cur_item_link)
        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   BUTTON_UNDER_VIDEO_BANNER =>")
        if self.element_is_visible(ButtonsUnderVideoBannerLocators.BUTTON_UNDER_VIDEO_BANNER_OLD):
            print(f"{datetime.now()}   => BUTTON_UNDER_VIDEO_BANNER IS PRESENT")
            return True
        else:
            print(f"{datetime.now()}   => BUTTON_UNDER_VIDEO_BANNER IS NOT PRESENT")
            pytest.skip("Checking element is not on this page")

    @allure.step("Click on button under video banner")
    def element_click(self):
        print(f"\n{datetime.now()}   2. Act")
        button_list = self.browser.find_elements(*ButtonsUnderVideoBannerLocators.BUTTON_UNDER_VIDEO_BANNER_OLD)
        if len(button_list) == 0:
            del button_list
            return False

        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )

        self.element_is_clickable(button_list[0], 5)

        try:
            button_list[0].click()
            print(f"{datetime.now()}   => Button under Video banner clicked")
        except ElementClickInterceptedException:
            print("'Sign up' form or page is automatically opened")

            page_ = SignupLogin(self.browser)
            if page_.close_signup_form():
                pass
            else:
                page_.close_signup_page()

            button_list[0].click()
            del page_

        del button_list
        return True


class ButtonsUnderVideoBanner(BasePage):

    def arrange_(self, cur_item_link, button_name):
        button_under_video = None
        print(f"\n{datetime.now()}   1. Arrange")
        # if not self.current_page_is(cur_item_link):
        #     self.link = cur_item_link
        #     self.open_page()

        match button_name:
            case "try_free_demo":
                button_under_video = ButtonsUnderVideoBannerLocators.BUTTON_TRY_FREE_DEMO_UNDER_VIDEO_BANNER
            case "create_account":
                button_under_video = ButtonsUnderVideoBannerLocators.BUTTON_CREATE_ACCOUNT_UNDER_VIDEO_BANNER
            case "trade_now":
                button_under_video = ButtonsUnderVideoBannerLocators.BUTTON_TRADE_NOW_UNDER_VIDEO_BANNER

        print(f"{datetime.now()}   Button '{button_name}' under video banner =>")
        if self.element_is_located(button_under_video, 5):
            print(f"{datetime.now()}   => BUTTON_UNDER_VIDEO_BANNER is present on the DOM of a page")
        else:
            print(f"{datetime.now()}   => BUTTON_UNDER_VIDEO_BANNER is not present on the DOM of a page after 5 sec")
            pytest.skip("Checking element is not present in the DOM of a page after 5 sec")

        del button_under_video

    @allure.step("Click on button under video banner")
    def click(self, button_name):
        button_under_video = None
        print(f"\n{datetime.now()}   2. Act")
        match button_name:
            case "try_free_demo":
                button_under_video = ButtonsUnderVideoBannerLocators.BUTTON_TRY_FREE_DEMO_UNDER_VIDEO_BANNER
            case "create_account":
                button_under_video = ButtonsUnderVideoBannerLocators.BUTTON_CREATE_ACCOUNT_UNDER_VIDEO_BANNER
            case "trade_now":
                button_under_video = ButtonsUnderVideoBannerLocators.BUTTON_TRADE_NOW_UNDER_VIDEO_BANNER

        button_list = self.browser.find_elements(*button_under_video)

        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )

        if not self.element_is_visible(button_under_video, 5):
            print(f"{datetime.now()}   => Button is not clickable after 5 sec.")
            pytest.fail(f"Bug! The button under Video banner is not clickable after 5 sec.")

        if not self.element_is_clickable(button_list[0], 5):
            print(f"{datetime.now()}   => Button is not clickable after 5 sec.")
            pytest.fail(f"Bug! The button under Video banner is not clickable after 5 sec.")

        button_list[0].click()
        print(f"{datetime.now()}   => Button under Video banner clicked")

        del button_list
        del button_under_video
        return True
