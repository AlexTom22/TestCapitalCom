"""
-*- coding: utf-8 -*-
@Time    : 2023/04/19 17:00 GMT+3
@Author  : Suleyman Alirzaev
"""
import os.path

import pytest
import allure
import random
# import sys
# from memory_profiler import profile
from datetime import datetime
from pages.Menu.menu import MenuSection
from tests.build_dynamic_arg import build_dynamic_arg
from pages.Elements.HeaderButtonLogin import HeaderButtonLogin
from pages.Elements.HeaderButtonTrade import HeaderButtonTrade
# from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
# from pages.Elements.ButtonStartTradingInArticle import ArticleStartTrading
# from pages.Elements.ButtonsMostTradedWidget import MostTraded
from pages.Elements.AssertClass import AssertClass
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.testing_elements_locators import CommoditiesPageElements

count = 1


@pytest.fixture()
def prob_run_tc():
    """
    Fixture для выбора % рандомных тестов
    """
    prob = 100
    if random.randint(1, 100) <= prob:
        return ""
    else:
        return f"{datetime.now()}   Тест не попал в {prob}% выполняемых тестов."


@pytest.fixture(
    scope="class",
    params=[
        # "ar",
        # "bg",
        # "cn",
        # "cs",
        # "da",
        # "de",
        # "el",
        # "",  # "en"
        "es",
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
        "au",  # Australia - "ASIC" - https://capital.com/?country=au
        "gb",  # United Kingdom - "FCA" - https://capital.com/?country=gb
        "de",  # Germany - "CYSEC" - https://capital.com/?country=de
        "tr",  # Turkey - "SCB" - https://capital.com/?country=tr

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
        "Reg/NoAuth",
        "Auth"
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
        "captest852@yopmail.com",
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
        "Testpass123!",
    ],
)
def cur_password(request):
    """Fixture"""
    print(f"Current password - {request.param}")
    return request.param


@pytest.fixture()
def cur_time():
    """Fixture"""
    return str(datetime.now())


@pytest.mark.us_11_02_03_pre
@allure.epic('US_11.02.03 | Find materials pages in "Commodities trading" menu')
class TestMaterialItemsPreset:
    page_conditions = None

    # @allure.feature("TS_11.02.03 | Test menu [Education] > [Glossary of trading terms]")
    # @allure.story("TC_11.01.03_00 | Glossary of trading terms _ Pretest")
    # @allure.step("Start pretest")
    # @allure.title("TC_11.01.03_00 Pretest with: {cur_role}, {cur_language}, {cur_country}")
    # @profile(precision=3)
    def test_commodities_trading_item_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        global count
        print(f"PATH TO FILE IS: {os.path.abspath(__file__)}")
        print(f"\n\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_00")

        if count == 0:
            pytest.skip("Так надо")
            return

        link = build_dynamic_arg(self, d, worker_id, cur_language, cur_country,
                                 cur_role, cur_login, cur_password, prob_run_tc,
                                 "11.02.03", "",
                                 "00", "Pretest")

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_commodities_trading_move_focus_click(d, cur_language)

        # Записываем ссылки в файл
        name_file = f"tests/US_11_Education/US_11-02-03_Commodities_trading/list_of_href_{cur_language}.txt"
        list_items = d.find_elements(*CommoditiesPageElements.BUTTONS_COMMODITIES_PAGES)
        print(f"Commodities trading include {len(list_items)} material items on selected '{cur_language}' language")
        f = open(name_file, "w")
        try:
            for i in range(len(list_items)):
                item = list_items[i]
                f.write(item.get_property("href") + "\n")
        finally:
            f.close()

        count -= 1

        del page_menu


def pytest_generate_tests(metafunc):
    """
    Fixture generation test data
    """
    if "cur_item_link" in metafunc.fixturenames:
        cur_language = "es"
        name_file = f"tests/US_11_Education/US_11-02-03_Commodities_trading/list_of_href_{cur_language}.txt"

        list_item_link = list()
        try:
            file = open(name_file, "r")
        except FileNotFoundError:
            print(f"{datetime.now()}   There is no file with name {name_file}!")
        else:
            for line in file:
                list_item_link.append(line[:-1])
            file.close()

        metafunc.parametrize("cur_item_link", list_item_link, scope="class")


@pytest.mark.us_11_02_03
class TestCommoditiesTrading:
    page_conditions = None

    @allure.step("Start test of button [Log In] in Header")
    # @profile(precision=3)
    def test_01_button_login_in_header(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [Log In] in Header
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_01")
        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role,
                          cur_login, cur_password, prob_run_tc,
                          "11.02.03", "Educations > Menu item [Commodities trading]",
                          "01", "Testing button [Log In] in header")

        test_element = HeaderButtonLogin(d, cur_item_link)
        test_element.arrange_(d, cur_role, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        test_element.assert_login(d, cur_item_link)

    @allure.step("Start test of button [Trade] in Header")
    # @profile(precision=3)
    def test_02_button_trade_in_header(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [Trade] in Header
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_02")

        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role,
                          cur_login, cur_password, prob_run_tc,
                          "11.02.03", "Educations > Menu item [Commodities trading]",
                          "02", "Testing button [Trade] in header")

        test_element = HeaderButtonTrade(d, cur_item_link)
        test_element.arrange_(d, cur_role, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        test_element.assert_signup(d, cur_language, cur_role, cur_item_link)

    @allure.step("Start test of button [Start trading] on Main banner")
    def test_03_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [Start Trading] on Main banner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_03")
        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
                          prob_run_tc,
                          "11.02.03", "Educations > Menu item [Commodities trading]",
                          "03", "Testing button [Start Trading] on Main banner")

        test_element = MainBannerStartTrading(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        test_element.assert_signup(d, cur_language, cur_role, cur_item_link)

    @allure.step("Start test of button [Try demo] on Main banner")
    # @profile(precision=3)
    def test_04_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [Try demo] on Main banner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_04")
        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
                          prob_run_tc,
                          "11.02.03", "Educations > Menu item [Commodities trading]",
                          "04", "Testing button [Try demo] on Main banner")

        test_element = MainBannerTryDemo(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        test_element.assert_signup(d, cur_language, cur_role, cur_item_link)

    # @allure.step("Start test of button [Start trading] in article")
    # # @profile(precision=3)
    # def test_06_start_trading_in_article_button(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
    #         prob_run_tc, cur_time):
    #     """
    #     Check: Button [Start trading] in article
    #     Language: All. License: All.
    #     """
    #     print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_04")
    #     build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
    #                       prob_run_tc,
    #                       "11.02.03", "Educations > Menu item [Commodities trading]",
    #                       "06", "Testing button [Start trading] in article")
    #
    #     test_element = ArticleStartTrading(d, cur_item_link)
    #     test_element.arrange_(d, cur_item_link)
    #
    #     test_element.element_click()
    #
    #     test_element = AssertClass(d, cur_item_link)
    #     test_element.assert_signup(d, cur_language, cur_role, cur_item_link)

    @allure.step("Start test of button [Create your account] in block [Steps trading]")
    # @profile(precision=3)
    def test_08_block_steps_trading_button_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [1. Create your account] in block [Steps trading]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_08")
        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
                          prob_run_tc,
                          "11.02.03", "Educations > Menu item [Commodities trading]",
                          "08", "Testing button [Create your account] in block [Steps trading]")

        test_element = BlockStepTrading(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        test_element.assert_signup(d, cur_language, cur_role, cur_item_link)

    # @allure.step("Start test of buttons [Most traded] on Widget")
    # # @profile(precision=3)
    # def test_05_widget_most_traded_button(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
    #         prob_run_tc, cur_time):
    #     """
    #     Check: Buttons [Most traded] on Widget
    #     Language: All. License: All.
    #     """
    #     print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_05")
    #     link = build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
    #                              prob_run_tc,
    #                              "11.02.03", "Educations > Menu item [Commodities trading]",
    #                              "05", "Testing buttons [Most traded] on Widget")
    #
    #     page_menu = MenuSection(d, link)
    #     page_menu.menu_education_move_focus(d, cur_language)
    #     page_menu.sub_menu_commodities_trading_move_focus_click(d, cur_language)
    #
    #     test_element = MostTraded(d, link)
    #     test_element.arrange_(d, cur_role, link)
    #
    #     test_element.element_click()
    #
    #     test_element = AssertClass(d, link)
    #     test_element.assert_login(d, cur_language)
