"""
-*- coding: utf-8 -*-
@Time    : 2023/02/08 10:00
@Author  : Alexander Tomelo
"""
# import time
import pytest
# import allure
from tests.conditions import Conditions
# from pages.learn.learn_glossary import Glossary
from pages.menu import MenuBurger
# from pages.base_page import BasePage
from src.src import (
    CapitalComPageSrc,
)
from pages.learn.learn_glossary_locators import (
    FinancialDictionary,
)


@pytest.mark.parametrize(
    "cur_login, cur_password",
    [
        ("Empty", "Empty"),
        # ("aqa.tomelo.an@gmail.com", "iT9Vgqi6d$fiZ*Z"),
    ], scope="class"
)
class TestGlossaryStart:

    def test_glossary_item_pretest(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role,
            prob_run_tc, datetime_now
    ):

        page = Conditions(d, "")
        link = page.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )

        page = MenuBurger(d, link)
        page.click_menu_burger(d, cur_language)
        page.click_sub_menu_learn_to_trade(d, cur_language)
        page.click_glossary_item(d, cur_language)

        # Записываем ссылки в файл
        name_file = "tests/Learn/list_of_href.txt"
        if cur_language in [""]:
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
        else:
            print("Не проходит по языку")

# d.browser.execute_script(
#     'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
#     letter
# )
