"""
-*- coding: utf-8 -*-
@Time    : 2023/04/19 17:00 GMT+3
@Author  : Suleyman Alirzaev
"""
import pytest
import allure
# import sys
# from memory_profiler import profile
from datetime import datetime
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.Elements.BlockStepTrading import BlockStepTrading
# from pages.Elements.ButtonSellInContentBlock import SellButtonContentBlock
# from pages.Elements.ButtonBuyInContentBlock import BuyButtonContentBlock
from pages.Elements.ButtonsSellBuyInContentBlock import ButtonsSellBuyInContentBlock
from pages.Elements.ButtonGetStartedOnStickyBar import GetStartedOnStickyBar
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.Elements.ButtonStartTradingInContent import ContentStartTrading
from pages.Elements.ButtonCreateAccountBlockOpenAccountIn3min import ButtonCreateAccountInBlockOpenAccountIn3min
# from pages.Elements.ButtonSignupLoginOnPage import PageSignUpLogin
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import ButtonTradeOnWidgetMostTradedLocators

count = 1


def pytest_generate_tests(metafunc):
    """
    Fixture generation test data
    """
    if "cur_item_link" in metafunc.fixturenames:
        file_name = "tests/US_11_Education/US_11-02-03_Commodities_trading/list_of_href.txt"

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
            pytest.exit("Отсутствуют тестовые данные: нет списка ссылок на страницы")

        metafunc.parametrize("cur_item_link", list_item_link, scope="class")


@pytest.mark.us_11_02_03
class TestCommoditiesTrading:
    page_conditions = None

    def check_language(self, cur_language):
        if cur_language in ["", "ar", "de", "es", "fr", "it", "nl", "pl", "ro", "ru", "zh", "cn"]:
            return
        pytest.skip(f"This test is not for {cur_language} language")

    def check_country(self, cur_country):
        if cur_country in ["gb"]:
            pytest.skip(f"This test is not for {cur_country} country")

    @allure.step("Start test of button [Start trading] on Main banner")
    def test_01_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Start Trading] on Main banner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_01")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.03", "Educations > Menu item [Commodities trading]",
                             "01", "Testing button [Start Trading] on Main banner")

        self.check_language(cur_language)

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
                test_element.assert_trading_platform_v3(d, cur_item_link)

    @allure.step("Start test of button [Try demo] on Main banner")
    # @profile(precision=3)
    def test_02_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Try demo] on Main banner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_02")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.03", "Educations > Menu item [Commodities trading]",
                             "02", "Testing button [Try demo] on Main banner")

        self.check_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerTryDemo(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        # test_element.assert_signup(d, cur_language, cur_role, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, cur_item_link)

    @allure.step("Start test of button [Sell] in content block")
    # @profile(precision=3)
    def test_03_content_block_button_sell(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [1. Sell] in content block
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_03")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.03", "Educations > Menu item [Commodities trading]",
                             "03", "Testing button [Sell] in content block")

        self.check_language(cur_language)
        self.check_country(cur_country)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        if cur_country != 'gb':
            # test_element = SellButtonContentBlock(d, cur_item_link)
            test_element = ButtonsSellBuyInContentBlock(d, cur_item_link)
            test_element.arrange_(cur_item_link, button='sell')

            test_element.element_click(cur_role)

            test_element = AssertClass(d, cur_item_link)
            # test_element.assert_signup(d, cur_language, cur_role, cur_item_link)
            match cur_role:
                case "NoReg":
                    test_element.assert_signup(d, cur_language, cur_item_link)
                case "Reg/NoAuth":
                    test_element.assert_login(d, cur_language, cur_item_link)
                case "Auth":
                    test_element.assert_trading_platform_v3(d, cur_item_link)
        else:
            pytest.skip("This test not for FCA licence.")

    @allure.step("Start test of button [Buy] in content block")
    # @profile(precision=3)
    def test_04_content_block_button_buy(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [1. Buy] in content block
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_04")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.03", "Educations > Menu item [Commodities trading]",
                             "04", "Testing button [Buy] in content block")

        self.check_language(cur_language)
        self.check_country(cur_country)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        if cur_country != 'gb':
            # test_element = BuyButtonContentBlock(d, cur_item_link)
            test_element = ButtonsSellBuyInContentBlock(d, cur_item_link)
            test_element.arrange_(cur_item_link, button='buy')

            test_element.element_click(cur_role)

            test_element = AssertClass(d, cur_item_link)
            # test_element.assert_signup(d, cur_language, cur_role, cur_item_link)
            match cur_role:
                case "NoReg":
                    test_element.assert_signup(d, cur_language, cur_item_link)
                case "Reg/NoAuth":
                    test_element.assert_login(d, cur_language, cur_item_link)
                case "Auth":
                    test_element.assert_trading_platform_v3(d, cur_item_link)
        else:
            pytest.skip("This test not for FCA licence.")

    @allure.step("Start test of button [Start trading] in article")
    # @profile(precision=3)
    def test_05_start_trading_in_article_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Start trading] in article
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_05")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.03", "Educations > Menu item [Commodities trading]",
                             "05", "Testing button [Start trading] in article")

        self.check_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ContentStartTrading(d, cur_item_link)
        test_element.arrange_(cur_item_link)

        test_element.element_click(cur_item_link, cur_language, cur_role)

    @allure.step("Start test of buttons [Trade] in Most traded block")
    # @profile(precision=3)
    def test_06_most_traded_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Trade] in Most traded block
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_06")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.03", "Educations > Menu item [Commodities trading]",
                             "06", "Testing button [Trade] in Most traded block")

        self.check_language(cur_language)
        self.check_country(cur_country)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        if cur_country != 'gb':
            most_traded_quantity = d.find_elements(*ButtonTradeOnWidgetMostTradedLocators.MOST_TRADED)
            for i in range(len(most_traded_quantity)):
                test_element = ButtonTradeOnWidgetMostTraded(d, cur_item_link)
                test_element.arrange_v3(d, cur_item_link)

                # test_element.element_click(cur_item_link, cur_language, cur_role)
                test_element.element_click_v3(i, cur_role)

                test_element = AssertClass(d, cur_item_link)
                match cur_role:
                    case "NoReg":
                        # test_element.assert_signup(d, cur_language, cur_role, cur_item_link)
                        test_element.assert_signup(d, cur_language, cur_item_link)
                    case "Reg/NoAuth":
                        test_element.assert_login(d, cur_language, cur_item_link)
                    case "Auth":
                        test_element.assert_trading_platform_v3(d, cur_item_link)
        else:
            pytest.skip("This test not for FCA licence.")

    @allure.step("Start test of button [Get started] on Sticky bar")
    # @profile(precision=3)
    def test_07_sticky_bar_button_get_started(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [1. Get started] on Sticky bar
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_07")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.03", "Educations > Menu item [Commodities trading]",
                             "07", "Testing button [Get started] on Sticky bar")

        self.check_language(cur_language)
        self.check_country(cur_country)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = GetStartedOnStickyBar(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        # test_element.assert_signup(d, cur_language, cur_role, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, cur_item_link)

    @allure.step("Start test of button [Create your account] in block [Steps trading]")
    # @profile(precision=3)
    def test_08_block_steps_trading_button_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [1. Create your account] in block [Steps trading]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_08")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.03", "Educations > Menu item [Commodities trading]",
                             "08", "Testing button [Create your account] in block [Steps trading]")

        self.check_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        if cur_country != 'gb':
            test_element = BlockStepTrading(d, cur_item_link)
            test_element.arrange_(d, cur_item_link)

            test_element.element_click()

            test_element = AssertClass(d, cur_item_link)
            # test_element.assert_signup(d, cur_language, cur_role, cur_item_link)
            match cur_role:
                case "NoReg" | "Reg/NoAuth":
                    test_element.assert_signup(d, cur_language, cur_item_link)
                case "Auth":
                    test_element.assert_trading_platform_v3(d, cur_item_link)
        else:
            pytest.skip("This test not for FCA licence.")

    # @pytest.skip
    @allure.step("Start test of button [Create account] in block [Open a trading account in less than 3 minutes]")
    def test_09_block_open_account_3_min_button_create_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [Create account] in block [Open a trading account in less than 3 minutes]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_09")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.03", "Educations > Menu item [Commodities trading]",
                             "09", "Testing buttons [Create account] "
                                   "in block [Open a trading account in less than 3 minutes]")

        if cur_language not in ["de", "es", "it", "pl"]:
            pytest.skip(f"This test is not for {cur_language} language")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ButtonCreateAccountInBlockOpenAccountIn3min(d, cur_item_link)
        test_element.arrange_(cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, cur_item_link, True)

    # @allure.step("Start test of buttons [Sign up] on page")
    # # @profile(precision=3)
    # def test_05_sign_up_on_page_button(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
    #         prob_run_tc):
    #     """
    #     Check: Buttons [Sign up] on page
    #     Language: All. License: All.
    #     """
    #     print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_07")
    #     build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
    #                          "11.02.03", "Educations > Menu item [Commodities trading]",
    #                          "07", "Testing buttons [Sign up] on page")
    #
    #     page_conditions = Conditions(d, "")
    #     page_conditions.preconditions(
    #         d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
    #
    #     test_element = PageSignUpLogin(d, cur_item_link)
    #     test_element.arrange_(d, cur_item_link)
    #
    #     test_element.element_click(cur_item_link, cur_language, cur_role)
    #
