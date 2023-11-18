"""
-*- coding: utf-8 -*-
@Time    : 2023/06/25 19:30 GMT+3
@Author  : Suleyman Alirzaev
"""

import pytest
import allure
from datetime import datetime

from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.Elements.AssertClass import AssertClass
from pages.Elements.QRcodeDecoder import QRCodeDecode
from pages.Elements.ButtonExploreWebPlatform import ButtonExploreWebPlatform
from pages.Menu.menu import MenuSection
from pages.Elements.ButtonOnCounterBlock import ButtonCreateAccountOnCounterBlock


class USLink:
    user_story_menu_link = None

    def get_us_link(self, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        if cur_language not in ["", "de", "es", "fr", "it", "pl", "cn"]:
            pytest.skip(f"This test is not for {'en' if cur_language == '' else cur_language} language")

        page_conditions = Conditions(d, "")
        main_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
        if not self.user_story_menu_link:
            page_menu = MenuSection(d, main_link)
            page_menu.menu_education_move_focus(d, cur_language)
            us_link = page_menu.sub_menu_investmate_app_move_focus_click(d, cur_language)
            self.user_story_menu_link = us_link
        return self.user_story_menu_link


@pytest.mark.us_11_01_06
class TestInvestmateApp:
    page_conditions = None
    us_link = USLink()

    @allure.step("Start test of QR code in Investmate block")
    def test_01_qr_code_investmate_block(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: QR code in Investmate block
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.06_01")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.06", "Educations > Menu item [Investmate app]",
                             "01", "Testing QR code in Investmate block")

        menu_link = self.us_link.get_us_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = QRCodeDecode(d, menu_link, 'investmate')
        test_element.arrange().element_decode()

        test_element = AssertClass(d, menu_link)
        test_element.assert_app_store_investmate()

    @allure.step("Start test of QR code in Easy learning block")
    def test_02_qr_code_easy_learning_block(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: QR code in Easy learning block
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.06_04")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.06", "Educations > Menu item [Investmate app]",
                             "02", "Testing QR code in Easy learning block")

        menu_link = self.us_link.get_us_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = QRCodeDecode(d, menu_link, 'easy_learning')
        test_element.arrange().element_decode()

        test_element = AssertClass(d, menu_link)
        test_element.assert_app_store_investmate()

    @allure.step("Start test of button [Explore Web Platform] in Block 'capital.com'")
    def test_03_button_explore_web_platform(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [Explore Web Platform] in Block 'capital.com'
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.06_05")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.06", "Educations > Menu item [Investmate app]",
                             "03", "Testing button [Explore Web Platform] in block 'capital.com'")

        menu_link = self.us_link.get_us_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ButtonExploreWebPlatform(d, menu_link)
        test_element.arrange_(menu_link)

        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, menu_link)

        match cur_role:
            case "NoReg":
                test_element.assert_signup_form_on_the_trading_platform(d)
            case "Reg/NoAuth":
                test_element.assert_login_form_on_the_trading_platform(d)
            case "Auth":
                test_element.assert_trading_platform_v3(d, menu_link)

    @allure.step("Start test of QR code in Capital block")
    def test_04_qr_code_capital_block(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):

        """
        Check: QR code in Capital block
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.06_06")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.06", "Educations > Menu item [Investmate app]",
                             "04", "Testing QR code in Capital block")

        menu_link = self.us_link.get_us_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = QRCodeDecode(d, menu_link, 'capital')
        test_element.arrange().element_decode()

        test_element = AssertClass(d, menu_link)
        test_element.assert_app_store(d, menu_link)

    @allure.step("Start test of button [Create account] in block \"Why choose Capital?\"")
    def test_05_button_create_account_why_capital(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [Create account] in block "Why choose Capital?"
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.06_07")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.06", "Educations > Menu item [Investmate app]",
                             "05", "Testing button [Create account] in block \"Why choose Capital?\"")

        if cur_language in ['', 'pl', 'cn']:
            pytest.skip(f"This test is not for {'en' if cur_language == '' else cur_language} language")

        menu_link = self.us_link.get_us_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ButtonCreateAccountOnCounterBlock(d, menu_link)
        test_element.arrange_(menu_link)

        test_element.element_click()

        test_element = AssertClass(d, menu_link)

        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, menu_link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, menu_link)
