# -*- coding: utf-8 -*-
# @Time    : 2022/11/22 10:00
# @Author  : Alexander Tomelo

# import time
import pytest
import allure
import random
# from datetime import datetime
from tests.conditions import Conditions
# from pages.base_page import BasePage
from pages.Capital.capital import Capital
from pages.header import Header
# from pages.user_panel import UserPanel
from pages.Signup_login.signup_login import SignupLogin
from src.src import (
    CapitalComPageSrc,
    # TradingViewPageSrc,
    # ESGPageSrc,
    # LearnToTradePageSrc,
    # ProfessionalClientsAu,
)


@pytest.fixture()
def prob_run_tc():
    prob = 100
    if random.randint(1, 100) <= prob:
        return ""
    else:
        return f"Тест не попал в {prob}% выполняемых тестов.≠"


@pytest.mark.us_01
@pytest.mark.parametrize(
    "cur_login, cur_password",
    [
        ("Empty", "Empty"),
        # ("aqa.tomelo.an@gmail.com", "iT9Vgqi6d$fiZ*Z"),
    ], scope="class"
)
@allure.epic("US_01 | Testing 'Log In' / 'Signup' elements on the main page capital.com")
class Test_US_01:
    
    @allure.feature("F_01 | Testing header")
    @allure.story("S_01.01 | Testing 'Log In' button on the header")
    @allure.step("Start test button 'Log In' on header.")
    @allure.title("TC_01_01 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_01_01_header_button_login(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role, prob_run_tc, datetime_now
    ):
        """
        Check: Header -> button [Log In]
        Language: All. License: All.
        """
        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        print(f"worker_id = {worker_id}")

        page = Conditions(d, "")
        test_link = page.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )

        if cur_role != "Auth":
            page = Header(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()
            page.header_button_login_click()

            if cur_role == "NoReg":
                page = SignupLogin(d, test_link)
                page.should_be_login_form()
                page.close_login_form()
        else:
            pytest.mark.skip(f"This test not for 'Auth' role")

#
#
#
    @allure.feature("F_01 | Testing header")
    @allure.story("S_01.02 | Testing 'Trade Now' button on the header")
    @allure.step("Start test button 'Trade Now' on header.")
    @allure.title("TC_01_02 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_01_02_header_button_trade_now(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: Header -> button [Trade Now]
        Language: All. License: All.
        """
        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        print(f"worker_id = {worker_id}")

        page = Conditions(d, "")
        test_link = page.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )

        if cur_role != "Auth":
            page = Header(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            page.header_button_signup_click()

            if cur_role == "NoReg":
                page = SignupLogin(d, test_link)
                page.should_be_signup_form()
                page.close_signup_form()
        else:
            pytest.mark.skip(f"This test not for 'Auth' role")

#
#
#
    @allure.feature("F_02 | Testing 'Main' banner. Not for En language")
    @allure.story("S_02.01 | Testing 'Jetzt traden' button on the 'Main' banner")
    @allure.step("Start test button 'Jetzt traden' on 'Main' banner.")
    @allure.title("TC_02_01 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_02_01_banner_main_button_left(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: Banner [Main] -> button [Jetzt traden]
        Language: All, except En. License: All.
        """
        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        print(f"worker_id = {worker_id}")

        if cur_language not in [""]:
            page = Conditions(d, "")
            test_link = page.preconditions(
                d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
            )

            page = Capital(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            if page.tc0201_de_banner_main_button_left_click():
                # if cur_language == "ar":
                #     if cur_license in ["FCA"]:
                #         page.check_current_page_is("https://capital.com/trading/signup")
                #         d.back()
                #     else:
                if cur_role == "NoReg":
                    page = SignupLogin(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    page.check_current_page_is("https://capital.com/trading/platform/")
                    d.back()
            else:
                pytest.skip("Button [Jetzt traden] not available")
        else:
            pytest.skip(f"Test not for '{cur_language}' language")

#
#
#
    @allure.feature("F_02 | Testing 'Main' banner. Not for En language")
    @allure.story("S_02.02 | Testing 'Kostenloses Demokonto' button on the 'Main' banner")
    @allure.step("Start test button 'Kostenloses Demokonto' on 'Main' banner.")
    @allure.title("TC_02_02 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_02_02_banner_main_button_righ(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: Banner [Main] -> button [Kostenloses Demokonto]
        Language: All, except En. License: All.
        """
        print(f"worker_id = {worker_id}")
        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        if cur_language not in [""]:
            page = Conditions(d, "")
            test_link = page.preconditions(
                d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
            )

            page = Capital(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            if page.tc0202_de_banner_main_button_right_click():

                if cur_role == "NoReg":
                    page = SignupLogin(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    page.check_current_page_is("https://capital.com/trading/platform/")
                    d.back()
            else:
                pytest.skip("Button [Jetzt traden] not available")
        else:
            pytest.skip(f"Test not for '{cur_language}' language")

#
#
#
    @pytest.mark.xfail
    @allure.feature("F_03 | Testing '1' tab 'Main' banner. Only for 'En' language")
    @allure.story("S_03.01 | Testing 'Trade Now' button on the 1 tab 'Main' banner")
    @allure.step("Start test button 'Trade Now' on tab1 'Main' banner (for all License).")
    @allure.title("TC_03_01 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_03_01_banner_main_tab1_button_trade_now(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: tab "1" -> button "Trade now"
        Language: EN. License: All.
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        if cur_language in [""]:
            page = Conditions(d, "")
            test_link = page.preconditions(
                d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
            )

            page = Capital(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            page.banner_main_tab1_click()
            page.banner_main_tab1_button_trade_now_click()

            if cur_role == "NoReg":
                page = SignupLogin(d, test_link)
                page.should_be_signup_form()
                page.close_signup_form()
            elif cur_role == "Reg_NoAuth":
                pass
            elif cur_role == "Auth":
                page.check_current_page_is("https://capital.com/trading/platform/")
                d.back()
        else:
            pytest.skip(f"Test not for '{cur_language}' language")

#
#
#
    @pytest.mark.xfail
    @allure.feature("F_03 | Testing '1' tab 'Main' banner. Only for 'En' language")
    @allure.story("S_03.02 | Testing 'Practise for free' button on the 1 tab 'Main' banner")
    @allure.step("Start test button 'Practise for free' on tab1 'Main' banner (for all License).")
    @allure.title("TC_03_02 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_03_02_banner_main_tab1_button_practise_for_free(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: tab "1" -> button "Practice for free"
        Language: only En. Licence: All.
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        if cur_language in [""]:
            page = Conditions(d, "")
            test_link = page.preconditions(
                d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
            )

            page = Capital(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            page.banner_main_tab1_click()
            page.banner_main_tab1_button_practise_for_free_click()

            if cur_role == "NoReg":
                page = SignupLogin(d, test_link)
                page.should_be_signup_form()
                page.close_signup_form()
            elif cur_role == "Reg_NoAuth":
                pass
            elif cur_role == "Auth":
                page.check_current_page_is("https://capital.com/trading/platform/")
                d.back()
        else:
            pytest.skip(f"Test not for '{cur_language}' language")

#
#
#
    @pytest.mark.xfail
    @allure.feature("F_03 | Testing '1' tab 'Main' banner. Only for 'En' language")
    @allure.story("S_03.03 | Testing 'Open account' button on the 1 tab 'Main' banner")
    @allure.step("Start test button 'Open account' on tab1 'Main' banner.")
    @allure.title("TC_03_03 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_03_03_banner_main_tab1_button_open_account(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: tab "Spread betting" -> button "Open account"
        Language: only En. Licence: All.
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        if cur_language in [""]:
            page = Conditions(d, "")
            test_link = page.preconditions(
                d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
            )

            page = Capital(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            page.banner_main_tab1_click()
            page.banner_main_tab1_button_open_account_click()

            if cur_role == "NoReg":
                # Проверяем, что открылась форма SignUP
                page = SignupLogin(d, test_link)
                page.should_be_signup_form()
                page.close_signup_form()
            elif cur_role == "Reg_NoAuth":
                pass
            elif cur_role == "Auth":
                page.check_current_page_is("https://capital.com/trading/platform/")
                d.back()
        else:
            pytest.skip(f"Test not for '{cur_language}' language")

#
#
#
    @pytest.mark.xfail
    @allure.feature("F_03 | Testing '1' tab 'Main' banner. Only for 'En' language")
    @allure.story("S_03.04 | Testing 'Start trading' button on the 1 tab 'Main' banner")
    @allure.step("Start test button 'Start trading' on tab1 'Main' banner.")
    @allure.title("TC_03_04 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_03_04_banner_main_tab1_button_start_trading(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: tab "Spread betting" -> button "Open account"
        Language: only En. Licence: All.
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        if cur_language in [""]:
            page = Conditions(d, "")
            test_link = page.preconditions(
                d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
            )

            page = Capital(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            page.banner_main_tab1_click()
            page.banner_main_tab1_button_start_trading_click()

            if cur_role == "NoReg":
                # Проверяем, что открылась форма SignUP
                page = SignupLogin(d, test_link)
                page.should_be_signup_form()
                page.close_signup_form()
            elif cur_role == "Reg_NoAuth":
                pass
            elif cur_role == "Auth":
                page.should_be_link("https://capital.com/trading/platform")
                d.back()
        else:
            pytest.skip(f"Test not for '{cur_language}' language")

#
#
#
    @pytest.mark.xfail
    @allure.feature("F_04 | Testing '2' tab 'Main' banner. Only for 'En' language")
    @allure.story("S_04.01 | Testing 'Take me there' button on the 2 tab 'Main' banner")
    @allure.step("Start test button 'Take me there' on tab2 'Main' banner (for all License).")
    @allure.title("TC_04_01 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_04_01_banner_main_tab2_button_take_me_there(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: tab "Want to take your trading to the next level?" -> button "Take me there"
        Language: only En. Licence: All.
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        if cur_language in [""]:
            page = Conditions(d, "")
            test_link = page.preconditions(
                d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
            )

            page = Capital(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            page.banner_main_tab2_click()
            page.banner_main_tab2_button_take_me_there_click()

            if cur_role in ["NoReg", "Auth"]:
                page.check_current_page_is("https://capital.com/learn-to-trade")
                d.back()
            elif cur_role == "Reg_NoAuth":
                page.check_current_page_is("https://capital.com/trading/platform/")
                d.back()
        else:
            pytest.skip(f"Test not for '{cur_language}' language")

#
#
#
    @pytest.mark.xfail
    @allure.feature("F_04 | Testing '2' tab 'Main' banner. Only for 'En' language")
    @allure.story("S_04.02 | Testing 'Start trading' button on the 2 tab 'Main' banner")
    @allure.step("Start test button 'Start trading' on tab2 'Main' banner.")
    @allure.title("TC_04_02 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_04_02_banner_main_tab2_button_start_trading(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: tab "Industry-leading ..." -> button "Start trading"
        Language: only En. Licence: All.
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        if cur_language in [""]:
            page = Conditions(d, "")
            test_link = page.preconditions(
                d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
            )

            page = Capital(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            page.banner_main_tab2_click()
            page.banner_main_tab2_button_start_trading_click()

            if cur_role == "NoReg":
                # Проверяем, что открылась форма SignUP
                page = SignupLogin(d, test_link)
                page.should_be_signup_form()
                page.close_signup_form()
            elif cur_role == "Reg_NoAuth":
                pass
            elif cur_role == "Auth":
                page.check_current_page_is("https://capital.com/trading/platform/")
                d.back()
        else:
            pytest.skip(f"Test not for '{cur_language}' language")

#
#
#
    @pytest.mark.xfail
    @allure.feature("F_04 | Testing '2' tab 'Main' banner. Only for 'En' language")
    @allure.story("S_04.03 | Testing 'Practise for free' button on the 2 tab 'Main' banner")
    @allure.step("Start test button 'Practise for free' on tab2 'Main' banner.")
    @allure.title("TC_04_03 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_04_03_banner_main_tab2_button_practise_for_free(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: tab "Industry-leading ..." -> button "Practice for free"
        Language: only En. Licence: All.
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        if cur_language in [""]:
            page = Conditions(d, "")
            test_link = page.preconditions(
                d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
            )

            page = Capital(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            page.banner_main_tab2_click()
            page.banner_main_tab2_button_practise_for_free_click()

            if cur_role == "NoReg":
                page = SignupLogin(d, test_link)
                page.should_be_signup_form()
                page.close_signup_form()
            elif cur_role == "Reg_NoAuth":
                pass
            elif cur_role == "Auth":
                page.check_current_page_is("https://capital.com/trading/platform/")
                d.back()
        else:
            pytest.skip(f"Test not for '{cur_language}' language")

#
#
#
    @pytest.mark.xfail
    @allure.feature("F_05 | Testing '3' tab 'Main' banner. Only for 'En' language")
    @allure.story("S_05.01 | Testing 'Learn more' button on the 3 tab (1 layout) 'Main' banner")
    @allure.step("Start test button 'Learn more' on tab3 'Main' banner (Layout 1: ASIC).")
    @allure.title("TC_05_01 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_05_01_banner_main_tab3_l1_button_learn_more_asic(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: tab "Discover Pro Trading" -> button "Learn more"
        Language: only En. Licence: only ASIC.
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        if cur_language in [""]:
            if cur_license in ["ASIC"]:
                page = Conditions(d, "")
                test_link = page.preconditions(
                    d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
                )

                page = Capital(d, test_link)
                if not page.current_page_is(test_link):
                    page.open_page()

                layout = page.banner_main_tab3_click()
                print(f"Current layout # {layout}")
                if layout == 1:
                    page.banner_main_tab3_l1_button_learn_more_asic_click()
                    if cur_role in ["NoReg", "Auth"]:
                        page.check_current_page_is("https://capital.com/professional-clients-au")
                        d.back()
                    elif cur_role == "Reg_NoAuth":
                        pass
                else:
                    pytest.skip(f"Test not for {layout} layout")
            else:
                pytest.skip(f"Test not for '{cur_license}' licence")
        else:
            pytest.skip(f"Test not for '{cur_language}' language")

#
#
#
    @pytest.mark.xfail
    @allure.feature("F_05 | Testing '3' tab 'Main' banner. Only for 'En' language")
    @allure.story("S_05.02 | Testing 'Start trading' button on the 3 tab (1 layout) 'Main' banner")
    @allure.step("Start test button 'Start trading' on tab3 'Main' banner (Layout 1: ASIC).")
    @allure.title("TC_05_02 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_05_02_banner_main_tab3_l1_button_start_trading_asic(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: tab "Discover Pro Trading" -> button "Start trading"
        Language: only En. Licence: only ASIC.
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        if cur_language in [""]:
            if cur_license in ["ASIC"]:
                page = Conditions(d, "")
                test_link = page.preconditions(
                    d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
                )

                page = Capital(d, test_link)
                if not page.current_page_is(test_link):
                    page.open_page()

                layout = page.banner_main_tab3_click()
                print(f"Current layout # {layout}")
                if layout == 1:
                    page.banner_main_tab3_l1_button_start_trading_asic_click()
                    if cur_role in ["NoReg", "Ayth"]:
                        # Проверяем, что открылась page Sign Up "https://capital.com/trading/signup"
                        page.check_current_page_is("https://capital.com/trading/signup")
                        d.back()
                    elif cur_role == "Reg_NoAuth":
                        pass
                    # elif cur_role == "Auth":
                    #     page.check_current_page_is("https://capital.com/trading/platform/")
                    #     d.back()
                else:
                    pytest.skip(f"Test not for {layout} layout")
            else:
                pytest.skip(f"Test not for '{cur_license}' license")
        else:
            pytest.skip(f"Test not for '{cur_language}' language")

#
#
#
    @pytest.mark.xfail
    @allure.feature("F_05 | Testing '3' tab 'Main' banner. Only for 'En' language")
    @allure.story("S_05.03 | Testing 'Start trading' button on the 3 tab (2 layout) 'Main' banner")
    @allure.step("Start test button 'Start trading' on tab3 'Main' banner (Layout 2: All License, except ASIC).")
    @allure.title("TC_05_03 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_05_03_banner_main_tab3_l2_button_start_trading_asic(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: tab "Industry-leading support for new traders" -> button "Start trading"
        Language: only En. Licence: All, except ASIC.
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        if cur_language in [""]:
            if cur_license not in ["BAH"]:
                page = Conditions(d, "")
                test_link = page.preconditions(
                    d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
                )

                page = Capital(d, test_link)
                if not page.current_page_is(test_link):
                    page.open_page()

                layout = page.banner_main_tab3_click()
                print(f"Current layout # {layout}")
                if layout == 2:
                    page.banner_main_tab3_l2_button_start_trading_fca_click()
                    if cur_role == "NoReg":
                        page = SignupLogin(d, test_link)
                        page.should_be_signup_form()
                        page.close_signup_form()
                    elif cur_role == "Reg_NoAuth":
                        pass
                    elif cur_role == "Auth":
                        page.check_current_page_is("https://capital.com/trading/platform/")
                        d.back()
                else:
                    pytest.skip(f"Test not for {layout} layout")
            else:
                pytest.skip(f"Test not for '{cur_license}' license")
        else:
            pytest.skip(f"Test not for '{cur_language}' language")

#
#
#
    @pytest.mark.xfail
    @allure.feature("F_05 | Testing '3' tab 'Main' banner. Only for 'En' language")
    @allure.story("S_05.04 | Testing 'Practise for free' button on the 3 tab (2 layout) 'Main' banner")
    @allure.step("Start test button 'Practise for free' on tab3 'Main' banner (Layout 2: All, except ASIC).")
    @allure.title("TC_05_04 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_05_04_banner_main_tab3_l2_button_practise_fo_free_fca(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: tab "Industry-leading support for new traders" -> button "Practise for free"
        Language: only En. Licence: All, except ASIC.
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        if cur_language in [""]:
            if cur_license not in ["ASIC", "BAH"]:
                page = Conditions(d, "")
                test_link = page.preconditions(
                    d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
                )

                page = Capital(d, test_link)
                if not page.current_page_is(test_link):
                    page.open_page()

                layout = page.banner_main_tab3_click()
                print(f"Current layout # {layout}")
                if layout == 2:
                    page.banner_main_tab3_l2_button_practise_for_free_fca_click()
                    if cur_role == "NoReg":
                        page = SignupLogin(d, test_link)
                        page.should_be_signup_form()
                        page.close_signup_form()
                    elif cur_role == "Reg_NoAuth":
                        pass
                    elif cur_role == "Auth":
                        page.check_current_page_is("https://capital.com/trading/platform/")
                        d.back()
                else:
                    print(f"Test not for {layout} layout")
            else:
                pytest.skip(f"Test not for '{cur_license}' license")
        else:
            pytest.skip(f"Test not for '{cur_language}' language")

    @pytest.mark.xfail
    @allure.feature("F_05 | Testing '3' tab 'Main' banner. Only for 'En' language")
    @allure.story("S_05.05 | Testing 'Explore features' button on the 3 tab (2 layout) 'Main' banner")
    @allure.step("Start test button 'Explore features' on tab3 'Main' banner (Layout 2, only for 'BAH').")
    @allure.title("TC_05_05 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_05_05_banner_main_tab3_l2_button_explore_features(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: tab "Find us on ..." -> button "Explore features"
        Language: only En. Licence: BUH.
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        if cur_language in [""]:
            if cur_license in ["BAH"]:
                page = Conditions(d, "")
                test_link = page.preconditions(
                    d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
                )

                page = Capital(d, test_link)
                if not page.current_page_is(test_link):
                    page.open_page()

                layout = page.banner_main_tab3_click()
                print(f"Current layout # {layout}")
                if layout == 2:
                    page.tc0601_banner_main_tab4_button_explore_features_click()
                    if cur_role in ["NoReg", "Auth"]:
                        page = SignupLogin(d, test_link)
                        page.should_be_signup_form()
                        page.close_signup_form()
                    elif cur_role == "Reg_NoAuth":
                        pass
                else:
                    print(f"Test not for {layout} layout")
            else:
                pytest.skip(f"Test not for '{cur_license}' license")
        else:
            pytest.skip(f"Test not for '{cur_language}' language")

#
#
#
    @allure.feature("F_06 | Testing '4' tab 'Main' banner. Only for 'En' language")
    @allure.story("S_06.01 | Testing 'Explore features' button on the 4 tab 'Main' banner")
    @allure.step("Start test button 'Explore features' on tab4 'Main' banner.")
    @allure.title("TC_06_01 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_06_01_banner_main_tab4_button_explore_features(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: tab "Find us on ..." -> button "Explore features"
        Language: only En. Licence: All, except BUH.
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        if cur_language in [""]:
            if cur_license not in ["BAH"]:
                page = Conditions(d, "")
                test_link = page.preconditions(
                    d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
                )

                page = Capital(d, test_link)
                if not page.current_page_is(test_link):
                    page.open_page()

                page.tc0601_banner_main_tab4_click()
                page.tc0601_banner_main_tab4_button_explore_features_click()

                if cur_role in ["NoReg", "Auth"]:
                    page.check_current_page_is("https://www.tradingview.com/broker/Capitalcom/")
                    d.back()
                elif cur_role == "Reg_NoAuth":
                    pass
            else:
                pytest.skip(f"Test not for '{cur_license}' license")
        else:
            pytest.skip(f"Test not for '{cur_language}' language")

#
#
#
    @allure.feature("F_07 | Testing 'Why Capital.com?' banner. Not for 'En' language")
    @allure.story("S_07.01 | Testing 'Jetzt traden' button on the 'Warum Capital.com?' banner")
    @allure.step("Start test button 'Jetzt traden' on 'Warum Capital.com?' banner.")
    @allure.title("TC_07_01 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_07_01_banner_why_capital_button_trade_now(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: Banner [Warum Capital.com?] -> button [Jetzt traden]
        Language: All, except En. License: All.
        """
        print(f"worker_id = {worker_id}")
        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        if cur_language not in [""]:
            page = Conditions(d, "")
            test_link = page.preconditions(
                d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
            )

            page = Capital(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            if page.tc0701_de_banner_why_capital_button_trade_now_click():

                if cur_role == "NoReg":
                    # if 0 != 1:
                    #     page.check_current_page_is("https://capital.com/trading/signup")
                    #     d.back()
                    # else:
                    page = SignupLogin(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    page.check_current_page_is("https://capital.com/trading/platform/")
                    d.back()
            else:
                pytest.skip("Button [Jetzt traden] not available")
        else:
            pytest.skip(f"Test not for the '{cur_language}' language")

#
#
#
    @allure.feature("F_08 | Widget [Trading instrument]")
    @allure.story("S_08.01 | Widget [Trading instrument] tab [Most traded] button [Trade]")
    @allure.step("Start test 'Click 'Trade' buttons on the 'Most traded' tab 'Trading instrument' widget'.")
    @allure.title("TC_08_01 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_08_01_widget_trading_instrument(
        self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: widget "Trading instrument"
        Language: ALL. Licence: All.
        Widget has 2 layouts
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        tab_name = "Most"
        if not (cur_license == "FCA" and tab_name == "Crypto"):
            page = Conditions(d, "")
            test_link = page.preconditions(
                d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
            )

            page = Capital(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            layout = page.tc08_what_is_the_current_layout()
            page.tc08_widget_trading_instrument_tab_click(layout, tab_name)
            list_buttons = page.tc08_get_list_lines_from_tab(cur_language, layout, tab_name)
            for line in range(len(list_buttons)):
                page = Capital(d, test_link)
                page.tc08_selected_tab_and_line_button_trade_click(list_buttons, line)
                if cur_role == "NoReg":
                    page = SignupLogin(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    page.should_be_link("https://capital.com/trading/platform/")
                    d.back()
                    d.back()
        else:
            pytest.skip(f"The '{tab_name}' tab is not available for the '{cur_license}' license")

#
#
#
    @allure.feature("F_08 | Widget [Trading instrument]")
    @allure.story("S_08.02 | Widget [Trading instrument] tab [Commodities] button [Trade]")
    @allure.step("Start test 'Click 'Trade' buttons on the 'Commodities' tab 'Trading instrument' widget'.")
    @allure.title("TC_08_02 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_08_02_widget_trading_instrument(
        self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: widget "Trading instrument"
        Language: All. Licence: All.
        Widget has 2 layouts
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        tab_name = "Commodities"
        if not (cur_license == "FCA" and tab_name == "Crypto"):
            page = Conditions(d, "")
            test_link = page.preconditions(
                d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
            )

            page = Capital(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            layout = page.tc08_what_is_the_current_layout()
            page.tc08_widget_trading_instrument_tab_click(layout, tab_name)
            list_buttons = page.tc08_get_list_lines_from_tab(cur_language, layout, tab_name)

            for line in range(len(list_buttons)):
                page = Capital(d, test_link)
                page.tc08_selected_tab_and_line_button_trade_click(list_buttons, line)
                if cur_role == "NoReg":
                    page = SignupLogin(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                    # page = CapitalPage(d, test_link)
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    page.should_be_link("https://capital.com/trading/platform/")
                    d.back()
                    d.back()
        else:
            pytest.skip(f"The '{tab_name}' tab is not available for the '{cur_license}' license")

#
#
#
    @allure.feature("F_08 | Widget [Trading instrument]")
    @allure.story("S_08.03 | Widget [Trading instrument] tab [Indices] button [Trade]")
    @allure.step("Start test 'Click 'Trade' buttons on the 'Indices' tab 'Trading instrument' widget'.")
    @allure.title("TC_08_03 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_08_03_widget_trading_instrument(
        self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: widget "Trading instrument"
        Language: All. Licence: All.
        Widget has 2 layouts
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        tab_name = "Indices"
        if not (cur_license == "FCA" and tab_name == "Crypto"):
            page = Conditions(d, "")
            test_link = page.preconditions(
                d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
            )

            page = Capital(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            layout = page.tc08_what_is_the_current_layout()
            page.tc08_widget_trading_instrument_tab_click(layout, tab_name)
            list_buttons = page.tc08_get_list_lines_from_tab(cur_language, layout, tab_name)

            for line in range(len(list_buttons)):
                page = Capital(d, test_link)
                page.tc08_selected_tab_and_line_button_trade_click(list_buttons, line)
                if cur_role == "NoReg":
                    page = SignupLogin(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                    # page = CapitalPage(d, test_link)
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    page.should_be_link("https://capital.com/trading/platform/")
                    d.back()
                    d.back()
        else:
            pytest.skip(f"The '{tab_name}' tab is not available for the '{cur_license}' license")

#
#
#
    @allure.feature("F_08 | Widget [Trading instrument]")
    @allure.story("S_08.04 | Widget [Trading instrument] tab [Cryptocurrencies] button [Trade]")
    @allure.step("Start test 'Click 'Trade' buttons on the 'Cryptocurrencies' tab 'Trading instrument' widget'.")
    @allure.title("TC_08_04 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_08_04_widget_trading_instrument(
        self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: widget "Trading instrument"
        Language: All. Licence: All.
        Widget has 2 layouts
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        tab_name = "Crypto"
        if not (cur_license == "FCA" and tab_name == "Crypto"):
            page = Conditions(d, "")
            test_link = page.preconditions(
                d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
            )

            page = Capital(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            layout = page.tc08_what_is_the_current_layout()
            page.tc08_widget_trading_instrument_tab_click(layout, tab_name)
            list_buttons = page.tc08_get_list_lines_from_tab(cur_language, layout, tab_name)

            for line in range(len(list_buttons)):
                page = Capital(d, test_link)
                page.tc08_selected_tab_and_line_button_trade_click(list_buttons, line)
                if cur_role == "NoReg":
                    page = SignupLogin(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                    # page = CapitalPage(d, test_link)
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    page.should_be_link("https://capital.com/trading/platform/")
                    d.back()
                    d.back()
        else:
            pytest.skip(f"The '{tab_name}' tab is not available for the '{cur_license}' license")

#
#
#
    @allure.feature("F_08 | Widget [Trading instrument]")
    @allure.story("S_08.05 | Widget [Trading instrument] tab [Shares] button [Trade]")
    @allure.step("Start test 'Click 'Trade' buttons on the 'Shares' tab 'Trading instrument' widget'.")
    @allure.title("TC_08_05 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_08_05_widget_trading_instrument(
        self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: widget "Trading instrument"
        Language: All. Licence: All.
        Widget has 2 layouts
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        tab_name = "Shares"
        if not (cur_license == "FCA" and tab_name == "Crypto"):
            page = Conditions(d, "")
            test_link = page.preconditions(
                d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
            )

            page = Capital(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            layout = page.tc08_what_is_the_current_layout()
            page.tc08_widget_trading_instrument_tab_click(layout, tab_name)
            list_buttons = page.tc08_get_list_lines_from_tab(cur_language, layout, tab_name)

            for line in range(len(list_buttons)):
                page = Capital(d, test_link)
                page.tc08_selected_tab_and_line_button_trade_click(list_buttons, line)
                if cur_role == "NoReg":
                    page = SignupLogin(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                    # page = CapitalPage(d, test_link)
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    page.should_be_link("https://capital.com/trading/platform/")
                    d.back()
                    d.back()
        else:
            pytest.skip(f"The '{tab_name}' tab is not available for the '{cur_license}' license")

#
#
#
    @allure.feature("F_08 | Widget [Trading instrument]")
    @allure.story("S_08.06 | Widget [Trading instrument] tab [Forex] button [Trade]")
    @allure.step("Start test 'Click 'Trade' buttons on the 'Forex' tab 'Trading instrument' widget'.")
    @allure.title("TC_08_06 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_08_06_widget_trading_instrument(
        self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: widget "Trading instrument"
        Language: All. Licence: All.
        Widget has 2 layouts
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        tab_name = "Forex"
        if not (cur_license == "FCA" and tab_name == "Crypto"):
            page = Conditions(d, "")
            test_link = page.preconditions(
                d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
            )

            page = Capital(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            layout = page.tc08_what_is_the_current_layout()
            page.tc08_widget_trading_instrument_tab_click(layout, tab_name)
            list_buttons = page.tc08_get_list_lines_from_tab(cur_language, layout, tab_name)

            for line in range(len(list_buttons)):
                page = Capital(d, test_link)
                page.tc08_selected_tab_and_line_button_trade_click(list_buttons, line)
                if cur_role == "NoReg":
                    page = SignupLogin(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                    # page = Capital(d, test_link)
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    page.should_be_link("https://capital.com/trading/platform/")
                    d.back()
                    d.back()
        else:
            pytest.skip(f"The '{tab_name}' tab is not available for the '{cur_license}' license")

#
#
#
    @allure.feature("F_08 | Widget [Trading instrument]")
    @allure.story("S_08.07 | Widget [Trading instrument] tab [ETFs] button [Trade]")
    @allure.step("Start test 'Click 'Trade' button on the 'ETFs' tab 'Trading instrument' widget'.")
    @allure.title("TC_08_07 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_08_07_widget_trading_instrument(
        self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: widget "Trading instrument"
        Language: All. Licence: All.
        Widget has 2 layouts
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        tab_name = "ETFs"
        if not (cur_license == "FCA" and tab_name == "Crypto"):
            page = Conditions(d, "")
            test_link = page.preconditions(
                d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
            )

            page = Capital(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            layout = page.tc08_what_is_the_current_layout()
            page.tc08_widget_trading_instrument_tab_click(layout, tab_name)
            list_buttons = page.tc08_get_list_lines_from_tab(cur_language, layout, tab_name)

            for line in range(len(list_buttons)):
                page = Capital(d, test_link)
                page.tc08_selected_tab_and_line_button_trade_click(list_buttons, line)
                if cur_role == "NoReg":
                    page = SignupLogin(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                    # page = CapitalPage(d, test_link)
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    page.should_be_link("https://capital.com/trading/platform/")
                    d.back()
                    d.back()
        else:
            pytest.skip(f"The '{tab_name}' tab is not available for the '{cur_license}' license")

#
#
#
    @allure.feature("F_09 | Testing 'Still looking for ...' widget")
    @allure.story("S_09.01 | Testing 'Create your account' button on the 'Still looking for ...' widget")
    @allure.step("Start tests of widget 'Still looking for a broker you can trust?'.")
    @allure.title("TC_09_01 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_09_01_widget_still_looking_button_1_create_your_account(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: widget "Still looking for ..." -> button "1. Created your account"
        Language: All. Licence: All.
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        page = Conditions(d, "")
        test_link = page.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )

        page = Capital(d, test_link)
        if not page.current_page_is(test_link):
            page.open_page()

        page.widget_still_looking_button_1_create_your_account_click(cur_language)

        if cur_role == "NoReg":
            page = SignupLogin(d, test_link)
            page.should_be_signup_form()
            page.close_signup_form()
        elif cur_role == "Reg_NoAuth":
            pass
        elif cur_role == "Auth":
            page.should_be_link("https://capital.com/trading/platform")
            d.back()

#
#
#
    @allure.feature("F_10 | Testing 'Promo Market' widget")
    @allure.story("S_10.01 | Testing 'Trade Now' button on the 'Promo Market' widget")
    @allure.step("Run test for 'Promo Market' widget.")
    @allure.title("TC_10_01 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_10_01_widget_promo_market_button_trade_now(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: widget "Promo Market" -> button "Trade Now"
        Language: only En. Licence: All.
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        if cur_language in [""]:
            page = Conditions(d, "")
            test_link = page.preconditions(
                d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
            )

            page = Capital(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            qty = page.tc1001_how_many_dif_buttons_trade_now_on_widget_promo_market()
            if qty != 0:
                for i in range(qty):
                    page.tc1001_widget_promo_market_button_trade_now_click(i)

                    if cur_role == "NoReg":
                        page = SignupLogin(d, test_link)
                        page.should_be_signup_form()
                        page.close_signup_form()
                        page = Capital(d, test_link)
                    elif cur_role == "Reg_NoAuth":
                        pass
                    elif cur_role == "Auth":
                        page.should_be_link("https://capital.com/trading/platform")
                        d.back()
            else:
                pytest.fail("Widget is not present on the current page!")
        else:
            pytest.skip(f"Test not for '{cur_language}' language")

#
#
#
    @allure.feature("F_11 | Testing 'Explore our platform' widget")
    @allure.story("S_11.01 | Testing 'Try now' button on the 'Explore our platform' widget")
    @allure.step("Run test for widget 'Explore our platform'.")
    @allure.title("TC_11_01 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_11_01_widget_explore_our_platform(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: widget "Explore our platform" -> button "Try now"
        Language: All. Licence: All.
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        page = Conditions(d, "")
        test_link = page.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )

        page = Capital(d, test_link)
        if not page.current_page_is(test_link):
            page.open_page()

        page.tc1101_widget_explore_our_platform_button_tray_now_click(cur_language)

        if cur_role == "NoReg":
            # if cur_license in ["FCA"]:
            #     page.check_current_page_is("https://capital.com/trading/signup")
            #     d.back()
            # else:
            page = SignupLogin(d, test_link)
            page.should_be_signup_form()
            page.close_signup_form()
        elif cur_role == "Reg_NoAuth":
            pass
        elif cur_role == "Auth":
            page.should_be_link("https://capital.com/trading/platform")
            d.back()

#
#
#
    @allure.feature("F_12 | Testing 'New To Trading?' banner")
    @allure.story("S_12.01 | Testing 'Practise for free' button on the 'New To Trading?' banner")
    @allure.step("Test for 'Practise for free' button on the 'New To Trading?' banner.")
    @allure.title("TC_12_01 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_12_01_de_banner_new_to_trading_button_practise_for_free(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: Banner "New To Trading?" -> button "Practise for free"
        Language: All, except En. Licence: All.
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        if cur_language not in [""]:
            page = Conditions(d, "")
            test_link = page.preconditions(
                d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
            )

            page = Capital(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            page = Capital(d, test_link)
            if page.tc1201_de_banner_new_to_trading_button_practise_fo_free_click():
                if cur_role == "NoReg":
                    page = SignupLogin(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    page.should_be_link("https://capital.com/trading/platform/")
                    d.back()
            else:
                pytest.xfail("Banner is not present on the current page!")
        else:
            pytest.skip(f"Test not for '{cur_language}' language")

#
#
#
    @allure.feature("F_13 | Testing 'New to trading?' widget")
    @allure.story("S_13.01 | Testing 'Practise for free' button on the 'Explore our platform' widget")
    @allure.step("Run test for widget 'New to trading?'.")
    @allure.title("TC_13_01 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_13_01_widget_new_to_trading(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: widget "New to trading?" -> button "Practise for free"
        Language: All. Licence: All.
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        page = Conditions(d, "")
        test_link = page.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )

        page = Capital(d, test_link)
        if not page.current_page_is(test_link):
            page.open_page()

        page.tc1301_widget_new_to_trading_button_practise_for_free_click(cur_language)

        if cur_role == "NoReg":
            page = SignupLogin(d, test_link)
            page.should_be_signup_form()
            page.close_signup_form()
        elif cur_role == "Reg_NoAuth":
            pass
        elif cur_role == "Auth":
            page.should_be_link("https://capital.com/trading/platform")
            d.back()

#
#
#
    @allure.feature("F_14 | Testing 'Trading calculator' widget")
    @allure.story("S_14.01 | Testing 'Start trading' button on the 'Trading calculator' widget")
    @allure.step("Run test for button 'Start trading' for widget 'Trading calculator'.")
    @allure.title("TC_14_01 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_14_01_widget_trading_calculator_button_start_trading(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: widget "Trading calculator" -> button "Start trading"
        Language: All, except En. Licence: All.
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        if cur_language in [""]:
            page = Conditions(d, "")
            test_link = page.preconditions(
                d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
            )

            page = Capital(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            page.widget_trading_calculator_button_start_trading_click()

            if cur_role == "NoReg":
                page = SignupLogin(d, test_link)
                page.should_be_signup_form()
                page.close_signup_form()
            elif cur_role == "Reg_NoAuth":
                pass
            elif cur_role == "Auth":
                page.should_be_link("https://capital.com/trading/platform/")
                d.back()
        else:
            pytest.skip(f"Test not for '{cur_language}' language")

#
#
#
    @allure.feature("F_15 | Testing 'Trader's Dashboard' widget")
    @allure.story("S_15.01 | Testing 'Trade' button on the 'Trader's Dashboard' widget")
    @allure.step("Run test for buttons 'Trade' on 'Trader's Dashboard' widget.")
    @allure.title("TC_15_01 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_15_01_widget_traders_dashboard_button_trade(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: widget "Trader's Dashboard" -> button "Trade"
        Language: All, except En. Licence: All.
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        if cur_language in [""]:
            page = Conditions(d, "")
            test_link = page.preconditions(
                d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
            )

            page = Capital(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            qty = page.how_many_buttons_trade_on_widget_traders_dashboard()
            if qty != 0:
                for i in range(qty):
                    page = Capital(d, test_link)
                    page.widget_traders_dashboard_button_trade_click(i)

                    if cur_role == "NoReg":
                        page = SignupLogin(d, test_link)
                        page.should_be_signup_form()
                        page.close_signup_form()
                    elif cur_role == "Reg_NoAuth":
                        pass
                    elif cur_role == "Auth":
                        page.should_be_link("https://capital.com/trading/platform")
                        d.back()
            else:
                pytest.xfail("Widget is not present on the current page!")
        else:
            pytest.skip(f"Test not for '{cur_language}' language")

#
#
#
    @allure.feature("F_16 | Testing 'Counters' banner")
    @allure.story("S_16.01 | Testing 'Try now' button on the 'Counters' banner")
    @allure.step("Test for 'Try now' button on banner with counters.")
    @allure.title("TC_16_01 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_16_01_banner_of_counters_button_try_now(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license, prob_run_tc, datetime_now
    ):
        """
        Check: Banner of counters -> button "Try now"
        Language: All. Licence: All.
        """
        test_link = ""

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        print(f"worker_id = {worker_id}")
        print(f"test_link = {test_link}")

        page = Conditions(d, "")
        test_link = page.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )

        page = Capital(d, test_link)
        if not page.current_page_is(test_link):
            page.open_page()

        page = Capital(d, test_link)
        if page.tc1601_banner_of_counters_button_try_now_click():
            if cur_role == "NoReg":
                page = SignupLogin(d, test_link)
                page.should_be_signup_form()
                page.close_signup_form()
            elif cur_role == "Reg_NoAuth":
                pass
            elif cur_role == "Auth":
                page.should_be_link("https://capital.com/trading/platform")
                d.back()
        else:
            pytest.skip("Banner of counters is not present on the current page!")
