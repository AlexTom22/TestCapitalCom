"""
-*- coding: utf-8 -*-
@Time    : 2023/02/08 10:00
@Author  : Alexander Tomelo
"""
# import time
import pytest
import allure
import random
from datetime import datetime
from pages.conditions import Conditions
from pages.Header.header import Header
from pages.Learn.learn_glossary import ItemPage
# from pages.menu import MenuBurger
from pages.Signup_login.signup_login import SignupLogin
from src.src import (
    CapitalComPageSrc,
)
# from pages.learn.learn_glossary_locators import (
#     FinancialDictionary,
# )

list_href = list()


@pytest.fixture()
def prob_run_tc():
    prob = 100
    if random.randint(1, 100) <= prob:
        return ""
    else:
        return f"Тест не попал в {prob}% выполняемых тестов."


def pytest_generate_tests(metafunc):
    
    if "cur_item_link" in metafunc.fixturenames:
        cur_language = "sv"
        name_file = "tests/Learn/us_05/list_of_href"
        name_file += "_" + cur_language
        name_file += ".txt"

        list_item_link = list()
        try:
            file = open(name_file, "r")
        except FileNotFoundError:
            print(f"There is no file named {name_file}!")
        else:
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
@allure.epic('US_05.SL Testing Glossary Item page in "Learn to trade" menu')
class TestGlossaryItems:
    
    def datetime_now(self):
        return str(datetime.now())

    #
    #
    #
    @allure.feature("TS_05 | Test menu [Learn to Trade] / [Glossary] / [item]")
    @allure.story("TC_05.09 | Testing '1. Create your accaunt' button in 'Steps trading' block")
    @allure.step("Start tests of '1. Create your accaunt' button in 'Steps trading' block")
    @allure.title("TC_05.09 with parameters: {cur_language}, {cur_license}, {cur_role}")
    def test_05_09_block_steps_trading_button_1_create_your_account(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role,
            cur_item_link, prob_run_tc
    ):
        """
        Check: Button [1. Create your accaunt] in block [Steps trading]
        Language: All. License: All.
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {self.datetime_now()}")

        page5 = Conditions(d, "")
        page5.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )

        page5 = ItemPage(d, cur_item_link)
        if not page5.current_page_is(cur_item_link):
            page5.open_page()

        assert page5.tc_05_08_button_create_your_account_is_present(), \
            "Checking element is not on this page"

        page5.tc_05_08_button_create_your_account_click()

        page5 = SignupLogin(d, cur_item_link)
        if page5.should_be_signup_form(cur_language):
            page5.close_signup_form()
        elif page5.should_be_signup_page(cur_language):
            page5.close_signup_page()
        else:
            pytest.fail("Unknown registration method")

#
#
#
    @allure.feature("TS_05 | Test menu [Learn to Trade] / [Glossary] / [item]")
    @allure.story("TC_05.01 | Testing 'Log In' button on the header page")
    @allure.step("Start test button 'Log In' on header")
    @allure.title("TC_05.01 with parameters: {cur_language}, {cur_license}, {cur_role}")
    def test_05_01_header_button_login(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role,
            cur_item_link, prob_run_tc
    ):
        """
        Check: Header -> button [Log In]
        Language: All. License: All.
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {self.datetime_now()}")

        page5 = Conditions(d, "")
        page5.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )

        page5 = Header(d, cur_item_link)
        if not page5.current_page_is(cur_item_link):
            page5.open_page()

        if page5.header_button_login_click():
            page5 = SignupLogin(d, cur_item_link)
            if page5.should_be_login_form():
                page5.close_login_form()
            elif page5.should_be_login_page():
                page5.close_login_page()
            else:
                pytest.fail("Unknown registration method!")
        else:
            pytest.fail("Checking element is not on this page!")

    #
    #
    #
    @allure.feature("TS_05 | Test menu [Learn to Trade] / [Glossary] / [item]")
    @allure.story("TC_05.07 | Testing 'Create account' button on vertical banner")
    @allure.step("Start tests of 'Create account' button on vertical banner.")
    @allure.title("TC_05.07 with parameters: {cur_language}, {cur_license}, {cur_role}")
    def test_05_07_vert_banner_button_create_account(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role,
            cur_item_link, prob_run_tc
    ):
        """
        Check: Button [Create account] on vertical banner
        Language: All. License: All.
        """
        print(f"worker_id = {worker_id}")
    
        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {self.datetime_now()}")
    
        page5 = Conditions(d, "")
        page5.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )
    
        page5 = ItemPage(d, cur_item_link)
        if not page5.current_page_is(cur_item_link):
            page5.open_page()
    
        if page5.tc_05_09_vert_banner_create_account_click():
            page5 = SignupLogin(d, cur_item_link)
            if page5.should_be_signup_form(cur_language):
                page5.close_signup_form()
            elif page5.should_be_signup_page(cur_language):
                page5.close_signup_page()
            else:
                pytest.fail("Unknown registration method")
        else:
            pytest.fail("Checking element is not on this page")

    #
#
#
    @allure.feature("TS_05 | Test menu [Learn to Trade] / [Glossary] / [item]")
    @allure.story("TC_05.02 | Testing 'Trade Now' button on the header page")
    @allure.step("Start test button 'Trade Now' on header")
    @allure.title("TC_05.02 with parameters: {cur_language}, {cur_license}, {cur_role}")
    def test_05_02_header_button_trade_now(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role,
            cur_item_link, prob_run_tc
    ):
        """
        Check: Header -> button [Trade Now]
        Language: All. License: All.
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {self.datetime_now()}")

        page5 = Conditions(d, "")
        page5.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )

        page5 = Header(d, cur_item_link)
        if not page5.current_page_is(cur_item_link):
            page5.open_page()

        if page5.header_button_signup_click():
            page5 = SignupLogin(d, cur_item_link)
            if page5.should_be_signup_form(cur_language):
                page5.close_signup_form()
            elif page5.should_be_signup_page(cur_language):
                page5.close_signup_page()
            else:
                pytest.fail("Unknown registration method!")
        else:
            pytest.fail("Checking element is not on this page!")

#
#
#
    @allure.feature("TS_05 | Test menu [Learn to Trade] / [Glossary] / [item]")
    @allure.story("TC_05.03 | Testing video banner [Capital.com]")
    @allure.step("Start tests of video banner [Capital,com]")
    @allure.title("TC_05.03 with parameters: {cur_language}, {cur_license}, {cur_role}")
    def test_05_03_video_banner(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role,
            cur_item_link, prob_run_tc
    ):
        """
        Check: Video banner [Capital.com]
        Language: All. License: All.
        """
        print(f"worker_id = {worker_id}")
        
        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {self.datetime_now()}")
        
        page5 = Conditions(d, "")
        page5.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )
        
        page5 = ItemPage(d, cur_item_link)
        if not page5.current_page_is(cur_item_link):
            page5.open_page()

        if page5.tc_05_03_video_in_frame_click():
            page5 = SignupLogin(d, cur_item_link)
            if page5.should_be_signup_form(cur_language):
                page5.close_signup_form()
            elif page5.should_be_signup_page(cur_language):
                page5.close_signup_page()
            else:
                pytest.fail("Unknown registration method!")
        else:
            pytest.fail("Checking element is not on this page!")

    #
    #
    #
    @allure.feature("TS_05 | Test menu [Learn to Trade] / [Glossary] / [item]")
    @allure.story("TC_05.04 | Testing button [Create account] under video banner [Capital.com]")
    @allure.step("Start tests of button [Create account] under video banner [Capital.com]")
    @allure.title("TC_05.04 with parameters: {cur_language}, {cur_license}, {cur_role}")
    def test_05_04_button_create_account_under_video_banner(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role,
            cur_item_link, prob_run_tc
    ):
        """
        Check: Button [Create account] under video banner [Capital.com]
        Language: All. License: All.
        """
        print(f"worker_id = {worker_id}")
    
        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {self.datetime_now()}")
    
        page5 = Conditions(d, "")
        page5.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )
    
        page5 = ItemPage(d, cur_item_link)
        if not page5.current_page_is(cur_item_link):
            page5.open_page()
    
        if page5.tc_05_05_button_create_account_under_video_banner_click():
            page5 = SignupLogin(d, cur_item_link)
            if page5.should_be_signup_form(cur_language):
                page5.close_signup_form()
            elif page5.should_be_signup_page(cur_language):
                page5.close_signup_page()
            else:
                pytest.fail("Unknown registration method!")
        else:
            pytest.fail("Checking element is not on this page!")

    #
    #
    #
    @allure.feature("TS_05 | Test menu [Learn to Trade] / [Glossary] / [item]")
    @allure.story("TC_05.05 | Testing button [Trade now] under video banner [Capital.com]")
    @allure.step("Start tests of button [Trade now] under video banner [Capital.com]")
    @allure.title("TC_05.05 with parameters: {cur_language}, {cur_license}, {cur_role}")
    def test_05_05_button_trade_now_under_video_banner(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role,
            cur_item_link, prob_run_tc
    ):
        """
        Check: Button [Trade now] under video banner [Capital.com]
        Language: All. License: All.
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {self.datetime_now()}")

        page5 = Conditions(d, "")
        page5.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )

        page5 = ItemPage(d, cur_item_link)
        if not page5.current_page_is(cur_item_link):
            page5.open_page()

        if page5.tc_05_04_button_trade_now_under_video_banner_click():
            page5 = SignupLogin(d, cur_item_link)
            if page5.should_be_signup_form(cur_language):
                page5.close_signup_form()
            elif page5.should_be_signup_page(cur_language):
                page5.close_signup_page()
            else:
                pytest.fail("Unknown registration method!")
        else:
            pytest.fail("Checking element is not on this page!")

    #
    #
    #
    @allure.feature("TS_05 | Test menu [Learn to Trade] / [Glossary] / [item]")
    @allure.story("TC_05.06 | Testing 'Practise for free' button on vertical banner")
    @allure.step("Start tests of 'Practise for free' button on vertical banner.")
    @allure.title("TC_05.06 with parameters: {cur_language}, {cur_license}, {cur_role}")
    def test_05_06_vert_banner_button_practise_for_free(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role,
            cur_item_link, prob_run_tc
    ):
        """
        Check: Button [Practise for free] on vertical banner
        Language: All. License: All.
        """
        print(f"worker_id = {worker_id}")

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {self.datetime_now()}")

        page1 = Conditions(d, "")
        page1.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )

        page2 = ItemPage(d, cur_item_link)
        if not page2.current_page_is(cur_item_link):
            page2.open_page()

        if page2.tc_05_06_vert_banner_practise_for_free_is_present():
            pytest.fail("Checking element is not on this page")

        page2.tc_05_06_vert_banner_practise_for_free_click()
        print("5")

        page2 = SignupLogin(d, cur_item_link)
        if page2.should_be_signup_form(cur_language):
            page2.close_signup_form()
        elif page2.should_be_signup_page(cur_language):
            page2.close_signup_page()
        else:
            pytest.fail("Unknown registration method")

#
#
#
    @allure.feature("TS_05 | Test menu [Learn to Trade] / [Glossary] / [item]")
    @allure.story("TC_05.08 | Testing 'Practise for free' button on the hotizontal banner")
    @allure.step("Start tests of 'Practise for free' button on the horizontal banner")
    @allure.title("TC_05.08 with parameters: {cur_language}, {cur_license}, {cur_role}")
    def test_05_08_hor_banner_button_practise_for_free(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role,
            cur_item_link, prob_run_tc
    ):
        """
        Check: Button [Practise for free] on the horizontal banner
        Language: All. License: All.
        """
        print(f"worker_id = {worker_id}")
        
        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {self.datetime_now()}")
        
        page5 = Conditions(d, "")
        page5.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )
        
        page5 = ItemPage(d, cur_item_link)
        if not page5.current_page_is(cur_item_link):
            page5.open_page()
        
        if page5.tc_05_07_hor_banner_button_practise_for_free_is_present():
            pytest.fail("Checking element is not on this page")
        
        page5.tc_05_07_hor_banner_button_practise_for_free_click()
        
        page5 = SignupLogin(d, cur_item_link)
        if page5.should_be_signup_form(cur_language):
            page5.close_signup_form()
        elif page5.should_be_signup_page(cur_language):
            page5.close_signup_page()
        else:
            pytest.fail("Unknown registration method")
