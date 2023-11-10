"""
-*- coding: utf-8 -*-
@Time    : 2023/05/22 05:50
@Author  : Alexander Tomelo
"""
import allure
import pytest
import random  # for new method
from datetime import datetime
import conf
from pages.Menu.menu import MenuSection
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.conditions import Conditions
from src.src import CapitalComPageSrc



# @pytest.mark.us_11_01_07_pre
class TestGlossaryItemsPretest:
    page_conditions = None

