from datetime import datetime
import random  # for new method

import allure
import pytest

from conf import QTY_LINKS
from pages.common import Common
from pages.Menu.menu import MenuSection
from pages.Elements.BlockStepTrading import BlockStepTrading
# from pages.Elements.AssertClass import AssertClass
from pages.Elements.ButtonCreateAccountBlockOurCourses import ButtonCreateAccountBlockOurCourses
from pages.Elements.testing_elements_locators import CoursesPage
from tests.build_dynamic_arg import build_dynamic_arg_v3
from pages.conditions import Conditions
from src.src import CapitalComPageSrc

count = 1


@pytest.fixture()
def cur_time():
    """Fixture"""
    return str(datetime.now())


@pytest.mark.us_11_01_05
class TestTradingCourses:
    page_conditions = None

    @allure.step("Start test_11.01.05_01 button [Create account] in the block 'Our courses'.")
    def test_01_create_account_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc, cur_time):
        """
        Check: Block 'Our courses' -> button [Create account]
        Language: All. License: All. Role: All
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.05_01 и атрибутами:")
        print(f"\n{datetime.now()}   {self.__dict__}")
        link = build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                                    "11.01.05", "Education > Menu Item [Trading courses]",
                                    ".00_01", "Testing button [Create account] in block [Our courses]")

        if cur_language in ["ar"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trading_courses_move_focus_click(d, cur_language)

        test_element = ButtonCreateAccountBlockOurCourses(d, link)
        test_element.full_test(d, cur_language, cur_country, cur_role, link)

    @allure.step("Start test_11.01.05_04 button [1. Create your account] in block 'Steps trading'.")
    def test_04_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc, cur_time):
        """
        Check: Steps trading -> button [1. Create your account]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.05_04 и атрибутами:")
        print(f"\n{datetime.now()}   {self.__dict__}")

        link = build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                                    "11.01.05", "Education > Menu Item [Trading courses]",
                                    ".00_04", "Testing button [1. Create your account] in block [Steps trading]")

        if cur_language in ["ar"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trading_courses_move_focus_click(d, cur_language)

        test_element = BlockStepTrading(d, link)
        test_element.full_test(d, cur_language, cur_country, cur_role, link)

    @allure.step("Start pretest")
    def test_99_trading_courses_item_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        global count

        print(f"\n\n{datetime.now()}   Старт TC_11.01.05.00_99")
        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.01.05", "Education > Menu Item [Trading courses]",
                             ".00_99", "Pretest for US_11.01.05.01")

        if cur_language in ["ar"]:
            Common().skip_test_for_language(cur_language)

        if count == 0:
            pytest.skip("The list of Trading courses links is already created")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_trading_courses_move_focus_click(d, cur_language)
        del page_menu

        # Записываем ссылки в файл
        file_name = "tests/US_11_Education/US_11-01-05_Trading_courses/list_of_href.txt"
        list_items = d.find_elements(*CoursesPage.COURSES_PAGES_LIST)

        count_in = len(list_items)
        print(f"{datetime.now()}   Trading courses page include {count_in} lists item(s)")  # for new method
        file = None

        try:
            file = open(file_name, "w")
            count_out = 0
            url_prev = ""
            if count_in > 0:
                for i in range(QTY_LINKS):
                    if i < count_in:
                        while True:
                            k = random.randint(0, count_in - 1)
                            item = list_items[k]
                            url = item.get_property("href")
                            print(f"{datetime.now()}   {url}")
                            if url != url_prev:
                                break
                        file.write(url + "\n")
                        url_prev = url
                        print(f"{datetime.now()}   {url}")
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
