"""
-*- coding: utf-8 -*-
@Time    : 2023/02/08 10:00
@Author  : Alexander Tomelo
"""
import pytest
import allure
import random
# import sys
# from memory_profiler import profile
from datetime import datetime
# from pages.conditions import Conditions
from tests.bild_dynamic_arg import bild_dynamic_arg
from pages.Elements.HeaderButtonLogin import HeaderButtonLogin
from pages.Elements.HeaderButtonTrade import HeaderButtonTrade
from pages.Elements.ButtonInBanner import ButtonInBanner
from pages.Elements.VideoBanner import VideoBanner
from pages.Elements.ButtonUnderVideoBanner import ButtonUnderVideoBanner
from pages.Elements.ButtonOnVerOrHorBanner import ButtonOnVerOrHorBanner
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.AssertClass import AssertClass


@pytest.fixture()
def prob_run_tc():
    """
    Fixture for реализации вероятности выполнения теста
    """
    prob = 50
    if random.randint(1, 100) <= prob:
        return ""
    else:
        return f"{datetime.now()}   Тест не попал в {prob}% выполняемых тестов."


def pytest_generate_tests(metafunc):
    """
    Fixture generation test data
    """
    if "cur_item_link" in metafunc.fixturenames:
        cur_language = "et"
        name_file = "tests/US_11_Education/US_11-01-03_Glossary/list_of_href"
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
        # # "ar",
        # "bg",
        # "cn",  # Education to trade present, financial glossary not present
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
        # "dk",  # Denmark - "CYSEC" - https://capital.com/?country=dk
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


@pytest.mark.us_11_01_03_01
class TestGlossaryItems:

    page_conditions = None

    # def __init__(self, *args, **kwargs):
    #     global count_init
    #     print(f"{datetime.now()}   В классе TestGlossaryItems вызван метод __init__ {self}")
    #     count_init += 1
    # super().__init__(*args, **kwargs)

    #
    @allure.step("Start test of button [Log in] on Header")
    # @profile(precision=3)
    def test_01_header_button_login(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc, cur_time):
        """
        Check: Button [Log In]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03.01_01")
        bild_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc,
                         "11.01.03.01", "Educations > Menu item [Glossary of trading terms] > Trading Term",
                         "01", "Testing button [Log In] on Header")

        test_element = HeaderButtonLogin(d, cur_item_link)
        test_element.arrange_(d, cur_role, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        test_element.assert_login(d, cur_language)

    #
    @allure.step("Start test of button [Trade] on Header")
    # @profile(precision=3)
    def test_02_header_button_trade(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc, cur_time):
        """
        Check: Button [Trade]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03.01_02")
        bild_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc,
                         "11.01.03.01", "Educations > Menu item [Glossary of trading terms] > Trading Term",
                         "02", "Testing button [Trade] on Header")

        test_element = HeaderButtonTrade(d, cur_item_link)
        test_element.arrange_(d, cur_role, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        test_element.assert_signup(d, cur_language, cur_role, cur_item_link)

    #
    @allure.step("Start test of button [Start Trading]/[Create a demo account]/[Trade now]/[Try demo] on inBanner")
    # @profile(precision=3)
    def test_03_button_(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc, cur_time):
        """
        Check: Button on inBanner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03.01_03")
        bild_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc,
                         "11.01.03.01", "Educations > Menu item [Glossary of trading terms] > Trading Term",
                         "03", "Testing button on inBanner")

        test_element = ButtonInBanner(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        test_element.assert_signup(d, cur_language, cur_role, cur_item_link)

    #
    @allure.step("Start test of video banner [Capital.com]")
    # @profile(precision=3)
    def test_04_video_banner(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc, cur_time):
        """
        Check: Video banner [Capital.com]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03.01_04")
        bild_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc,
                         "11.01.03.01", "Educations > Menu item [Glossary of trading terms] > Trading Term",
                         "04", "Testing video banner [Capital.com]")

        test_element = VideoBanner(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        test_element.assert_signup(d, cur_language, cur_role, cur_item_link)

    #
    @allure.step("Start test of button under video banner [Capital.com]")
    # @profile(precision=3)
    def test_05_button_trade_now_under_video_banner(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc, cur_time):
        """
        Check: Button [Trade now] or [Create account] under video banner [Capital.com]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03.01_05")
        bild_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc,
                         "11.01.03.01", "Educations > Menu item [Glossary of trading terms] > Trading Term",
                         "05", "Testing button under video banner [Capital.com]")

        test_element = ButtonUnderVideoBanner(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        test_element.assert_signup(d, cur_language, cur_role, cur_item_link)

    #
    @allure.step("Start test of button on vertical or horizontal banner.")
    # @profile(precision=3)
    def test_06_vert_hor_banner_button_create_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc, cur_time):
        """
        Check: Button on vertical or horizontal banner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03.01_06")
        bild_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc,
                         "11.01.03.01", "Educations > Menu item [Glossary of trading terms] > Trading Term",
                         "06", "Testing buttons on vertical or horizontal banner")

        test_element = ButtonOnVerOrHorBanner(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        test_element.assert_signup(d, cur_language, cur_role, cur_item_link)

    #
    @allure.step("Start test of button 'Create your account' in 'Steps trading' block")
    # @profile(precision=3)
    def test_07_block_steps_trading_button_1_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc, cur_time):
        """
        Check: Button [1. Create your account] in block [Steps trading]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03.01_07")
        bild_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc,
                         "11.01.03.01", "Educations > Menu item [Glossary of trading terms] > Trading Term",
                         "07", "Testing button [Create your account] in block [Steps trading]")

        test_element = BlockStepTrading(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        test_element.assert_signup(d, cur_language, cur_role, cur_item_link)
