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
from pages.capital_page import CapitalPage
from pages.header_element import HeaderElement
from pages.signup_login_form import SignupLoginForm
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
flag_preconditions = False
accept_all_cookies = False


@pytest.mark.parametrize(
    "cur_login, cur_password",
    [
        ("Empty", "Empty"),
        # ("qa.tomelo.an@gmail.com", "???"),
    ], scope="class"
)
@pytest.mark.parametrize(
    "cur_role",
    [
        "NoReg",
        # "Reg_NoAuth",
        # "Auth",
    ], scope="class"
)
@pytest.mark.parametrize(
    "cur_license",
    [
        "ASIC",
        "FCA",
        "CYSEC",
        "NBRB",
        "CCSTV",
        "SEY",
    ], scope="class"
)
@pytest.mark.parametrize(
    "cur_language",
    [
        "",
        # "ar",
        # "bg",
        # "cn",
        # "cs",
        # "da",
        # "de",
        # "el",
        # "as",
        # "et",
        # "fi",
        # "fr",
        # "hr",
        # "id",
        # "lt",
        # "lv",
        # "nl",
        # "pl",
        # "pt",
        # "ro",
        # "ru",
        # "sk",
        # "sl",
        # "sv",
        # "th",
        # "vi",
        # "zh",
    ], scope="class"
)
class Tests:

    @allure.step("Run preconditions with param-s:")
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
    @allure.step("Start test button 'Log In' on header")
    def test_01_header_button_login(
            self, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        global test_link
        global page
        global flag_preconditions

        if cur_language in [""]:
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
        else:
            print("Тест не для текущих параметров")

#
#
#
    @allure.step("Start test button 'Trade Now' on header")
    def test_02_header_button_trade_now(
            self, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        global test_link
        global page
        global flag_preconditions

        if cur_language in [""]:
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
        else:
            print("Тест не для текущих параметров")

#
#
#
    @allure.step("Start test button 'Trade Now' on tab1 'Main' banner (for all License)")
    def test_03_banner_main_tab1_button_trade_now(
            self, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: tab "1" -> button "Trade now"
        Language - EN. License - All
        """
        global test_link
        global page
        global flag_preconditions

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
    @allure.step("Start test button 'Practise for free' on tab1 'Main' banner (for all License)")
    def test_03_banner_main_tab1_button_practise_for_free(
            self, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: tab "1" -> button "Practice for free"
        Licence: FCA. Language - EN.
        """
        global test_link
        global page
        global flag_preconditions

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

    # @allure.step("Start test button 'Open account' on tab1 'Main' banner")
    # def test_03_3_banner_main_tab1_button_open_account(
    #         self, d, cur_login, cur_password, cur_role, cur_language, cur_license
    # ):
    #     """
    #     Check: tab "Spread betting" -> button "Open account"
    #     Licence: FCA. Language - EN.
    #     """
    #     global test_link
    #     global page
    #     global flag_preconditions
    #
    #     if cur_language in [""]:
    #         if cur_license in []:
    #             self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)
    #
    #             page = CapitalPage(d, test_link)
    #             if not page.current_page_is(test_link):
    #                 page.open_page()
    #
    #             page.baner_main_tab1_click()
    #             page.banner_main_tab1_button_open_account_click()
    #
    #             if cur_role == "NoReg":
    #                 # Проверяем, что открылась форма SignUP
    #                 page = SignupLoginForm(d, test_link)
    #                 page.should_be_signup_form()
    #                 page.close_signup_form()
    #             elif cur_role == "Reg_NoAuth":
    #                 pass
    #             elif cur_role == "Auth":
    #                 pass
    #         else:
    #             print("")
    #     else:
    #         print("Тест не для текущих параметров")
    #

#
#
#
    @allure.step("Start test button 'Take me there' on tab2 'Main' banner (for all License)")
    def test_04_banner_main_tab2_button_take_me_there(
            self, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: tab "Want to take your trading to the next level?" -> button "Take me there"
        Licence: FCA. Language - EN.
        """
        global test_link
        global page
        global flag_preconditions

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
    # @allure.step("Start test button 'Start trading' on tab2 'Main' banner")
    # def test_04_2_banner_main_tab2_button_start_trading(
    #         self, d, cur_login, cur_password, cur_role, cur_language, cur_license
    # ):
    #     """
    #     Check: tab "Industry-leading ..." -> button "Start trading"
    #     Licence: FCA. Language - EN.
    #     """
    #     global test_link
    #     global page
    #     global flag_preconditions
    #
    #     if cur_language in [""]:
    #         if cur_license in []:
    #             self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)
    #
    #             page = CapitalPage(d, test_link)
    #             if not page.current_page_is(test_link):
    #                 page.open_page()
    #
    #             page.banner_main_tab2_click()
    #             page.banner_main_tab2_button_start_trading_click()
    #
    #             if cur_role == "NoReg":
    #                 # Проверяем, что открылась форма SignUP
    #                 page = SignupLoginForm(d, test_link)
    #                 page.should_be_signup_form()
    #                 page.close_signup_form()
    #             elif cur_role == "Reg_NoAuth":
    #                 pass
    #             elif cur_role == "Auth":
    #                 pass
    #         else:
    #             print("")
    #     else:
    #         print("Тест не для текущих параметров")
    #
    # @allure.step("Start test button 'Practise for free' on tab2 'Main' banner")
    # def test_04_3_banner_main_tab2_button_practise_for_free(
    #         self, d, cur_login, cur_password, cur_role, cur_language, cur_license
    # ):
    #     """
    #     Check: tab "Industry-leading ..." -> button "Practice for free"
    #     Licence: FCA. Language - EN.
    #     """
    #     global test_link
    #     global page
    #     global flag_preconditions
    #
    #     if cur_language in [""]:
    #         if cur_license in []:
    #             self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)
    #
    #             page = CapitalPage(d, test_link)
    #             if not page.current_page_is(test_link):
    #                 page.open_page()
    #
    #             page.banner_main_tab2_click()
    #             page.banner_main_tab2_button_practise_for_free_click()
    #
    #             if cur_role == "NoReg":
    #                 page = SignupLoginForm(d, test_link)
    #                 page.should_be_signup_form()
    #                 page.close_signup_form()
    #             elif cur_role == "Reg_NoAuth":
    #                 pass
    #             elif cur_role == "Auth":
    #                 pass
    #         else:
    #             print("")
    #     else:
    #         print("Тест не для текущих параметров")
    #

    @allure.step("Start test button 'Learn more' on tab3 'Main' banner (Layout 1: ASIC)")
    def test_05_banner_main_tab3_l1_button_learn_more_asic(
            self, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: tab "Discover Pro Trading" -> button "Learn more"
        Licence: ASIC. Language - EN.
        """
        global test_link
        global page
        global flag_preconditions

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
#
#
    @allure.step("Start test button 'Start trading' on tab3 'Main' banner (Layout 1: ASIC)")
    def test_05_banner_main_tab3_l1_button_start_trading_asic(
            self, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: tab "Discover Pro Trading" -> button "Start trading"
        Licence: ASIC. Language - EN.
        """
        global test_link
        global page
        global flag_preconditions

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

    @allure.step("Start test button 'Start trading' on tab3 'Main' banner (Layout 2: All License, except ASIC)")
    def test_05_banner_main_tab3_l2_button_start_trading_asic(
            self, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: tab "Industry-leading support for new traders" -> button "Start trading"
        Licence: except ASIC. Language - EN.
        """
        global test_link
        global page
        global flag_preconditions

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

    @allure.step("Start test button 'Practise for free' on tab3 'Main' banner (Layout 2: All, except ASIC)")
    def test_05_banner_main_tab3_l2_button_practise_fo_free_fca(
            self, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: tab "Industry-leading support for new traders" -> button "Practise for free"
        Licence: FCA. Language - EN.
        """
        global test_link
        global page
        global flag_preconditions

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
#
#
    @allure.step("Start test button 'Explore features' on tab4 'Main' banner (for all License")
    def test_06_banner_main_tab4_button_explore_features(
            self, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: tab "Find us on ..." -> button "Explore features"
        Licence: ALL. Language - EN.
        """
        global test_link
        global page
        global flag_preconditions

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

# #
# #
# #
# #
# #
# # Widget “Trading instrument” -> Tab "Most Trading"
#     @pytest.mark.parametrize(
#         "tab_name",
#         [
#             "Most Trading",
#             "Commodities",
#             "Indices",
#             "Shares",
#             "Forex",
#             "ETFs",
#         ],
#     )
#     def test_widget_trading_instrument_tab_most_trading(
#         self, d, cur_login, cur_password, cur_role, cur_language, cur_license, tab_name
#     ):
#         """
#         Check: widget "Trading instrument" -> tab "Most traded"
#         Licence: FCA. Language - EN.
#         """
#         global test_link
#         global page
#         global flag_preconditions
#
#         if cur_language in [""]:
#             if cur_license in ["ASIC", "FCA", "CYSEC", "NBRB", "CCSTV", "SEY"]:
#                 if not flag_preconditions:
#                     self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)
#                     flag_preconditions = True
#
#                 print(f"{cur_license}, {cur_language}, {cur_role}, {cur_login}, {cur_password}")
#                 page = CapitalPage(d, test_link)
#                 page.open_page()
#
#                 page.select_tab_on_widget_trading_instrument(tab_name)
#
#                 for y in range(7):
#                     # page = CapitalPage(d, test_link)
#                     page.click_button_trade_on_selected_line(tab_name, y)
#                     if cur_role == "NoReg":
#                         page = SignupLoginForm(d, test_link)
#                         page.should_be_signup_form()
#                         page.close_signup_frame()
#                         page = CapitalPage(d, test_link)
#                     elif cur_role == "Reg_NoAuth":
#                         pass
#                     elif cur_role == "Auth":
#                         pass
#             else:
#                 print("")
#         else:
#             print("Тест не для текущих параметров")
#
# #
# #
# #
# #
# #
# #
# # Widget "Still looking for a broker you can trust?"
#     def test_widget_still_looking_button_1_create_your_accaunt(
#             self, d, cur_login, cur_password, cur_role, cur_language, cur_license
#     ):
#         """
#         Check: widget "Still looking for ..." -> button "1. Ctreated your account"
#         Licence: FCA. Language - EN.
#         """
#         global test_link
#         global page
#         global flag_preconditions
#
#         if cur_language in [""]:
#             if cur_license in ["ASIC", "FCA", "CYSEC", "NBRB", "CCSTV", "SEY"]:
#                 if not flag_preconditions:
#                     self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)
#                     flag_preconditions = True
#
#                 print(cur_license, cur_language, cur_role, cur_login, cur_password)
#                 page = CapitalPage(d, test_link)
#                 page.open_page()
#
#                 page.click_widget_still_looking_button_1_create_your_account()
#
#                 if cur_role == "NoReg":
#                     page = SignupLoginForm(d, test_link)
#                     page.should_be_signup_form()
#                     page.close_signup_form()
#                 elif cur_role == "Reg_NoAuth":
#                     pass
#                 elif cur_role == "Auth":
#                     pass
#             else:
#                 print("")
#         else:
#             print("Тест не для текущих параметров")
#
# #
# #
# #
# #
# #
# # Widget "Promo Market"
#     def test_widget_promo_market_button_trade_now(
#             self, d, cur_login, cur_password, cur_role, cur_language, cur_license
#     ):
#         """
#         Check: widget "Promo Market" -> button "Trade Now"
#         Licence: FCA. Language - EN.
#         """
#         global test_link
#         global page
#         global flag_preconditions
#
#         if cur_language in [""]:
#             if cur_license in ["ASIC", "FCA", "CYSEC", "NBRB", "CCSTV", "SEY"]:
#                 if not flag_preconditions:
#                     self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)
#                     flag_preconditions = True
#
#                 print(f"{cur_license}, {cur_language}, {cur_role}, {cur_login}, {cur_password}")
#                 page = CapitalPage(d, test_link)
#                 page.open_page()
#
#                 page.click_widget_promo_market_button_trade_now()
#
#                 if cur_role == "NoReg":
#                     page = SignupLoginForm(d, test_link)
#                     page.should_be_signup_form()
#                     page.close_signup_form()
#                 elif cur_role == "Reg_NoAuth":
#                     pass
#                 elif cur_role == "Auth":
#                     pass
#             else:
#                 print("")
#         else:
#             print("Тест не для текущих параметров")
#
# #
# #
# #
# #
# #
# #   Widget "Explore our platform"
#     def test_widget_explore_our_platform(
#             self, d, cur_login, cur_password, cur_role, cur_language, cur_license
#     ):
#         """
#         Check: widget "Explore our platform" -> button "Try now"
#         Licence: FCA. Language - EN.
#         """
#         global test_link
#         global page
#         global flag_preconditions
#
#         if cur_language in [""]:
#             if cur_license in ["ASIC", "FCA", "CYSEC", "NBRB", "CCSTV", "SEY"]:
#                 if not flag_preconditions:
#                     self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)
#                     flag_preconditions = True
#
#                 print(cur_license, cur_language, cur_role, cur_login, cur_password)
#                 page = CapitalPage(d, test_link)
#                 page.open_page()
#
#                 page.click_button_tray_now_on_widget_explore_our_platform()
#
#                 if cur_role == "NoReg":
#                     page = SignupLoginForm(d, test_link)
#                     page.should_be_signup_form()
#                     page.close_signup_form()
#                 elif cur_role == "Reg_NoAuth":
#                     pass
#                 elif cur_role == "Auth":
#                     pass
#             else:
#                 print("")
#         else:
#             print("Тест не для текущих параметров")
#
# #
# #
# #
# #
# #
# # Wigget "New to trading ?"         +
#     def test_widget_new_to_trading(
#             self, d, cur_login, cur_password, cur_role, cur_language, cur_license
#     ):
#         """
#         Check: widget "New to trading?" -> button "Practise for free"
#         Licence: FCA. Language - EN.
#         """
#         global test_link
#         global page
#         global flag_preconditions
#
#         if cur_language in [""]:
#             if cur_license in ["ASIC", "FCA", "CYSEC", "NBRB", "CCSTV", "SEY"]:
#                 if not flag_preconditions:
#                     self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)
#                     flag_preconditions = True
#
#                 print(cur_license, cur_language, cur_role, cur_login, cur_password)
#                 page = CapitalPage(d, test_link)
#                 page.open_page()
#
#                 page.click_button_practise_for_free_on_widget_new_to_trading()
#
#                 if cur_role == "NoReg":
#                     page = SignupLoginForm(d, test_link)
#                     page.should_be_signup_form()
#                     page.close_signup_form()
#                 elif cur_role == "Reg_NoAuth":
#                     pass
#                 elif cur_role == "Auth":
#                     pass
#             else:
#                 print("")
#         else:
#             print("Тест не для текущих параметров")

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
