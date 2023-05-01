"""
-*- coding: utf-8 -*-
@Time    : 2023/04/29 00:30
@Author  : Suleyman Alirzaev
"""
from datetime import datetime
import pytest
import allure
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.testing_elements_locators import CommoditiesPageElements
from selenium.common.exceptions import ElementClickInterceptedException

global button_list


class ArticleStartTrading(BasePage):

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   BUTTON_START_TRADING_IN_ARTICLE is visible? =>")
        if self.element_is_visible(CommoditiesPageElements.BUTTON_START_TRADING_IN_ARTICLE):
            print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE is visible on the page!")
        else:
            print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE is not visible on the page!")
            pytest.skip("Checking element is not present on this page")

    @allure.step("Click button [Start trading] in article")
    def element_click(self):
        print(f"\n{datetime.now()}   2. Act")
        print(f"{datetime.now()}   BUTTON_START_TRADING_IN_ARTICLE is present? =>")
        button_list = self.browser.find_elements(*CommoditiesPageElements.BUTTON_START_TRADING_IN_ARTICLE)
        print(f"BUTTON_LIST_IS:{button_list} and LEN IS {len(button_list)}")

        if len(button_list) >= 1:
            for i in range(len(button_list)):
                self.ClickButton(len(button_list))
        else:
            print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE is not present on the page!")
            del button_list
            pytest.skip("Checking element is not present on this page")
            # return False

    def ClickButton(self, times):
        button_list = self.browser.find_elements(*CommoditiesPageElements.BUTTON_START_TRADING_IN_ARTICLE)
        print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE is present on the page!")

        print(f"{datetime.now()}   BUTTON_START_TRADING_IN_ARTICLE scroll =>")

        for i in range(times):
            try:
                self.browser.execute_script(
                    'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                    button_list[i]
                )
                self.element_is_clickable(button_list[i], 5)
            except IndexError:
                print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE_#{i+1} is not present on the page!")
            except Exception as e:
                print(f"Exception occurred: {e}")

            # try:
            #     self.browser.execute_script(
            #         'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            #         button_list[0]
            #     )
            #     self.element_is_clickable(button_list[i], 5)
            # except IndexError:
            #     print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE_#{i+1} is not present on the page!")

            try:
                button_list[i].click()
                print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE_#{i+1} clicked!")
                page_ = SignupLogin(self.browser)
                if page_.close_signup_form():
                    pass
                else:
                    page_.close_signup_page()
                button_list[i].click()
                del page_

            except ElementClickInterceptedException:
                print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE_#{i+1} NOT CLICKED")
                print(f"{datetime.now()}   'Sign up' form or page is auto opened")
            except IndexError:
                print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE_#{i+1} is not present on the page!")
            except Exception as e:
                print(f"Exception occurred: {e}")
        # del page_

        del button_list
        return True

        # try:
        #     self.browser.execute_script(
        #         'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
        #         button_list[0]
        #     )
        #     self.element_is_clickable(button_list[0], 5)
        # except IndexError:
        #     print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE_#1 is not present on the page!")
        #
        # try:
        #     self.browser.execute_script(
        #         'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
        #         button_list[0]
        #     )
        #     self.element_is_clickable(button_list[0], 5)
        # except IndexError:
        #     print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE_#1 is not present on the page!")
        #
        # try:
        #     button_list[0].click()
        #     print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE_#1 clicked!")
        #     page_ = SignupLogin(self.browser)
        #     if page_.close_signup_form():
        #         pass
        #     else:
        #         page_.close_signup_page()
        #     button_list[0].click()
        #
        # except ElementClickInterceptedException:
        #     print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE_#1 NOT CLICKED")
        #     print(f"{datetime.now()}   'Sign up' form or page is auto opened")
        # except IndexError:
        #     print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE_#1 is not present on the page!")
        #
        # try:
        #     self.browser.execute_script(
        #         'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
        #         button_list[1]
        #     )
        #     self.element_is_clickable(button_list[1], 5)
        # except IndexError:
        #     print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE_#2 is not present on the page!")
        #
        # try:
        #     button_list[1].click()
        #     print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE_#2 clicked!")
        #     page_ = SignupLogin(self.browser)
        #     if page_.close_signup_form():
        #         pass
        #     else:
        #         page_.close_signup_page()
        #     button_list[1].click()
        #
        # except ElementClickInterceptedException:
        #     print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE_#2 NOT CLICKED")
        #     print(f"{datetime.now()}   'Sign up' form or page is auto opened")
        # except IndexError:
        #     print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE_#2 is not present on the page!")


