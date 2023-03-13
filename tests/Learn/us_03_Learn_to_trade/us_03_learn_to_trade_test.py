

import pytest
import allure
import random
from datetime import datetime
from pages.conditions import Conditions
from pages.Header.header import Header
from pages.Menu.menu import BurgerMenu
from pages.Signup_login.signup_login import SignupLogin
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


@pytest.mark.parametrize(
    "cur_login, cur_password",
    [
        ("Empty", "Empty"),
        # ("aqa.tomelo.an@gmail.com", "iT9Vgqi6d$fiZ*Z"),
    ], scope="class"
)
class Test_US_03:

    @allure.feature("F_03 | Testing header")
    @allure.story("S_01.01 | Testing 'Log In' button on the header")
    @allure.step("Start test button 'Log In' on header.")
    @allure.title("TC_03_01 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    # Установка данных в хедере.
    def test_03_01_header_button_login(
            self, d, cur_login, cur_password, cur_language, cur_license, cur_role, prob_run_tc, datetime_now):
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
            page3 = BurgerMenu(d, test_link)
            page3.burger_menu_click(d)
            page3.menu_section_learn_to_trade_click(d, cur_language)
            page3.click_learn_to_trade_item(d, cur_language)
            page3 = LearnToTrade(d, test_link)
            page3.tc_03_current_url()
            page3.tc_03_should_be_learn_to_trade_text()

            page3.tc_03_01_click_button_login()

            page3 = SignupLogin(d, test_link)
            page3.should_be_login_form()
            page3.close_login_form()
        else:
            pytest.mark.skip(f"This test not for 'Auth' role")

    @allure.feature("F_03_02 | Testing header")
    @allure.story("S_01.02 | Testing 'Trade_Now' button on the header")
    @allure.step("Start test button 'Trade_Now' on header.")
    @allure.title("TC_03_02 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_03_01_header_button_trade_now(
            self, d, cur_login, cur_password, cur_language, cur_license, cur_role, prob_run_tc, datetime_now):
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
            page3 = BurgerMenu(d, test_link)
            page3.burger_menu_click(d)
            page3.menu_section_learn_to_trade_click(d, cur_language)
            page3.click_learn_to_trade_item(d, cur_language)
            page3 = LearnToTrade(d, test_link)
            page3.tc_03_current_url()
            page3.tc_03_should_be_learn_to_trade_text()

            page3.tc_03_02_click_button_trade_now()

            page3 = SignupLogin(d, test_link)
            page3.should_be_signup_page(cur_language)
            page3.close_signup_page()
        else:
            pytest.mark.skip(f"This test not for 'Auth' role")

