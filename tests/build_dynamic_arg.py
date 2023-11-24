"""
-*- coding: utf-8 -*-
@Time    : 2023/04/14 16:30
@Author  : Alexander Tomelo
"""
import pytest
import allure
# import sys
from datetime import datetime

count = 1


def build_dynamic_arg_v2(obj, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                         us, desc_feature, num_tc, desc_story):
    """
    function for dynamic bild names pf epic, feature and story
    """
    global count

    tc = f"TC_{us}_{num_tc}"
    print(d.get_window_size())
    print(f"\n{datetime.now()}   browser = {d.name}")
    print(f"\n{datetime.now()}   worker_id = {worker_id}")
    print(f"\n{datetime.now()}   Start {tc}")
    print(f"\n{datetime.now()}   {obj}.{obj.page_conditions}")
    print(f"\n{datetime.now()}   0. Arrange")

    language = cur_language
    if cur_language == "":
        language = "en"
    dynamic_epic = f"Language: {language} / US_{us} | {desc_feature}"
    dynamic_feature = f"Country: {cur_country} / Role: {cur_role} / TS_{us} | {desc_feature}"
    dynamic_story = f"TC_{us}_{num_tc} | {desc_story}"

    allure.dynamic.epic(dynamic_epic)
    allure.dynamic.feature(dynamic_feature)
    allure.dynamic.story(dynamic_story)
    allure.dynamic.title(f"TC_{us}_{num_tc} with parameters: {language}, {cur_country}, {cur_role}")
    del dynamic_story
    del dynamic_feature
    del dynamic_epic
    del language
    del tc

    if prob_run_tc != "":
        pytest.skip(f"{prob_run_tc}")


def build_dynamic_arg_v3(obj, d, worker_id, cur_language, cur_country, cur_role,
                         us, desc_feature, num_tc, desc_story):
    """
    function for dynamic bild names pf epic, feature and story
    """
    global count

    # tc = f"TC_{us}_{num_tc}"
    print(d.get_window_size())
    # print(f"\n{datetime.now()}   browser = {d.name}")
    print(f"\n{datetime.now()}   worker_id = {worker_id}")
    # print(f"\n{datetime.now()}   Start {tc}")
    print(f"\n{datetime.now()}   0. Allure grouping")

    language = cur_language
    if cur_language == "":
        language = "en"
    dynamic_epic = f"Language: {language} / US_{us} | {desc_feature}"
    dynamic_feature = f"Country: {cur_country} / Role: {cur_role} / TS_{us} | {desc_feature}"
    dynamic_story = f"TC_{us}{num_tc} | {desc_story}"

    allure.dynamic.epic(dynamic_epic)
    allure.dynamic.feature(dynamic_feature)
    allure.dynamic.story(dynamic_story)
    allure.dynamic.title(f"TC_{us}{num_tc} with parameters: {language}, {cur_country}, {cur_role}")
    del dynamic_story
    del dynamic_feature
    del dynamic_epic
    del language
    # del tc
