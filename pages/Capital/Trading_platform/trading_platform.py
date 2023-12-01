"""
-*- coding: utf-8 -*-
@Time    : 2023/04/14 11:00
@Author  : Alexander Tomelo
"""

import allure
from datetime import datetime

# import pytest

from pages.Capital.Trading_platform.Topbar.topbar import TopBar
from pages.base_page import BasePage
from test_data.trading_platform_data import data as tp_data
from pages.Capital.Trading_platform.trading_platform_locators \
    import TradingPlatformSignupFormLocators as TPSignupFormLocators, TradingInstruments
from pages.Capital.Trading_platform.trading_platform_locators \
    import TopBarLocators
from test_data.trading_platform_data import data


class TradingPlatform(BasePage):
    @allure.step("Checking that the trading platform page has opened")
    # @profile(precision=3)
    def should_be_trading_platform_page(self, d, link):
        """Check if the page is open"""
        print(f"{datetime.now()}   Checking that the trading platform page has opened")
        if self.current_page_url_contain_the(link):
            page_ = TopBar(d, link)
            if page_.trading_platform_logo_is_present():
                d.back()
                del page_
                assert True
            else:
                # d.back()
                del page_
                assert False, 'Page with title "Trading Platform | Capital.com" not loaded'
        else:
            assert False, f'Loaded page with not {link} url. Current url is {self.browser.current_url}'

    @allure.step("Checking that the trading platform page has opened - ver 2")
    def should_be_trading_platform_page_v2(self, d, cur_link, demo=False):
        """Check if the trading platform page is open"""
        print(f"{datetime.now()}   Checking that the trading platform page has opened =>")
        platform_url = data["PLATFORM_DEMO_URL"] if demo else data["PLATFORM_URL/"]
        # print(platform_url)
        # print(self.wait_for_change_url(platform_url, 120))
        if self.wait_for_target_url(platform_url, 10):
            print(f"{datetime.now()}   => Opened page with {self.browser.current_url} url. Expected: {platform_url} ")
            self.should_be_page_title_v2(data["PAGE_TITLE"])
            self.should_be_platform_logo()
            self.should_be_corresponding_trading_instrument()
            self.open_page()
            assert True, 'Trading platform with title "Trading Platform | Capital.com" opened'
        else:
            print(f"{datetime.now()}   => Loaded page {self.browser.current_url} with not {platform_url} url")
            cur_url = self.browser.current_url
            self.open_page()
            assert False, f"Loaded page with {cur_url} url, but expected {platform_url}"

    @allure.step("Checking that the trading platform page has opened - ver 3")
    def should_be_trading_platform_page_v3(self, demo=False):
        """Check if the trading platform page is open"""
        print(f"{datetime.now()}   Checking that the trading platform page has opened (v3) =>")
        platform_url = data["PLATFORM_URL"]
        if self.current_page_url_contain_the(platform_url):
            print(f"{datetime.now()}   => Opened page with {self.browser.current_url} url. Expected: {platform_url} ")
            self.should_be_page_title_v2(data["PAGE_TITLE"])
            self.should_be_platform_logo()
            if demo:
                self.should_be_platform_demo_mode()
            else:
                self.should_be_platform_live_mode()
            self.open_page()
        else:
            print(f"{datetime.now()}   => Loaded page {self.browser.current_url} with not {platform_url} url")
            # self.link = self.browser.current_url
            # self.open_page()
            assert False, "Bug! The trading platform page is not opened"

    @allure.step("Checking that the trading platform page has opened - ver 4")
    def should_be_trading_platform_page_v4(self, d, cur_link, tpd, tpi, trade_instrument):
        """
        Check if the trading platform page for the corresponding trade instrument is opened
        Args:
            d: Webdriver
            cur_link: Link in the list of 3 random items and start page of the sidebar
            tpd: open Trade platform in Demo mode (True). Live mode (False)
            tpi: open Trade platform for corresponding trade instrument (False)
            trade_instrument: corresponding trade instrument (False)
        """
        print(f"{datetime.now()}   Checking that the trading platform page has opened (v4) =>")
        platform_url = data["PLATFORM_URL/"]
        cur_url = self.browser.current_url
        if self.wait_for_target_url(platform_url, 15):

            self.should_be_page_title_v2(data["PAGE_TITLE"])
            self.should_be_platform_logo()
            if tpd:
                self.should_be_platform_demo_mode(20)
                print(f"{datetime.now()}   => The page with {cur_url} url was opened in DEMO mode")
            else:
                self.should_be_platform_live_mode(20)
                print(f"{datetime.now()}   => The page with {cur_url} url was opened in lIVE mode")
            if tpi:
                print(f"{datetime.now()}   => Opened page with {cur_url} url for corresponding trading"
                      f" instrument '{trade_instrument}'")
                self.should_be_corresponding_trading_instrument(cur_url, trade_instrument)

            assert True, 'Trading platform with title "Trading Platform | Capital.com" opened'
            self.open_page()
        else:
            if tpd:
                print(f"{datetime.now()}   => Loaded page {self.browser.current_url} with not {platform_url} url")
                assert False, (f"Bug!. Loaded page with {cur_url} url, but expected the Trading platform in"
                               f"Demo mode(timeout=20c)")
            else:
                print(f"{datetime.now()}   => Loaded page {self.browser.current_url} with not {platform_url} url")
                assert False, (f"Bug!. Loaded page with {cur_url} url, but expected the Trading platform in"
                               f"Live mode(timeout=20c)")

    @allure.step("Checking that the trading platform page has opened with selected item and operation")
    def should_be_trading_platform_with_sel_item_and_operation(self, sel_item, sel_operation, demo=False):
        print(f"{datetime.now()}   "
              f"Checking that the trading platform page has opened with selected regime, item, operation =>")

        platform_url = data["PLATFORM_DEMO_URL"] if demo else data["PLATFORM_URL"]
        # print(platform_url)
        # print(self.wait_for_change_url(platform_url, 120))
        if self.wait_for_target_url(platform_url, 60):
            print(f"{datetime.now()}   => Opened page with {self.browser.current_url} url. Expected: {platform_url} ")
            self.should_be_page_title_v2(data["PAGE_TITLE"])
            self.should_be_platform_logo()
            print(f"{datetime.now()}   !!! надо писать проверку выбранного инструмента и операции")
            self.open_page()
            assert True, 'Trading platform with title "Trading Platform | Capital.com", "Capital.com" Logo,  opened'
        else:
            print(f"{datetime.now()}   => Loaded page {self.browser.current_url} with not {platform_url} url")
            cur_url = self.browser.current_url
            self.open_page()
            assert False, f"Loaded page with {cur_url} url, but expected {platform_url}"

    @allure.step("Check if the Logo element is present on the page")
    def should_be_platform_logo(self):
        """Check that the Capital.com Logo is present"""
        """Check if the app title"""
        print(f"{datetime.now()}   Checking that the Trading platform LOGO is present on the page =>")
        assert self.element_is_visible(TopBarLocators.LOGO, 30), \
            "Trading platform LOGO is not present on the page"

    @allure.step("Check if the trading platform opened in DEMO mode")
    def should_be_platform_demo_mode(self, timeout=30):
        """Check that Trading platform opened in Demo mode"""
        print(f"{datetime.now()}   Checking that the Trading platform opened in DEMO mode =>")
        assert self.element_is_visible(TopBarLocators.MODE_DEMO, timeout), \
            "Bug! Trading platform is opened not in DEMO mode"

    @allure.step("Check if the trading platform opened in LIVE mode")
    def should_be_platform_live_mode(self, timeout=30):
        """Check that Trading platform opened in Live mode"""
        print(f"{datetime.now()}   Checking that the Trading platform opened in LIVE mode =>")
        assert self.element_is_visible(TopBarLocators.MODE_LIVE, timeout), \
            "Bug! Trading platform is opened in not LIVE mode"

    @allure.step("Check that form [Sign Up] is opened on the Trading Platform page")
    # @profile(precision=3)
    def should_be_signup_form_on_the_trading_platform(self):
        """
        Check there are an elements to on 'Sign up' page on the Trading Platform
        """
        print(f"{datetime.now()}   Start method Check that [Sign up] page opened =>")

        if self.current_page_url_contain_the(tp_data["SIGNUP_URL"]):
            print(f"{datetime.now()}   'Sign up' page opened on the Trading Platform")
            print(f"{datetime.now()}   SIGNUP_FRAME =>")
            assert self.element_is_visible(TPSignupFormLocators.SIGNUP_FRAME, 30), \
                f"{datetime.now()}   The layout of the 'SignUp' page has not visible"

            print(f"{datetime.now()}   INPUT_EMAIL =>")
            assert self.element_is_visible(TPSignupFormLocators.USERNAME), \
                f"{datetime.now()}   Problem with 'Username (email)' field"

            print(f"{datetime.now()}   INPUT_PASS =>")
            assert self.element_is_visible(TPSignupFormLocators.PASSWORD), \
                f"{datetime.now()}   Problem with 'Password' field"

            print(f"{datetime.now()}   BUTTON_CONTINUE =>")
            assert self.element_is_visible(TPSignupFormLocators.BUTTON_CONTINUE), \
                f"{datetime.now()}   Problem with 'Continue' button"
            # self.open_page()
        else:
            # self.open_page()
            print("'SignUp' page on the Trading Platform is not opened")
            assert False

    @allure.step("Check that form [Login] is opened on the Trading Platform page")
    # @profile(precision=3)
    def should_be_login_form_on_the_trading_platform(self):
        """
        Check there are an elements to on 'Log in' page on the Trading Platform
        """
        print(f"{datetime.now()}   Start method Check that [Log in] page opened =>")
        print(self.browser.current_url)
        if self.current_page_url_contain_the(tp_data["LOGIN_URL"]):
            print(f"{datetime.now()}   'Log in' page opened on the Trading Platform")

            print(f"{datetime.now()}   LOGIN_FRAME =>")
            assert self.element_is_visible(TPSignupFormLocators.LOGIN_FRAME, 30), \
                f"{datetime.now()}   The layout of the 'Login' page has changed"

            print(f"{datetime.now()}   INPUT_EMAIL =>")
            assert self.element_is_visible(TPSignupFormLocators.USERNAME), \
                f"{datetime.now()}   Problem with 'Username (email)' field"

            print(f"{datetime.now()}   INPUT_PASS =>")
            assert self.element_is_visible(TPSignupFormLocators.PASSWORD), \
                f"{datetime.now()}   Problem with 'Password' field"

            print(f"{datetime.now()}   BUTTON_CONTINUE =>")
            assert self.element_is_visible(TPSignupFormLocators.BUTTON_CONTINUE), \
                f"{datetime.now()}   Problem with 'Continue' button"
            self.open_page()
        elif self.current_page_url_contain_the(tp_data["SIGNUP_URL"]):
            print(f"{datetime.now()}   'Sign up' page opened on the Trading Platform")
            print(f"{datetime.now()}   SIGNUP_FRAME =>")
            if self.element_is_visible(TPSignupFormLocators.SIGNUP_FRAME):
                print(f"{datetime.now()}   SIGNUP_FRAME is visible")
            else:
                print(f"{datetime.now()}   SIGNUP_FRAME is not visible")
            print(f"{datetime.now()}   'Login' page on the Trading Platform is not opened")
            assert False, "Bug!!! Opened a 'Sign up' form instead of a 'Login' form on the Trading Platform"
        else:
            # self.open_page()
            print(f"{datetime.now()}   'Login' page on the Trading Platform is not opened")
            assert False, "'Login' page on the Trading Platform is not opened"

    @allure.step("Check the corresponding trading instrument")
    def should_be_corresponding_trading_instrument(self, cur_url, trade_instrument):
        """
        Check Trading platform is opened for corresponding trade instrument
        """
        # проверяем, что открыта трейдинговая платформа на вкладке [Charts]
        assert "charting" in cur_url or "spotlight" in cur_url, \
            f"!!!Bug. Trading platform was Not opened for corresponding trading instrument '{trade_instrument}'"
        print(f"{datetime.now()}   Trading Platform for '{trade_instrument}' trading instrument is opened")
        # определяем, какие вкладки открыты и избегаем ошибки пустого списка
        top_chart_trade_list = self.elements_are_located(TradingInstruments.LIST_TRADE_INSTRUMENTS, 3)
        trade_instrument_name = trade_instrument.split(" ")[0]
        try:
            if len(top_chart_trade_list) == 0:
                assert False, (f"Trading platform for '{trade_instrument}' trade instrument was opened, "
                               f"but no one trade instrument on the Charts List")
        except TypeError:
            assert False, (f"Trading platform for '{trade_instrument}' trade instrument was opened, "
                           f"but no one trade instrument on the Charts List =(empty list)=")

        # проверяем, есть ли вкладка для запрашиваемого торгового инструмента
        count = True
        for element in top_chart_trade_list:
            if trade_instrument_name in element.text:
                print(f"{datetime.now()}   Trade instrument '{trade_instrument}' is on the Top Charts List")
                count = False
                break
        if count:
            assert False, f"Bug!!!. Trade instrument '{trade_instrument}' is Not on the Top Charts List"

        # проверяем, что запрашиваемый торговый инструмент выбран
        selected_trade_instrument = self.element_is_visible(TradingInstruments.SELECTED_TRADE_INSTRUMENTS).text
        assert trade_instrument_name in selected_trade_instrument, (f"Bug!!!. Trade instrument '{trade_instrument}'"
                                                                    f" is on the Top Charts List, but Not selected")
        print(f"{datetime.now()}   Trade instrument '{trade_instrument}' is on the Top Charts List and selected")
