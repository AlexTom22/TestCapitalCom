"""
-*- coding: utf-8 -*-
@Time    : 2023/30/09 20:10
@Author  : Mila Podchasova
"""
import allure
import pytest
import random  # for new method
from datetime import datetime

import conf
from pages.Education.Trading_strategies_guide_locators import TradingStrategiesContentList
from pages.Menu.menu import MenuSection
from pages.common import Common
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.conditions import Conditions
from src.src import CapitalComPageSrc

count = 1


class TestTradingStrategiesGuidePretest:
    page_conditions = None

    @allure.step("Start test_11.03.01_00 pretest")
    def test_trading_strategies_guide_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        global count

        print(f"\n\n{datetime.now()}   Работает obj {self} с именем TC_11.03.01_00")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.03.01", "Education > Menu item [Trading Strategies Guides]",
                             "00", "Pretest")

        if count == 0:
            pytest.skip("Так надо")

        # if cur_language not in ["", "de", "es", "it"]:
        #     pytest.skip(f"Test-case not for '{cur_language}' language")

        if cur_language not in ["", "de", "es", "it"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)
        del page_menu

        # Записываем ссылки в файл
        name_file = "tests/US_11_Education/US_11-03-01_trading_strategies_guide/list_of_href.txt"
        list_items = d.find_elements(*TradingStrategiesContentList.LISTS)
        count_in = len(list_items)
        print(f"{datetime.now()}   Trading Strategies Guide page include {count_in} lists item(s)")  # for new method
        file = None

        try:
            file = open(name_file, "w")
            count_out = 0
            if count_in > 0:
                for i in range(conf.QTY_LINKS):
                    if i < count_in:
                        k = random.randint(1, count_in)
                        item = list_items[k - 1]
                        file.write(item.get_property("href") + "\n")
                        count_out += 1

            file.write(d.current_url + "\n")  # для добавления головной страницы
            count_in += 1  # для добавления головной страницы
            count_out += 1  # для добавления головной страницы
            print(f"{datetime.now()}   Plus 1 main page Trading Strategies Guide. Total: {count_in} for testing")

        finally:
            file.close()
            del file

        print(f"{datetime.now()}   Test data include {count_out} item(s)")
        if count_in != 0:
            print(f"{datetime.now()}   The test coverage = {count_out/count_in*100} %")
        else:
            print(f"{datetime.now()}   The test coverage = 0 %")

        count -= 1
