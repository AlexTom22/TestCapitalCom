"""
-*- coding: utf-8 -*-
@Time    : 2023/05/23 18:30 GMT+3
@Author  : Suleyman Alirzaev
"""
import pytest
import allure
from datetime import datetime
from pages.Menu.menu import MenuSection
from tests.build_dynamic_arg import build_dynamic_arg_v3
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.Elements.testing_elements_locators import SubPages

count = 1


@pytest.mark.us_11_01_03_pre
# @allure.epic('US_11.01.03 | Find links pages in "CFD trading guide" menu')
class TestCFDTradingGuidePretest:
    page_conditions = None

    def check_language(self, cur_language):
        if cur_language not in ["", "de", "es", "fr", "nl", "pl", "ru", "zh"]:
            pytest.skip(f"This test suit is not for {cur_language} language")

    @allure.step("Start pretest")
    def test_cfd_trading_guide_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        global count

        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.01.03", "Educations > Menu item [CFD trading guide]",
                             ".00_99", "Pretest for US_11.01.03.01")

        self.check_language(cur_language)

        if count == 0:
            pytest.skip('The list of "CFD trading guide" links is already created')

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_cfd_trading_guide_move_focus_click(d, cur_language)
        del page_menu

        file_name = "tests/US_11_Education/US_11-01-03_cfd_trading_guide/list_of_href.txt"
        list_items = d.find_elements(*SubPages.SUB_PAGES_LIST)

        count_in = len(list_items)
        print(f"{datetime.now()}   CFD Trading include {count_in} items on selected '{cur_language}' language")
        file = None

        try:
            file = open(file_name, "w")
            count_out = 0
            if count_in > 0:
                for i in range(count_in):
                    item = list_items[i]
                    file.write(item.get_property("href") + "\n")
                    print(f'{datetime.now()}   {item.get_property("href")}')
                    count_out += 1
        finally:
            file.close()
            del file

        print(f"{datetime.now()}   Test data include {count_out} item(s)")
        if count_in != 0:
            print(f"{datetime.now()}   The test coverage = {count_out/count_in*100} %")
        else:
            print(f"{datetime.now()}   The test coverage = 0 %")
        count -= 1
