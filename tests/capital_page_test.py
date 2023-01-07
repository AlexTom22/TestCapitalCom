# -*- coding: utf-8 -*-
# @Time    : 2022/11/22 10:00
# @Author  : Alexander Tomelo
import time
import pytest
import allure
import pages.base_page
# import pages.capital_page
# import pages.header_element
# import pages.signup_login_form
from pages.capital_com.capital_page import CapitalPage
from pages.capital_com.header_element import HeaderElement
from pages.capital_com.signup_login_form import SignupLoginForm
from src.src import (
    CapitalComPageSrc,
    TradingViewPageSrc,
    ESGPageSrc,
    LearnToTradePageSrc,
    ProfessionalClientsAu,
)

test_link = "?"
prev_role = "?"
prev_license = "?"
prev_language = "?"
page = None
# flag_preconditions = False
accept_all_cookies = False


@pytest.mark.parametrize(
    "cur_login, cur_password",
    [
        ("Empty", "Empty"),
        # ("qa.tomelo.an@gmail.com", "???"),
    ], scope="class"
)
@allure.epic('Testing capital.com. All language. All license')
class Tests:

    @allure.step("Run preconditions")
    def preconditions(self, d, cur_login, cur_password, cur_role, cur_language, cur_license):
        # global start_link
        global test_link
        global prev_role
        global prev_license
        global prev_language
        global page
        global accept_all_cookies

        # устанавливаем Язык, если не соответствует предыдущему
        if cur_language != prev_language:
            url_language = f"{CapitalComPageSrc.URL}{cur_language}"
            test_link = url_language
            page = CapitalPage(d, test_link)
            page.open_page()
            prev_language = cur_language
            # Check установленного языка

        # Accept All Cookies if not accepted
        if not accept_all_cookies:
            d.delete_all_cookies()
            page.button_accept_all_cookies_click()
            accept_all_cookies = True

        # устанавливаем Лицензию, если не соответствует предыдущей
        if cur_license != prev_license:
            license_url = f"{CapitalComPageSrc.URL}?license={cur_license}"
            page = CapitalPage(d, license_url)
            page.open_page()
            prev_license = cur_license

        # Настраиваем в соответствии с параметром "Роль"
        if cur_role != prev_role:
            if cur_role == "NoReg":
                pass
            elif cur_role == "Reg_NoAuth":
                self.to_do_registration(d, cur_login, cur_password)
            elif cur_role == "Auth":
                self.to_do_authorization(d, cur_login, cur_password)
            else:
                print(f"Задан не существующий параметр роли - '{cur_role}'.\nТест будет выполнять с ролью 'NoReg'")
                prev_role = "NoReg"

#
#
#
    @allure.feature("F_01 | Testing header")
    @allure.story("S_01.01 | Testing 'Log In' button on the header")
    @allure.step("Start test button 'Log In' on header")
    def test_01_01_header_button_login(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role
    ):
        global test_link
        global page

        print(f"worker_id = {worker_id}")

        if cur_license in ["ASIC", "FCA", "CYSEC", "NBRB", "CCSTV", "SEY"]:
            self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

            page = HeaderElement(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()
            page.click_button_login_on_header()

            if cur_role == "NoReg":
                page = SignupLoginForm(d, test_link)
                page.should_be_login_form()
                page.close_login_form()
        else:
            print("")

#
#
#
    @allure.feature("F_01 | Testing header")
    @allure.story("S_01.02 | Testing 'Trade Now' button on the header")
    @allure.step("Start test button 'Trade Now' on header")
    def test_01_02_header_button_trade_now(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        global test_link
        global page

        print(f"worker_id = {worker_id}")

        if cur_license in ["ASIC", "FCA", "CYSEC", "NBRB", "CCSTV", "SEY"]:
            self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

            page = HeaderElement(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()
            page.click_button_signup_on_header()

            if cur_role == "NoReg":
                page = SignupLoginForm(d, test_link)
                page.should_be_signup_form()
                page.close_signup_form()
        else:
            print("")

#
#
#
    @allure.feature("F_02 | Testing 'Main' banner. Not for En language")
    @allure.story("S_02.01 | Testing 'Jetzt traden' button on the 'Main' banner")
    @allure.step("Start test button 'Jetzt traden' on 'Main' banner")
    def test_02_01_banner_main_button_left(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: Bunner [Main] -> button [Jetzt traden]
        Language - DE, IT. License - All
        """
        global test_link
        global page

        print(f"worker_id = {worker_id}")

        if cur_language not in [""]:
            if cur_license in ["ASIC", "FCA", "CYSEC", "NBRB", "CCSTV", "SEY"]:
                self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

                page = CapitalPage(d, test_link)
                if not page.current_page_is(test_link):
                    page.open_page()

                if page.de_banner_main_button_left_click():
                    if cur_role == "NoReg":
                        page = SignupLoginForm(d, test_link)
                        page.should_be_signup_form()
                        page.close_signup_form()
                    elif cur_role == "Reg_NoAuth":
                        pass
                    elif cur_role == "Auth":
                        pass
                else:
                    print("Button [Jetzt traden] not available")
            else:
                print("")
        else:
            print("Тест не для текущих параметров")

#
#
#
    @allure.feature("F_02 | Testing 'Main' banner. Not for En language")
    @allure.story("S_02.02 | Testing 'Kostenloses Demokonto' button on the 'Main' banner")
    @allure.step("Start test button 'Kostenloses Demokonto' on 'Main' banner")
    def test_02_02_banner_main_button_righ(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: Bunner [Main] -> button [Kostenloses Demokonto]
        Language - not for En. License - All
        """
        global test_link
        global page

        print(f"worker_id = {worker_id}")

        if cur_language not in [""]:
            if cur_license in ["ASIC", "FCA", "CYSEC", "NBRB", "CCSTV", "SEY"]:
                self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

                page = CapitalPage(d, test_link)
                if not page.current_page_is(test_link):
                    page.open_page()

                if page.de_banner_main_button_righ_click():

                    if cur_role == "NoReg":
                        page = SignupLoginForm(d, test_link)
                        page.should_be_signup_form()
                        page.close_signup_form()
                    elif cur_role == "Reg_NoAuth":
                        pass
                    elif cur_role == "Auth":
                        pass
                else:
                    print("Button [Jetzt traden] not available")
            else:
                print("")
        else:
            print("Тест не для текущих параметров")

#
#
#
    @allure.feature("F_03 | Testing '1' tab 'Main' banner. Only for 'En' language")
    @allure.story("S_03.01 | Testing 'Trade Now' button on the 1 tab 'Main' banner")
    @allure.step("Start test button 'Trade Now' on tab1 'Main' banner (for all License)")
    def test_03_01_banner_main_tab1_button_trade_now(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: tab "1" -> button "Trade now"
        Language - EN. License - All
        """
        global test_link
        global page

        print(f"worker_id = {worker_id}")

        if cur_language in [""]:
            if cur_license in ["ASIC", "FCA", "CYSEC", "NBRB", "CCSTV", "SEY"]:
                self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

                page = CapitalPage(d, test_link)
                if not page.current_page_is(test_link):
                    page.open_page()

                page.banner_main_tab1_click()
                page.banner_main_tab1_button_trade_now_click()

                if cur_role == "NoReg":
                    page = SignupLoginForm(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    pass
            else:
                print("")
        else:
            print("Тест не для текущих параметров")

#
#
#
    @allure.feature("F_03 | Testing '1' tab 'Main' banner. Only for 'En' language")
    @allure.story("S_03.02 | Testing 'Practise for free' button on the 1 tab 'Main' banner")
    @allure.step("Start test button 'Practise for free' on tab1 'Main' banner (for all License)")
    def test_03_02_banner_main_tab1_button_practise_for_free(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: tab "1" -> button "Practice for free"
        Licence: FCA. Language - EN.
        """
        global test_link
        global page

        print(f"worker_id = {worker_id}")

        if cur_language in [""]:
            self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

            page = CapitalPage(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            page.banner_main_tab1_click()
            page.banner_main_tab1_button_practise_for_free_click()

            if cur_role == "NoReg":
                if cur_license in ["ASIC", "FCA", "CYSEC", "NBRB", "CCSTV", "SEY"]:
                    page = SignupLoginForm(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
            elif cur_role == "Reg_NoAuth":
                pass
            elif cur_role == "Auth":
                pass
        else:
            print("Тест не для текущих параметров")

#
#
#
    @allure.feature("F_03 | Testing '1' tab 'Main' banner. Only for 'En' language")
    @allure.story("S_03.03 | Testing 'Open account' button on the 1 tab 'Main' banner")
    @allure.step("Start test button 'Open account' on tab1 'Main' banner")
    def test_03_03_banner_main_tab1_button_open_account(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: tab "Spread betting" -> button "Open account"
        Licence: FCA. Language - EN.
        """
        global test_link
        global page

        print(f"worker_id = {worker_id}")

        if cur_language in [""]:
            if cur_license in []:
                self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

                page = CapitalPage(d, test_link)
                if not page.current_page_is(test_link):
                    page.open_page()

                page.baner_main_tab1_click()
                page.banner_main_tab1_button_open_account_click()

                if cur_role == "NoReg":
                    # Проверяем, что открылась форма SignUP
                    page = SignupLoginForm(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    pass
            else:
                print("")
        else:
            print("Тест не для текущих параметров")

#
#
#
    @allure.feature("F_04 | Testing '2' tab 'Main' banner. Only for 'En' language")
    @allure.story("S_04.01 | Testing 'Take me there' button on the 2 tab 'Main' banner")
    @allure.step("Start test button 'Take me there' on tab2 'Main' banner (for all License)")
    def test_04_01_banner_main_tab2_button_take_me_there(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: tab "Want to take your trading to the next level?" -> button "Take me there"
        Licence: FCA. Language - EN.
        """
        global test_link
        global page

        print(f"worker_id = {worker_id}")

        if cur_language in [""]:
            self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

            page = CapitalPage(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            page.banner_main_tab2_click()
            page.banner_main_tab2_button_take_me_there_click()

            if cur_role == "NoReg":
                if cur_license in ["ASIC", "FCA", "CYSEC", "NBRB", "CCSTV", "SEY"]:
                    # https://capital.com/learn-to-trade
                    page.check_current_page_is("https://capital.com/learn-to-trade")
                elif cur_license in []:
                    # https://capital.com/why-capital-com
                    page.check_current_page_is("https://capital.com/why-capital-com")
                d.back()
            elif cur_role == "Reg_NoAuth":
                pass
            elif cur_role == "Auth":
                pass
        else:
            print("Тест не для текущего Language")

#
#
#
    @allure.feature("F_04 | Testing '2' tab 'Main' banner. Only for 'En' language")
    @allure.story("S_04.02 | Testing 'Start trading' button on the 2 tab 'Main' banner")
    @allure.step("Start test button 'Start trading' on tab2 'Main' banner")
    def test_04_02_banner_main_tab2_button_start_trading(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: tab "Industry-leading ..." -> button "Start trading"
        Licence: FCA. Language - EN.
        """
        global test_link
        global page

        print(f"worker_id = {worker_id}")

        if cur_language in [""]:
            if cur_license in []:
                self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

                page = CapitalPage(d, test_link)
                if not page.current_page_is(test_link):
                    page.open_page()

                page.banner_main_tab2_click()
                page.banner_main_tab2_button_start_trading_click()

                if cur_role == "NoReg":
                    # Проверяем, что открылась форма SignUP
                    page = SignupLoginForm(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    pass
            else:
                print("")
        else:
            print("Тест не для текущих параметров")

#
#
#
    @allure.feature("F_04 | Testing '2' tab 'Main' banner. Only for 'En' language")
    @allure.story("S_04.03 | Testing 'Practise for free' button on the 2 tab 'Main' banner")
    @allure.step("Start test button 'Practise for free' on tab2 'Main' banner")
    def test_04_03_banner_main_tab2_button_practise_for_free(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: tab "Industry-leading ..." -> button "Practice for free"
        Licence: FCA. Language - EN.
        """
        global test_link
        global page

        print(f"worker_id = {worker_id}")

        if cur_language in [""]:
            if cur_license in []:
                self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

                page = CapitalPage(d, test_link)
                if not page.current_page_is(test_link):
                    page.open_page()

                page.banner_main_tab2_click()
                page.banner_main_tab2_button_practise_for_free_click()

                if cur_role == "NoReg":
                    page = SignupLoginForm(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    pass
            else:
                print("")
        else:
            print("Тест не для текущих параметров")

#
#
#
    @allure.feature("F_05 | Testing '3' tab 'Main' banner. Only for 'En' language")
    @allure.story("S_05.01 | Testing 'Learn more' button on the 3 tab (1 layout) 'Main' banner")
    @allure.step("Start test button 'Learn more' on tab3 'Main' banner (Layout 1: ASIC)")
    def test_05_01_banner_main_tab3_l1_button_learn_more_asic(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: tab "Discover Pro Trading" -> button "Learn more"
        Licence: ASIC. Language - EN.
        """
        global test_link
        global page

        print(f"worker_id = {worker_id}")

        if cur_language in [""]:

            if cur_license in ["ASIC"]:
                self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)
                page = CapitalPage(d, test_link)
                if not page.current_page_is(test_link):
                    page.open_page()

                layout = page.banner_main_tab3_click()
                print(f"Current layout # {layout}")
                if layout == 1:
                    page.banner_main_tab3_l1_button_learn_more_asic_click()
                    if cur_role == "NoReg":
                        # https://capital.com/professional-clients-au
                        page.check_current_page_is("https://capital.com/professional-clients-au")
                        # Проверяем, что открылась page Sign Up "https://capital.com/trading/signup"
                        # page.check_current_page_is("https://capital.com/trading/signup")
                        d.back()
                        # page.open_page()
                        # page.check_open_esg_page()
                    elif cur_role == "Reg_NoAuth":
                        pass
                    elif cur_role == "Auth":
                        pass
                else:
                    print(f"Test not for layout # {layout}")
            else:
                print("Test not for current Licence")
        else:
            print("This test not for current Language")

#
#
#
    @allure.feature("F_05 | Testing '3' tab 'Main' banner. Only for 'En' language")
    @allure.story("S_05.02 | Testing 'Start trading' button on the 3 tab (1 layout) 'Main' banner")
    @allure.step("Start test button 'Start trading' on tab3 'Main' banner (Layout 1: ASIC)")
    def test_05_02_banner_main_tab3_l1_button_start_trading_asic(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: tab "Discover Pro Trading" -> button "Start trading"
        Licence: ASIC. Language - EN.
        """
        global test_link
        global page

        print(f"worker_id = {worker_id}")

        if cur_language in [""]:
            if cur_license in ["ASIC"]:
                self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)
                page = CapitalPage(d, test_link)
                if not page.current_page_is(test_link):
                    page.open_page()

                layout = page.banner_main_tab3_click()
                print(f"Current layout # {layout}")
                if layout == 1:
                    page.banner_main_tab3_l1_button_start_trading_asic_click()
                    if cur_role == "NoReg":
                        # Проверяем, что открылась page Sign Up "https://capital.com/trading/signup"
                        page.check_current_page_is("https://capital.com/trading/signup")
                        d.back()
                    elif cur_role == "Reg_NoAuth":
                        pass
                    elif cur_role == "Auth":
                        pass
                else:
                    print(f"Test not for layout # {layout}")
            else:
                print("Test not for current License")
        else:
            print("Test not for current Language")

#
#
#
    @allure.feature("F_05 | Testing '3' tab 'Main' banner. Only for 'En' language")
    @allure.story("S_05.03 | Testing 'Start trading' button on the 3 tab (2 layout) 'Main' banner")
    @allure.step("Start test button 'Start trading' on tab3 'Main' banner (Layout 2: All License, except ASIC)")
    def test_05_03_banner_main_tab3_l2_button_start_trading_asic(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: tab "Industry-leading support for new traders" -> button "Start trading"
        Licence: except ASIC. Language - EN.
        """
        global test_link
        global page

        print(f"worker_id = {worker_id}")

        if cur_language in [""]:
            if cur_license in ["FCA", "CYSEC", "NBRB", "CCSTV", "SEY"]:
                self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)
                page = CapitalPage(d, test_link)
                if not page.current_page_is(test_link):
                    page.open_page()

                layout = page.banner_main_tab3_click()
                print(f"Current layout # {layout}")
                if layout == 2:
                    page.banner_main_tab3_l2_button_start_trading_fca_click()
                    if cur_role == "NoReg":
                        # Проверяем, что открылась форма "Sign Up"
                        page = SignupLoginForm(d, test_link)
                        page.should_be_signup_form()
                        page.close_signup_form()
                    elif cur_role == "Reg_NoAuth":
                        pass
                    elif cur_role == "Auth":
                        pass
                else:
                    print(f"Test not for layout # {layout}")
            else:
                print("Test not for current License")
        else:
            print("Test not for current Language")

#
#
#
    @allure.feature("F_05 | Testing '3' tab 'Main' banner. Only for 'En' language")
    @allure.story("S_05.04 | Testing 'Practise for free' button on the 3 tab (2 layout) 'Main' banner")
    @allure.step("Start test button 'Practise for free' on tab3 'Main' banner (Layout 2: All, except ASIC)")
    def test_05_04_banner_main_tab3_l2_button_practise_fo_free_fca(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: tab "Industry-leading support for new traders" -> button "Practise for free"
        Licence: FCA. Language - EN.
        """
        global test_link
        global page

        print(f"worker_id = {worker_id}")

        if cur_language in [""]:
            if cur_license in ["FCA", "CYSEC", "NBRB", "CCSTV", "SEY"]:
                self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)
                page = CapitalPage(d, test_link)
                if not page.current_page_is(test_link):
                    page.open_page()

                layout = page.banner_main_tab3_click()
                print(f"Current layout # {layout}")
                if layout == 2:
                    page.banner_main_tab3_l2_button_practise_for_free_fca_click()
                    if cur_role == "NoReg":
                        # Проверяем, что открылась форма "Sign Up"
                        page = SignupLoginForm(d, test_link)
                        page.should_be_signup_form()
                        page.close_signup_form()
                    elif cur_role == "Reg_NoAuth":
                        pass
                    elif cur_role == "Auth":
                        pass
                    else:
                        print("Test not for current layout")
            else:
                print("Test not for current License")
        else:
            print("Test not for current Language")

#
#
#
    @allure.feature("F_06 | Testing '4' tab 'Main' banner. Only for 'En' language")
    @allure.story("S_06.01 | Testing 'Explore features' button on the 4 tab 'Main' banner")
    @allure.step("Start test button 'Explore features' on tab4 'Main' banner (for {cur_license} License")
    def test_06_01_banner_main_tab4_button_explore_features(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: tab "Find us on ..." -> button "Explore features"
        Licence: ALL. Language - EN.
        """
        global test_link
        global page

        print(f"worker_id = {worker_id}")

        if cur_language in [""]:
            if cur_license in ["ASIC", "FCA", "CYSEC", "NBRB", "CCSTV", "SEY"]:
                self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)
                page = CapitalPage(d, test_link)
                if not page.current_page_is(test_link):
                    page.open_page()

                page.banner_main_tab4_click()
                page.banner_main_tab4_button_explore_features_click()

                if cur_role == "NoReg":
                    # Проверяем, что открылась страница https://www.tradingview.com/broker/Capitalcom/
                    page.check_current_page_is("https://www.tradingview.com/broker/Capitalcom/")
                    d.back()
                    # page.open_page()
                    # page.check_open_tradingview_page()
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    pass
            else:
                print("")
        else:
            print("Тест не для текущих параметров")

#
#
#
    @allure.feature("F_07 | Testing 'Why Capital.com?' banner. Not for 'En' language")
    @allure.story("S_07.01 | Testing 'Jetzt traden' button on the 'Warum Capital.com?' banner")
    @allure.step("Start test button 'Jetzt traden' on 'Warum Capital.com?' banner")
    def test_03_01_banner_why_capital_button_trade_now(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: Banner [Warum Capital.com?] -> button [Jetzt traden]
        Language - DE, IT, PT. License - All
        """
        global test_link
        global page

        print(f"worker_id = {worker_id}")

        # if cur_language in ["de", "it", "pt"]:
        if cur_language not in [""]:
            if cur_license in ["ASIC", "FCA", "CYSEC", "NBRB", "CCSTV", "SEY"]:
                self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

                page = CapitalPage(d, test_link)
                if not page.current_page_is(test_link):
                    page.open_page()

                if page.de_banner_why_capital_button_trade_now_click():

                    if cur_role == "NoReg":
                        page = SignupLoginForm(d, test_link)
                        page.should_be_signup_form()
                        page.close_signup_form()
                    elif cur_role == "Reg_NoAuth":
                        pass
                    elif cur_role == "Auth":
                        pass
                else:
                    print("Button [Jetzt traden] not available")
            else:
                print("")
        else:
            print("Тест не для текущих параметров")

#
#
#
    @allure.feature("F_08 | Widget [Trading instrument]")
    @allure.story("S_08.01 | Widget [Trading instrument] tab [Most traded] button [Trade]")
    @allure.step("Start test 'Click 'Trade' buttons on the 'Most traded' tab 'Trading instrument' widget'")
    def test_08_01_widget_trading_instrument(
        self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: widget "Trading instrument"
        Licence: All. Language - ALL.
        Widgen has 2 layouts
        """
        global test_link
        global page

        tab_name = "Most traded"
        print(f"worker_id = {worker_id}")

        if not (cur_license == "FCA" and tab_name == "Cryptocurrencies"):
            self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

            page = CapitalPage(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            layout = page.what_is_the_current_layout(cur_language)
            page.widget_trading_instrument_cur_tab_click(cur_language, layout, tab_name)
            list_buttons = page.get_list_lines_cur_tab(cur_language, layout, tab_name)
            for line in range(len(list_buttons)):
                page = CapitalPage(d, test_link)
                page.selected_tab_and_line_button_trade_click(list_buttons, line)
                if cur_role == "NoReg":
                    page = SignupLoginForm(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    pass
        else:
            print(f'The tab "{tab_name}" is not available for the license "{cur_license}"')

#
#
#
    @allure.feature("F_08 | Widget [Trading instrument]")
    @allure.story("S_08.02 | Widget [Trading instrument] tab [Commodities] button [Trade]")
    @allure.step("Start test 'Click 'Trade' buttons on the 'Commodities' tab 'Trading instrument' widget'")
    def test_08_02_widget_trading_instrument(
        self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: widget "Trading instrument"
        Licence: All. Language - EN.
        Widgen has 2 layouts
        """
        global test_link
        global page

        tab_name = "Commodities"
        print(f"worker_id = {worker_id}")

        if not (cur_license == "FCA" and tab_name == "Cryptocurrencies"):
            self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

            page = CapitalPage(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            layout = page.what_is_the_current_layout(cur_language)
            page.widget_trading_instrument_cur_tab_click(cur_language, layout, tab_name)
            list_buttons = page.get_list_lines_cur_tab(cur_language, layout, tab_name)

            for line in range(len(list_buttons)):
                page = CapitalPage(d, test_link)
                page.selected_tab_and_line_button_trade_click(list_buttons, line)
                if cur_role == "NoReg":
                    page = SignupLoginForm(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                    # page = CapitalPage(d, test_link)
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    pass
        else:
            print(f'The tab "{tab_name}" is not available for the license "{cur_license}"')

#
#
#
    @allure.feature("F_08 | Widget [Trading instrument]")
    @allure.story("S_08.03 | Widget [Trading instrument] tab [Indices] button [Trade]")
    @allure.step("Start test 'Click 'Trade' buttons on the 'Indices' tab 'Trading instrument' widget'")
    def test_08_03_widget_trading_instrument(
        self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: widget "Trading instrument"
        Licence: All. Language - EN.
        Widgen has 2 layouts
        """
        global test_link
        global page

        tab_name = "Indices"
        print(f"worker_id = {worker_id}")

        if not (cur_license == "FCA" and tab_name == "Cryptocurrencies"):
            self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

            page = CapitalPage(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            layout = page.what_is_the_current_layout(cur_language)
            page.widget_trading_instrument_cur_tab_click(cur_language, layout, tab_name)
            list_buttons = page.get_list_lines_cur_tab(cur_language, layout, tab_name)

            for line in range(len(list_buttons)):
                page = CapitalPage(d, test_link)
                page.selected_tab_and_line_button_trade_click(list_buttons, line)
                if cur_role == "NoReg":
                    page = SignupLoginForm(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                    # page = CapitalPage(d, test_link)
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    pass
        else:
            print(f'The tab "{tab_name}" is not available for the license "{cur_license}"')

#
#
#
    @allure.feature("F_08 | Widget [Trading instrument]")
    @allure.story("S_08.04 | Widget [Trading instrument] tab [Cryptocurrencies] button [Trade]")
    @allure.step("Start test 'Click 'Trade' buttons on the 'Cryptocurrencies' tab 'Trading instrument' widget'")
    def test_08_04_widget_trading_instrument(
        self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: widget "Trading instrument"
        Licence: All. Language - EN.
        Widgen has 2 layouts
        """
        global test_link
        global page

        tab_name = "Cryptocurrencies"
        print(f"worker_id = {worker_id}")

        if not (cur_license == "FCA" and tab_name == "Cryptocurrencies"):
            self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

            page = CapitalPage(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            layout = page.what_is_the_current_layout(cur_language)
            page.widget_trading_instrument_cur_tab_click(cur_language, layout, tab_name)
            list_buttons = page.get_list_lines_cur_tab(cur_language, layout, tab_name)

            for line in range(len(list_buttons)):
                page = CapitalPage(d, test_link)
                page.selected_tab_and_line_button_trade_click(list_buttons, line)
                if cur_role == "NoReg":
                    page = SignupLoginForm(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                    # page = CapitalPage(d, test_link)
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    pass
        else:
            print(f'The tab "{tab_name}" is not available for the license "{cur_license}"')

#
#
#
    @allure.feature("F_08 | Widget [Trading instrument]")
    @allure.story("S_08.05 | Widget [Trading instrument] tab [Shares] button [Trade]")
    @allure.step("Start test 'Click 'Trade' buttons on the 'Shares' tab 'Trading instrument' widget'")
    def test_08_05_widget_trading_instrument(
        self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: widget "Trading instrument"
        Licence: All. Language - EN.
        Widgen has 2 layouts
        """
        global test_link
        global page

        tab_name = "Shares"
        print(f"worker_id = {worker_id}")

        if not (cur_license == "FCA" and tab_name == "Cryptocurrencies"):
            self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

            page = CapitalPage(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            layout = page.what_is_the_current_layout(cur_language)
            page.widget_trading_instrument_cur_tab_click(cur_language, layout, tab_name)
            list_buttons = page.get_list_lines_cur_tab(cur_language, layout, tab_name)

            for line in range(len(list_buttons)):
                page = CapitalPage(d, test_link)
                page.selected_tab_and_line_button_trade_click(list_buttons, line)
                if cur_role == "NoReg":
                    page = SignupLoginForm(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                    # page = CapitalPage(d, test_link)
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    pass
        else:
            print(f'The tab "{tab_name}" is not available for the license "{cur_license}"')

#
#
#
    @allure.feature("F_08 | Widget [Trading instrument]")
    @allure.story("S_08.06 | Widget [Trading instrument] tab [Forex] button [Trade]")
    @allure.step("Start test 'Click 'Trade' buttons on the 'Forex' tab 'Trading instrument' widget'")
    def test_08_06_widget_trading_instrument(
        self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: widget "Trading instrument"
        Licence: All. Language - EN.
        Widgen has 2 layouts
        """
        global test_link
        global page

        tab_name = "Forex"
        print(f"worker_id = {worker_id}")

        if not (cur_license == "FCA" and tab_name == "Cryptocurrencies"):
            self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

            page = CapitalPage(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            layout = page.what_is_the_current_layout(cur_language)
            page.widget_trading_instrument_cur_tab_click(cur_language, layout, tab_name)
            list_buttons = page.get_list_lines_cur_tab(cur_language, layout, tab_name)

            for line in range(len(list_buttons)):
                page = CapitalPage(d, test_link)
                page.selected_tab_and_line_button_trade_click(list_buttons, line)
                if cur_role == "NoReg":
                    page = SignupLoginForm(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                    # page = CapitalPage(d, test_link)
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    pass
        else:
            print(f'The tab "{tab_name}" is not available for the license "{cur_license}"')

#
#
#
    @allure.feature("F_08 | Widget [Trading instrument]")
    @allure.story("S_08.07 | Widget [Trading instrument] tab [ETFs] button [Trade]")
    @allure.step("Start test 'Click 'Trade' button on the 'ETFs' tab 'Trading instrument' widget'")
    def test_08_07_widget_trading_instrument(
        self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: widget "Trading instrument"
        Licence: All. Language - EN.
        Widgen has 2 layouts
        """
        global test_link
        global page

        tab_name = "ETFs"
        print(f"worker_id = {worker_id}")

        if not (cur_license == "FCA" and tab_name == "Cryptocurrencies"):
            self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

            page = CapitalPage(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            layout = page.what_is_the_current_layout(cur_language)
            page.widget_trading_instrument_cur_tab_click(cur_language, layout, tab_name)
            list_buttons = page.get_list_lines_cur_tab(cur_language, layout, tab_name)

            for line in range(len(list_buttons)):
                page = CapitalPage(d, test_link)
                page.selected_tab_and_line_button_trade_click(list_buttons, line)
                if cur_role == "NoReg":
                    page = SignupLoginForm(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                    # page = CapitalPage(d, test_link)
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    pass
        else:
            print(f'The tab "{tab_name}" is not available for the license "{cur_license}"')

#
#
#
    @allure.feature("F_09 | Testing 'Still looking for ...' widget")
    @allure.story("S_09.01 | Testing 'Create your account' button on the 'Still looking for ...' widget")
    @allure.step("Start tests of widget 'Still looking for a broker you can trust?'")
    def test_09_01_widget_still_looking_button_1_create_your_account(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: widget "Still looking for ..." -> button "1. Ctreated your account"
        Licence: All. Language - EN, DE, IT.
        """
        global test_link
        global page

        print(f"worker_id = {worker_id}")

        if cur_license in ["ASIC", "FCA", "CYSEC", "NBRB", "CCSTV", "SEY"]:
            self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

            page = CapitalPage(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            page.widget_still_looking_button_1_create_your_account_click(cur_language)

            if cur_role == "NoReg":
                page = SignupLoginForm(d, test_link)
                page.should_be_signup_form()
                page.close_signup_form()
            elif cur_role == "Reg_NoAuth":
                pass
            elif cur_role == "Auth":
                pass
        else:
            print("")

#
#
#
    @allure.feature("F_10 | Testing 'Promo Market' widget")
    @allure.story("S_10.01 | Testing 'Trade Now' button on the 'Promo Market' widget")
    @allure.step("Run test for 'Promo Market' widget")
    def test_10_01_widget_promo_market_button_trade_now(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: widget "Promo Market" -> button "Trade Now"
        Licence: ALL. Language - EN.
        """
        global test_link
        global page

        print(f"worker_id = {worker_id}")

        if cur_language in [""]:
            if cur_license in ["ASIC", "FCA", "CYSEC", "NBRB", "CCSTV", "SEY"]:
                self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

                page = CapitalPage(d, test_link)
                if not page.current_page_is(test_link):
                    page.open_page()
                time.sleep(1)
                qty = page.how_many_dif_buttons_trade_now_on_widget_promo_market()
                if qty != 0:
                    for i in range(qty):
                        page.widget_promo_market_button_trade_now_click(i)

                        if cur_role == "NoReg":
                            page = SignupLoginForm(d, test_link)
                            page.should_be_signup_form()
                            page.close_signup_form()
                            page = CapitalPage(d, test_link)
                        elif cur_role == "Reg_NoAuth":
                            pass
                        elif cur_role == "Auth":
                            pass
                else:
                    print("Widget is not present on the current page!")
            else:
                print("")
        else:
            print("Test not for current language!")

#
#
#
    @allure.feature("F_11 | Testing 'Explore our platform' widget")
    @allure.story("S_11.01 | Testing 'Try now' button on the 'Explore our platform' widget")
    @allure.step("Run test for widget 'Explore our platform'")
    def test_11_01_widget_explore_our_platform(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: widget "Explore our platform" -> button "Try now"
        Licence: ALL. Language - ALL.
        """
        global test_link
        global page

        print(f"worker_id = {worker_id}")

        if cur_license in ["ASIC", "FCA", "CYSEC", "NBRB", "CCSTV", "SEY"]:
            self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

            page = CapitalPage(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            page.widget_explore_our_platform_button_tray_now_click(cur_language)

            if cur_role == "NoReg":
                page = SignupLoginForm(d, test_link)
                page.should_be_signup_form()
                page.close_signup_form()
            elif cur_role == "Reg_NoAuth":
                pass
            elif cur_role == "Auth":
                pass
        else:
            print("")

#
#
#
    @allure.feature("F_12 | Testing 'New To Trading?' banner")
    @allure.story("S_12.01 | Testing 'Practise for free' button on the 'New To Trading?' banner")
    @allure.step("Test for 'Practise for free' button on the 'New To Trading?' banner")
    def test_12_01_de_banner_new_to_trading_button_practise_for_free(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: Banner "New To Trading?" -> button "Practise for free"
        Licence: ALL. Language - DE, IT.
        """
        global test_link
        global page

        print(f"worker_id = {worker_id}")

        if cur_language not in [""]:
            if cur_license in ["ASIC", "FCA", "CYSEC", "NBRB", "CCSTV", "SEY"]:
                self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

                page = CapitalPage(d, test_link)
                if not page.current_page_is(test_link):
                    page.open_page()

                page = CapitalPage(d, test_link)
                if page.de_banner_new_to_trading_button_practise_fo_free_click():
                    if cur_role == "NoReg":
                        page = SignupLoginForm(d, test_link)
                        page.should_be_signup_form()
                        page.close_signup_form()
                    elif cur_role == "Reg_NoAuth":
                        pass
                    elif cur_role == "Auth":
                        pass
                else:
                    print("Banner of counters is not present on the current page!")
            else:
                print("")
        else:
            print("Test not for current language!")

#
#
#
    @allure.feature("F_13 | Testing 'New to trading?' widget")
    @allure.story("S_13.01 | Testing 'Practise for free' button on the 'Explore our platform' widget")
    @allure.step("Run test for widget 'New to trading?'")
    def test_13_01_widget_new_to_trading(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: widget "New to trading?" -> button "Practise for free"
        Licence: FCA. Language - EN.
        """
        global test_link
        global page

        print(f"worker_id = {worker_id}")

        if cur_license in ["ASIC", "FCA", "CYSEC", "NBRB", "CCSTV", "SEY"]:
            self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

            page = CapitalPage(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            assert \
                page.widget_new_to_trading_button_practise_for_free_click(cur_language), \
                "'New to trading?' widget is not present on this page!"

            if cur_role == "NoReg":
                page = SignupLoginForm(d, test_link)
                page.should_be_signup_form()
                page.close_signup_form()
            elif cur_role == "Reg_NoAuth":
                pass
            elif cur_role == "Auth":
                pass
        else:
            print("")

#
#
#
    @allure.feature("F_14 | Testing 'Trading calculator' widget")
    @allure.story("S_14.01 | Testing 'Start trading' button on the 'Trading calculator' widget")
    @allure.step("Run test for button 'Start trading' for widget 'Trading calculator'")
    def test_14_01_widget_trading_calculator_button_start_trading(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: widget "Trading calculator" -> button "Start trading"
        Licence: ALL. Language - EN.
        """
        global test_link
        global page

        print(f"worker_id = {worker_id}")

        if cur_language in [""]:
            if cur_license in ["ASIC", "FCA", "CYSEC", "NBRB", "CCSTV", "SEY"]:
                self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

                page = CapitalPage(d, test_link)
                if not page.current_page_is(test_link):
                    page.open_page()

                page.widget_trading_calculator_button_start_trading_click()

                if cur_role == "NoReg":
                    page = SignupLoginForm(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    pass
            else:
                print("")
        else:
            print("Тест не для текущих параметров")

#
#
#
    @allure.feature("F_15 | Testing 'Trader's Dashboard' widget")
    @allure.story("S_15.01 | Testing 'Trade' button on the 'Trader's Dashboard' widget")
    @allure.step("Run test for buttons 'Trade' on 'Trader's Dashboard' widget")
    def test_15_01_widget_traders_dashboard_button_trade(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: widget "Trader's Dashboard" -> button "Trade"
        Licence: ALL. Language - EN.
        """
        global test_link
        global page

        print(f"worker_id = {worker_id}")

        if cur_language in [""]:
            if cur_license in ["ASIC", "FCA", "CYSEC", "NBRB", "CCSTV", "SEY"]:
                self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

                page = CapitalPage(d, test_link)
                if not page.current_page_is(test_link):
                    page.open_page()

                qty = page.how_many_buttons_trade_on_widget_traders_dashboard()
                if qty != 0:
                    for i in range(qty):
                        page = CapitalPage(d, test_link)
                        page.widget_traders_dashboard_button_trade_click(i)

                        if cur_role == "NoReg":
                            page = SignupLoginForm(d, test_link)
                            page.should_be_signup_form()
                            page.close_signup_form()
                        elif cur_role == "Reg_NoAuth":
                            pass
                        elif cur_role == "Auth":
                            pass
                else:
                    print("Widget is not present on the current page!")
            else:
                print("")
        else:
            print("Test not for current language!")

#
#
#
    @allure.feature("F_16 | Testing 'Counters' banner")
    @allure.story("S_16.01 | Testing 'Try now' button on the 'Counters' banner")
    @allure.step("Test for 'Try now' button on banner with counters")
    def test_16_01_banner_of_counters_button_try_now(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: Banner of counters -> button "Try now"
        Licence: ALL. Language - EN, DE, IT.
        """
        global test_link
        global page

        print(f"worker_id = {worker_id}")

        if cur_license in ["ASIC", "FCA", "CYSEC", "NBRB", "CCSTV", "SEY"]:
            self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

            page = CapitalPage(d, test_link)
            if not page.current_page_is(test_link):
                page.open_page()

            page = CapitalPage(d, test_link)
            if page.banner_of_counters_button_try_now_click():
                if cur_role == "NoReg":
                    page = SignupLoginForm(d, test_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                elif cur_role == "Reg_NoAuth":
                    pass
                elif cur_role == "Auth":
                    pass
            else:
                print("Banner of counters is not present on the current page!")
        else:
            print("")

#
#
#
#
# авторизация пользователя
    # def to_do_authorization(self, d, test_link, test_login, test_password):
    #     global link
    #     global page
    #     assert test_login != "", "Авторизация невозможна. Не указан e-mail"
    #     assert test_password != "", "Авторизация невозможна. Не указан пароль"
    #     # нажать в хедере на кнопку "Log in"
    #     page = HeaderElement(d, test_link)
    #     # page.open_page()
    #     page.click_button_login_on_header()
    #     # проверить, открылась ли форма "Log in"
    #     # ввести логин, вести пароль, нажать подтвердить

    # регистрация пользователя
    # def to_do_registration(self, d, cur_login, cur_password):
    #     global link
    #     global page
    #     assert cur_login != "", "Регистрация невозможна. Не указан e-mail"
    #     assert cur_password != "", "Регистация невозможна. Не указан пароль"
    #     # нажать в хедере на кнопку "Log in"
    #     # page = HeaderElement(d, test_link)
    #     # page.open_page()
    #     page.click_button_login_on_header()
    #     # проверить, открылась ли форма "Log in"
    #     # перейти на форму "Sigup", нажав кнопку "SignUp"
    #     # проверить, открылась ли форма "SignUp"
    #     # ввести логин, вести пароль, нажать подтвердить
