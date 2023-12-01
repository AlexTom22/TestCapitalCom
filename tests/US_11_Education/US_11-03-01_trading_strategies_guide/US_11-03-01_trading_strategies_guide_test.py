import allure
import conf
import pytest
from datetime import datetime
import random  # for new method

from pages.Education.Trading_strategies_guide_locators import TradingStrategiesContentList
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.common import Common
from tests.build_dynamic_arg import build_dynamic_arg_v3
from pages.Menu.menu import MenuSection
from pages.conditions import Conditions
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.AssertClass import AssertClass
from src.src import CapitalComPageSrc

count = 1


@pytest.fixture()
def cur_time():
    return str(datetime.now())


@pytest.mark.us_11_03_01
class TestTradingStrategiesGuides:
    page_conditions = None

    @allure.step("Start test_11.03.01_01 of button [Start Trading] on Main banner")
    def test_01_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Start Trading]
        Language: All. License: All.
        """
        link = build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                                    "11.03.01",
                                    "Education > Menu item [Trading Strategies Guides]",
                                    "_01",
                                    "Testing button [Start Trading] on Main banner")

        if cur_language not in ["", "de", "es", "it", "cn", "zh", "ru"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)

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

    @allure.step("Start test_11.03.01_02 of button [Try demo] on Main banner")
    def test_02_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Try demo] on Main banner
        Language: All. License: All.
        """
        link = build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                                    "11.03.01",
                                    "Education > Menu item [Trading Strategies Guides]",
                                    "_02",
                                    "Testing button [Try demo] on Main banner")

        if cur_language not in ["", "de", "es", "it", "cn", "zh", "ru"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)

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
                test_element.assert_trading_platform_v3(d, link, True)

    @allure.step("Start test_11.03.01_03 of buttons [Trade] in Most traded block")
    def test_03_most_traded_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Trade] in Most traded block
        Language: All. License: All.
        """
        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.03.01",
                             "Education > Menu item [Trading Strategies Guides]",
                             "_03",
                             "Testing button [Trade] in Most traded block")

        if cur_country == 'gb':
            pytest.skip("This test is not supported on UK location")

        if cur_language not in ["", "de", "es", "it", "cn", "zh", "ru"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)

        test_element = ButtonTradeOnWidgetMostTraded(d, link)
        test_elements_list = test_element.arrange_v2_()
        for index, element in enumerate(test_elements_list):
            print(f"\n{datetime.now()}   Testing element #{index + 1}")
            if not test_element.element_click_v2(element):
                pytest.fail("Testing element is not clicked")
            check_element = AssertClass(d, link)
            match cur_role:
                case "NoReg":
                    check_element.assert_signup(d, cur_language, link)
                case "Reg/NoAuth":
                    check_element.assert_login(d, cur_language, link)
                case "Auth":
                    check_element.assert_trading_platform_v3(d, link)

    @allure.step("Start test_11.03.01_04 button 'Create_verify_your_account' on the page.")
    def test_04_create_verify_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Steps trading -> button [1. Create your account]
        Language: All. License: All.
        """
        link = build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                                    "11.03.01",
                                    "Education > Menu item [Trading Strategies Guides]",
                                    "_04",
                                    "Testing button [1. Create your account] in block [Steps trading]")

        if cur_language not in ["", "de", "es", "it", "cn", "zh", "ru"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)

        test_element = BlockStepTrading(d, link)
        test_element.arrange_(d, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, link)

    @allure.step("Start pretest")
    def test_99_trading_strategies_guide_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):

        global count

        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.03.01", "Education > Menu item [Trading Strategies Guides]",
                             "_99", "Pretest for US_11.03.01.01")

        if cur_language not in ["", "de", "es", "it", "zh", "ru"]:
            Common().skip_test_for_language(cur_language)

        if count == 0:
            pytest.skip("The list of Trading courses links is already created")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)
        del page_menu

        # Записываем ссылки в файл
        name_file = "tests/US_11_Education/US_11-03-01_trading_strategies_guide/list_of_href.txt"
        list_items = d.find_elements(*TradingStrategiesContentList.LISTS)

        count_in = len(list_items)
        print(f"{datetime.now()}   Trading Strategies Guide page include {count_in} lists item(s)")  # for new method
        file = None

        try:
            file = open(name_file, "w")
            count_out = 0
            if count_in > 0:
                for i in range(conf.QTY_LINKS):
                    if i < count_in:
                        k = random.randint(1, count_in)
                        item = list_items[k - 1]
                        file.write(item.get_property("href") + "\n")
                        count_out += 1
        finally:
            file.close()
            del file

        print(f"{datetime.now()}   Test data include {count_out} item(s)")
        if count_in != 0:
            print(f"{datetime.now()}   The test coverage = {count_out/count_in*100} %")
        else:
            print(f"{datetime.now()}   The test coverage = 0 %")

        count -= 1
