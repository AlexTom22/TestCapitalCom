"""
-*- coding: utf-8 -*-
@Time    : 2023/01/27 10:00
@Author  : Alexander Tomelo
"""
import allure
import datetime

import pytest

from pages.base_page import BasePage
from pages.Menu.menu_locators import (
    Menu,
    MenuUS05,
)


class BurgerMenu(BasePage):

    @allure.step(f"{datetime.datetime.now()}.   Click button [Burger menu].")
    def burger_menu_click(self, d):
        
        menu1 = d.find_element(*Menu.MENU)

        self.element_is_clickable(menu1)
        menu1.click()

    @allure.step(f"{datetime.datetime.now()}.   Click 'Learn to trade' menu section.")
    def menu_section_learn_to_trade_click(self, d, test_language):
        match test_language:
            # case "ar":  menu1 = d.find_element(*MenuUS05.SUB_MENU_AR_LEARN_TO_TRADE)
            case "bg":  menu1 = d.find_element(*MenuUS05.SUB_MENU_BG_LEARN_TO_TRADE)
            case "cs":  menu1 = d.find_element(*MenuUS05.SUB_MENU_CS_LEARN_TO_TRADE)
            case "da":  menu1 = d.find_element(*MenuUS05.SUB_MENU_DA_LEARN_TO_TRADE)
            case "de":  menu1 = d.find_element(*MenuUS05.SUB_MENU_DE_LEARN_TO_TRADE)
            case "el":  menu1 = d.find_element(*MenuUS05.SUB_MENU_EL_LEARN_TO_TRADE)
            case "":    menu1 = d.find_element(*MenuUS05.SUB_MENU_EN_LEARN_TO_TRADE)
            case "es":  menu1 = d.find_element(*MenuUS05.SUB_MENU_ES_LEARN_TO_TRADE)
            case "et":  menu1 = d.find_element(*MenuUS05.SUB_MENU_ET_LEARN_TO_TRADE)
            case "fi":  menu1 = d.find_element(*MenuUS05.SUB_MENU_FI_LEARN_TO_TRADE)
            case "fr":  menu1 = d.find_element(*MenuUS05.SUB_MENU_FR_LEARN_TO_TRADE)
            case "hr":  menu1 = d.find_element(*MenuUS05.SUB_MENU_HR_LEARN_TO_TRADE)
            case "hu":  menu1 = d.find_element(*MenuUS05.SUB_MENU_HU_LEARN_TO_TRADE)
            # case "id":  menu1 = d.find_element(*MenuUS05.SUB_MENU_ID_LEARN_TO_TRADE)
            case "it":  menu1 = d.find_element(*MenuUS05.SUB_MENU_IT_LEARN_TO_TRADE)
            case "lt":  menu1 = d.find_element(*MenuUS05.SUB_MENU_LT_LEARN_TO_TRADE)
            case "lv":  menu1 = d.find_element(*MenuUS05.SUB_MENU_LV_LEARN_TO_TRADE)
            case "nl":  menu1 = d.find_element(*MenuUS05.SUB_MENU_NL_LEARN_TO_TRADE)
            case "pl":  menu1 = d.find_element(*MenuUS05.SUB_MENU_PL_LEARN_TO_TRADE)
            case "pt":  menu1 = d.find_element(*MenuUS05.SUB_MENU_PT_LEARN_TO_TRADE)
            case "ro":  menu1 = d.find_element(*MenuUS05.SUB_MENU_RO_LEARN_TO_TRADE)
            case "ru":  menu1 = d.find_element(*MenuUS05.SUB_MENU_RU_LEARN_TO_TRADE)
            case "sk":  menu1 = d.find_element(*MenuUS05.SUB_MENU_SK_LEARN_TO_TRADE)
            case "sl":  menu1 = d.find_element(*MenuUS05.SUB_MENU_SL_LEARN_TO_TRADE)
            case "sv":  menu1 = d.find_element(*MenuUS05.SUB_MENU_SV_LEARN_TO_TRADE)
            case "zh":  menu1 = d.find_element(*MenuUS05.SUB_MENU_ZH_LEARN_TO_TRADE)

            case _:     pytest.fail(f"For '{test_language}' language test in development")

        self.element_is_clickable(menu1)
        menu1.click()

    @allure.step(f"{datetime.datetime.now()}.   Click 'Glossary' hyperlink.")
    def section_learn_to_trade_item_glossary_click(self, d, test_language):
        match test_language:
            # case "ar":  menu1 = d.find_element(*MenuUS05.SUB_MENU_AR_GLOSSARY)
            case "bg":  menu1 = d.find_element(*MenuUS05.SUB_MENU_BG_GLOSSARY)
            case "cs":  menu1 = d.find_element(*MenuUS05.SUB_MENU_CS_GLOSSARY)
            case "da":  menu1 = d.find_element(*MenuUS05.SUB_MENU_DA_GLOSSARY)
            case "de":  menu1 = d.find_element(*MenuUS05.SUB_MENU_DE_GLOSSARY)
            case "el":  menu1 = d.find_element(*MenuUS05.SUB_MENU_EL_GLOSSARY)
            case "":    menu1 = d.find_element(*MenuUS05.SUB_MENU_EN_GLOSSARY)
            case "es":  menu1 = d.find_element(*MenuUS05.SUB_MENU_ES_GLOSSARY)
            case "et":  menu1 = d.find_element(*MenuUS05.SUB_MENU_ET_GLOSSARY)
            case "fi":  menu1 = d.find_element(*MenuUS05.SUB_MENU_FI_GLOSSARY)
            case "fr":  menu1 = d.find_element(*MenuUS05.SUB_MENU_FR_GLOSSARY)
            case "hr":  menu1 = d.find_element(*MenuUS05.SUB_MENU_HR_GLOSSARY)
            case "hu":  menu1 = d.find_element(*MenuUS05.SUB_MENU_HU_GLOSSARY)
            # case "id":  menu1 = d.find_element(*MenuUS05.SUB_MENU_ID_GLOSSARY)
            case "it":  menu1 = d.find_element(*MenuUS05.SUB_MENU_IT_GLOSSARY)
            case "lt":  menu1 = d.find_element(*MenuUS05.SUB_MENU_LT_GLOSSARY)
            case "lv":  menu1 = d.find_element(*MenuUS05.SUB_MENU_LV_GLOSSARY)
            case "nl":  menu1 = d.find_element(*MenuUS05.SUB_MENU_NL_GLOSSARY)
            case "pl":  menu1 = d.find_element(*MenuUS05.SUB_MENU_PL_GLOSSARY)
            case "pt":  menu1 = d.find_element(*MenuUS05.SUB_MENU_PT_GLOSSARY)
            case "ro":  menu1 = d.find_element(*MenuUS05.SUB_MENU_RO_GLOSSARY)
            case "ru":  menu1 = d.find_element(*MenuUS05.SUB_MENU_RU_GLOSSARY)
            case "sk":  menu1 = d.find_element(*MenuUS05.SUB_MENU_SK_GLOSSARY)
            case "sl":  menu1 = d.find_element(*MenuUS05.SUB_MENU_SL_GLOSSARY)
            case "sv":  menu1 = d.find_element(*MenuUS05.SUB_MENU_SV_GLOSSARY)
            case "zh":  menu1 = d.find_element(*MenuUS05.SUB_MENU_ZH_GLOSSARY)

            case _:     pytest.fail(f"For '{test_language}' language test in development")

        self.element_is_clickable(menu1)
        menu1.click()
