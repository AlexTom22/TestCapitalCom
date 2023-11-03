"""
-*- coding: utf-8 -*-
@Time    : 2023/11/03 00:40
@Author  : Mike Taran
"""
import allure
import pytest
# import time
# import os
# import sys
# import psutil
# import subprocess
# from memory_profiler import profile
from pages.common import Common
import conf
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
from pages.Elements.testing_elements_locators import ButtonTradeOnWidgetMostTradedLocators
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


@pytest.mark.us_11_02_02
class TestSharesTrading:
    page_conditions = None

    @allure.step("Start test of button [Start trading] on Main banner")
    def test_01_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [Start Trading] on Main banner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.02_01")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.02", "Educations > Menu item [Shares trading]",
                             "01", "Testing button [Start Trading] on Main banner")

        if cur_language in ["el", "hu", "nl"]:
            pytest.skip(conf.MSG_SKIP_LANGUAGE)

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
                test_element.assert_trading_platform_v2(d, cur_item_link)

    @allure.step("Start test of button [Try demo] on Main banner")
    @pytest.mark.skip(reason="Этот тест пропускается, потому что ...")
    def test_02_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [Try demo] on Main banner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.02_02")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.02", "Educations > Menu item [Shares trading]",
                             "02", "Testing button [Try demo] on Main banner")

        if cur_language not in ["", "ar", "de", "es", "fr", "it", "ru", "cn"]:
            Common().skip_test_for_language(cur_language)

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
                test_element.assert_trading_platform_v2(d, cur_item_link, True)

    @allure.step("Start test of button [Start trading] in article")
    @pytest.mark.skip(reason="Этот тест пропускается, потому что ...")
    def test_03_start_trading_button_in_content(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [Start trading] in content
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.02_03")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.02", "Educations > Menu item [Shares trading]",
                             "03", "Testing button [Start trading] in article")

        if cur_language not in ["", "ar", "it"]:
            Common().skip_test_for_language(cur_language)

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
                    test_element.assert_trading_platform_v2(d, cur_item_link)

    @allure.step("Start test of button [Sell] in content block")
    @pytest.mark.skip(reason="Этот тест пропускается, потому что ...")
    def test_04_content_block_button_sell(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [Sell] in content block
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.02_04")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.02", "Educations > Menu item [Shares trading]",
                             "04", "Testing button [Sell] in content block")

        if cur_country in ["gb"]:
            Common().skip_test_for_country(cur_country)

        if cur_language not in ["", "de", "es", "it", "ru", "cn"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = SellButtonContentBlock(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click(cur_role)

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link)

    @allure.step("Start test of button [Buy] in content block")
    @pytest.mark.skip(reason="Этот тест пропускается, потому что ...")
    def test_05_content_block_button_buy(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [Buy] in content block
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.02_05")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.02", "Educations > Menu item [Shares trading]",
                             "05", "Testing button [Buy] in content block")

        if cur_country in ["gb"]:
            Common().skip_test_for_country(cur_country)

        if cur_language not in ["", "de", "es", "it", "ru", "cn"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BuyButtonContentBlock(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click(cur_role)

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link)

    @allure.step("Start test of buttons [Trade] in Most traded block")
    @pytest.mark.skip(reason="Этот тест пропускается, потому что ...")
    def test_06_most_traded_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [Trade] in Most traded block
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.02_06")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.02", "Educations > Menu item [Shares trading]",
                             "06", "Testing button [Trade] in Most traded block")

        if cur_country in ["gb"]:
            Common().skip_test_for_country(cur_country)

        if cur_language not in ["", "ar", "de", "es", "fr", "it", "ru", "cn"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        most_traded_quantity = d.find_elements(*ButtonTradeOnWidgetMostTradedLocators.MOST_TRADED_LIST)
        for i in range(len(most_traded_quantity)):
            test_element = ButtonTradeOnWidgetMostTraded(d, cur_item_link)
            test_element.arrange_v3(d, cur_item_link)

            test_element.element_click_v3(i, cur_role)

            test_element = AssertClass(d, cur_item_link)
            match cur_role:
                case "NoReg":
                    test_element.assert_signup(d, cur_language, cur_item_link)
                case "Reg/NoAuth":
                    test_element.assert_login(d, cur_language, cur_item_link)
                case "Auth":
                    test_element.assert_trading_platform_v3(d, cur_item_link)

    @allure.step("Start test of button '1. Create your account' in 'Steps trading' block")
    @pytest.mark.skip(reason="Этот тест пропускается, потому что ...")
    def test_07_block_steps_trading_button_1_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [1. Create your account] in block [Steps trading]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.02_07")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.02", "Educations > Menu item [Shares trading]",
                             "07", "Testing button [1. Create your account] in block [Steps trading]")

        if cur_language not in ["", "ar", "de", "es", "fr", "it", "ru", "cn"]:
            Common().skip_test_for_language(cur_language)

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
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link)

    @allure.step("Start test of button [Get started] on Sticky bar")
    @pytest.mark.skip(reason="Этот тест пропускается, потому что ...")
    def test_08_sticky_bar_button_get_started(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [1. Get started] on Sticky bar
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.02_08")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.02", "Educations > Menu item [Shares trading]",
                             "08", "Testing button [Get started] on Sticky bar")

        if cur_country in ["gb"]:
            Common().skip_test_for_country(cur_country)

        if cur_language not in ["", "es", "it"]:
            Common().skip_test_for_language(cur_language)

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
                test_element.assert_trading_platform_v2(d, cur_item_link)

#
# class Tools:
#     @staticmethod
#     def clear_console():
#         if psutil.WINDOWS:
#             return os.system("cls")
#         else:
#             return os.system("clear")
#
#     @staticmethod
#     def check_output(command: str):
#         try:
#             return subprocess.check_output(command, shell=True,
#                                            universal_newlines=True,
#                                            stderr=subprocess.DEVNULL)
#
#         except subprocess.CalledProcessError:
#             return False
#
#
# def _swap():
#     used = round(psutil.swap_memory().used / 1e+6)
#     all_ = round(psutil.swap_memory().total / 1e+6)
#
#     return f'{used}MiB / {all_}MiB '
#
#
# def _storage():
#     all_ = round(psutil.disk_usage('/.').total / 1e+9)
#     used = round(psutil.disk_usage('/.').used / 1e+9)
#
#     return f'{used}GiB / {all_}GiB '
