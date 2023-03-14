"""
-*- coding: utf-8 -*-
@Time    : 2023/01/27 10:00
@Author  : Alexander Tomelo
"""
import pytest
from datetime import datetime


@pytest.fixture(
    scope="class",
    params=[
#        "ar",
#        "bg",
#        "cn",
#        "cs",
#        "da",
       "de",
#        "el",
#         "",  # "en"
#        "es",
#        "et",
#        "fi",
#        "fr",
#        "hr",
#        "hu",
#        "id",
#        "it",
#        "lt",
#        "lv",
#        "nl",
#        "pl",
#        "pt",
#        "ro",
#        "ru",
#        "sk",
#        "sl",
#        "sv",
#        "th",
#        "vi",
#        "zh",
    ],
)
def cur_language(request):
    print(f"Current test language - {request.param}")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
#        "ASIC",
#       "FCA",
       "CYSEC",
       # "NBRB",
       # "CCSTV",
       # "SEY",
       # "BAH",
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
def datetime_now():
    return str(datetime.now())

# def pytest_addoption(parser):
#     parser.addoption("--all", action="store_true", help="run all combinations")
#
