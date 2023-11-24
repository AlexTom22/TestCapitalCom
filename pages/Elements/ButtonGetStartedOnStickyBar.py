"""
-*- coding: utf-8 -*-
@Time    : 2023/04/20 22:00
@Author  : Suleyman Alirzaev
"""
from datetime import datetime
import pytest
import allure

from pages.Elements.AssertClass import AssertClass
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.testing_elements_locators import ButtonsOnPageLocators
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException


class GetStartedOnStickyBar(BasePage):

    def full_test_with_tpi(self, d, cur_language, cur_country, cur_role, cur_item_link):
        self.arrange_(d, cur_item_link)

        self.element_click()
        check_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                check_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                check_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                check_element.assert_trading_platform_v4(d, cur_item_link)

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v0")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        button_list = self.elements_are_located(ButtonsOnPageLocators.BUTTON_ON_STICKY_BAR, timeout=20)

        if not button_list:
            print(f"{datetime.now()}   => BUTTON_ON_STICKY_BAR is not present on the page!")
            pytest.skip("ARRANGE: Checking element (BUTTON_ON_STICKY_BAR) is not on this page")

        # print(f"{datetime.now()}   BUTTON_GET_STARTED_ON_STICKY_BAR is visible? =>")
        # # if self.element_is_visible(ButtonsOnPageLocators.BUTTON_ON_STICKY_BAR):
        # try:
        #     if self.browser.find_element(*ButtonsOnPageLocators.BUTTON_ON_STICKY_BAR):
        #         print(f"{datetime.now()}   => BUTTON_GET_STARTED_ON_STICKY_BAR is visible on the page!")
        # except NoSuchElementException:
        #     print(f"{datetime.now()}   => BUTTON_GET_STARTED_ON_STICKY_BAR is not visible on the page!")
        #     pytest.skip("Checking element is not on this page")

    @allure.step("Click button [Get started] on Sticky bar")
    def element_click(self):
        print(f"\n{datetime.now()}   2. Act_v0")
        print(f"{datetime.now()}   BUTTON_GET_STARTED_ON_STICKY_BAR is present? =>")
        button_list = self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_ON_STICKY_BAR)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_GET_STARTED_ON_STICKY_BAR is not present on the page!")
            del button_list
            return False
        print(f"{datetime.now()}   => BUTTON_GET_STARTED_ON_STICKY_BAR is present on the page!")

        print(f"{datetime.now()}   BUTTON_GET_STARTED_ON_STICKY_BAR scroll =>")

        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )

        self.element_is_clickable(button_list[0], 5)

        try:
            button_list[0].click()
            print(f"{datetime.now()}   => BUTTON_GET_STARTED_ON_STICKY_BAR clicked!")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => BUTTON_GET_STARTED_ON_STICKY_BAR NOT CLICKED")
            print(f"{datetime.now()}   'Sign up' form or page is auto opened")

            page_ = SignupLogin(self.browser)
            if page_.close_signup_form():
                pass
            else:
                page_.close_signup_page()

            button_list[0].click()
            del page_

        del button_list
        return True
