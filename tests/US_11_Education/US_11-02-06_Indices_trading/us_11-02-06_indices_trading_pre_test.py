"""
-*- coding: utf-8 -*-
@Time    : 2023/06/25 18:30 GMT+3
@Author  : Andrey Bozhko
"""
import random
from datetime import datetime

import pytest
import allure
from pages.Menu.menu import MenuSection
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.Elements.testing_elements_locators import SubPages

first_run_pretest = True


@pytest.mark.us_11_02_06_pre
class TestIndicesTradingGuidePreset:
    page_conditions = None

    @allure.step("Start pretest")
    def test_indices_trading_guide_pretest(self, worker_id, d, cur_language, cur_country, cur_role, cur_login,
                                           cur_password, prob_run_tc):
        test_title = ("11.02.06", "Educations > Menu item [Indices Trading]", "00", "Pretest")

        global first_run_pretest

        print(f"{datetime.now()} ====== START testing {', '.join(test_title)} ======")

        link = build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc, *test_title)

        if not first_run_pretest:
            print(f"{datetime.now()} Skip the pretest, since we've already passed it before.")
            print(f"{datetime.now()} ====== SKIP testing {', '.join(test_title)} ======")
            pytest.skip("Skip the pretest, since we've already passed it before.")

        if cur_language not in ["", "ar", "de", "es", "it", "ch"]:
            print(f"{datetime.now()} Test section released not for '{cur_language}' language.")
            print(f"{datetime.now()} ====== SKIP testing {', '.join(test_title)} ======")
            pytest.skip(f"Test section released not for '{cur_language}' language.")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_indices_trading_move_focus_click(d, cur_language)

        name_file = "tests/US_11_Education/US_11-02-06_Indices_trading/list_of_href.txt"

        list_items = d.find_elements(*SubPages.SUB_PAGES_LIST)

        href_list = list()
        if len(list_items) > 0:
            href_list = list(map(lambda element: element.get_property("href"), list_items))
        else:
            href_list.append(d.current_url)

        count_all = len(href_list)
        print(f"{datetime.now()} Indices Trading Guide include {count_all} items on selected "
                    f"'{'en' if cur_language == '' else cur_language}' language")
        print(f"{datetime.now()} Choose no more than 3 random items")
        random_list = random.sample(href_list, 3 if count_all >= 3 else count_all)
        with open(name_file, "w", encoding='UTF-8') as f:
            for val in random_list:
                f.write(val + "\n")
                print(f"{datetime.now()} The element '{val}' has been added to the file")
        print(f"{datetime.now()} Test data include {len(random_list)} Indices Trading Guide item(s)")
        print(f"{datetime.now()} The probability of test coverage = {len(random_list) / count_all * 100} %")
        first_run_pretest = False

        print(f"{datetime.now()} ====== END testing {', '.join(test_title)} ======")
