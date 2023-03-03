import pytest
import allure
import random
from tests.conditions import Conditions
from pages.header import Header
from pages.menu import MenuBurger
from pages.signup_login import SignupLogin
from pages.Learn.learn_to_trade import LearnToTrade
from src.src import (
    CapitalComPageSrc,
    # TradingViewPageSrc,
    # ESGPageSrc,
    # LearnToTradePageSrc,
    # ProfessionalClientsAu,
)


# Процент проведения тестов
@pytest.fixture()
def prob_run_tc():
    prob = 100
    if random.randint(1, 100) <= prob:
        return ""
    else:
        return f"Тест не попал в {prob}% выполняемых тестов.≠"


class Test_US_03:

    @allure.feature("F_03 | Testing header")
    @allure.story("S_01.01 | Testing 'Log In' button on the header")
    @allure.step("Start test button 'Log In' on header.")
    @allure.title("TC_03_01 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    # Установка данных в хедере.
    def test_03_01_header_button_login(
            self, d, cur_login, cur_password, cur_language, cur_license, cur_role, prob_run_tc, datetime_now
    ):
        """
        Check: Header -> button [Log In]
        Language: En. License: FCA.
        """
        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        page3 = Conditions(d, "")
        test_link = page3.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )

        if cur_role == "NoReg":
            page3 = Header(d, test_link)
            if not page3.current_page_is(test_link):
                page3.open_page()
            page3 = MenuBurger(d, test_link)
            page3.click_menu_burger()
            page3.click_sub_menu_learn_to_trade()
            page3.click_learn_to_trade_item()
            page3 = LearnToTrade(d, test_link)
            page3.tc_03_should_be_learn_to_trade_text()

            page3.tc_03_01_click_button_login()

            page3 = SignupLogin(d, test_link)
            page3.should_be_login_form()
            page3.close_login_form()
        else:
            pytest.mark.skip(f"This test not for 'Auth' role")
