"""
-*- coding: utf-8 -*-
@Time    : 2023/03/28 09:00
@Author  : Alexander Tomelo
"""

import pytest
import allure
from datetime import datetime

from pages.AppStore.app_store import AppStore
from pages.Capital.Trading_platform.trading_platform import TradingPlatform
from pages.GooglePlay.google_play import GooglePlay
from pages.base_page import BasePage
from pages.Signup_login.signup_login import SignupLogin


class AssertClass(BasePage):
    page_signup_login = None
    page_trading = None
    page_app_store = None
    page_google_play = None
    platform_url = ""

    def __init__(self, *args):
        super().__init__(*args)
        # self.is_captcha()

    @allure.step('Checking that "Signup" opened')
    def assert_signup(self, d, cur_language, cur_link):
        """Method Assert Signup"""
        print(f"\n{datetime.now()}   3. Assert_v0")
        self.page_signup_login = SignupLogin(d, cur_link)
        if self.page_signup_login.should_be_signup_form(cur_language):
            self.page_signup_login.close_signup_form()
        elif self.page_signup_login.should_be_signup_page(cur_language):
            self.page_signup_login.close_signup_page()
        elif self.page_signup_login.should_be_trading_platform_signup_form(cur_language):
            self.page_signup_login.close_trading_platform_signup_form()
        else:
            del self.page_signup_login
            pytest.fail("Bug! Sign Up form is not opened")
        # time.sleep(2)
        del self.page_signup_login

    @allure.step('Checking that "Login" form or page opened')
    def assert_login(self, d, cur_language, cur_link):
        """Method Assert Login form or page"""
        print(f"\n{datetime.now()}   3. Assert_Login_v0")
        self.page_signup_login = SignupLogin(d, cur_link)
        if self.page_signup_login.should_be_login_form():
            self.page_signup_login.close_login_form()
            del self.page_signup_login
        elif self.page_signup_login.should_be_login_page():
            self.page_signup_login.close_login_page()
            del self.page_signup_login
        elif self.page_signup_login.should_be_trading_platform_login_form(cur_language):
            self.page_signup_login.close_trading_platform_login_form()
            del self.page_signup_login
        elif self.page_signup_login.should_be_signup_form(cur_language):
            pytest.fail("Bug! Opened a 'Sign up' form instead of a 'Login'", False)
        elif self.page_signup_login.should_be_signup_page(cur_language):
            pytest.fail("Bug! Opened a 'Sign up' page instead of a 'Login'", False)
        elif self.page_signup_login.should_be_trading_platform_signup_form(cur_language):
            pytest.fail("Bug! Opened a 'Sign up' form on trading platform instead of a 'Login'", False)
        else:
            del self.page_signup_login
            pytest.fail("Bug! Unknown situation", False)

    @allure.step('Checking that "Trading platform" page opened')
    def assert_trading_platform(self, d):
        print(f"\n{datetime.now()}   3. Assert_v0")
        # time.sleep(1)
        self.platform_url = "https://capital.com/trading/platform/"
        # self.platform_url = "https://capital.com/trading/platform"
        self.page_trading = TradingPlatform(d)
        self.page_trading.should_be_trading_platform_page_v2(d, self.platform_url)
        del self.page_trading

    @allure.step('Checking that "Trading platform" page opened - ver 2')
    def assert_trading_platform_v2(self, d, cur_link, demo=False):
        print(f"\n{datetime.now()}   3. Assert_v2")
        self.page_trading = TradingPlatform(d, cur_link)
        self.page_trading.should_be_trading_platform_page_v2(d, cur_link, demo)

    @allure.step('Checking that "Trading platform" page opened - ver 3')
    def assert_trading_platform_v3(self, d, cur_link, demo=False):
        print(f"\n{datetime.now()}   3. Assert_v3")
        self.page_trading = TradingPlatform(d, cur_link)
        self.page_trading.should_be_trading_platform_page_v3(demo)

    @allure.step('Checking that "Trading platform" page opened - ver 4')
    def assert_trading_platform_v4(self, d, cur_link, tpd=False, tpi=False, trade_instrument=""):
        """
                Check if the trading platform page for the corresponding trade instrument is opened
                Args:
                    d: Webdriver
                    cur_link: Link in the list of 3 random items and start page of the sidebar
                    "Shares trading" is selected (Param)
                    tpd: open Trade platform in Demo mode (False)
                    tpi: open Trade platform for corresponding trade instrument (False)
                    trade_instrument: corresponding trade instrument (False)
        """
        print(f"\n{datetime.now()}   3. Assert_v4")
        self.page_trading = TradingPlatform(d, cur_link)
        self.page_trading.should_be_trading_platform_page_v4(d, cur_link, tpd, tpi, trade_instrument)

    @allure.step('Checking that "Trading platform" page opened with corresponding trading instrument - ver 5')
    def assert_trading_platform_with_selected_item_and_operation(self, cur_link, sel_item, sel_operation):
        print(f"\n{datetime.now()}   3. Assert_v5")
        self.page_trading = TradingPlatform(self.browser, cur_link)
        self.page_trading.should_be_trading_platform_with_sel_item_and_operation(sel_item, sel_operation)

    @allure.step('Checking that "Trading platform" page opened in demo mode')
    def assert_trading_platform_demo(self, d):
        print(f"\n{datetime.now()}   3. Assert_v0")
        self.platform_url = "https://capital.com/trading/platform/?mode=demo"
        self.page_trading = TradingPlatform(d)
        self.page_trading.should_be_trading_platform_page(d, self.platform_url)
        del self.page_trading

    @allure.step('Checking that "App Store" page opened')
    def assert_app_store(self, d, cur_link):
        print(f"\n{datetime.now()}   3. Assert_v0")
        self.page_app_store = AppStore(d, cur_link)
        self.page_app_store.should_be_app_store_page(cur_link)

    @allure.step('Checking that "App Store Investmate" page opened')
    def assert_app_store_investmate(self):
        print(f"\n{datetime.now()}   3. Assert_v0")
        self.page_app_store = AppStore(self.browser, self.link)
        self.page_app_store.should_be_app_store_investmane_page()

    @allure.step('Checking that "Google Play" page opened')
    def assert_google_play(self, d, cur_link):
        print(f"\n{datetime.now()}   3. Assert_v0")
        self.page_google_play = GooglePlay(d, cur_link)
        self.page_google_play.should_be_google_play_page(cur_link)

    @allure.step('Checking that "Sign Up" form on the Trading Platform page opened')
    def assert_signup_form_on_the_trading_platform(self, d):
        print(f"\n{datetime.now()}   3. Assert_v0")
        self.page_trading = TradingPlatform(d, self.link)
        self.page_trading.should_be_signup_form_on_the_trading_platform()

    @allure.step('Checking that "Login" form on the Trading Platform page opened')
    def assert_login_form_on_the_trading_platform(self, d):
        print(f"\n{datetime.now()}   3. Assert_v0")
        self.page_trading = TradingPlatform(d, self.link)
        self.page_trading.should_be_login_form_on_the_trading_platform()
