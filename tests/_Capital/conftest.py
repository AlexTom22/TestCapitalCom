"""
-*- coding: utf-8 -*-
@Time    : 2023/01/27 10:00
@Author  : Alexander Tomelo
"""
import pytest
# import os
# import conf
import allure
import random
from datetime import datetime
# from pages.menu import MenuBurger
# from tests.conditions import Conditions
# from pages.learn.learn_glossary import Glossary
# from pages.base_page import BasePage
#
# from selenium import webdriver
# from src.src import (
#     CapitalComPageSrc,
# )
# from pages.learn.learn_glossary_locators import (
#     FinancialDictionary,
# )


@pytest.fixture(
    scope="class",
    params=[
        "ar",
        "bg",
        "cn",
        "cs",
        "da",
        "de",
        "el",
        "",  # "en"
        "es",
        "et",
        "fi",
        "fr",
        "hr",
        "hu",
        "id",
        "it",
        "lt",
        "lv",
        "nl",
        "pl",
        "pt",
        "ro",
        "ru",
        "sk",
        "sl",
        "sv",
        "th",
        "vi",
        "zh",
    ],
)
def cur_language(request):
    print(f"Current test language - {request.param}")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
        "ASIC",
        "FCA",
        "CYSEC",
        "NBRB",
        "CCSTV",
        "SEY",
        "BAH",
    ],
)
def cur_license(request):
    print(f"Current test license - {request.param}")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
        "NoReg",
        # "Reg_NoAuth",
        # "Auth",
    ],
)
def cur_role(request):
    print(f"Current test role - {request.param}")
    return request.param


@pytest.fixture()
def prob_run_tc():
    prob = 50
    if random.randint(1, 100) <= prob:
        return ""
    else:
        return f"Тест не попал в {prob}% выполняемых тестов.≠"


@pytest.fixture()
def datetime_now():
    return str(datetime.now())


# def pytest_addoption(parser):
#     parser.addoption("--all", action="store_true", help="run all combinations")

# # @pytest.fixture(scope="class",
# #                 # autouse=True,
# #                 )
# def test_start(self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role,
#                prob_run_tc, datetime_now):
#     # def cur_item_link(d, cur_login, cur_password, cur_language, cur_license, cur_role):
#     cur_item_link = list([
#         "https://capital.com/de/aktie-definition",
#         # "https://capital.com/de/basispunkt-definition"
#     ])
#     for item in cur_item_link:
#         self.test_05_01_header_button_login(
#             self, worker_id, d, item, cur_login, cur_password, cur_language, cur_license, cur_role,
#             prob_run_tc, datetime_now
#         )
