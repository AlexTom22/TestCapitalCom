"""
-*- coding: utf-8 -*-
@Time    : 2023/04/11 19:00
@Author  : Alexander Tomelo
"""
import pytest
import allure
import random
# import sys
# from memory_profiler import profile
from datetime import datetime
from pages.Menu.menu import MenuSection
from tests.bild_dynamic_arg import bild_dynamic_arg
from pages.Elements.HeaderButtonLogin import HeaderButtonLogin
from pages.Elements.HeaderButtonTrade import HeaderButtonTrade
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.AssertClass import AssertClass


@pytest.fixture()
def prob_run_tc():
    """
    Fixture for реализации вероятности выполнения теста
    """
    prob = 100
    if random.randint(1, 100) <= prob:
        return ""
    else:
        return f"{datetime.now()}   Тест не попал в {prob}% выполняемых тестов."


@pytest.fixture(
    scope="class",
    params=[
        # # "ar",
        # "bg",
        # # "cn",  # Education to trade present, financial glossary not present
        # "cs",
        # "da",
        # "de",
        # "el",
        # "",  # "en"
        # "es",
        "et",
        # "fi",
        # "fr",
        # "hr",
        # "hu",
        # # "id",
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
        # # "th",
        # # "vi",
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
        "au",  # Australia - "ASIC" - https://capital.com/?country=au
        # "gb",  # United Kingdom - "FCA" - https://capital.com/?country=gb
        # "de",  # Germany - "CYSEC" - https://capital.com/?country=de
        # "tr",  # Turkey - "SCB" - https://capital.com/?country=tr

        # "bg",  # Bulgaria - "CYSEC" - https://capital.com/?country=bg
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
        "NoReg",
        # "Reg/NoAuth",
        # "Auth"
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
        "aqa.tomelo.an@gmail.com",
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
        "iT9Vgqi6d$fiZ*Z",
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


@pytest.mark.us_11_01_03
class TestGlossaryOfTradingTerms:

    page_conditions = None

    # def __init__(self, *args, **kwargs):
    #     global count_init
    #     print(f"{datetime.now()}   В классе TestGlossaryItems вызван метод __init__ {self}")
    #     count_init += 1
    # super().__init__(*args, **kwargs)

    @allure.step("Start test of button [Log in] on Header")
    def test_01_header_button_login(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc, cur_time):
        """
        Check: Button [Log In]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_01")
        link = bild_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
                                prob_run_tc,
                                "11.01.03", "Educations > Menu item [Glossary of trading terms]",
                                "01", "Testing button [Log In] on Header")

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_glossary_move_focus_click(d, cur_language)

        test_element = HeaderButtonLogin(d, link)
        test_element.arrange_(d, cur_role, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        test_element.assert_login(d, cur_language)

    @allure.step("Start test of button [Trade] on Header")
    # @profile(precision=3)
    def test_02_header_button_trade(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc, cur_time):
        """
        Check: Button [Trade]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_02")
        link = bild_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
                                prob_run_tc,
                                "11.01.03", "Educations > Menu item [Glossary of trading terms]",
                                "02", "Testing button [Trade] on Header")

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_glossary_move_focus_click(d, cur_language)

        test_element = HeaderButtonTrade(d, link)
        test_element.arrange_(d, cur_role, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        test_element.assert_signup(d, cur_language, cur_role, link)

    #
    @allure.step("Start test of button 'Create your account' in 'Steps trading' block")
    # @profile(precision=3)
    def test_03_block_steps_trading_button_1_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc, cur_time):
        """
        Check: Button [1. Create your account] in block [Steps trading]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_03")
        link = bild_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role,
                                cur_login, cur_password, prob_run_tc,
                                "11.01.03", "Educations > Menu item [Glossary of trading terms]",
                                "03", "Testing button [Create your account] in block [Steps trading]")

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_glossary_move_focus_click(d, cur_language)

        test_element = BlockStepTrading(d, link)
        test_element.arrange_(d, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        test_element.assert_signup(d, cur_language, cur_role, link)
