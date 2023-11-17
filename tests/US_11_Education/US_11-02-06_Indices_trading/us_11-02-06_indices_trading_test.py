import pytest
import allure
import logging

from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.ButtonStartTradingInContent import ContentStartTrading
from pages.Elements.ButtonBuyInContentBlock import BuyButtonContentBlock
from pages.Elements.ButtonGetStartedOnStickyBar import GetStartedOnStickyBar
from pages.Elements.ButtonSellInContentBlock import SellButtonContentBlock
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.Elements.AssertClass import AssertClass

logger = logging.getLogger()


def pytest_generate_tests(metafunc):
    logger.info(f"====== Start Fixture generation test data ======")

    if "cur_item_link" in metafunc.fixturenames:
        file_name = "tests/US_11_Education/US_11-02-06_Indices_trading/list_of_href.txt"
        list_item_link = list()
        try:
            logger.info(f"Try reading the file with name {file_name}")
            with open(file_name, "r", encoding='UTF-8') as file:
                for line in file:
                    list_item_link.append(line[:-1])
            logger.info(f"File opened successfully")
            logger.info(f"Test data include {len(list_item_link)} Indices Trading Guide item(s)")
        except FileNotFoundError:
            logger.warning(f"There is no file with name {file_name}!")

        if len(list_item_link) == 0:
            pytest.skip("No test data: no list of links to pages")

        metafunc.parametrize("cur_item_link", list_item_link, scope="class")

    logger.info(f"====== End Fixture generation test data ======")


@pytest.mark.us_11_02_06
class TestIndicesTrading:
    page_conditions = None

    @staticmethod
    def only_four_tests(cur_item_link):
        if cur_item_link in ("https://capital.com/trade-indices",
                             "https://capital.com/trade-nasdaq",
                             "https://capital.com/ar/trade-indices",
                             "https://capital.com/de/indizeshandel",
                             "https://capital.com/es/trade-indices",
                             "https://capital.com/it/trading-su-indici",
                             "https://capital.com/cn/trade-indices"):
            logger.info(f"There is no test item on this page")
            logger.info(f"====== SKIP testing page {cur_item_link} ======")
            pytest.skip("There is no test item on this page")

    @staticmethod
    def not_for_the_sixth_test(cur_item_link):
        if cur_item_link in ("https://capital.com/trade-asx-200",
                             "https://capital.com/de/trade-asx-200",
                             "https://capital.com/de/trade-dax",
                             "https://capital.com/de/trade-nikkei225",
                             "https://capital.com/es/trade-dax",
                             "https://capital.com/it/fare-trading-nikkei-225"):
            logger.info(f"There is no test item on this page")
            logger.info(f"====== SKIP testing page {cur_item_link} ======")
            pytest.skip("There is no test item on this page")

    @allure.step("Start test of button [Start trading] on Main banner")
    def test_01_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Start Trading] on Main banner
        Language: All. License: All.
        """
        test_title = ("11.02.06", "Educations > Menu item [Indices Trading]", "01",
                      "Testing button [Start Trading] on Main banner")

        logger.info(f"====== START testing {', '.join(test_title)} ======")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc, *test_title)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerStartTrading(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        if not test_element.element_click():
            logger.warning(f"Testing element is not clicked")
            logger.info(f"====== FAIL testing {', '.join(test_title)} ======")
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, cur_item_link)

        logger.info(f"====== END testing {', '.join(test_title)} ======")

    @allure.step("Start test of button [Try demo] on Main banner")
    def test_02_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Try demo] on Main banner
        Language: All. License: All.
        """
        test_title = ("11.02.06", "Educations > Menu item [Indices Trading]",
                      "02", "Testing button [Try demo] on Main banner")

        logger.info(f"====== START testing {', '.join(test_title)} ======")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc, *test_title)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerTryDemo(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        if not test_element.element_click():
            logger.warning(f"Testing element is not clicked")
            logger.info(f"====== FAIL testing {', '.join(test_title)} ======")
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, cur_item_link, demo=True)

        logger.info(f"====== END testing {', '.join(test_title)} ======")

    @allure.step("Start test of buttons [Trade] in Most traded block")
    def test_03_most_traded_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Trade] in Most traded block
        Language: All. License: All.
        """

        test_title = ("11.02.06", "Educations > Menu item [Indices Trading]",
                      "03", "Testing button [Trade] in Most traded block")

        logger.info(f"====== START testing {', '.join(test_title)} ======")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc, *test_title)

        if cur_country == 'gb':
            logger.info(f"This test is not supported on UK location")
            logger.info(f"====== SKIP testing {', '.join(test_title)} ======")
            pytest.skip("This test is not supported on UK location")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ButtonTradeOnWidgetMostTraded(d, cur_item_link)
        test_elements_list = test_element.arrange_v2_()
        for index, element in enumerate(test_elements_list):
            logger.info(f"Testing element #{index + 1}")
            if not test_element.element_click_v2(element):
                logger.warning(f"Testing element is not clicked")
                logger.info(f"====== FAIL testing {', '.join(test_title)} ======")
                pytest.fail("Testing element is not clicked")
            check_element = AssertClass(d, cur_item_link)
            match cur_role:
                case "NoReg":
                    check_element.assert_signup(d, cur_language, cur_item_link)
                case "Reg/NoAuth":
                    check_element.assert_login(d, cur_language, cur_item_link)
                case "Auth":
                    check_element.assert_trading_platform_v3(d, cur_item_link)

        logger.info(f"====== END testing {', '.join(test_title)} ======")

    @allure.step("Start test of button [1. Create & verify your account] in Block 'Steps trading'")
    def test_04_create_and_verify_your_account_button_in_block_steps_trading(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [1. Create & verify your account] in block 'Steps trading'
        Language: All. License: All.
        """
        test_title = ("11.02.06", "Educations > Menu item [Indices Trading]", "04",
                      "Testing button [1. Create & verify your account] in Block 'Steps trading'")

        logger.info(f"====== START testing {', '.join(test_title)} ======")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc, *test_title)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BlockStepTrading(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        if not test_element.element_click():
            logger.warning(f"Testing element is not clicked")
            logger.info(f"====== FAIL testing {', '.join(test_title)} ======")
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, cur_item_link)

        logger.info(f"====== END testing {', '.join(test_title)} ======")

    @allure.step("Start test of button [Get started] on Sticky bar")
    def test_05_sticky_bar_button_get_started(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [1. Get started] on Sticky bar
        Language: All. License: All.
        """
        test_title = ("11.02.06", "Educations > Menu item [Indices Trading]",
                      "05", "Testing button [Get started] on Sticky bar")

        logger.info(f"====== START testing {', '.join(test_title)} ======")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc, *test_title)

        self.only_four_tests(cur_item_link)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = GetStartedOnStickyBar(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        if not test_element.element_click():
            logger.warning(f"Testing element is not clicked")
            logger.info(f"====== FAIL testing {', '.join(test_title)} ======")
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, cur_item_link)

        logger.info(f"====== END testing {', '.join(test_title)} ======")

    @allure.step("Start test of button [Start trading] in content block")
    def test_06_start_trading_in_content_block_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Start trading] in article
        Language: All. License: All.
        """
        test_title = ("11.02.06", "Educations > Menu item [Indices Trading]",
                      "06", "Testing button [Start trading] in Content block")

        logger.info(f"====== START testing {', '.join(test_title)} ======")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc, *test_title)

        self.only_four_tests(cur_item_link)
        self.not_for_the_sixth_test(cur_item_link)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ContentStartTrading(d, cur_item_link)
        test_elements_list = test_element.arrange_v2_()

        for index, element in enumerate(test_elements_list):
            logger.info(f"Testing element #{index + 1}")
            if not test_element.element_click_v2(element):
                logger.warning(f"Testing element is not clicked")
                logger.info(f"====== FAIL testing {', '.join(test_title)} ======")
                pytest.fail("Testing element is not clicked")

            check_element = AssertClass(d, cur_item_link)
            match cur_role:
                case "NoReg":
                    check_element.assert_signup(d, cur_language, cur_item_link)
                case "Reg/NoAuth":
                    check_element.assert_login(d, cur_language, cur_item_link)
                case "Auth":
                    check_element.assert_trading_platform_v3(d, cur_item_link)

        logger.info(f"====== END testing {', '.join(test_title)} ======")

    @allure.step("Start test of button [Sell] in content block")
    def test_07_content_block_button_sell(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [Sell] in content block
        Language: All. License: All.
        """
        test_title = ("11.02.06", "Educations > Menu item [Indices Trading]",
                      "07", "Testing button [Sell] in content block")

        logger.info(f"====== START testing {', '.join(test_title)} ======")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc, *test_title)

        self.only_four_tests(cur_item_link)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = SellButtonContentBlock(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        if not test_element.element_click(cur_role):
            logger.warning(f"Testing element is not clicked")
            logger.info(f"====== FAIL testing {', '.join(test_title)} ======")
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, cur_item_link)

        logger.info(f"====== END testing {', '.join(test_title)} ======")

    @allure.step("Start test of button [Buy] in content block")
    def test_08_content_block_button_buy(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [Buy] in content block
        Language: All. License: All.
        """
        test_title = ("11.02.06", "Educations > Menu item [Indices Trading]",
                      "08", "Testing button [Buy] in content block")

        logger.info(f"====== START testing {', '.join(test_title)} ======")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc, *test_title)

        self.only_four_tests(cur_item_link)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BuyButtonContentBlock(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        if not test_element.element_click(cur_role):
            logger.warning(f"Testing element is not clicked")
            logger.info(f"====== FAIL testing {', '.join(test_title)} ======")
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, cur_item_link)

        logger.info(f"====== END testing {', '.join(test_title)} ======")
