"""
-*- coding: utf-8 -*-
@Time    : 2023/02/08 10:00
@Author  : Alexander Tomelo
"""
import pytest
import random
import allure
# from memory_profiler import profile
from datetime import datetime
from tests.bild_dynamic_arg import bild_dynamic_arg
from pages.Menu.menu import MenuSection
from pages.Education.glossary_locators import (
    FinancialDictionary,
)


@pytest.fixture()
# @pytest.fixture(scope="class")
def prob_run_tc():
    """Fixture"""
    prob = 100
    if random.randint(1, 100) <= prob:
        return ""
    else:
        return f"{datetime.now()}   Тест не попал в {prob}% выполняемых тестов.≠"


@pytest.fixture(
    scope="class",
    params=[
        # "ar",
        # "bg",
        # "cn",  # Education to trade present, financial glossary not present
        # "cs",
        # "da",
        # "de",
        # "el",
        # "",  # "en"
        # "es",
        # "et",
        # "fi",
        # "fr",
        # "hr",
        # "hu",
        # "id",
        # "it",
        # "lt",
        # "lv",
        # "nl",
        # "pl",
        # "pt",
        # "ro",
        # "ru",
        # "sk",
        # "sl",
        # "sv",
        # "th",
        # "vi",
        # "zh",
    ],
)
def cur_language(request):
    """Fixture"""
    print(f"Current test language - {request.param}")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
        # "au",  # Australia - "ASIC" - https://capital.com/?country=au
        # "gb",  # United Kingdom - "FCA" - https://capital.com/?country=gb
        # "bg",  # Bulgaria - "CYSEC" - https://capital.com/?country=bg
        # "de",  # Germany - "CYSEC" - https://capital.com/?country=de
        # "tr",  # Turkey - "SCB" - https://capital.com/?country=tr

        # "NBRB" - пока не проверяем
        # "SFB",
        # "FSA"
    ],
)
def cur_country(request):
    """Fixture"""
    print(f"Current country of trading - {request.param}")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
        # "NoReg",
        # "Reg/NoAuth",
        # "Auth",
    ],
)
def cur_role(request):
    """Fixture"""
    print(f"Current test role - {request.param}")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
        # "Empty",
        # "aqa.tomelo.an@gmail.com",
    ],
)
def cur_login(request):
    """Fixture"""
    print(f"Current login - {request.param}")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
        # "Empty",
        # "iT9Vgqi6d$fiZ*Z",
    ],
)
def cur_password(request):
    """Fixture"""
    print(f"Current login - {request.param}")
    return request.param


@pytest.fixture()
def cur_time():
    """Fixture"""
    return str(datetime.now())


@pytest.mark.us_11_01_03_01_pre
@allure.epic('US_11.01.03 | Testing Glossary Item page in "Education to trade" menu')
class TestGlossaryItemsPreset:

    @allure.feature("TS_11.01.03 | Test menu [Education] > [Glossary of trading terms]")
    @allure.story("TC_11.01.03_00 | Glossary of trading terms _ Pretest")
    @allure.step("Start pretest")
    @allure.title("TC_11.01.03_01 Pretest with: {cur_role}, {cur_language}, {cur_country}")
    # @profile(precision=3)
    def test_glossary_item_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        # self, worker_id, d, cur_language, cur_role, prob_run_tc):

        link = bild_dynamic_arg(self, d, worker_id, cur_language, cur_country,
                                cur_role, cur_login, cur_password, prob_run_tc,
                                "11.01.03", "",
                                "00", "Pretest")

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, link)
        page_menu.sub_menu_glossary_move_focus_click(d, link)

        # Записываем ссылки в файл
        name_file = "tests/US_11_Education/US_11-01-03-Glossary/list_of_href"
        name_file += "bg" + cur_language
        name_file += ".txt"
        list_items = d.find_elements(*FinancialDictionary.ITEM_LIST)
        print(f"Glossary include {len(list_items)} financial item(s)")
        f = open(name_file, "w")
        try:
            for i in range(len(list_items)):
                item = list_items[i]
                f.write(item.get_property("href") + "\n")
        finally:
            f.close()

# d.browser.execute_script(
#     'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
#     letter
# )
