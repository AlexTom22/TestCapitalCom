from datetime import datetime
import allure
import pytest
from pages.Menu.menu import MenuSection
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.AssertClass import AssertClass
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.conditions import Conditions
from src.src import CapitalComPageSrc


@pytest.fixture()
def cur_time():
    return str(datetime.now())


"""Выбор процента проведения тестов"""


@pytest.mark.us_11_02_01
class TestMarketGuides:
    page_conditions = None

    @allure.step("Start test_11.02.01_03 button '1. Create & verify your account' on the page.")
    def test_01_create_verify_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc, cur_time):
        """
        Check: Block "Steps trading" -> button [1. Create & verify your account]
        Language: En. License: FCA. Role All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.01_01 и атрибутами:")
        print(f"\n{datetime.now()}   {self.__dict__}")

        link = build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                                    "11.02.01", "Education > Menu Item [Market guides]",
                                    "01", "Testing button [Create your account] in block [Steps trading]")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_market_guides_move_focus_click(d, cur_language)

        test_element = BlockStepTrading(d, link)
        test_element.arrange_(d, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, link)
