"""
-*- coding: utf-8 -*-
@Time    : 2023/01/27 10:00
@Author  : Alexander Tomelo
"""
# import pytest
# import random
# from datetime import datetime


# @pytest.fixture(
#     scope="class",
#     params=[
#         # "NoReg",
#         # "Reg/NoAuth",
#         "Auth",
#     ],
# )
# def cur_role(request):
#     """Fixture"""
#     print(f"Current test role - {request.param}")
#     return request.param
#

# @pytest.fixture(
#     scope="class",
#     params=[
#         "Empty",
#         # "aqa.tomelo.an@gmail.com",
#     ],
# )
# def cur_login(request):
#     """Fixture"""
#     print(f"Current login - {request.param}")
#     return request.param
#
#
# @pytest.fixture(
#     scope="class",
#     params=[
#         "Empty",
#         # "iT9Vgqi6d$fiZ*Z",
#     ],
# )
# def cur_password(request):
#     """Fixture"""
#     print(f"Current login - {request.param}")
#     return request.param
#
#
# @pytest.fixture()
# def cur_time():
#     """Fixture"""
#     return str(datetime.now())
#
# def pytest_addoption(parser):
#     parser.addoption("--all", action="store_true", help="run all combinations")
#
