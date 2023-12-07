"""
-*- coding: utf-8 -*-
@Time    : 2023/01/27 10:00
@Author  : Alexander Tomelo
"""
import logging
# import re
import time

import allure
from datetime import datetime
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

import conf
from pages.base_page import BasePage
from pages.Menu.menu_locators import (
    Menu1101,
    MenuLanguageAndCountry,
    MenuUS11Education,
    MenuUS11LearningHub,
    MenuUS11TradingCourses,
    MenuUS11Glossary,
    MenuUS11MarketGuides,
    MenuUS11CommoditiesTrading,
    MenuUS11ForexTrading,
    MenuUS11CryptocurrencyTrading,
    MenuUS11CFDTradingGuide,
    MenuUS11SpreadBettingGuide,
    MenuUS11ETFTrading,
    MenuUS11TradingStrategiesGuide,
    MenuUS11DayTrading,
    MenuUS11IndicesTrading,
    MenuUS11InvestmateApp,
    MenuUS11TrendTrading,
    MenuUS11WhatIsMargin,
    MenuUS11TradingPsychologyGuide, MenuUS11PositionTrading, MenuUS11SwingTrading, MenuUS11ScalpTrading,
    MenuUS11SharesTrading
)
# from src.src import CapitalComPageSrc

logger = logging.getLogger()


class MenuSection(BasePage):

    @allure.step('Select "Education" menu, "CFD trading guide" submenu')
    def open_education_cfd_trading_menu(self, d, cur_language, link):

        print(f'\n{datetime.now()}   START [Open "Education" menu, "CFD trading guide" submenu] =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.menu_education_move_focus(d, cur_language)
        self.sub_menu_cfd_trading_guide_move_focus_click(d, cur_language)

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step('Select "Education" menu, "Forex trading" submenu')
    def open_education_forex_trading_menu(self, d, cur_language, link):

        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.menu_education_move_focus(d, cur_language)
        self.sub_menu_forex_trading_move_focus_click(d, cur_language)

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    def open_education_shares_trading_menu(self, d, cur_language, link):

        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()
        self.menu_education_move_focus(d, cur_language)
        cur_menu_link = self.sub_menu_shares_trading_move_focus_click(d, cur_language)
        return cur_menu_link

    @allure.step(f"{datetime.now()}.   Click 'Language and Country' menu section.")
    def menu_language_and_country_move_focus(self, test_language):
        d = self.browser
        # menu = list()
        menu = d.find_elements(*MenuLanguageAndCountry.MENU_LANGUAGE_AND_COUNTRY)  # not Glossary
        if len(menu) == 0:
            print(f"\n\n{datetime.now()}   => Language and Country menu not present")
            allure.attach(self.browser.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
            pytest.skip(f"For '{test_language}' language menu [Language & Country] not present")
        print(f"\n\n{datetime.now()}   => Language and Country menu is present")

        if not self.element_is_visible(MenuLanguageAndCountry.MENU_LANGUAGE_AND_COUNTRY, 5):
            print(f"\n\n{datetime.now()}   => Language and Country menu not visible")
            pytest.fail("Language and Country menu not visible")
        print(f"\n\n{datetime.now()}   => Language and Country menu is visible")

        # if not self.element_is_clickable(MenuLanguageAndCountry.MENU_LANGUAGE_AND_COUNTRY, 5):
        #     print(f"\n\n{datetime.now()}   => Language and Country menu not clickable")
        #     pytest.fail("Language and Country menu not clickable")
        # print(f"\n\n{datetime.now()}   => Language and Country menu is clickable")
        #

        time.sleep(1)
        menu = d.find_element(*MenuLanguageAndCountry.MENU_LANGUAGE_AND_COUNTRY)  # not Glossary
        ActionChains(d) \
            .move_to_element(menu) \
            .pause(0.5) \
            .perform()
        del menu

        print(f"\n\n{datetime.now()}   => Focus is moved on Language and Country menu ")

    @allure.step(f"{datetime.now()}.   Click 'Education' menu section.")
    def menu_education_move_focus(self, d, test_language):
        ed_menu_locator = None
        match test_language:
            case "":
                ed_menu_locator = MenuUS11Education.SUB_MENU_EN_LEARN_TO_TRADE
            case "ar":
                ed_menu_locator = MenuUS11Education.SUB_MENU_AR_LEARN_TO_TRADE
            case "de":
                ed_menu_locator = MenuUS11Education.SUB_MENU_DE_LEARN_TO_TRADE
            case "el":
                ed_menu_locator = MenuUS11Education.SUB_MENU_EL_LEARN_TO_TRADE
            case "es":
                ed_menu_locator = MenuUS11Education.SUB_MENU_ES_LEARN_TO_TRADE
            case "fr":
                ed_menu_locator = MenuUS11Education.SUB_MENU_FR_LEARN_TO_TRADE
            case "it":
                ed_menu_locator = MenuUS11Education.SUB_MENU_IT_LEARN_TO_TRADE
            case "hu":
                ed_menu_locator = MenuUS11Education.SUB_MENU_HU_LEARN_TO_TRADE
            case "nl":
                ed_menu_locator = MenuUS11Education.SUB_MENU_NL_LEARN_TO_TRADE
            case "pl":
                ed_menu_locator = MenuUS11Education.SUB_MENU_PL_LEARN_TO_TRADE
            case "ro":
                ed_menu_locator = MenuUS11Education.SUB_MENU_RO_LEARN_TO_TRADE
            case "ru":
                ed_menu_locator = MenuUS11Education.SUB_MENU_RU_LEARN_TO_TRADE
            case "zh":
                ed_menu_locator = MenuUS11Education.SUB_MENU_ZH_LEARN_TO_TRADE
            case "cn":
                ed_menu_locator = MenuUS11Education.SUB_MENU_CN_LEARN_TO_TRADE

        menu = d.find_elements(*ed_menu_locator)
        if len(menu) == 0:
            print(f"{datetime.now()}   => Education menu not present")
            allure.attach(self.browser.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
            pytest.skip(f"For '{test_language}' language menu [Education] not present")
        print(f"{datetime.now()}   => Education menu is present")

        if not self.element_is_visible(ed_menu_locator, 5):
            print(f"{datetime.now()}   => Education menu not visible")
            pytest.fail("Education menu not visible")
        print(f"{datetime.now()}   => Education menu is visible")

        time.sleep(1)
        menu = d.find_elements(*ed_menu_locator)  # not Glossary
        ActionChains(d) \
            .move_to_element(menu[0]) \
            .pause(0.5) \
            .perform()
        del menu
        print(f"{datetime.now()}   => Education menu focus moved")

    @allure.step(f"{datetime.now()}.   Click 'learning hub' menu section.")
    def sub_menu_learning_hub_move_focus_click(self, d, test_language):
        sub_menu = None
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_EN_ITEM_LEARNING_HUB)
            case "ar":
                sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_AR_ITEM_LEARNING_HUB)
            case "de":
                sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_DE_ITEM_LEARNING_HUB)
            case "el":
                sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_EL_ITEM_LEARNING_HUB)
            case "es":
                sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_ES_ITEM_LEARNING_HUB)
            case "fr":
                sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_FR_ITEM_LEARNING_HUB)
            case "it":
                sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_IT_ITEM_LEARNING_HUB)
            case "hu":
                sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_HU_ITEM_LEARNING_HUB)
            case "nl":
                sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_NL_ITEM_LEARNING_HUB)
            case "pl":
                sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_PL_ITEM_LEARNING_HUB)
            case "ro":
                sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_RO_ITEM_LEARNING_HUB)
            case "ru":
                sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_RU_ITEM_LEARNING_HUB)
            case "zh":
                sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_ZH_ITEM_LEARNING_HUB)
            case "cn":
                sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_CN_ITEM_LEARNING_HUB)

        if len(sub_menu) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education > Learning hub\" submenu doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()
        del sub_menu

        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Glossary' hyperlink.")
    def sub_menu_glossary_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_EN_GLOSSARY)
            case "ar":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_AR_GLOSSARY)
            case "id":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_ID_GLOSSARY)
            case "bg":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_BG_GLOSSARY)
            case "cn":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_CN_GLOSSARY)
            case "cs":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_CS_GLOSSARY)
            case "da":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_DA_GLOSSARY)
            case "de":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_DE_GLOSSARY)
            case "el":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_EL_GLOSSARY)
            case "es":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_ES_GLOSSARY)
            case "et":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_ET_GLOSSARY)
            case "fi":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_FI_GLOSSARY)
            case "fr":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_FR_GLOSSARY)
            case "hr":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_HR_GLOSSARY)
            case "hu":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_HU_GLOSSARY)
            case "it":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_IT_GLOSSARY)
            case "lt":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_LT_GLOSSARY)
            case "lv":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_LV_GLOSSARY)
            case "nl":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_NL_GLOSSARY)
            case "pl":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_PL_GLOSSARY)
            case "pt":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_PT_GLOSSARY)
            case "ro":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_RO_GLOSSARY)
            case "ru":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_RU_GLOSSARY)
            case "sk":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_SK_GLOSSARY)
            case "sl":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_SL_GLOSSARY)
            case "sv":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_SV_GLOSSARY)
            case "th":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_TH_GLOSSARY)
            case "vi":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_VI_GLOSSARY)
            case "zh":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_ZH_GLOSSARY)

        if len(sub_menu) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education > Glossary of trading terms\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()
        print(f"\n\n{datetime.now()}   => Glossary sub-menu clicked")

        del sub_menu
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Forex trading' submenu.")
    def sub_menu_forex_trading_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_EN_FOREX_TRADING)
            case "ar":
                sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_AR_FOREX_TRADING)
            case "de":
                sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_DE_FOREX_TRADING)
            case "es":
                sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_ES_FOREX_TRADING)
            case "fr":
                sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_FR_FOREX_TRADING)  # одна страница
            case "it":
                sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_IT_FOREX_TRADING)
            case "ru":
                sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_RU_FOREX_TRADING)  # одна страница
            case "zh":
                sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_ZH_FOREX_TRADING)  # одна страница
            case "cn":
                sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_CN_FOREX_TRADING)  # одна страница
            # case "hu":
            #     sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_HU_FOREX_TRADING)
            # case "nl":
            #     sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_NL_FOREX_TRADING)
            # case "pl":
            #     sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_PL_FOREX_TRADING)
            # case "ro":
            #     sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_RO_FOREX_TRADING)

        if len(sub_menu) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education > Forex Trading\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()
        print(f"\n\n{datetime.now()}   => Forex trading sub-menu clicked")

        del sub_menu
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Basics_of_trading' hyperlink.")
    def sub_menu_basics_of_trading_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_EN_ITEM_BASICS_OF_TRADING)
            case "de":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_DE_ITEM_BASICS_OF_TRADING)
            case "ru":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_RU_ITEM_BASICS_OF_TRADING)
            case "bg":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_BG_ITEM_BASICS_OF_TRADING)
            case "cs":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_CS_ITEM_BASICS_OF_TRADING)
            case "fr":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_FR_ITEM_BASICS_OF_TRADING)
            case "ar":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_AR_ITEM_BASICS_OF_TRADING)
            case "et":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_ET_ITEM_BASICS_OF_TRADING)
            case "da":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_DA_ITEM_BASICS_OF_TRADING)
            case "el":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_EL_ITEM_BASICS_OF_TRADING)
            case "es":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_ES_ITEM_BASICS_OF_TRADING)
            case "hr":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_HR_ITEM_BASICS_OF_TRADING)
            case "it":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_IT_ITEM_BASICS_OF_TRADING)
            case "lv":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_LV_ITEM_BASICS_OF_TRADING)
            case "hu":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_HU_ITEM_BASICS_OF_TRADING)
            case "nl":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_NL_ITEM_BASICS_OF_TRADING)
            case "pl":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_PL_ITEM_BASICS_OF_TRADING)
            case "pt":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_PT_ITEM_BASICS_OF_TRADING)
            case "ro":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_RO_ITEM_BASICS_OF_TRADING)
            case "sk":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_SK_ITEM_BASICS_OF_TRADING)
            case "sl":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_SL_ITEM_BASICS_OF_TRADING)
            case "fi":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_FI_ITEM_BASICS_OF_TRADING)
            case "sv":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_SV_ITEM_BASICS_OF_TRADING)
            case "vi":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_VI_ITEM_BASICS_OF_TRADING)
            case "zh":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_ZH_ITEM_BASICS_OF_TRADING)
            case "lt":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_LT_ITEM_BASICS_OF_TRADING)
            case "cn":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_CN_ITEM_BASICS_OF_TRADING)

        if len(sub_menu) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education > Menu item [The basics of trading]\" "
                        f"doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()

        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Trading courses hyperlink.")
    def sub_menu_trading_courses_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_EN_ITEM_TRADING_COURSES)
            case "de":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_DE_ITEM_TRADING_COURSES)
            case "ru":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_RU_ITEM_TRADING_COURSES)
            case "bg":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_BG_ITEM_TRADING_COURSES)
            case "cs":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_CS_ITEM_TRADING_COURSES)
            case "fr":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_FR_ITEM_TRADING_COURSES)
            case "ar":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_AR_ITEM_TRADING_COURSES)
            case "et":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_ET_ITEM_TRADING_COURSES)
            case "da":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_DA_ITEM_TRADING_COURSES)
            case "el":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_EL_ITEM_TRADING_COURSES)
            case "es":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_ES_ITEM_TRADING_COURSES)
            case "hr":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_HR_ITEM_TRADING_COURSES)
            case "it":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_IT_ITEM_TRADING_COURSES)
            case "lv":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_LV_ITEM_TRADING_COURSES)
            case "hu":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_HU_ITEM_TRADING_COURSES)
            case "nl":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_NL_ITEM_TRADING_COURSES)
            case "pl":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_PL_ITEM_TRADING_COURSES)
            case "pt":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_PT_ITEM_TRADING_COURSES)
            case "ro":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_RO_ITEM_TRADING_COURSES)
            case "sk":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_SK_ITEM_TRADING_COURSES)
            case "sl":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_SL_ITEM_TRADING_COURSES)
            case "fi":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_FI_ITEM_TRADING_COURSES)
            case "sv":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_SV_ITEM_TRADING_COURSES)
            case "vi":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_VI_ITEM_TRADING_COURSES)
            case "zh":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_ZH_ITEM_TRADING_COURSES)
            case "lt":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_LT_ITEM_TRADING_COURSES)
            case "cn":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_CN_ITEM_TRADING_COURSES)
            case "id":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_ID_ITEM_TRADING_COURSES)

        if len(sub_menu) == 0:
            pytest.skip(f"For '{test_language}' language [Trading courses] submenu item "
                        f"doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()

        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Commodities trading' hyperlink.")
    def sub_menu_commodities_trading_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "ar":
                sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_AR_COMMODITIES_TRADING)
            # case "bg":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_BG_COMMODITIES_TRADING)
            # case "cs":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_CS_COMMODITIES_TRADING)
            case "cn":
                sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_CN_COMMODITIES_TRADING)
            # case "da":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_DA_COMMODITIES_TRADING)
            case "de":
                sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_DE_COMMODITIES_TRADING)
            # case "el":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_EL_COMMODITIES_TRADING)
            case "":
                sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_EN_COMMODITIES_TRADING)
            case "es":
                sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_ES_COMMODITIES_TRADING)
            # case "et":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_ET_COMMODITIES_TRADING)
            # case "fi":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_FI_COMMODITIES_TRADING)
            case "fr":
                sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_FR_COMMODITIES_TRADING)
            # case "hr":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_HR_COMMODITIES_TRADING)
            # case "hu":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_HU_COMMODITIES_TRADING)
            # case "id":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_ID_COMMODITIES_TRADING)
            case "it":
                sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_IT_COMMODITIES_TRADING)
            # case "lt":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_LT_COMMODITIES_TRADING)
            # case "lv":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_LV_COMMODITIES_TRADING)
            case "nl":
                sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_NL_COMMODITIES_TRADING)
            case "pl":
                sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_PL_COMMODITIES_TRADING)
            # case "pt":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_PT_COMMODITIES_TRADING)
            case "ro":
                sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_RO_COMMODITIES_TRADING)
            case "ru":
                sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_RU_COMMODITIES_TRADING)
            # case "sk":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_SK_COMMODITIES_TRADING)
            # case "sl":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_SL_COMMODITIES_TRADING)
            # case "sv":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_SV_COMMODITIES_TRADING)
            case "zh":
                sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_ZH_COMMODITIES_TRADING)
            # case "th":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_TH_COMMODITIES_TRADING)
            case "vi":
                sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_VI_COMMODITIES_TRADING)

        if len(sub_menu) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education > Commodities Trading\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()

        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Market guides hyperlink.")
    def sub_menu_market_guides_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_EN_ITEM_MARKET_GUIDES)
            case "de":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_DE_ITEM_MARKET_GUIDES)
            case "ru":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_RU_ITEM_MARKET_GUIDES)
            case "bg":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_BG_ITEM_MARKET_GUIDES)
            case "cs":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_CS_ITEM_MARKET_GUIDES)
            case "fr":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_FR_ITEM_MARKET_GUIDES)
            case "ar":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_AR_ITEM_MARKET_GUIDES)
            case "et":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_ET_ITEM_MARKET_GUIDES)
            case "da":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_DA_ITEM_MARKET_GUIDES)
            case "el":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_EL_ITEM_MARKET_GUIDES)
            case "es":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_ES_ITEM_MARKET_GUIDES)
            case "hr":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_HR_ITEM_MARKET_GUIDES)
            case "it":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_IT_ITEM_MARKET_GUIDES)
            case "lv":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_LV_ITEM_MARKET_GUIDES)
            case "hu":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_HU_ITEM_MARKET_GUIDES)
            case "nl":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_NL_ITEM_MARKET_GUIDES)
            case "pl":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_PL_ITEM_MARKET_GUIDES)
            case "pt":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_PT_ITEM_MARKET_GUIDES)
            case "ro":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_RO_ITEM_MARKET_GUIDES)
            case "sk":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_SK_ITEM_MARKET_GUIDES)
            case "sl":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_SL_ITEM_MARKET_GUIDES)
            case "fi":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_FI_ITEM_MARKET_GUIDES)
            case "sv":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_SV_ITEM_MARKET_GUIDES)
            case "vi":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_VI_ITEM_MARKET_GUIDES)
            case "zh":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_ZH_ITEM_MARKET_GUIDES)
            case "lt":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_LT_ITEM_MARKET_GUIDES)
            case "cn":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_CN_ITEM_MARKET_GUIDES)

        if len(sub_menu) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education | Menu title [Market Guides]\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()

        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Cryptocurrency trading' hyperlink.")
    def sub_menu_cryptocurrency_trading_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_EN_CRYPTOCURRENCY_TRADING)
            case "de":
                sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_DE_CRYPTOCURRENCY_TRADING)
            case "es":
                sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_ES_CRYPTOCURRENCY_TRADING)
            case "fr":
                sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_FR_CRYPTOCURRENCY_TRADING)
            case "it":
                sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_IT_CRYPTOCURRENCY_TRADING)
            case "pl":
                sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_PL_CRYPTOCURRENCY_TRADING)
            case "ro":
                sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_RO_CRYPTOCURRENCY_TRADING)
            case "ru":
                sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_RU_CRYPTOCURRENCY_TRADING)
            case "zh":
                sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_ZH_CRYPTOCURRENCY_TRADING)
            case "cn":
                sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_CN_CRYPTOCURRENCY_TRADING)

            # case "ar": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_AR_CRYPTOCURRENCY_TRADING)
            # case "bg": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_BG_CRYPTOCURRENCY_TRADING)
            # case "cs": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_CS_CRYPTOCURRENCY_TRADING)
            # case "da": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_DA_CRYPTOCURRENCY_TRADING)
            # case "el": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_EL_CRYPTOCURRENCY_TRADING)
            # case "et": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_ET_CRYPTOCURRENCY_TRADING)
            # case "fi": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_FI_CRYPTOCURRENCY_TRADING)
            # case "hr": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_HR_CRYPTOCURRENCY_TRADING)
            # case "hu": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_HU_CRYPTOCURRENCY_TRADING)
            # case "id": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_ID_CRYPTOCURRENCY_TRADING)
            # case "lt": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_LT_CRYPTOCURRENCY_TRADING)
            # case "lv": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_LV_CRYPTOCURRENCY_TRADING)
            # case "nl": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_NL_CRYPTOCURRENCY_TRADING)
            # case "pt": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_PT_CRYPTOCURRENCY_TRADING)
            # case "sk": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_SK_CRYPTOCURRENCY_TRADING)
            # case "sl": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_SL_CRYPTOCURRENCY_TRADING)
            # case "sv": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_SV_CRYPTOCURRENCY_TRADING)
            # case "th": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_TH_CRYPTOCURRENCY_TRADING)
            # case "vi": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_VI_CRYPTOCURRENCY_TRADING)

        if len(sub_menu) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education -> Cryptocurrency trading\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()

        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'CFD trading guide' hyperlink.")
    def sub_menu_cfd_trading_guide_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            # case "ar":  sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_AR_CFD_TRADING_GUIDE)
            case "bg":
                sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_BG_CFD_TRADING_GUIDE)
            # case "cn": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_CN_CFD_TRADING_GUIDE)
            case "cs":
                sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_CS_CFD_TRADING_GUIDE)
            # case "da": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_DA_CFD_TRADING_GUIDE)
            case "de":
                sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_DE_CFD_TRADING_GUIDE)
            # case "el": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_EL_CFD_TRADING_GUIDE)
            case "":
                sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_EN_CFD_TRADING_GUIDE)
            case "es":
                sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_ES_CFD_TRADING_GUIDE)
            # case "et": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_ET_CFD_TRADING_GUIDE)
            # case "fi": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_FI_CFD_TRADING_GUIDE)
            case "fr":
                sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_FR_CFD_TRADING_GUIDE)
            # case "hr": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_HR_CFD_TRADING_GUIDE)
            # case "hu": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_HU_CFD_TRADING_GUIDE)
            # case "id": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_ID_CFD_TRADING_GUIDE)
            case "it":
                sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_IT_CFD_TRADING_GUIDE)
            # case "lt": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_LT_CFD_TRADING_GUIDE)
            # case "lv": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_LV_CFD_TRADING_GUIDE)
            case "nl":
                sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_NL_CFD_TRADING_GUIDE)
            case "pl":
                sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_PL_CFD_TRADING_GUIDE)
            # case "pt": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_PT_CFD_TRADING_GUIDE)
            case "ro":
                sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_RO_CFD_TRADING_GUIDE)
            case "ru":
                sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_RU_CFD_TRADING_GUIDE)
            # case "sk": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_SK_CFD_TRADING_GUIDE)
            # case "sl": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_SL_CFD_TRADING_GUIDE)
            case "sv":
                sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_SV_CFD_TRADING_GUIDE)
            # case "th": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_TH_CFD_TRADING_GUIDE)
            case "vi":
                sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_VI_CFD_TRADING_GUIDE)
            case "zh":
                sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_ZH_CFD_TRADING_GUIDE)

        if len(sub_menu) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->CFD trading guide\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()

        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Spread betting guide' hyperlink.")
    def sub_menu_spread_betting_guide_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS11SpreadBettingGuide.SUB_MENU_EN_SPREAD_BETTING_GUIDE)
            case "es":
                sub_menu = d.find_elements(*MenuUS11SpreadBettingGuide.SUB_MENU_ES_SPREAD_BETTING_GUIDE)
            case "cn":
                sub_menu = d.find_elements(*MenuUS11SpreadBettingGuide.SUB_MENU_CN_SPREAD_BETTING_GUIDE)

        if len(sub_menu) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education > Spread betting guide\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()

        return d.current_url

    @allure.step(f"{datetime.now()}.   Set language")
    def set_language(self, cur_language):
        d = self.browser

        if cur_language == "":
            cur_language = "en"
        css_loc_lang = 'header a[data-type="nav_lang_' + cur_language + '"]'
        language_str_list = d.find_elements(By.CSS_SELECTOR, css_loc_lang)
        if len(language_str_list) == 0:
            pytest.fail(f"For test language '{cur_language}' problem № 2 with set language")

        ActionChains(d) \
            .move_to_element(language_str_list[0]) \
            .pause(0.5) \
            .click() \
            .perform()

        return d.current_url

    @allure.step(f"{datetime.now()}.   Set country")
    def set_country(self, cur_country):
        d = self.browser

        elements = d.find_elements(*MenuLanguageAndCountry.DROP_DOWN_LIST_COUNTRY)
        if len(elements) == 0:
            pytest.fail(f"For test country '{cur_country}' problem № 1 with set country")
        ActionChains(d) \
            .move_to_element(elements[0]) \
            .pause(0.5) \
            .click() \
            .pause(1) \
            .perform()

        # self.send_keys(cur_country, *MenuLanguageAndCountry.COUNTRIES_SEARCH_INPUT)
        # time.sleep(1)
        # countries_list = d.find_elements(*MenuLanguageAndCountry.COUNTRIES_LIST)
        # if len(countries_list) == 0:
        #     pytest.fail(f"For test country '{cur_country}' problem № 2 with set country")
        #
        css_sel_country = 'a[data-country="' + cur_country + '"]'
        if conf.DEBUG:
            print(f"\n{datetime.now()} Debug:   css_country_selector = {css_sel_country}")
        country_str_list = d.find_elements(By.CSS_SELECTOR, css_sel_country)
        if len(country_str_list) == 0:
            time.sleep(10)
            pytest.fail(f"Test country '{cur_country}' not listed")

        ActionChains(d) \
            .move_to_element(country_str_list[0]) \
            .pause(0.5) \
            .click() \
            .perform()

        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'ETF trading' hyperlink.")
    def sub_menu_etf_trading_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "ar":
                sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_AR_ETF_TRADING)
            case "cn":
                sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_CN_ETF_TRADING)
            case "de":
                sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_DE_ETF_TRADING)
            case "":
                sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_EN_ETF_TRADING)
            case "es":
                sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_ES_ETF_TRADING)
            case "it":
                sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_IT_ETF_TRADING)
            case "ru":
                sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_RU_ETF_TRADING)

        if len(sub_menu) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->ETF trading\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()

        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Trading Strategies Guide' hyperlink.")
    def sub_menu_trading_strategies_guide_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_EN_TRADING_STRATEGIES_GUIDE)
            case "ar":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_AR_TRADING_STRATEGIES_GUIDE)
            case "bg":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_BG_TRADING_STRATEGIES_GUIDE)
            case "cn":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_CN_TRADING_STRATEGIES_GUIDE)
            case "cs":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_CS_TRADING_STRATEGIES_GUIDE)
            case "da":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_DA_TRADING_STRATEGIES_GUIDE)
            case "de":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_DE_TRADING_STRATEGIES_GUIDE)
            case "el":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_EL_TRADING_STRATEGIES_GUIDE)
            case "es":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_ES_TRADING_STRATEGIES_GUIDE)
            case "et":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_ET_TRADING_STRATEGIES_GUIDE)
            case "fi":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_FI_TRADING_STRATEGIES_GUIDE)
            case "fr":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_FR_TRADING_STRATEGIES_GUIDE)
            case "hr":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_HR_TRADING_STRATEGIES_GUIDE)
            case "hu":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_HU_TRADING_STRATEGIES_GUIDE)
            case "id":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_ID_TRADING_STRATEGIES_GUIDE)
            case "it":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_IT_TRADING_STRATEGIES_GUIDE)
            case "lt":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_LT_TRADING_STRATEGIES_GUIDE)
            case "lv":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_LV_TRADING_STRATEGIES_GUIDE)
            case "nl":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_NL_TRADING_STRATEGIES_GUIDE)
            case "pl":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_PL_TRADING_STRATEGIES_GUIDE)
            case "pt":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_PT_TRADING_STRATEGIES_GUIDE)
            case "ro":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_RO_TRADING_STRATEGIES_GUIDE)
            case "ru":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_RU_TRADING_STRATEGIES_GUIDE)
            case "sk":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_SK_TRADING_STRATEGIES_GUIDE)
            case "sl":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_SL_TRADING_STRATEGIES_GUIDE)
            case "sv":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_SV_TRADING_STRATEGIES_GUIDE)
            case "zh":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_ZH_TRADING_STRATEGIES_GUIDE)
            case "th":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_TH_TRADING_STRATEGIES_GUIDE)
            case "vi":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_VI_TRADING_STRATEGIES_GUIDE)

        if len(sub_menu) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->Trading Strategies Guide\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()

        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Day Trading' hyperlink.")
    def sub_menu_day_trading_move_focus_click(self, d, test_language):
        sub_menu = d.find_elements(*MenuUS11DayTrading.SUB_MENU_ALL_DAY_TRADING)

        if len(sub_menu) > 0:
            ActionChains(d) \
                .move_to_element(sub_menu[0]) \
                .pause(0.5) \
                .click() \
                .perform()
        else:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->Day Trading\" doesn't exist on production")
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Indices Trading' hyperlink.")
    def sub_menu_indices_trading_move_focus_click(self, d, test_language):
        logger.info(f"Click 'Indices Trading' hyperlink in submenu")
        match test_language:
            case "de":
                sub_menu = d.find_elements(*MenuUS11IndicesTrading.SUB_MENU_DE_INDICES_TRADING)
            case "it":
                sub_menu = d.find_elements(*MenuUS11IndicesTrading.SUB_MENU_IT_INDICES_TRADING)
            case _:
                sub_menu = d.find_elements(*MenuUS11IndicesTrading.SUB_MENU_ALL_INDICES_TRADING)

        if len(sub_menu) > 0:
            logger.info(f"The menu item is found")
            ActionChains(d) \
                .move_to_element(sub_menu[0]) \
                .pause(0.5) \
                .click() \
                .perform()
            logger.info(f"Indices Trading menu click")
        else:
            logger.warning(f"For test language '{test_language}' "
                           f"the page \"Education->Indices Trading\" doesn't exist on production")
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->Indices Trading\" doesn't exist on production")
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Investmate app' hyperlink.")
    def sub_menu_investmate_app_move_focus_click(self, d, test_language):
        match test_language:
            case "de":
                sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_DE_INVESTMATE_APP)
            case "es":
                sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_ES_INVESTMATE_APP)
            case "fr":
                sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_FR_INVESTMATE_APP)
            case "it":
                sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_IT_INVESTMATE_APP)
            case _:
                sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_ALL_INVESTMATE_APP)

        if len(sub_menu) > 0:
            ActionChains(d) \
                .move_to_element(sub_menu[0]) \
                .pause(0.5) \
                .click() \
                .perform()
            print(f"\n\n{datetime.now()}   => 'Investmate App' menu click")
        else:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->Investmate app\" doesn't exist on production")
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Trend Trading' menu item.")
    def sub_menu_trend_trading_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "": sub_menu = d.find_elements(*MenuUS11TrendTrading.SUB_MENU_EN_ITEM_TREND_TRADING)
            # case "de": sub_menu = d.find_elements(*MenuUS11TrendTrading.SUB_MENU_DE_ITEM_TREND_TRADING)

        if len(sub_menu) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->Trend Trading\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()
        print(f"\n\n{datetime.now()}   => Trend trading menu item clicked")

        del sub_menu
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'What is a margin?' hyperlink.")
    def sub_menu_what_is_a_margin_move_focus_click(self, d, test_language):
        sub_menu = d.find_elements(*MenuUS11WhatIsMargin.SUB_MENU_ALL_WHAT_IS_A_MARGIN)
        if len(sub_menu) > 0:
            ActionChains(d) \
                .move_to_element(sub_menu[0]) \
                .pause(0.5) \
                .click() \
                .perform()
            print(f"\n\n{datetime.now()}   => 'What is a margin?' menu click")
        else:
            pytest.fail(f"For test language '{test_language}' "
                        f"the page \"Education->What is a margin?\" doesn't exist on production")
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Trading Psychology Guide' hyperlink.")
    def sub_menu_trading_psychology_guide_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_ALL_TRADING_PSYCHOLOGY_GUIDE)
            case "ar":
                sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_AR_TRADING_PSYCHOLOGY_GUIDE)
            case "de":
                sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_DE_TRADING_PSYCHOLOGY_GUIDE)
            case "el":
                sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_EL_TRADING_PSYCHOLOGY_GUIDE)
            case "es":
                sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_ES_TRADING_PSYCHOLOGY_GUIDE)
            case "fr":
                sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_FR_TRADING_PSYCHOLOGY_GUIDE)
            case "it":
                sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_IT_TRADING_PSYCHOLOGY_GUIDE)
            case "hu":
                sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_HU_TRADING_PSYCHOLOGY_GUIDE)
            case "nl":
                sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_NL_TRADING_PSYCHOLOGY_GUIDE)
            case "pl":
                sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_PL_TRADING_PSYCHOLOGY_GUIDE)
            case "ro":
                sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_RO_TRADING_PSYCHOLOGY_GUIDE)
            case "ru":
                sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_RU_TRADING_PSYCHOLOGY_GUIDE)
            case "zh":
                sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_ZH_TRADING_PSYCHOLOGY_GUIDE)
            case "cn":
                sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_CN_TRADING_PSYCHOLOGY_GUIDE)

        if len(sub_menu) > 0:
            ActionChains(d) \
                .move_to_element(sub_menu[0]) \
                .pause(0.5) \
                .click() \
                .perform()
            print(f"\n\n{datetime.now()}   => Trading Psychology Guide menu click")
        else:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->Trading Psychology Guide\" doesn't exist on production")
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Position Trading' hyperlink.")
    def sub_menu_position_trading_move_focus_click(self, d, test_language):
        sub_menu = d.find_elements(*MenuUS11PositionTrading.SUB_MENU_ALL_POSITION_TRADING)
        if len(sub_menu) > 0:
            ActionChains(d) \
                .move_to_element(sub_menu[0]) \
                .pause(0.5) \
                .click() \
                .perform()
            print(f"\n\n{datetime.now()}   => 'Position Trading' menu click")
        else:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->Position Trading\" doesn't exist on production")
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Swing Trading' hyperlink.")
    def sub_menu_swing_trading_move_focus_click(self, d, test_language):
        sub_menu = d.find_elements(*MenuUS11SwingTrading.SUB_MENU_ALL_SWING_TRADING)
        if len(sub_menu) > 0:
            ActionChains(d) \
                .move_to_element(sub_menu[0]) \
                .pause(0.5) \
                .click() \
                .perform()
            print(f"\n\n{datetime.now()}   => 'Swing Trading' menu click")
        else:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->Swing Trading\" doesn't exist on production")
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Scalp Trading' hyperlink.")
    def sub_menu_scalp_trading_move_focus_click(self, d, test_language):
        sub_menu = d.find_elements(*MenuUS11ScalpTrading.SUB_MENU_ALL_SCALP_TRADING)

        if len(sub_menu) > 0:
            ActionChains(d) \
                .move_to_element(sub_menu[0]) \
                .pause(0.5) \
                .click() \
                .perform()
            print(f"\n\n{datetime.now()}   => 'Scalp Trading' menu click")
        else:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->Scalp Trading\" doesn't exist on production")
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Shares trading' submenu.")
    def sub_menu_shares_trading_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS11SharesTrading.SUB_MENU_EN_SHARES_TRADING)
            case "ar":
                sub_menu = d.find_elements(*MenuUS11SharesTrading.SUB_MENU_AR_SHARES_TRADING)
            case "de":
                sub_menu = d.find_elements(*MenuUS11SharesTrading.SUB_MENU_DE_SHARES_TRADING)
            case "cn":
                sub_menu = d.find_elements(*MenuUS11SharesTrading.SUB_MENU_CN_SHARES_TRADING)
            case "cs":
                sub_menu = d.find_elements(*MenuUS11SharesTrading.SUB_MENU_DE_SHARES_TRADING)
            case "es":
                sub_menu = d.find_elements(*MenuUS11SharesTrading.SUB_MENU_ES_SHARES_TRADING)
            case "fr":
                sub_menu = d.find_elements(*MenuUS11SharesTrading.SUB_MENU_FR_SHARES_TRADING)
            case "it":
                sub_menu = d.find_elements(*MenuUS11SharesTrading.SUB_MENU_IT_SHARES_TRADING)
            case "nl":
                sub_menu = d.find_elements(*MenuUS11SharesTrading.SUB_MENU_NL_SHARES_TRADING)
            case "pl":
                sub_menu = d.find_elements(*MenuUS11SharesTrading.SUB_MENU_PL_SHARES_TRADING)
            case "ro":
                sub_menu = d.find_elements(*MenuUS11SharesTrading.SUB_MENU_RO_SHARES_TRADING)
            case "ru":
                sub_menu = d.find_elements(*MenuUS11SharesTrading.SUB_MENU_RU_SHARES_TRADING)
            case "zh":
                sub_menu = d.find_elements(*MenuUS11SharesTrading.SUB_MENU_ZH_SHARES_TRADING)

        if len(sub_menu) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education > Shared Trading\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()
        print(f"\n\n{datetime.now()}   => Shares trading sub-menu clicked")

        del sub_menu
        return d.current_url
