"""
-*- coding: utf-8 -*-
@Time    : 2023/02/08 10:00
@Author  : Alexander Tomelo
"""
import pytest
import random
import allure
from tests.conditions import Conditions
from pages.Menu.menu import BurgerMenu
from src.src import (
    CapitalComPageSrc,
)
from pages.Learn.learn_glossary_locators import (
    FinancialDictionary,
)


@pytest.fixture()
# @pytest.fixture(scope="class")
def prob_run_tc():
    prob = 100
    if random.randint(1, 100) <= prob:
        return ""
    else:
        return f"Тест не попал в {prob}% выполняемых тестов.≠"


@pytest.mark.us_05_pre
@pytest.mark.parametrize(
    "cur_login, cur_password",
    [
        ("Empty", "Empty"),
        # ("aqa.tomelo.an@gmail.com", "iT9Vgqi6d$fiZ*Z"),
    ], scope="class"
)
@allure.epic('US_05. Testing Glossary Item page in "Learn to trade" menu. All language. All license')
class TestGlossaryItemsPretest:

    @allure.feature("TS_05 | Test menu [Learn to Trade] / [Glossary] / [item]")
    @allure.story("TC_05.00 | Learn Glossary > Pretest")
    @allure.step("Start pretest")
    @allure.title("TC_05.01.01 Pretest with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_glossary_item_pretest(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role,
            prob_run_tc, datetime_now
    ):

        page = Conditions(d, "")
        link = page.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )

        page = BurgerMenu(d, link)
        page.burger_menu_click(d)
        page.menu_section_learn_to_trade_click(d, cur_language)
        page.section_learn_to_trade_item_glossary_click(d, cur_language)

        # Записываем ссылки в файл
        name_file = "tests/Learn/us_05/list_of_href"
        name_file += "_" + cur_language
        name_file += ".txt"
        # list_letters = d.browser.find_elements(*FinancialDictionary.ALPHABET_LIST_EN)
        list_items = d.find_elements(*FinancialDictionary.ITEM_LIST_EN)
        f = open(name_file, "w")
        try:
            for i in range(len(list_items)):
                item = list_items[i]
                # list_href.append(item.get_property("href"))
                f.write(item.get_property("href") + "\n")
        finally:
            f.close()

# d.browser.execute_script(
#     'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
#     letter
# )
