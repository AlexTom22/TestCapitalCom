import pytest
import allure
from datetime import datetime

from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.ButtonDownloadAppStore import ButtonDownloadAppStore
from pages.Elements.ButtonExploreWebPlatform import ButtonExploreWebPlatform
from pages.Elements.ButtonGetItOnGooglePlay import ButtonGetItOnGooglePlay
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.conditions import Conditions
from pages.Menu.menu import MenuSection
from pages.Elements.AssertClass import AssertClass
from pages.Elements.HeaderButtonLogin import HeaderButtonLogin
from pages.Elements.HeaderButtonTrade import HeaderButtonTrade
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from src.src import CapitalComPageSrc


@pytest.fixture()
def cur_time():
    return str(datetime.now())


@pytest.mark.us_11_03_03
class TestTrendTrading:
    page_conditions = None

    # @allure.step("Start test of button [Log in] in the Header")
    # def test_01_header_button_login(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
    #         prob_run_tc):
    #     """
    #     Check: Button [Log In]
    #     Language: En. License: All.
    #     """
    #     print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.03_01")
    #
    #     build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
    #                          "11.03.03", "Education > Menu item [Trend Trading]",
    #                          "01", "Testing button [Log In] in the Header")
    #
    #     if cur_language != "":
    #         pytest.skip("This test-case only for english language")
    #
    #     page_conditions = Conditions(d, "")
    #     link = page_conditions.preconditions(
    #         d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
    #
    #     page_menu = MenuSection(d, link)
    #     page_menu.menu_education_move_focus(d, cur_language)
    #     link = page_menu.sub_menu_trend_trading_move_focus_click(d, cur_language)
    #
    #     test_element = HeaderButtonLogin(d, link)
    #     test_element.arrange_(d, cur_role, link)
    #
    #     if not test_element.element_click():
    #         pytest.fail("Testing element is not clicked")
    #
    #     test_element = AssertClass(d, link)
    #     match cur_role:
    #         case "NoReg" | "Reg/NoAuth":
    #             test_element.assert_login(d, cur_language, link)
    #         case "Auth":
    #             test_element.assert_trading_platform_v2(d, link)
    #
    # @allure.step("Start test of button [Sign up] in the Header")
    # def test_02_header_button_signup(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc, cur_time):
    #     """
    #     Check: Button [Sign up]
    #     Language: En. License: All.
    #     """
    #     print(f"\n{datetime.now()}  Работает obj {self} с именем TC_11.03.03_02")
    #
    #     link = build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
    #                                 "11.03.03", "Education > Menu item [Trend Trading]",
    #                                 "02", "Testing button [Sign up] in the Header")
    #
    #     if cur_language != "":
    #         pytest.skip("This test-case only for english language")
    #
    #     page_conditions = Conditions(d, "")
    #     page_conditions.preconditions(
    #         d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
    #
    #     page_menu = MenuSection(d, link)
    #     page_menu.menu_education_move_focus(d, cur_language)
    #     link = page_menu.sub_menu_trend_trading_move_focus_click(d, cur_language)
    #
    #     test_element = HeaderButtonTrade(d, link)
    #     test_element.arrange_(d, cur_role, link)
    #
    #     if not test_element.element_click():
    #         pytest.fail("Testing element is not clicked")
    #
    #     test_element = AssertClass(d, link)
    #     match cur_role:
    #         case "NoReg" | "Reg/NoAuth":
    #             test_element.assert_signup(d, cur_language, link)
    #         case "Auth":
    #             test_element.assert_trading_platform_v2(d, link)

    @allure.step("Start test of button [Start Trading] on the Main banner")
    def test_03_button_start_trading_main_banner(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [Start Trading]
        Language: En. License: All.
        """
        print(f"\n{datetime.now()}  Работает obj {self} с именем TC_11.03.03_03")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.03.03",
                             "Education > Menu item [Trend Trading]",
                             "03",
                             "Testing button [Start Trading] in the Main banner 'What is trend trading?'")

        if cur_language != "":
            pytest.skip("This test-case only for english language")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trend_trading_move_focus_click(d, cur_language)

        test_element = MainBannerStartTrading(d, link)
        test_element.arrange_(d, link)

        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, link)

    @allure.step("Start test of button [Try demo] on Main banner")
    def test_04_button_try_demo_main_banner(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [Try demo] on Main banner
        Language: En. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.03_04")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.03.03", "Education > Menu item [Trend Trading]",
                             "04", "Testing button [Try demo] on Main banner")

        if cur_language != "":
            pytest.skip("This test-case only for english language")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trend_trading_move_focus_click(d, cur_language)

        test_element = MainBannerTryDemo(d, link)
        test_element.arrange_(d, link)

        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, link, demo=True)

    @allure.step("Start test of buttons [Trade] in Most traded block")
    def test_05_most_traded_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [Trade] in Most traded block
        Language: En. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.03_05")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.03.03", "Education > Menu item [Trend Trading]",
                             "05", "Testing button [Trade] in Most traded block")

        if cur_country == 'gb':
            pytest.skip("This test is not supported on UK location")

        if cur_language != "":
            pytest.skip("This test-case only for english language")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trend_trading_move_focus_click(d, cur_language)

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

    @allure.step("Start test of button [Download on the App Store] in Block 'Sign up and trade smart today!'")
    def test_06_button_download_on_the_app_store(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [Download on the App Store] in Block "Sign up and trade smart today!"
        Language: En. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.03_06")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.03.03", "Education > Menu item [Trend Trading]", "06",
                             "Test button [Download on the App Store] in Block \"Sign up and trade smart today!\"")

        if cur_language != "":
            pytest.skip("This test-case only for english language")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trend_trading_move_focus_click(d, cur_language)

        test_element = ButtonDownloadAppStore(d, link)
        test_element.arrange_(link)
        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")
        test_element = AssertClass(d, link)
        test_element.assert_app_store(d, link)

    @allure.step("Start test of button [Get it on Google Play] in Block 'Sign up and trade smart today!'")
    def test_07_button_get_it_on_google_play(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [Get it on Google Play] in Block "Sign up and trade smart today!"
        Language: En. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.03_07")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.03.03", "Education > Menu item [Trend Trading]",
                             "07", "Test button [Get it on Google Play] in Block \"Sign up and trade smart today!\"")

        if cur_language != "":
            pytest.skip("This test-case only for english language")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trend_trading_move_focus_click(d, cur_language)

        test_element = ButtonGetItOnGooglePlay(d, link)
        test_element.arrange_(link)
        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, link)
        test_element.assert_google_play(d, link)

    @allure.step("Start test of button [Explore Web Platform] in Block 'Sign up and trade smart today!'")
    def test_08_button_explore_web_platform(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [Explore Web Platform] in Block "Sign up and trade smart today!"
        Language: En. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.03_08")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.03.03", "Education > Menu item [Trend Trading]",
                             "08", "Testing button [Explore Web Platform] in Block \"Sign up and trade smart today!\"")

        if cur_language != "":
            pytest.skip("This test-case only for english language")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trend_trading_move_focus_click(d, cur_language)

        test_element = ButtonExploreWebPlatform(d, link)
        test_element.arrange_(link)
        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup_form_on_the_trading_platform(d)
                #  test_element.assert_signup(d, cur_language, link)
            case "Reg/NoAuth":
                test_element.assert_login_form_on_the_trading_platform(d)
                #  test_element.assert_login(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, link)

    @allure.step("Start test of button [1. Create & verify your account] in Block 'Steps trading'")
    def test_09_create_and_verify_your_account_button_in_block_steps_trading(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [1. Create & verify your account] in block 'Steps trading'
        Language: En. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.03_09")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.03.03", "Education > Menu item [Trend Trading]",
                             "09", "Testing button [1. Create & verify your account] in Block 'Steps trading'")

        if cur_language != "":
            pytest.skip("This test-case only for english language")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trend_trading_move_focus_click(d, cur_language)

        test_element = BlockStepTrading(d, link)
        test_element.arrange_(d, link)

        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, link)
