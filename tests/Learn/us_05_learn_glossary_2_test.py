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
from pages.header import Header
from pages.Learn.learn_glossary import ItemPage
# from pages.menu import MenuBurger
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
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

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
    @allure.feature("TS_05 | Test menu [Learn to Trade] / [Glossary] / [item]")
    @allure.story("TC_05.02 | Testing 'Trade Now' button on the header page")
    @allure.step("Start test button 'Trade Now' on header.")
    @allure.title("TC_05_02 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_05_02_header_button_trade_now(
            self, worker_id, d, cur_item_link, cur_login, cur_password, cur_language, cur_license, cur_role,
            prob_run_tc, datetime_now
    ):
        """
        Check: Header -> button [Trade Now]
        Language: All. License: All.
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        page5 = Conditions(d, "")
        page5.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )

        if cur_role == "NoReg":
            page5 = Header(d, cur_item_link)
            if not page5.current_page_is(cur_item_link):
                page5.open_page()
            page5.click_button_signup_on_header()
            if cur_role == "NoReg":
                page5 = SignupLoginForm(d, cur_item_link)
                page5.should_be_signup_form()
                page5.close_signup_form()

        elif cur_role == "Auth":
            pytest.mark.skip(f"This test not for 'Auth' role")
        elif cur_role == "RegNoAuth":
            pytest.mark.skip(f"This test not for 'RegNoAuth' role")

#
#
#
    @allure.feature("TS_05 | Test menu [Learn to Trade] / [Glossary] / [item]")
    @allure.story("TC_05.03 | Testing 'Video' frame")
    @allure.step("Start tests of 'Video' frame.")
    @allure.title("TC_05_03 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_05_03_video_frame(
            self, worker_id, d, cur_item_link, cur_login, cur_password, cur_language, cur_license, cur_role,
            prob_run_tc, datetime_now
    ):
        """
        Check: Header -> button [Trade Now]
        Language: All. License: All.
        """
        print(f"worker_id = {worker_id}")
        
        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")
        
        page5 = Conditions(d, "")
        page5.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )
        
        if cur_role == "NoReg":
            page5 = ItemPage(d, cur_item_link)
            if not page5.current_page_is(cur_item_link):
                page5.open_page()
            page5.tc_05_03_video_in_frame_click()
            if cur_role == "NoReg":
                page5 = SignupLoginForm(d, cur_item_link)
                page5.should_be_signup_form()
                page5.close_signup_form()
        elif cur_role == "Auth":
            pytest.mark.skip(f"This test not for 'Auth' role")
        elif cur_role == "RegNoAuth":
            pytest.mark.skip(f"This test not for 'RegNoAuth' role")
    
    #
    #
    #
    @allure.feature("TS_05 | Test menu [Learn to Trade] / [Glossary] / [item]")
    @allure.story("TC_05.04 | Testing 'Trade Now' button")
    @allure.step("Start tests of 'Trade Now' button.")
    @allure.title("TC_05_04 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_05_04_button_trade_now_on_frame(
            self, worker_id, d, cur_item_link, cur_login, cur_password, cur_language, cur_license, cur_role,
            prob_run_tc, datetime_now
    ):
        """
        Check: Header -> button [Trade Now]
        Language: All. License: All.
        """
        print(f"worker_id = {worker_id}")
        
        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")
        
        page5 = Conditions(d, "")
        page5.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )
        
        if cur_role == "NoReg":
            page5 = ItemPage(d, cur_item_link)
            if not page5.current_page_is(cur_item_link):
                page5.open_page()
            page5.tc_05_04_button_trade_now_in_frame_click()
            if cur_role == "NoReg":
                page5 = SignupLoginForm(d, cur_item_link)
                page5.should_be_signup_form()
                page5.close_signup_form()
        elif cur_role == "Auth":
            pytest.mark.skip(f"This test not for 'Auth' role")
        elif cur_role == "RegNoAuth":
            pytest.mark.skip(f"This test not for 'RegNoAuth' role")
    
    #
    #
    #
    @allure.feature("TS_05 | Test menu [Learn to Trade] / [Glossary] / [item]")
    @allure.story("TC_05.05 | Testing 'Practise for free' button")
    @allure.step("Start tests of 'Practise for free' button.")
    @allure.title("TC_05_05 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_05_05_button_practise_for_free(
            self, worker_id, d, cur_item_link, cur_login, cur_password, cur_language, cur_license, cur_role,
            prob_run_tc, datetime_now
    ):
        """
        Check: Header -> button [Trade Now]
        Language: All. License: All.
        """
        print(f"worker_id = {worker_id}")
        
        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")
        
        page5 = Conditions(d, "")
        page5.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )
        
        if cur_role == "NoReg":
            page5 = ItemPage(d, cur_item_link)
            if not page5.current_page_is(cur_item_link):
                page5.open_page()
            page5.tc_05_05_button_practise_for_free_click()
            if cur_role == "NoReg":
                page5 = SignupLoginForm(d, cur_item_link)
                page5.should_be_signup_form()
                page5.close_signup_form()
        elif cur_role == "Auth":
            pytest.mark.skip(f"This test not for 'Auth' role")
        elif cur_role == "RegNoAuth":
            pytest.mark.skip(f"This test not for 'RegNoAuth' role")

#
#
#
    @allure.feature("TS_05 | Test menu [Learn to Trade] / [Glossary] / [item]")
    @allure.story("TC_05.06 | Testing 'Practise for free' button")
    @allure.step("Start tests of 'Practise for free' button.")
    @allure.title("TC_05_06 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_05_06_widget_still_looking_button_1_create_your_account(
            self, worker_id, d, cur_item_link, cur_login, cur_password, cur_language, cur_license, cur_role,
            prob_run_tc, datetime_now
    ):
        """
        Check: Header -> button [Trade Now]
        Language: All. License: All.
        """
        print(f"worker_id = {worker_id}")
        
        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")
        
        page5 = Conditions(d, "")
        page5.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )
        
        if cur_role == "NoReg":
            page5 = ItemPage(d, cur_item_link)
            if not page5.current_page_is(cur_item_link):
                page5.open_page()
            page5.tc_05_06_button_create_and_verify_account_click()
            if cur_role == "NoReg":
                page5 = SignupLoginForm(d, cur_item_link)
                page5.should_be_signup_form()
                page5.close_signup_form()
        elif cur_role == "Auth":
            pytest.mark.skip(f"This test not for 'Auth' role")
        elif cur_role == "RegNoAuth":
            pytest.mark.skip(f"This test not for 'RegNoAuth' role")
