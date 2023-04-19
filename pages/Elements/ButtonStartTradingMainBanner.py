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
# from pages.Elements.testing_elements_locators import HeaderButtonTradeLocators
from pages.Education.commodities_trading_locators import CommoditiesTradingPageLocator
from selenium.common.exceptions import ElementClickInterceptedException



class MainBannerStartTrading(BasePage):

    def arrange_(self, d, cur_role, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if cur_role == "Auth":
            pytest.skip('This test not for "Auth" role')

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        if not self.main_banner_button_start_trading_is_visible():
            pytest.skip("Checking element is not on this page")

    def main_banner_button_start_trading_is_visible(self):
        print(f"{datetime.now()}   BUTTON_START_TRADING is visible? =>")
        if self.element_is_visible(CommoditiesTradingPageLocator.LOCATOR_COMMODITIES_TRADING_MAINBANNER_START_TRADING):
            print(f"{datetime.now()}   => BUTTON_START_TRADING is visible on the page!")
            return True
        else:
            print(f"{datetime.now()}   => BUTTON_START_TRADING is not visible on the page!")
            return False

    @allure.step("Click button [Start Trading]")
    def element_click(self):
        print(f"\n{datetime.now()}   2. Act")
        print(f"{datetime.now()}   BUTTON_START_TRADING is present? =>")
        button_list = self.browser.find_elements(*CommoditiesTradingPageLocator.LOCATOR_COMMODITIES_TRADING_MAINBANNER_START_TRADING)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_START_TRADING is not present on the page!")
            del button_list
            return False
        print(f"{datetime.now()}   => BUTTON_START_TRADING is present on the page!")

        print(f"{datetime.now()}   BUTTON_START_TRADING scroll =>")
        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )

        print(f"{datetime.now()}   BUTTON_START_TRADING is clickable? =>")
        self.element_is_clickable(button_list[0], 5)

        print(f"{datetime.now()}   BUTTON_START_TRADING click =>")
        try:
            button_list[0].click()
            print(f"{datetime.now()}   => BUTTON_START_TRADING clicked!")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => 'Sign up' or 'Log in' form is automatically opened")
            page_ = SignupLogin(self.browser)
            page_.close_signup_form()
            del page_
            button_list[0].click()

        del button_list
        return True
