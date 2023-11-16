"""
-*- coding: utf-8 -*-
@Time    : 2023/00/00
@Author  : Azarov Pavel
"""
import pytest
import allure
import random  # for new method
from datetime import datetime

from conf import QTY_LINKS
from pages.Elements.AssertClass import AssertClass
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.Menu.menu import MenuSection
from pages.common import Common
from tests.build_dynamic_arg import build_dynamic_arg_v3
from pages.conditions import Conditions
from pages.Education.shares_trading_locators import SharesTradingItem
from src.src import CapitalComPageSrc

count = 1


@pytest.fixture()
def cur_time():
    """Fixture"""
    return str(datetime.now())


def check_language(cur_language):
    if cur_language not in ["hu", "nl", "el"]:
        return
    pytest.skip(f"This test is not for {cur_language} language")


def check_country(cur_country):
    if cur_country in ["gb"]:
        pytest.skip(f"This test is not for {cur_country} country")


@pytest.mark.us_11_02_02
class TestSharesTrading:
    page_conditions = None

    @allure.step("Start test of button [Start trading] on Main banner")
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_01_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc, cur_time):
        """
        Check: Button [Start Trading] on Main banner
        Language: All (Except: EL, HU, NL). License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.02_01")

        cur_item_link = build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                                             "11.02.02", "Educations > Menu item [Shares trading]",
                                             ".00_01", "Testing button [Start Trading] on Main banner")

        check_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, cur_item_link)
        page_menu.menu_education_move_focus(d, cur_language)
        cur_item_link = page_menu.sub_menu_shares_trading_move_focus_click(d, cur_language)
        del page_menu

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
            prob_run_tc):
        """
        Check: Button [Try demo] on Main banner
        Language: All (Except: EL, HU, NL). License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.02_02")
        cur_item_link = build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                                             "11.02.02", "Educations > Menu item [Shares trading]",
                                             ".00_02", "Testing button [Try demo] on Main banner")

        check_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, cur_item_link)
        page_menu.menu_education_move_focus(d, cur_language)
        cur_item_link = page_menu.sub_menu_shares_trading_move_focus_click(d, cur_language)
        del page_menu

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

    @allure.step("Start test of buttons [Trade] in Most traded block")
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_06_most_traded_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc):
        """
        Check: Button [Trade] in Most traded block
        Language: All (Except: EL, HU, NL). License: All (Except: FCA).
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.02_06")
        cur_item_link = build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                                             "11.02.02", "Educations > Menu item [Shares trading]",
                                             ".00_06", "Testing button [Trade] in Most traded block")

        check_language(cur_language)
        check_country(cur_country)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, cur_item_link)
        page_menu.menu_education_move_focus(d, cur_language)
        cur_item_link = page_menu.sub_menu_shares_trading_move_focus_click(d, cur_language)
        del page_menu

        test_element = ButtonTradeOnWidgetMostTraded(d, cur_item_link)
        test_element.clear_chart_list()
        num_item = test_element.arrange_v4(cur_item_link)
        random_indexes = random.sample(range(0, num_item), 2)
        counter = 0
        for i, index in enumerate(random_indexes):
            if counter:
                test_element.clear_chart_list()
                test_element.arrange_v4(cur_item_link)

            print(f"\n{datetime.now()}   Testing Most traded random element #{i + 1}")
            trade_instrument = test_element.element_click_v4(index)
            if not trade_instrument:
                pytest.fail("Testing element is not clicked")

            check_element = AssertClass(d, cur_item_link)
            counter += 1
            match cur_role:
                case "NoReg":
                    check_element.assert_signup(d, cur_language, cur_item_link)
                case "Reg/NoAuth":
                    check_element.assert_login(d, cur_language, cur_item_link)
                case "Auth":
                    check_element.assert_trading_platform_v4(d, cur_item_link, False, True, trade_instrument)

    @allure.step("Start test of button '1. Create your account' in 'Steps trading' block")
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_08_block_steps_trading_button_1_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc):
        """
        Check: Button [1. Create your account] in block [Steps trading]
        Language: All (Except: EL, HU, NL). License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.02_08")
        cur_item_link = build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                                             "11.02.02", "Educations > Menu item [Shares trading]",
                                             ".00_08",
                                             "Testing button [1. Create your account] in block [Steps trading]")

        check_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, cur_item_link)
        page_menu.menu_education_move_focus(d, cur_language)
        cur_item_link = page_menu.sub_menu_shares_trading_move_focus_click(d, cur_language)
        del page_menu

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

    @allure.step("Start pretest: collect the trade instrument list")
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_99_shares_trading_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        global count

        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.02")

        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.02.02", "Educations > Menu item [Shares trading]",
                             ".00_99", "Pretest for US_11.02.02.01")

        if cur_language in ["ar"]:
            Common().skip_test_for_language(cur_language)

        if count == 0:
            pytest.skip("The list of Share Trading links is already created")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_shares_trading_move_focus_click(d, cur_language)
        del page_menu

        # Записываем ссылки в файл
        file_name = "tests/US_11_Education/US_11-02-02_Shares_trading/list_of_href.txt"
        list_items = d.find_elements(*SharesTradingItem.ITEM_LIST)

        count_in = len(list_items)
        print(f"{datetime.now()}   Shares trading include {count_in} item(s) on page")
        file = None

        try:
            file = open(file_name, "w")
            count_out = 0
            if count_in > 0:
                for i in range(QTY_LINKS):
                    if i < count_in:
                        k = random.randint(1, count_in - 1)
                        item = list_items[k]
                        file.write(item.get_property("href") + "\n")
                        print(f"{datetime.now()}   {item.get_property('href')}")
                        count_out += 1
        finally:
            file.close()
            del file

        print(f"{datetime.now()}   Test data include {count_out} item(s)")
        if count_in != 0:
            print(f"{datetime.now()}   The test coverage = {count_out / count_in * 100} %")
        else:
            print(f"{datetime.now()}   The test coverage = 0 %")

        count -= 1
