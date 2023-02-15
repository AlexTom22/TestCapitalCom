"""
-*- coding: utf-8 -*-
@Time    : 2023/01/27 10:00
@Author  : Alexander Tomelo
"""

import time
import pytest
import allure
from tests.conditions import Conditions
from capital.markets.markets import Markets
from capital.header import Header
from capital.user_panel import UserPanel
from capital.signup_login_form import SignupLoginForm
from src.src import (
    CapitalComPageSrc,
    MarketsSrc,
    TradingViewPageSrc,
    ESGPageSrc,
    LearnToTradePageSrc,
    ProfessionalClientsAu,
)


@allure.epic('Testing Markets page All language. All license')
class MarketsTests:

    @allure.feature("F_01 | Testing header")
    @allure.story("S_01.01 | Testing 'Log In' button on the header")
    @allure.step("Start test button 'Log In' on header.")
    @allure.title("TC_01_01 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_01_01_header_button_login(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role, prob_run_tc, datetime_now
    ):
        """
        Check: Header -> button [Log In]
        Language: All. License: All.
        """
        page = None
        time.sleep(1)

        print(f"worker_id = {worker_id}")

        page = Conditions(CapitalComPageSrc.URL, MarketsSrc.EP)
        page.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

        if cur_role != "Auth":
            page = Header(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()
            page.click_button_login_on_header()

            if cur_role == "NoReg":
                page = SignupLoginForm(d, test_link)
                page.should_be_login_form()
                page.close_login_form()
        else:
            pytest.mark.skip(f"This test not for 'Auth' role")

#
#
#
    @allure.feature("F_01 | Testing header")
    @allure.story("S_01.02 | Testing 'Trade Now' button on the header")
    @allure.step("Start test button 'Trade Now' on header.")
    @allure.title("TC_01_02 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_01_02_header_button_trade_now(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: Header -> button [Trade Now]
        Language: All. License: All.
        """
        global test_link
        global page

        time.sleep(1)

        print(f"worker_id = {worker_id}")

        self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

        if cur_role != "Auth":
            page = Header(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            page.click_button_signup_on_header()

            if cur_role == "NoReg":
                page = SignupLoginForm(d, test_link)
                page.should_be_signup_form()
                page.close_signup_form()
        else:
            pytest.mark.skip(f"This test not for 'Auth' role")

#
#
#
    @allure.feature("F_08 | Widget [Trading instrument]")
    @allure.story("S_08.01 | Widget [Trading instrument] tab [Most traded] button [Trade]")
    @allure.step("Start test 'Click 'Trade' buttons on the 'Most traded' tab 'Trading instrument' widget'.")
    @allure.title("TC_08_01 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_08_01_widget_trading_instrument(
        self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: widget "Trading instrument"
        Language: ALL. Licence: All.
        Widget has 2 layouts
        """
        global test_link
        global page

        time.sleep(1)

        tab_name = "Most"
        print(f"worker_id = {worker_id}")

        if not (cur_license == "FCA" and tab_name == "Crypto"):
            self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

            page = Markets(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            layout = page.tc08_what_is_the_current_layout()
            page.tc08_widget_trading_instrument_tab_click(layout, tab_name)
            list_buttons = page.tc08_get_list_lines_from_tab(cur_language, layout, tab_name)
            for line in range(len(list_buttons)):
                page = Markets(d, test_link)
                page.tc08_selected_tab_and_line_button_trade_click(list_buttons, line)
                if cur_role == "NoReg":
                    page = SignupLoginForm(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    page.should_be_link("https://capital.com/trading/platform/")
                    d.back()
                    d.back()
        else:
            pytest.skip(f"The '{tab_name}' tab is not available for the '{cur_license}' license")

#
#
#
    @allure.feature("F_08 | Widget [Trading instrument]")
    @allure.story("S_08.02 | Widget [Trading instrument] tab [Commodities] button [Trade]")
    @allure.step("Start test 'Click 'Trade' buttons on the 'Commodities' tab 'Trading instrument' widget'.")
    @allure.title("TC_08_02 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_08_02_widget_trading_instrument(
        self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: widget "Trading instrument"
        Language: All. Licence: All.
        Widget has 2 layouts
        """
        global test_link
        global page

        time.sleep(1)

        tab_name = "Commodities"
        print(f"worker_id = {worker_id}")

        if not (cur_license == "FCA" and tab_name == "Crypto"):
            self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

            page = Markets(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            layout = page.tc08_what_is_the_current_layout()
            page.tc08_widget_trading_instrument_tab_click(layout, tab_name)
            list_buttons = page.tc08_get_list_lines_from_tab(cur_language, layout, tab_name)

            for line in range(len(list_buttons)):
                page = Markets(d, test_link)
                page.tc08_selected_tab_and_line_button_trade_click(list_buttons, line)
                if cur_role == "NoReg":
                    page = SignupLoginForm(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                    # page = CapitalPage(d, test_link)
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    page.should_be_link("https://capital.com/trading/platform/")
                    d.back()
                    d.back()
        else:
            pytest.skip(f"The '{tab_name}' tab is not available for the '{cur_license}' license")

#
#
#
    @allure.feature("F_08 | Widget [Trading instrument]")
    @allure.story("S_08.03 | Widget [Trading instrument] tab [Indices] button [Trade]")
    @allure.step("Start test 'Click 'Trade' buttons on the 'Indices' tab 'Trading instrument' widget'.")
    @allure.title("TC_08_03 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_08_03_widget_trading_instrument(
        self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: widget "Trading instrument"
        Language: All. Licence: All.
        Widget has 2 layouts
        """
        global test_link
        global page

        time.sleep(1)

        tab_name = "Indices"
        print(f"worker_id = {worker_id}")

        if not (cur_license == "FCA" and tab_name == "Crypto"):
            self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

            page = Markets(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            layout = page.tc08_what_is_the_current_layout()
            page.tc08_widget_trading_instrument_tab_click(layout, tab_name)
            list_buttons = page.tc08_get_list_lines_from_tab(cur_language, layout, tab_name)

            for line in range(len(list_buttons)):
                page = Markets(d, test_link)
                page.tc08_selected_tab_and_line_button_trade_click(list_buttons, line)
                if cur_role == "NoReg":
                    page = SignupLoginForm(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                    # page = CapitalPage(d, test_link)
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    page.should_be_link("https://capital.com/trading/platform/")
                    d.back()
                    d.back()
        else:
            pytest.skip(f"The '{tab_name}' tab is not available for the '{cur_license}' license")

#
#
#
    @allure.feature("F_08 | Widget [Trading instrument]")
    @allure.story("S_08.04 | Widget [Trading instrument] tab [Cryptocurrencies] button [Trade]")
    @allure.step("Start test 'Click 'Trade' buttons on the 'Cryptocurrencies' tab 'Trading instrument' widget'.")
    @allure.title("TC_08_04 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_08_04_widget_trading_instrument(
        self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: widget "Trading instrument"
        Language: All. Licence: All.
        Widget has 2 layouts
        """
        global test_link
        global page

        time.sleep(1)

        tab_name = "Crypto"
        print(f"worker_id = {worker_id}")

        if not (cur_license == "FCA" and tab_name == "Crypto"):
            self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

            page = Markets(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            layout = page.tc08_what_is_the_current_layout()
            page.tc08_widget_trading_instrument_tab_click(layout, tab_name)
            list_buttons = page.tc08_get_list_lines_from_tab(cur_language, layout, tab_name)

            for line in range(len(list_buttons)):
                page = Markets(d, test_link)
                page.tc08_selected_tab_and_line_button_trade_click(list_buttons, line)
                if cur_role == "NoReg":
                    page = SignupLoginForm(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                    # page = CapitalPage(d, test_link)
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    page.should_be_link("https://capital.com/trading/platform/")
                    d.back()
                    d.back()
        else:
            pytest.skip(f"The '{tab_name}' tab is not available for the '{cur_license}' license")

#
#
#
    @allure.feature("F_08 | Widget [Trading instrument]")
    @allure.story("S_08.05 | Widget [Trading instrument] tab [Shares] button [Trade]")
    @allure.step("Start test 'Click 'Trade' buttons on the 'Shares' tab 'Trading instrument' widget'.")
    @allure.title("TC_08_05 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_08_05_widget_trading_instrument(
        self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: widget "Trading instrument"
        Language: All. Licence: All.
        Widget has 2 layouts
        """
        global test_link
        global page

        time.sleep(1)

        tab_name = "Shares"
        print(f"worker_id = {worker_id}")

        if not (cur_license == "FCA" and tab_name == "Crypto"):
            self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

            page = Markets(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            layout = page.tc08_what_is_the_current_layout()
            page.tc08_widget_trading_instrument_tab_click(layout, tab_name)
            list_buttons = page.tc08_get_list_lines_from_tab(cur_language, layout, tab_name)

            for line in range(len(list_buttons)):
                page = Markets(d, test_link)
                page.tc08_selected_tab_and_line_button_trade_click(list_buttons, line)
                if cur_role == "NoReg":
                    page = SignupLoginForm(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                    # page = CapitalPage(d, test_link)
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    page.should_be_link("https://capital.com/trading/platform/")
                    d.back()
                    d.back()
        else:
            pytest.skip(f"The '{tab_name}' tab is not available for the '{cur_license}' license")

#
#
#
    @allure.feature("F_08 | Widget [Trading instrument]")
    @allure.story("S_08.06 | Widget [Trading instrument] tab [Forex] button [Trade]")
    @allure.step("Start test 'Click 'Trade' buttons on the 'Forex' tab 'Trading instrument' widget'.")
    @allure.title("TC_08_06 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_08_06_widget_trading_instrument(
        self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: widget "Trading instrument"
        Language: All. Licence: All.
        Widget has 2 layouts
        """
        global test_link
        global page

        time.sleep(1)

        tab_name = "Forex"
        print(f"worker_id = {worker_id}")

        if not (cur_license == "FCA" and tab_name == "Crypto"):
            self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

            page = Markets(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            layout = page.tc08_what_is_the_current_layout()
            page.tc08_widget_trading_instrument_tab_click(layout, tab_name)
            list_buttons = page.tc08_get_list_lines_from_tab(cur_language, layout, tab_name)

            for line in range(len(list_buttons)):
                page = Markets(d, test_link)
                page.tc08_selected_tab_and_line_button_trade_click(list_buttons, line)
                if cur_role == "NoReg":
                    page = SignupLoginForm(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                    # page = CapitalPage(d, test_link)
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    page.should_be_link("https://capital.com/trading/platform/")
                    d.back()
                    d.back()
        else:
            pytest.skip(f"The '{tab_name}' tab is not available for the '{cur_license}' license")

#
#
#
    @allure.feature("F_08 | Widget [Trading instrument]")
    @allure.story("S_08.07 | Widget [Trading instrument] tab [ETFs] button [Trade]")
    @allure.step("Start test 'Click 'Trade' button on the 'ETFs' tab 'Trading instrument' widget'.")
    @allure.title("TC_08_07 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_08_07_widget_trading_instrument(
        self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: widget "Trading instrument"
        Language: All. Licence: All.
        Widget has 2 layouts
        """
        global test_link
        global page

        time.sleep(1)

        tab_name = "ETFs"
        print(f"worker_id = {worker_id}")

        if not (cur_license == "FCA" and tab_name == "Crypto"):
            self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

            page = Markets(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            layout = page.tc08_what_is_the_current_layout()
            page.tc08_widget_trading_instrument_tab_click(layout, tab_name)
            list_buttons = page.tc08_get_list_lines_from_tab(cur_language, layout, tab_name)

            for line in range(len(list_buttons)):
                page = Markets(d, test_link)
                page.tc08_selected_tab_and_line_button_trade_click(list_buttons, line)
                if cur_role == "NoReg":
                    page = SignupLoginForm(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                    # page = CapitalPage(d, test_link)
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    page.should_be_link("https://capital.com/trading/platform/")
                    d.back()
                    d.back()
        else:
            pytest.skip(f"The '{tab_name}' tab is not available for the '{cur_license}' license")

#
#
#
    @allure.feature("F_09 | Testing 'Still looking for ...' widget")
    @allure.story("S_09.01 | Testing 'Create your account' button on the 'Still looking for ...' widget")
    @allure.step("Start tests of widget 'Still looking for a broker you can trust?'.")
    @allure.title("TC_09_01 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_09_01_widget_still_looking_button_1_create_your_account(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: widget "Still looking for ..." -> button "1. Created your account"
        Language: All. Licence: All.
        """
        global test_link
        global page

        time.sleep(1)

        print(f"worker_id = {worker_id}")

        self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

        page = Markets(d, test_link)
        if not page.current_page_is(test_link):
            page.open_page()

        page.widget_still_looking_button_1_create_your_account_click(cur_language)

        if cur_role == "NoReg":
            page = SignupLoginForm(d, test_link)
            page.should_be_signup_form()
            page.close_signup_form()
        elif cur_role == "Reg_NoAuth":
            pass
        elif cur_role == "Auth":
            page.should_be_link("https://capital.com/trading/platform")
            d.back()
