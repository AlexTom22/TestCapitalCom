"""
-*- coding: utf-8 -*-
@Time    : 2023/04/24 08:30
@Author  : Liudmila Dankevich
"""
from datetime import datetime
import pytest
import allure
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from selenium.common.exceptions import ElementClickInterceptedException
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import BlockOurCoursesLocators


class ButtonCreateAccountBlockOurCourses(BasePage):

    def full_test(self, d, cur_language, cur_country, cur_role, link):
        self.arrange_(d, link)

        self.element_click()

        test_element = AssertClass(d, link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, link)

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")
        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        if not self.button_create_account_is_visible():
            # pytest.fail("Checking element is not on this page")
            pytest.skip("Checking element is not on this page")

    @allure.step("Check if the element is present on the page")
    # @profile(precision=3)
    def button_create_account_is_visible(self):
        print(f"{datetime.now()}   BUTTON_CREATE_ACCOUNT =>")
        if self.element_is_visible(BlockOurCoursesLocators.BUTTON_CREATE_ACCOUNT):
            print(f"{datetime.now()}   => BUTTON_CREATE_ACCOUNT IS PRESENT")
            return True
        else:
            print(f"{datetime.now()}   => BUTTON_CREATE_ACCOUNT IS NOT PRESENT")
            return False

        # Act
    @allure.step("Click 'Button Create account' button in 'Our courses' section")
    def element_click(self):
        """Method"""
        print(f"\n{datetime.now()}   2. Act")
        button_list = self.browser.find_elements(*BlockOurCoursesLocators.BUTTON_CREATE_ACCOUNT)
        if len(button_list) == 0:
            del button_list
            return False
        print(f"{datetime.now()}   "
              f"{len(button_list)} checking element(s) with current CSS locator is(are) present(s) on this page")
        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )
        self.element_is_clickable(button_list[0], 10)
        try:
            button_list[0].click()
            print(f"{datetime.now()}   => BUTTON_CREATE_ACCOUNT is clicked")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => BUTTON_CREATE_ACCOUNT NOT CLICKED")
            print(f"{datetime.now()}   'Sign up' form is auto opened")
            page_ = SignupLogin(self.browser)
            if page_.close_signup_form():
                pass
            else:
                page_.close_signup_page()
            button_list[0].click()
            del page_

        del button_list
        return True
