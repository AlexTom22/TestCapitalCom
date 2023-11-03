"""
-*- coding: utf-8 -*-
@Time    : 2023/00/00
@Author  : Azarov Pavel
"""
import pytest
import allure
import random  # for new method
from datetime import datetime
from pages.Menu.menu import MenuSection
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.conditions import Conditions
from pages.Education.shares_trading_locators import SharesTradingItem
from src.src import CapitalComPageSrc

count = 1


class TestSharesTradingPretest:

    page_conditions = None

    @allure.step("Start pretest")
    def test_shares_trading_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        global count

        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.02")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.02", "Educations > Menu item [Shares trading]",
                             "00", "Pretest")

        if count == 0:
            pytest.skip("The list of Share Trading links is already created")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_shares_trading_move_focus_click(d, cur_language)
        del page_menu

        # Записываем ссылки в файл
        file_name = "tests/US_11_Education/US_11-02-02_Shares_trading/list_of_href.txt"
        list_items = d.find_elements(*SharesTradingItem.ITEM_LIST)

        count_in = len(list_items)
        print(f"{datetime.now()}   Shares trading include {count_in} item(s) on page")
        file = None

        try:
            file = open(file_name, "w")
            count_out = 0
            if count_in > 0:
                for i in range(3):
                    if i < count_in:
                        k = random.randint(1, count_in)
                        item = list_items[k - 1]
                        file.write(item.get_property("href") + "\n")
                        count_out += 1

            file.write(d.current_url + "\n")    # для добавления головной страницы
            count_in += 1    # для добавления головной страницы
            count_out += 1    # для добавления головной страницы
            print(f"{datetime.now()}   Plus 1 main page Shares trading. Total: {count_in} for testing")

        finally:
            file.close()
            del file

        print(f"{datetime.now()}   Test data include {count_out} item(s)")
        if count_in != 0:
            print(f"{datetime.now()}   The test coverage = {count_out/count_in*100} %")
        else:
            print(f"{datetime.now()}   The test coverage = 0 %")
        count -= 1
