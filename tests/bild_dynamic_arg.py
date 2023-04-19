"""
-*- coding: utf-8 -*-
@Time    : 2023/04/14 16:30
@Author  : Alexander Tomelo
"""
import pytest
import allure
import sys
from datetime import datetime
from pages.conditions import Conditions
# from pages.Signup_login.signup_login import SignupLogin
# from pages.base_page import BasePage
from src.src import CapitalComPageSrc


def bild_dynamic_arg(obj, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc,
                     us, desc_feature, num_tc, desc_story):
    """
    function for dynamic bild names pf epic, feature and story
    """
    tc = "TC_" + us + "_" + num_tc
    print(f"\n{datetime.now()}   worker_id = {worker_id}")
    print(f"\n{datetime.now()}   Start {tc}")
    print(f"\n{datetime.now()}   {obj}.{obj.page_conditions}")
    print(f"\n{datetime.now()}   0. Arrange")

    dynamic_epic = "US_" + us + " / Role: " + cur_role
#       "US_" + us + " | " + "Testing Glossary Item page in menu 'Education to trade'" + " / " + cur_role
    dynamic_feature = "TS_" + us + " | " + desc_feature + " / Language: " + cur_language
    dynamic_story = "Country: " + cur_country + " / " + "TC_" + us + "_" + num_tc + " | " + desc_story

    allure.dynamic.epic(dynamic_epic)
    allure.dynamic.feature(dynamic_feature)
    allure.dynamic.story(dynamic_story)
    allure.dynamic.title(f"TC_{us}_{num_tc} with parameters: {cur_language}, {cur_country}, {cur_role}")
    del dynamic_story
    del dynamic_feature
    del dynamic_epic

    obj.page_conditions = Conditions(d, "")
    print(f"\n{datetime.now()}   {obj}.{obj.page_conditions}")
    link = obj.page_conditions.preconditions(
        d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

    print(f"\n{datetime.now()}   {obj}.{obj.page_conditions}")
    print(f"{datetime.now()}   sys.getrefcount(page_conditions) = {sys.getrefcount(obj.page_conditions)}")
    del obj.page_conditions
    del tc

    if prob_run_tc != "":
        pytest.skip(f"{prob_run_tc}")

    return link
