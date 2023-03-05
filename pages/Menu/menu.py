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
            case "ru":  menu1 = d.find_element(*MenuUS05.SUB_MENU_RU_LEARN_TO_TRADE)
            case _:     pytest.fail(f"For '{test_language}' language test in development")

        self.element_is_clickable(menu1)
        menu1.click()

    @allure.step(f"{datetime.datetime.now()}.   Click 'Glossary' hyperlink.")
    def section_learn_to_trade_item_glossary_click(self, d, test_language):
        match test_language:
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
            case "ru":  menu1 = d.find_element(*MenuUS05.SUB_MENU_RU_GLOSSARY)
            case _:     pytest.fail(f"For '{test_language}' language test in development")

        self.element_is_clickable(menu1)
        menu1.click()
