"""
-*- coding: utf-8 -*-
@Time    : 2023/07/28 18:15 GMT+3
@Author  : Aleksandr Tomelo
"""

import random
import pytest
import allure
from datetime import datetime
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
# from pages.Elements.ButtonSignupLoginOnPage import PageSignUpLogin
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import ButtonTradeOnWidgetMostTradedLocators
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.Menu.menu import MenuSection


def check_language(cur_language, list_languages):
    if cur_language not in list_languages:
        pytest.skip(f"This test is not for '{cur_language}' language")


def check_country(cur_country, list_countries):
    if cur_country in list_countries:
        pytest.skip(f"This test is not for '{cur_country}' country")


@pytest.mark.us_11_02_07
class TestETFTrading:
    page_conditions = None

    @allure.step("Start test of button [Start trading] on Main banner")
    def test_01_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [Start Trading] on Main banner
        Language: All. License: All. Role: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.07_01")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.07", "Educations > Menu item [ETF trading]",
                             "01", "Testing button [Start Trading] on Main banner")

        check_language(cur_language, ["", "ar", "de", "es", "it", "ru", "cn"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_etf_trading_move_focus_click(d, cur_language)

        test_element = MainBannerStartTrading(d, link)
        test_element.arrange_(d, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, link)

    @allure.step("Start test of button [Try demo] on Main banner")
    def test_02_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [Try demo] on Main banner
        Language: All. License: All. Role: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.07_02")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.07", "Educations > Menu item [ETF trading]",
                             "02", "Testing button [Try demo] on Main banner")

        check_language(cur_language, ["", "ar", "de", "es", "it", "ru", "cn"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_etf_trading_move_focus_click(d, cur_language)

        test_element = MainBannerTryDemo(d, link)
        test_element.arrange_(d, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, link)

    @allure.step("Start test of buttons [Trade] in Most traded block")
    def test_03_most_traded_widget_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [Trade] in Most traded widget
        Language: All. License: All. Role: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.07_03")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.07", "Educations > Menu item [ETF trading]",
                             "03", "Testing button [Trade] in Most traded widget")

        check_country(cur_country, ["gb"])
        check_language(cur_language, ["", "ar", "de", "es", "it", "ru", "cn"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_etf_trading_move_focus_click(d, cur_language)

        most_traded_list = d.find_elements(*ButtonTradeOnWidgetMostTradedLocators.MOST_TRADED_LIST)
        for _ in range(2):
            test_element = ButtonTradeOnWidgetMostTraded(d, link)
            test_element.arrange_v3(d, link)

            i = random.randint(0, len(most_traded_list) - 1)
            print(f"\n{datetime.now()}   Random index = {i}")
            sel_item = test_element.element_click_v3(i, cur_role)
            sel_operation = None

            test_element = AssertClass(d, link)
            match cur_role:
                case "NoReg":
                    test_element.assert_signup(d, cur_language, link)
                case "Reg/NoAuth":
                    test_element.assert_login(d, cur_language, link)
                case "Auth":
                    test_element.assert_trading_platform_v3(d, link)

    # @allure.step("Start test of buttons [Sign up] on page")
    # def test_04_sign_up_on_page_button(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
    #     """
    #     Check: Button [Start trading] in article
    #     Language: All. License: All.
    #     """
    #     build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
    #                          "11.02.07", "Educations > Menu item [ETF trading]",
    #                          "04", "Testing buttons [Sign up] on page")
    #
    #     check_language(cur_language, ["", "ar", "de", "es", "it", "ru", "cn"])
    #
    #     page_conditions = Conditions(d, "")
    #     link = page_conditions.preconditions(
    #         d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
    #
    #     page_menu = MenuSection(d, link)
    #     page_menu.menu_education_move_focus(d, cur_language)
    #     link = page_menu.sub_menu_etf_trading_move_focus_click(d, cur_language)
    #
    #     test_element = PageSignUpLogin(d, link)
    #     test_element.arrange_(d, link)
    #
    #     test_element.element_click(link, cur_language, cur_role)

    @allure.step("Start test of button [Create your account] in block [Steps trading]")
    def test_05_block_steps_trading_button_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [1. Create your account] in block [Steps trading]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.07_05")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.07", "Educations > Menu item [ETF trading]",
                             "05", "Testing button [1. Create & verify your account] in block [Steps trading]")

        check_language(cur_language, ["", "ar", "de", "es", "it", "ru", "cn"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_etf_trading_move_focus_click(d, cur_language)

        test_element = BlockStepTrading(d, link)
        test_element.arrange_(d, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, link)
