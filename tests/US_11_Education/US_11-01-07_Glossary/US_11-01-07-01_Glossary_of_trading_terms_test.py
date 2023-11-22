"""
-*- coding: utf-8 -*-
@Time    : 2023/02/08 10:00
@Author  : Alexander Tomelo
"""
import allure
import pytest
# import os
# import sys
# import psutil
# import subprocess
# from memory_profiler import profile
from datetime import datetime
from tests.build_dynamic_arg import build_dynamic_arg_v3
from pages.conditions import Conditions
# from pages.Elements.HeaderButtonLogin import HeaderButtonLogin
# from pages.Elements.HeaderButtonTrade import HeaderButtonTrade
from pages.Elements.ButtonInBanner import ButtonInBanner
from pages.Elements.VideoBanner import VideoBanner
from pages.Elements.ButtonsUnderVideoBanner import ButtonUnderVideoBanner
from pages.Elements.ButtonsUnderVideoBanner import ButtonsUnderVideoBanner
# from pages.Elements.ButtonOnVerOrHorBanner import ButtonOnVerOrHorBanner
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.AssertClass import AssertClass
from src.src import CapitalComPageSrc


def pytest_generate_tests(metafunc):
    """
    Fixture generation test data
    """

    if "cur_item_link" in metafunc.fixturenames:
        file_name = "tests/US_11_Education/US_11-01-07_Glossary/list_of_href.txt"

        list_item_link = list()

        try:
            file = open(file_name, "r")
        except FileNotFoundError:
            print(f"{datetime.now()}   There is no file with name {file_name}!")
        else:
            for line in file:
                list_item_link.append(line[:-1])
            file.close()

        if len(list_item_link) == 0:
            pytest.skip("Отсутствуют тестовые данные: нет списка ссылок на страницы")

        metafunc.parametrize("cur_item_link", list_item_link, scope="class")


@pytest.mark.us_11_01_07
class TestGlossaryItems:

    page_conditions = None

    @allure.step("Start test of button 'Create your account' in 'Steps trading' block")
    # @profile(precision=3)
    def test_01(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check: Button [1. Create your account] in block [Steps trading]
        Language: All. License: All.
        """

        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.07.01_01")
        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.01.07",
                             "Educations > Menu item [Glossary of trading terms]",
                             ".01_01",
                             "Testing button [1. Create your account] in block [Steps trading]")

        if cur_language not in ["", "de", "el", "es", "fr", "it", "hu", "nl", "pl", "ro", "ru", "zh"]:
            pytest.skip(f"This test-case is not for {cur_language} language")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BlockStepTrading(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, cur_item_link)

    @allure.step("Start test of video banner [Capital.com]")
    def test_02(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check: Video banner [Capital.com]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.07.01_02")
        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.01.07",
                             "Educations > Menu item [Glossary of trading terms]",
                             ".01_02",
                             "Testing video banner [Capital.com]")

        if cur_language not in ["", "de", "el", "es", "fr", "it", "hu", "pl"]:
            pytest.skip(f"This test-case is not for {cur_language} language")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = VideoBanner(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, cur_item_link)

    @allure.step("Start test of button [Try Free Demo] under video banner [Capital.com]")
    def test_03(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check: Button [Try Free Demo] under video banner [Capital.com]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.07.01_03")
        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.01.07",
                             "Educations > Menu item [Glossary of trading terms]",
                             ".01_03",
                             "Testing button [Try Free Demo] under video banner [Capital.com]")

        if cur_language not in [""]:
            pytest.skip(f"This test-case is not for {cur_language} language")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        button_name = "try_free_demo"
        test_element = ButtonsUnderVideoBanner(d)
        test_element.arrange_(cur_item_link, button_name)

        test_element.click(button_name)

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link, True)

    @allure.step("Start test of button [Create account] under video banner [Capital.com]")
    def test_04(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check: Button [Create account] under video banner [Capital.com]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.07.01_04")
        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.01.07",
                             "Educations > Menu item [Glossary of trading terms]",
                             ".01_04",
                             "Testing button [Create account] under video banner [Capital.com]")

        if cur_language not in ["de", "el", "es", "it", "hu"]:
            pytest.skip(f"This test-case is not for {cur_language} language")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        button_name = "create_account"
        test_element = ButtonsUnderVideoBanner(d)
        test_element.arrange_(cur_item_link, button_name)

        test_element.click(button_name)

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, cur_item_link)

    @allure.step("Start test of button [Trade now] under video banner [Capital.com]")
    def test_05(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check: Button [Trade now] under video banner [Capital.com]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.07.01_05")
        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.01.07",
                             "Educations > Menu item [Glossary of trading terms]",
                             ".01_05",
                             "Testing button [Trade now] under video banner [Capital.com]")

        if cur_language not in ["es", "fr", "pl"]:
            pytest.skip(f"This test-case is not for {cur_language} language")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        button_name = "trade_now"
        test_element = ButtonsUnderVideoBanner(d)
        test_element.arrange_(cur_item_link, button_name)

        test_element.click(button_name)

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, cur_item_link)

    @allure.step("Start test of button [Create a demo account] in Block [Build your skills with (a) risk-free demo "
                 "account]")
    def test_06(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check: Button 'Create a demo account' on inBanner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.07.01_06")
        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.01.07",
                             "Educations > Menu item [Glossary of trading terms]",
                             ".01_06",
                             "Testing button [Create a demo account] "
                             "in Block [Build your skills with a risk-free demo account]")

        if cur_language not in [""]:
            pytest.skip(f"This test-case is not for {cur_language} language")

        pytest.skip("Не готов")

        page_conditions = Conditions(d, "")
        # page_conditions = Conditions()
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ButtonInBanner(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, cur_item_link, True)

    @allure.step("Start test of button [Start Trading] in Block [Got a trading idea? Try it now.]")
    def test_07(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check: Button [Start trading] in Block [Got a trading idea? Try it now.]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.07.01_07")
        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.01.07",
                             "Educations > Menu item [Glossary of trading terms]",
                             ".01_07",
                             "Testing button [Start Trading] in Block [Got a trading idea? Try it now.]")

        if cur_language not in ["", "hu"]:
            pytest.skip(f"This test-case is not for {cur_language} language")

        pytest.skip("Не готов")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ButtonInBanner(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link)

    @allure.step("Start test of button [Try demo] in Block [Learn first. Trade CFDs with virtual money.]")
    def test_08(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check: Button 'Try demo' in Block [Learn first. Trade CFDs with virtual money.]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.07.01_08")
        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.01.07",
                             "Educations > Menu item [Glossary of trading terms]",
                             ".01_08",
                             "Testing button 'Try demo' in Block [Learn first. Trade CFDs with virtual money.]")

        if cur_language not in ["", "el", "hu"]:
            pytest.skip(f"This test-case is not for {cur_language} language")

        pytest.skip("Не готов")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ButtonInBanner(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, cur_item_link, True)

    @allure.step("Start test of button [Trade now] "
                 "in Block [Start a global, multi-asset portfolio with (an) award-winning platform]")
    def test_09(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check: Button [Trade now] in Block [Start a global, multi-asset portfolio with (an) award-winning platform]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.07.01_09")
        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.01.07",
                             "Educations > Menu item [Glossary of trading terms]",
                             ".01_09",
                             "Testing button [Trade now] "
                             "in Block [Start a global, multi-asset portfolio with (an) award-winning platform]")

        if cur_language not in [""]:
            pytest.skip(f"This test-case is not for {cur_language} language")

        pytest.skip("Не готов")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ButtonInBanner(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link)

    @allure.step("Start test of button [Create account] in Block [Open a trading account in less than 3 minutes]")
    def test_10(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check: Button [Create account] in Block [Open a trading account in less than 3 minutes]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.07.01_10")
        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.01.07",
                             "Educations > Menu item [Glossary of trading terms]",
                             ".01_10",
                             "Testing button [Create account] "
                             "in Block [Open a trading account in less than 3 minutes]")

        if cur_language not in ["de", "el", "es", "fr", "it", "hu", "pl"]:
            pytest.skip(f"This test-case is not for {cur_language} language")

        pytest.skip("Не готов")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ButtonUnderVideoBanner(d, cur_item_link)
        test_element.arrange_(cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link)

    @allure.step("Start test of button [Try Free Demo] in Block [New to trading? Learn to trade with Capital.com]")
    def test_11(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check: Button [Try Free Demo] in Block [New to trading? Learn to trade with Capital.com]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.07.01_11")
        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.01.07",
                             "Educations > Menu item [Glossary of trading terms]",
                             ".01_11",
                             "Testing button [Try Free Demo] "
                             "in Block [New to trading? Learn to trade with Capital.com]")

        if cur_language not in ["de", "es", "it"]:
            pytest.skip(f"This test-case is not for {cur_language} language")

        pytest.skip("Не готов")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ButtonUnderVideoBanner(d, cur_item_link)
        test_element.arrange_(cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link, True)

    @allure.step("Start test of Click button [Free practice] in Block [New to trading? Learn to trade with "
                 "Capital.com]")
    def test_12(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check: Button [Free practice] in Block [New to trading? Learn to trade with Capital.com]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.07.01_12")
        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.01.07",
                             "Educations > Menu item [Glossary of trading terms]",
                             ".01_12",
                             "Testing button [Free practice] "
                             "in Block [New to trading? Learn to trade with Capital.com]")

        if cur_language not in ["pl"]:
            pytest.skip(f"This test-case is not for {cur_language} language")

        pytest.skip("Не готов")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ButtonUnderVideoBanner(d, cur_item_link)
        test_element.arrange_(cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link)

    @allure.step("Start test of button [Trade now] in Block [Are you ready to trade? Create the account in minutes]")
    def test_13(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check: Button [Trade now] in Block [Are you ready to trade? Create the account in minutes]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.07.01_13")
        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.01.07",
                             "Educations > Menu item [Glossary of trading terms]",
                             ".01_13",
                             "Testing button [Trade now] "
                             "in Block [Are you ready to trade? Create the account in minutes]")

        if cur_language not in ["fr"]:
            pytest.skip(f"This test-case is not for {cur_language} language")

        pytest.skip("Не готов")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ButtonInBanner(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link)

    # @allure.step("Start test of button on vertical or horizontal banner.")
    # # @profile(precision=3)
    # def test_05_vert_hor_banner_button_create_account(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
    #         cur_item_link, prob_run_tc):
    #     """
    #     Check: Button on vertical or horizontal banner
    #     Language: All. License: All.
    #     """
    #     print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.07_05")
    #     build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
    #                          "11.01.07",
    #                          "Educations > Menu item [Glossary of trading terms]",
    #                          "05",
    #                          "Testing buttons on vertical or horizontal banner")
    #
    #     page_conditions = Conditions(d, "")
    #     page_conditions.preconditions(
    #         d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
    #
    #     test_element = ButtonOnVerOrHorBanner(d, cur_item_link)
    #     test_element.arrange_(d, cur_item_link)
    #
    #     test_element.element_click()
    #
    #     test_element = AssertClass(d, cur_item_link)
    #     match cur_role:
    #         case "NoReg":
    #             test_element.assert_signup(d, cur_language, cur_item_link)
    #         case "Reg/NoAuth":
    #             test_element.assert_login(d, cur_language, cur_item_link)
    #         case "Auth":
    #             test_element.assert_trading_platform_v2(d, cur_item_link, True)
    #
    #
#
# class Tools:
#     @staticmethod
#     def clear_console():
#         if psutil.WINDOWS:
#             return os.system("cls")
#         else:
#             return os.system("clear")
#
#     @staticmethod
#     def check_output(command: str):
#         try:
#             return subprocess.check_output(command, shell=True,
#                                            universal_newlines=True,
#                                            stderr=subprocess.DEVNULL)
#
#         except subprocess.CalledProcessError:
#             return False
#
#
# def _swap():
#     used = round(psutil.swap_memory().used / 1e+6)
#     all_ = round(psutil.swap_memory().total / 1e+6)
#
#     return f'{used}MiB / {all_}MiB '
#
#
# def _storage():
#     all_ = round(psutil.disk_usage('/.').total / 1e+9)
#     used = round(psutil.disk_usage('/.').used / 1e+9)
#
#     return f'{used}GiB / {all_}GiB '
