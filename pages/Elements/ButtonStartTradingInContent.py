"""
-*- coding: utf-8 -*-
@Time    : 2023/04/29 00:30
@Author  : Suleyman Alirzaev
"""
from datetime import datetime
import pytest
import allure
from selenium.webdriver import ActionChains
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.testing_elements_locators import ButtonsOnPageLocators
from selenium.common.exceptions import ElementClickInterceptedException
from pages.Elements.AssertClass import AssertClass


class ContentStartTrading(BasePage):
    def full_test_with_tpi(self, d, cur_language, cur_country, cur_role, cur_item_link):
        qty = self.arrange_v3(cur_item_link)

        for i in range(qty):
            self.element_click_v3(i)

            test_element = AssertClass(d, cur_item_link)
            match cur_role:
                case "NoReg":
                    test_element.assert_signup(d, cur_language, cur_item_link)
                case "Reg/NoAuth":
                    test_element.assert_login(d, cur_language, cur_item_link)
                case "Auth":
                    test_element.assert_trading_platform_v4(d, cur_item_link)

    def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link):
        self.arrange_(cur_item_link)

        self.element_click(cur_item_link, cur_language, cur_role)

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, cur_item_link)

    def arrange_(self, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v0")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Is present BUTTON_START_TRADING_IN_ARTICLE? =>")
        buttons = self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE)
        if len(buttons) == 0:
            pytest.skip("Checking element is not on this page")
        print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE is present")

        print(f"{datetime.now()}   Is visible BUTTON_START_TRADING_IN_ARTICLE? =>")

        if not self.element_is_visible(ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE, 5):
            pytest.fail("Checking element is present in DOM this page, but not visible")

    def arrange_v3(self, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v3")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Is visible BUTTON_START_TRADING_IN_ARTICLE? =>")

        print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE =>")
        buttons = self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE)
        if not buttons:
            print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE2 =>")
            buttons = self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE2)
            if not buttons:
                pytest.skip("Checking element is not on this page")
        return len(buttons)

    @allure.step("Click button BUTTON_START_TRADING_IN_ARTICLE")
    def element_click(self, cur_item_link, cur_language, cur_role):
        print(f"\n{datetime.now()}   2. Act_v0")
        button_list = None
        print(f"{datetime.now()}   Start Click button BUTTON_START_TRADING_IN_ARTICLE =>")
        if self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE):
            button_list = self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE)
        elif self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE2):
            button_list = self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE2)

        if len(button_list) >= 1:
            self.click__button(len(button_list), cur_item_link, cur_language, cur_role)
        else:
            print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE is not present on the page!")
            pytest.skip("Checking element is not present on this page")

    @allure.step("Click button BUTTON_START_TRADING_IN_ARTICLE. V3")
    def element_click_v3(self, i):
        print(f"\n{datetime.now()}   2. Act_v3")
        button_list = list()
        print(f"{datetime.now()}   Start Click button BUTTON_START_TRADING_IN_ARTICLE =>")
        if self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE):
            button_list = self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE)
        elif self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE2):
            button_list = self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE2)

        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});', button_list[int(i)]
        )
        if not self.element_is_clickable(button_list[int(i)], 5):
            print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE is not clickable")
            pytest.fail("BUTTON_START_TRADING_IN_ARTICLE is not clickable")

        # button_list[0].click()
        self.browser.execute_script("arguments[0].click();", button_list[int(i)])
        print(f"{datetime.now()}   => BUTTON_CREATE_YOUR_ACCOUNT is clicked")

    def click__button(self, times, cur_item_link, cur_language, cur_role):
        for i in range(times):
            if self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE):
                button_list = self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE)
            elif self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE2):
                button_list = self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE2)
            else:
                print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE is not present on the page!")
                pytest.skip("Checking element is not present on this page")
                return False

            print(f"{datetime.now()}   BUTTON_START_TRADING_IN_ARTICLE_#{i + 1} scroll =>")
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                button_list[i]
            )

            print(f"{datetime.now()}   Is BUTTON_START_TRADING_IN_ARTICLE_#{i + 1} clickable? =>")
            if self.element_is_clickable(button_list[i], 5):
                print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE_#{i + 1} is clickable")

            print(f"{datetime.now()}   BUTTON_START_TRADING_IN_ARTICLE_#{i + 1} click =>")
            try:
                button_list[i].click()
                print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE_#{i + 1} clicked!")
                test_element = AssertClass(self.browser, cur_item_link)
                # test_element.assert_signup(self.browser, cur_language, cur_item_link)
                match cur_role:
                    case "NoReg":
                        test_element.assert_signup(self.browser, cur_language, cur_item_link)
                    case "Reg/NoAuth":
                        test_element.assert_login(self.browser, cur_language, cur_item_link)
                    case "Auth":
                        test_element.assert_trading_platform(self.browser)
                self.browser.get(cur_item_link)

            except ElementClickInterceptedException:
                print(f"{datetime.now()}   'Signup' or 'Login' form is automatically opened")
                page_ = SignupLogin(self.browser)
                if page_.close_signup_form():
                    pass
                else:
                    page_.close_signup_form()
                del page_
            del button_list

        return True

    @allure.step("Works ARRANGE START_TRADING_IN_ARTICLE (generator) - ver 2")
    def arrange_v2_(self):
        print(f"\n{datetime.now()}   1. Arrange_v2")

        if not self.current_page_is(self.link):
            self.open_page()

        print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE =>")
        # item_list = self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE)

        item_list = self.elements_are_located(ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE, timeout=10)

        locators_ver_one = True
        if not item_list:
            print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE2 =>")
            # item_list = self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE2)

            item_list = self.elements_are_located(ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE2, timeout=10)
            locators_ver_one = False
            if not item_list:
                pytest.fail("ARRANGE: No items found for testing")
        print(f"{datetime.now()}   => Found {len(item_list)} elements BUTTON_START_TRADING_IN_ARTICLE")
        for i in range(len(item_list)):
            yield item_list[i]
            if i > 0:
                self.open_page()
                item_list = self.browser.find_elements(*(ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE
                                                         if locators_ver_one
                                                         else ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE2))

    @allure.step("Click button START_TRADING_IN_ARTICLE - ver 2")
    def element_click_v2(self, web_element):
        print(f"\n{datetime.now()}   2. Act_v2")
        print(f"{datetime.now()}   Start Click button START_TRADING_IN_ARTICLE =>")
        print(f"{datetime.now()}   START_TRADING_IN_ARTICLE scroll =>")
        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            web_element
        )
        print(f"{datetime.now()}   START_TRADING_IN_ARTICLE click ver 2 =>")
        ActionChains(self.browser) \
            .move_to_element(web_element) \
            .click() \
            .perform()
        return True

#
# """
# -*- coding: utf-8 -*-
# @Time    : 2023/04/29 00:30
# @Author  : Suleyman Alirzaev
# """
# from datetime import datetime
# import pytest
# import allure
# from pages.Signup_login.signup_login import SignupLogin
# from pages.base_page import BasePage
# from pages.Elements.testing_elements_locators import ButtonsOnPageLocators
# from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
# from pages.Elements.AssertClass import AssertClass
# from selenium.webdriver.common.action_chains import ActionChains
#
# class ContentStartTrading(BasePage):
#
#     def arrange_(self, d, cur_item_link):
#         print(f"\n{datetime.now()}   1. Arrange")
#
#         if not self.current_page_is(cur_item_link):
#             self.link = cur_item_link
#             self.open_page()
#
#         print(f"{datetime.now()}   Is visible BUTTON_START_TRADING_IN_ARTICLE? =>")
#
#         print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE =>")
#         if not self.element_is_visible(ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE):
#             print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE2 =>")
#             if not self.element_is_visible(ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE2):
#                 pytest.skip("Checking element is not on this page")
#
#     @allure.step("Click button BUTTON_START_TRADING_IN_ARTICLE")
#     def element_click(self, cur_item_link, cur_language, cur_role):
#         print(f"\n{datetime.now()}   2. Act")
#         print(f"{datetime.now()}   Start Click button BUTTON_START_TRADING_IN_ARTICLE =>")
#         if self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE):
#             self.button_list = self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE)
#         elif self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE2):
#             self.button_list = self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE2)
#         if len(self.button_list) >= 1:
#             self.ClickButton(len(self.button_list), cur_item_link, cur_language, cur_role)
#         else:
#             print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE is not present on the page!")
#             # del self.button_list
#             pytest.skip("Checking element is not present on this page")
#             return False
#
#     def ClickButton(self, times, cur_item_link, cur_language, cur_role):
#         for i in range(times):
#             print(f"{datetime.now()}   BUTTON_START_TRADING_IN_ARTICLE_#{i + 1} scroll =>")
#             # self.browser.execute_script(
#             #     'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
#             #     button_list[i]
#             # )
#             hover = ActionChains(self.browser).move_to_element(self.button_list[i])
#
#             print(f"{datetime.now()}   Is BUTTON_START_TRADING_IN_ARTICLE_#{i + 1} clickable? =>")
#             if self.element_is_clickable(self.button_list[i], 5):
#                 print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE_#{i + 1} is clickable")
#
#             print(f"{datetime.now()}   BUTTON_START_TRADING_IN_ARTICLE_#{i + 1} click =>")
#             try:
#                 hover.perform()
#                 self.button_list[i].click()
#                 print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE_#{i + 1} clicked!")
#                 test_element = AssertClass(self.browser, cur_item_link)
#                 test_element.assert_signup(self.browser, cur_language, cur_role, cur_item_link)
#                 self.browser.get(cur_item_link)
#
#             except ElementClickInterceptedException:
#                 print(f"{datetime.now()}   'Signup' or 'Login' form is automatically opened")
#                 page_ = SignupLogin(self.browser)
#                 if page_.close_signup_form():
#                     pass
#                 else:
#                     page_.close_signup_form()
#                 del page_
#             del self.button_list
#
#         return True
