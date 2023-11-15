"""
-*- coding: utf-8 -*-
@Time    : 2023/11/03 00:40
@Author  : Mike Taran
"""
import allure
import pytest
from pages.Elements.ButtonOnHorizontalBanner import ButtonOnHorizontalBanner
import random
# import time
# import os
# import sys
# import psutil
# import subprocess
# from memory_profiler import profile
from pages.common import Common
# import conf
from datetime import datetime
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.conditions import Conditions
# from pages.Elements.HeaderButtonLogin import HeaderButtonLogin
# from pages.Elements.HeaderButtonTrade import HeaderButtonTrade
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.Elements.ButtonStartTradingInContent import ContentStartTrading
from pages.Elements.ButtonSellInContentBlock import SellButtonContentBlock
from pages.Elements.ButtonBuyInContentBlock import BuyButtonContentBlock
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.ButtonGetStartedOnStickyBar import GetStartedOnStickyBar
# from pages.Elements.ButtonFreeDemoOnHorizontalBanner import ButtonFreeDemoOnHorizontalBanner
from pages.Elements.AssertClass import AssertClass
from src.src import CapitalComPageSrc


def pytest_generate_tests(metafunc):
    """
    Fixture generation test data
    """
    if "cur_item_link" in metafunc.fixturenames:
        file_name = "tests/US_11_Education/US_11-02-02_Shares_trading/list_of_href.txt"

        list_item_link = list()
        try:
            file = open(file_name, "r")
        except FileNotFoundError:
            print(f"{datetime.now()}   There is no file with name {file_name}!")
        else:
            for line in file:
                list_item_link.append(line[:-1])
            file.close()

        if len(list_item_link) == 0:
            pytest.skip("Отсутствуют тестовые данные: нет списка ссылок на страницы")

        metafunc.parametrize("cur_item_link", list_item_link, scope="class")


def check_language(cur_language):
    if cur_language not in ["hu", "nl", "el"]:
        return
    pytest.skip(f"This test is not for {cur_language} language")


def check_country(cur_country):
    if cur_country in ["gb"]:
        pytest.skip(f"This test is not for {cur_country} country")


num_tc = "01"


@pytest.mark.us_11_02_02
class TestSharesTrading:
    page_conditions = None

    @allure.step("Start test of button [Start trading] on Main banner")
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_01_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [Start Trading] on Main banner
        Language: All (Except: EL, HU, NL). License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.02_01")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.02", "Educations > Menu item [Shares trading]", num_tc,
                             "Testing button [Start Trading] on Main banner")

        check_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerStartTrading(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link)

    @allure.step("Start test of button [Try demo] on Main banner")
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_02_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [Try demo] on Main banner
        Language: All (Except: EL, HU, NL). License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.02_02")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.02", "Educations > Menu item [Shares trading]",
                             "02", "Testing button [Try demo] on Main banner")

        check_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerTryDemo(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link, True)

    @allure.step("Start test of button [Sell] in content block")
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_03_content_block_button_sell(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [Sell] in content block
        Language: All (Except: EL, HU, NL, AR, ZH, CN). License: All (Except: FCA).
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.02_03")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.02", "Educations > Menu item [Shares trading]",
                             "03", "Testing button [Sell] in content block")

        check_language(cur_language)
        if cur_language in ["ar", "zh", "cn"]:
            Common().skip_test_for_language(cur_language)
        check_country(cur_country)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = SellButtonContentBlock(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        trade_instrument = test_element.element_click(cur_role)

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link, False, True, trade_instrument)

    @allure.step("Start test of button [Buy] in content block")
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_04_content_block_button_buy(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [Buy] in content block
        Language: All (Except: EL, HU, NL, AR, ZH, CN). License: All (Except: FCA).
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.02_04")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.02", "Educations > Menu item [Shares trading]",
                             "04", "Testing button [Buy] in content block")

        check_language(cur_language)
        if cur_language in ["ar", "zh", "cn"]:
            Common().skip_test_for_language(cur_language)
        check_country(cur_country)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BuyButtonContentBlock(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        trade_instrument = test_element.element_click(cur_role)

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link, False, True, trade_instrument)

    @allure.step("Start test of button [Start trading] in article")
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_05_start_trading_button_in_content(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [Start trading] in content
        Language: All (Except: EL, HU, NL). License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.02_05")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.02", "Educations > Menu item [Shares trading]",
                             "05", "Testing button [Start trading] in article")

        check_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ContentStartTrading(d, cur_item_link)
        qty = test_element.arrange_v3(cur_item_link)

        for i in range(qty):
            test_element.element_click_v3(i)

            test_element = AssertClass(d, cur_item_link)
            match cur_role:
                case "NoReg":
                    test_element.assert_signup(d, cur_language, cur_item_link)
                case "Reg/NoAuth":
                    test_element.assert_login(d, cur_language, cur_item_link)
                case "Auth":
                    test_element.assert_trading_platform_v4(d, cur_item_link)

    @allure.step("Start test of buttons [Trade] in Most traded block")
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_06_most_traded_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [Trade] in Most traded block
        Language: All (Except: EL, HU, NL). License: All (Except: FCA).
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.02_06")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.02", "Educations > Menu item [Shares trading]",
                             "06", "Testing button [Trade] in Most traded block")

        check_language(cur_language)
        check_country(cur_country)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ButtonTradeOnWidgetMostTraded(d, cur_item_link)
        test_element.clear_chart_list()
        num_item = test_element.arrange_v4(cur_item_link)
        random_indexes = random.sample(range(0, num_item), 2)
        count = 0
        for i, index in enumerate(random_indexes):
            if count:
                test_element.clear_chart_list()
                test_element.arrange_v4(cur_item_link)

            print(f"\n{datetime.now()}   Testing Most traded random element #{i + 1}")
            trade_instrument = test_element.element_click_v4(index)
            if not trade_instrument:
                pytest.fail("Testing element is not clicked")

            check_element = AssertClass(d, cur_item_link)
            count += 1
            match cur_role:
                case "NoReg":
                    check_element.assert_signup(d, cur_language, cur_item_link)
                case "Reg/NoAuth":
                    check_element.assert_login(d, cur_language, cur_item_link)
                case "Auth":
                    check_element.assert_trading_platform_v4(d, cur_item_link, False, True, trade_instrument)

    @allure.step("Start test of button [Get started] on Sticky bar")
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_07_sticky_bar_button_get_started(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [1. Get started] on Sticky bar
        Language: All (Except: EL, HU, NL, AR, ZH, CN). License: All (Except: FCA).
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.02_07")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.02", "Educations > Menu item [Shares trading]",
                             "07", "Testing button [Get started] on Sticky bar")

        check_language(cur_language)
        if cur_language in ["ar", "zh", "cn"]:
            Common().skip_test_for_language(cur_language)
        check_country(cur_country)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = GetStartedOnStickyBar(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link)

    @allure.step("Start test of button '1. Create your account' in 'Steps trading' block")
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_08_block_steps_trading_button_1_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [1. Create your account] in block [Steps trading]
        Language: All (Except: EL, HU, NL). License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.02_08")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.02", "Educations > Menu item [Shares trading]",
                             "08", "Testing button [1. Create your account] in block [Steps trading]")

        check_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BlockStepTrading(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link)

    @allure.step("Start test of button in block [Horizontal banner]")
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_09_block_hor_banner_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [Create account] in block [Open a trading account in less than 3 minutes]
        Language: All (Except: EN, EL, HU, NL). License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_09")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.02", "Educations > Menu item [Shares trading]",
                             "09", "Testing button"
                                   "in block [Horizontal banner]")

        check_language(cur_language)
        if cur_language in [""]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ButtonOnHorizontalBanner(d, cur_item_link)
        test_element.arrange_(cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link, False)
