"""
-*- coding: utf-8 -*-
@Time    : 2023/11/07 18:00
@Author  : Mike Taran
"""
from datetime import datetime
import pytest
import allure

from pages.Elements.AssertClass import AssertClass
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from selenium.common.exceptions import ElementClickInterceptedException
from pages.Elements.testing_elements_locators import ButtonOnVerticalBannerLocators


class ButtonOnVerticalBanner(BasePage):

    def full_test_with_tpi(self, d, cur_language, cur_country, cur_role, link, banner00_ver_tpd, banner00_ver_tp,
                           banner01_ver_tpd, banner01_ver_tp):
        tpd = False
        self.arrange_(link)

        # Checking if [SignUP for is popped up on the page]
        page_signup_login = SignupLogin(d, link)
        page_signup_login.check_popup_signup_form()

        data_id = self.element_click()
        # проверка Demo mode
        if data_id in banner00_ver_tpd or data_id in banner01_ver_tpd:
            tpd = True
        # проверка, что баннер учтен в матрице покрытия
        if (data_id in banner00_ver_tp or data_id in banner01_ver_tp or data_id in banner00_ver_tpd or
                data_id in banner01_ver_tpd):
            test_element = AssertClass(d, link)
            match cur_role:
                case "NoReg":
                    test_element.assert_signup(d, cur_language, link)
                case "Reg/NoAuth":
                    test_element.assert_login(d, cur_language, link)
                case "Auth":
                    if tpd:
                        print(f"{datetime.now()}   For Vertical banner [type-id={data_id}] Trading platform should be open "
                              f"in Demo Mode =>")
                    else:
                        print(f"{datetime.now()}   For Vertical banner [type-id={data_id}] Trading platform should be open "
                              f"in Live Mode =>")
                    test_element.assert_trading_platform_v4(d, link, tpd)
        else:
            print(f"\n{datetime.now()}   The Vertical banner [type-id={data_id}] is Not in the Test List ")
            assert False, f"\n{datetime.now()}   The Vertical banner [type-id={data_id}] is Not in the Test List "

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
