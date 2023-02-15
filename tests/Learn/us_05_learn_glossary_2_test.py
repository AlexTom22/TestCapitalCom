"""
-*- coding: utf-8 -*-
@Time    : 2023/02/08 10:00
@Author  : Alexander Tomelo
"""
# import time
import pytest
import allure
# import random
# from datetime import datetime
from tests.conditions import Conditions
# from pages.learn.learn_glossary import Glossary
# from pages.menu import MenuBurger
from pages.header import Header
from pages.signup_login_form import SignupLoginForm
from src.src import (
    CapitalComPageSrc,
)
# from pages.learn.learn_glossary_locators import (
#     FinancialDictionary,
# )

list_href = list()


def pytest_generate_tests(metafunc):
    
    if "cur_item_link" in metafunc.fixturenames:
        
        name_file = "tests/Learn/list_of_href.txt"
        list_item_link = list()
        file = open(name_file, "r")
        for line in file:
            list_item_link.append(line[:-1])
        file.close()
        metafunc.parametrize("cur_item_link", list_item_link, scope="class")


@pytest.mark.us_05
@pytest.mark.parametrize(
    "cur_login, cur_password",
    [
        ("Empty", "Empty"),
        # ("aqa.tomelo.an@gmail.com", "iT9Vgqi6d$fiZ*Z"),
    ], scope="class"
)
@allure.epic('US_05. Testing Glossary Item page in "Learn to trade" menu. All language. All license')
class TestGlossaryItems:

    @allure.feature("TS_05 | Test menu [Learn to Trade] / [Glossary] / [item]")
    @allure.story("TC_05.01 | Testing 'Log In' button on the header page")
    @allure.step("Start test button 'Log In' on header.")
    @allure.title("TC_05_01 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_05_01_header_button_login(
            self, worker_id, d, cur_item_link, cur_login, cur_password, cur_language, cur_license, cur_role,
            prob_run_tc, datetime_now
    ):
        """
        Check: Header -> button [Log In]
        Language: All. License: All.
        """
        # page5 = None

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        print(f"worker_id = {worker_id}")

        page5 = Conditions(d, "")
        page5.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )

        if cur_role != "Auth":
            page5 = Header(d, cur_item_link)
            if not page5.current_page_is(cur_item_link):
                page5.open_page()
            page5.click_button_login_on_header()

            if cur_role == "NoReg":
                page5 = SignupLoginForm(d, cur_item_link)
                page5.should_be_login_form()
                page5.close_login_form()
        else:
            pytest.mark.skip(f"This test not for 'Auth' role")

#
#
#
    # @allure.feature("TS_05 | Test menu [Learn to Trade] / [Glossary] / [item]")
    # @allure.story("TC_05.02 | Testing 'Trade Now' button on the header page")
    # @allure.step("Start test button 'Trade Now' on header.")
    # @allure.title("TC_05_02 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    # def test_05_02_header_button_trade_now(
    #         self, worker_id, d, cur_item_link, cur_login, cur_password, cur_role, cur_language, cur_license,
    #         prob_run_tc, datetime_now
    # ):
    #     """
    #     Check: Header -> button [Trade Now]
    #     Language: All. License: All.
    #     """
    #     if prob_run_tc != "":
    #         pytest.skip(f"{prob_run_tc}   {datetime_now}")
    #
    #     print(f"worker_id = {worker_id}")
    #
    #     page5 = Conditions()
    #     page5.preconditions(
    #         d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
    #     )
    #
    #     # page5 = MenuBurger()
    #     # page5.click_menu_burger(d, cur_language)
    #     # page5.click_sub_menu_learn_to_trade(d, cur_language)
    #     # page5.click_glossary_item(d, cur_language)
    #
    #     if cur_role != "Auth":
    #         page5 = Header(d, cur_item_link)
    #         if not page5.current_page_is(cur_item_link):
    #             page5.open_page()
    #
    #         page5.click_button_signup_on_header()
    #
    #         if cur_role == "NoReg":
    #             page = SignupLoginForm(d, cur_item_link)
    #             page.should_be_signup_form()
    #             page.close_signup_form()
    #     else:
    #         pytest.mark.skip(f"This test not for 'Auth' role")
    #
#
#
#
#     @allure.feature("US_05 | Test menu [Learn to Trade] / [Glossary] / [item]")
#     @allure.story("TC_05.03 | Testing 'Video' frame")
#     @allure.step("Start tests of 'Video' frame.")
#     @allure.title("TC_05_03 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
#     def test_05_03_widget_still_looking_button_1_create_your_account(
#             self, worker_id, d, cur_item_link, cur_login, cur_password, cur_role, cur_language, cur_license,
#             prob_run_tc, datetime_now
#     ):
#         """
#         Check: widget "Still looking for ..." -> button "1. Created your account"
#         Language: All. Licence: All.
#         """
#         test_link = None
#         page = None
#
#         if prob_run_tc != "":
#             pytest.skip(f"{prob_run_tc}   {datetime_now}")
#
#         print(f"worker_id = {worker_id}")
#
#         self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)
#
#         page = Markets(d, test_link)
#         if not page.current_page_is(test_link):
#             page.open_page()
#
#         page = MenuBurger()
#         page.click_menu_burger(d, cur_language)
#         page.click_sub_menu_learn_to_trade(d, cur_language)
#         page.click_glossary_item(d, cur_language)
#
#         page.widget_still_looking_button_1_create_your_account_click(cur_language)
#
#         if cur_role == "NoReg":
#             page = SignupLoginForm(d, test_link)
#             page.should_be_signup_form()
#             page.close_signup_form()
#         elif cur_role == "Reg_NoAuth":
#             pass
#         elif cur_role == "Auth":
#             page.should_be_link("https://capital.com/trading/platform")
#             d.back()
#
# #
# #
# #
#     @allure.feature("US_05 | Test menu [Learn to Trade] / [Glossary] / [item]")
#     @allure.story("TC_05.04 | Testing 'Trade Now' button")
#     @allure.step("Start tests of button 'Trade Now'.")
#     @allure.title("TC_05_04 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
#     def test_05_04_widget_still_looking_button_1_create_your_account(
#             self, worker_id, d, cur_item_link, cur_login, cur_password, cur_role, cur_language, cur_license,
#             prob_run_tc, datetime_now
#     ):
#         """
#         Check: widget "Still looking for ..." -> button "1. Created your account"
#         Language: All. Licence: All.
#         """
#         global test_link
#         global page
#
#         if prob_run_tc != "":
#             pytest.skip(f"{prob_run_tc}   {datetime_now}")
#
#         print(f"worker_id = {worker_id}")
#
#         self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)
#
#         page = Markets(d, test_link)
#         if not page.current_page_is(test_link):
#             page.open_page()
#
#         page = MenuBurger()
#         page.click_menu_burger(d, cur_language)
#         page.click_sub_menu_learn_to_trade(d, cur_language)
#         page.click_glossary_item(d, cur_language)
#
#
#         page.widget_still_looking_button_1_create_your_account_click(cur_language)
#
#         if cur_role == "NoReg":
#             page = SignupLoginForm(d, test_link)
#             page.should_be_signup_form()
#             page.close_signup_form()
#         elif cur_role == "Reg_NoAuth":
#             pass
#         elif cur_role == "Auth":
#             page.should_be_link("https://capital.com/trading/platform")
#             d.back()
#
# #
# #
# #
#     @allure.feature("US_05 | Test menu [Learn to Trade] / [Glossary] / [item]")
#     @allure.story("TC_05.05 | Testing 'Create your account' button on the 'Still looking for ...' widget")
#     @allure.step("Start tests of widget 'Still looking for a broker you can trust?'.")
#     @allure.title("TC_05_05 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
#     def test_05_05_widget_still_looking_button_1_create_your_account(
#             self, worker_id, d, cur_item_link, cur_login, cur_password, cur_role, cur_language, cur_license,
#             prob_run_tc, datetime_now
#     ):
#         """
#         Check: widget "Still looking for ..." -> button "1. Created your account"
#         Language: All. Licence: All.
#         """
#         global test_link
#         global page
#
#         if prob_run_tc != "":
#             pytest.skip(f"{prob_run_tc}   {datetime_now}")
#
#         print(f"worker_id = {worker_id}")
#
#         self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)
#
#         page = Markets(d, test_link)
#         if not page.current_page_is(test_link):
#             page.open_page()
#
#         page = MenuBurger()
#         page.click_menu_burger(d, cur_language)
#         page.click_sub_menu_learn_to_trade(d, cur_language)
#         page.click_glossary_item(d, cur_language)
#
#         page.widget_still_looking_button_1_create_your_account_click(cur_language)
#
#         if cur_role == "NoReg":
#             page = SignupLoginForm(d, test_link)
#             page.should_be_signup_form()
#             page.close_signup_form()
#         elif cur_role == "Reg_NoAuth":
#             pass
#         elif cur_role == "Auth":
#             page.should_be_link("https://capital.com/trading/platform")
#             d.back()
