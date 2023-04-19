"""
-*- coding: utf-8 -*-
@Time    : 2023/02/08 10:00
@Author  : Alexander Tomelo
"""
import pytest
import allure
import random
import sys
# from memory_profiler import profile
from datetime import datetime
from pages.conditions import Conditions
from src.src import (
    CapitalComPageSrc,
)
from pages.Elements.testing_elements import (
    HeaderButtonLogin,
    HeaderButtonSignup,
    VideoBanner,
    ButtonUnderVideoBanner,
    ButtonOnVerticalOrHorizontalBanner,
    BlockStillLookingForButtonCreateYouAccount,
    AssertClass
)
# from pages.menu import MenuBurger

# from pages.learn.learn_glossary_locators import (
#     FinancialDictionary,
# )


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


def pytest_generate_tests(metafunc):
    """
    Fixture generation test data
    """
    if "cur_item_link" in metafunc.fixturenames:
        cur_language = "hr"
        name_file = "tests/US_11 Education/US_11.01.03 Glossary/list_of_href"
        name_file += "_" + cur_language
        name_file += ".txt"

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
        "hr",
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
        "bg",  # Bulgaria - "CYSEC" - https://capital.com/?country=bg
        # "de",  # Germany - "CYSEC" - https://capital.com/?country=de
        "tr",  # Turkey - "SCB" - https://capital.com/?country=tr

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
        "Auth",
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


@pytest.mark.us_11_glossary
class TestGlossaryItems:

    page_conditions = None

    # def __init__(self, *args, **kwargs):
    #     global count_init
    #     print(f"{datetime.now()}   В классе TestGlossaryItems вызван метод __init__ {self}")
    #     count_init += 1
    # super().__init__(*args, **kwargs)

    #
    #
    #
    @allure.step("Start test of button 'Log In' on header")
    @allure.title("TC_05.01")
    # @profile(precision=3)
    def test_05_01_header_button_login(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc, cur_time
    ):
        """
        Check: Header -> button [Log In]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_05_01")
        self.bild_dynamic_arg(d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc,
                              "05", "01", "Testing 'Log In' button on the header page")

        pytest.skip("Заглушка")

        if cur_role == "Auth":
            pytest.skip(f"Testing element is not present for {cur_role} role")

        test_element = HeaderButtonLogin(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)
        test_element.act_()

        test_element = AssertClass(d, cur_item_link)
        test_element.assert_login(d, cur_item_link)
        print(f"\n{datetime.now()}   Ссылок на test_element - {sys.getrefcount(test_element)}")
        test_element = None
        print(f"\n{datetime.now()}   После None, ссылок на test_element - {sys.getrefcount(test_element)}")

    #
    #
    #
    @allure.step("Start test of button 'Trade Now' on header")
    @allure.title("TC_05.02")
    # @profile(precision=3)
    def test_05_02_header_button_trade_now(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc, cur_time
    ):
        """
        Check: Header -> button [Trade Now]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_05_02 и атрибутами:")
        print(f"\n{datetime.now()}   {self.__dict__}")
        self.bild_dynamic_arg(d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc,
                              "05", "02", "Testing 'Trade Now' button on the header page")

        pytest.skip("Заглушка")

        if cur_role == "Auth":
            pytest.skip(f"Testing element is not present for {cur_role} role")

        test_element = HeaderButtonSignup(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.act_()

        test_element = AssertClass(d, cur_item_link)
        test_element.assert_signup(d, cur_language, cur_role, cur_item_link)
        test_element = ""
        print(f"\n{datetime.now()}   После '', ссылок на test_element - {sys.getrefcount(test_element)}")

    #
    #
    #
    @allure.step("Start test of video banner [Capital.com]")
    @allure.title("TC_05.03")
    # @profile(precision=3)
    def test_05_03_video_banner(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc, cur_time
    ):
        """
        Check: Video banner [Capital.com]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_05_03 и атрибутами:")
        print(f"\n{datetime.now()}   {self.__dict__}")
        self.bild_dynamic_arg(d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc,
                              "05", "03", "Testing video banner [Capital.com]")

        pytest.skip("Заглушка")

        test_element = VideoBanner(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.act_()

        test_element = AssertClass(d, cur_item_link)
        test_element.assert_signup(d, cur_language, cur_role, cur_item_link)

    #
    #
    #
    @allure.step("Start test of button under video banner [Capital.com]")
    @allure.title("TC_05.04")
    # @profile(precision=3)
    def test_05_04_button_trade_now_under_video_banner(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc, cur_time
    ):
        """
        Check: Button [Trade now] or [Create account] under video banner [Capital.com]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_05_04 и атрибутами:")
        print(f"\n{datetime.now()}   {self.__dict__}")
        self.bild_dynamic_arg(d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc,
                              "05", "04", "Testing button under video banner [Capital.com]")

        pytest.skip("Заглушка")

        test_element = ButtonUnderVideoBanner(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.act_()

        test_element = AssertClass(d, cur_item_link)
        test_element.assert_signup(d, cur_language, cur_role, cur_item_link)

    #
    #
    #
    @allure.step("Start test of button on vertical or horizontal banner.")
    @allure.title("TC_05.05")
    # @profile(precision=3)
    def test_05_05_vert_hor_banner_button_create_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc, cur_time
    ):
        """
        Check: Button on vertical or horizontal banner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_05_05 и атрибутами:")
        print(f"\n{datetime.now()}   {self.__dict__}")
        self.bild_dynamic_arg(d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc,
                              "05", "05", "Testing buttons on vertical or horizontal banner")

        pytest.skip("Заглушка")

        test_element = ButtonOnVerticalOrHorizontalBanner(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.act_()

        test_element = AssertClass(d, cur_item_link)
        test_element.assert_signup(d, cur_language, cur_role, cur_item_link)

    #
    #
    #
    @allure.step("Start test of button 'Create your account' in 'Steps trading' block")
    @allure.title("TC_05.06")
    # @profile(precision=3)
    def test_05_06_block_steps_trading_button_1_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc, cur_time
    ):
        """
        Check: Button [1. Create your account] in block [Steps trading]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_05_06 и атрибутами:")
        print(f"\n{datetime.now()}   {self.__dict__}")
        self.bild_dynamic_arg(d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc,
                              "05", "06", "Testing button [Create your account] in block [Steps trading]")

        pytest.skip("Заглушка")

        test_element = BlockStillLookingForButtonCreateYouAccount(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.act_()

        test_element = AssertClass(d, cur_item_link)
        test_element.assert_signup(d, cur_language, cur_role, cur_item_link)

# @profile(precision=3)
    def bild_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc,
                         us, num_tc, desc_story):
        """
        function for dynamic bild names pf epic, feature and story
        """
        # global page_conditions
        # global count_init
        tc = "TC_" + us + "_" + num_tc
        print(f"\n{datetime.now()}   worker_id = {worker_id}")
        print(f"\n{datetime.now()}   Start {tc}")
        print(f"\n{datetime.now()}   {self}.{self.page_conditions}")
        print(f"\n{datetime.now()}   0. Arrange")

        dynamic_epic = \
            "US_" + us + " | " + "Testing Glossary Item page in menu 'Education to trade'" + " / " + cur_role
        #        "US_" + us + " | " + "Testing Glossary Item page in menu 'Education to trade'" +
        #        " / {" + cur_role + "}"
        dynamic_feature = \
            "TS_" + us + " | " + "Test menu 'Education to Trade' > 'Glossary page' > 'Item page'" + " / " + cur_language
        #         "TS_" + us + " | " + "Test menu 'Education to Trade' > 'Glossary page' > 'Item page'" + " / {" +
        # cur_language + "}"
        dynamic_story = \
            cur_country + " / " + "TC_" + us + "_" + num_tc + " | " + desc_story
        #       "{" + cur_license + "} / " + "TC_" + us + "_" + num_tc + " | " + desc_story

        allure.dynamic.epic(dynamic_epic)
        allure.dynamic.feature(dynamic_feature)
        allure.dynamic.story(dynamic_story)
        allure.dynamic.title(f"TC_{us}_{num_tc} with parameters: {cur_language}, {cur_country}, {cur_role}")
        del dynamic_story
        del dynamic_feature
        del dynamic_epic

        self.page_conditions = Conditions(d, "", tc)
        print(f"\n{datetime.now()}   {self}.{self.page_conditions}")
        # print(f"\n{datetime.now()}   {tc} После создания объекта класса Conditions, имеем"
        #       f"\nобъект класса TestGlossaryItems: {self}"
        #       f"\nи объект класса Conditions (page_conditions): {self.page_conditions}")

        # print(f"\n{datetime.now()}   {tc} К объекту cls Preconditions применяем метод .preconditions")
        self.page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        # print(f"\n{datetime.now()}   После отработки метода preconditions(...) объекта {self.page_conditions}")
        print(f"\n{datetime.now()}   {self}.{self.page_conditions}")
        print(f"{datetime.now()}   sys.getrefcount(page_conditions) = {sys.getrefcount(self.page_conditions)}")
        del self.page_conditions
        del tc

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}")
