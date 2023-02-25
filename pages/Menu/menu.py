"""
-*- coding: utf-8 -*-
@Time    : 2023/01/27 10:00
@Author  : Alexander Tomelo
"""
import allure
import datetime

import pytest

from pages.base_page import BasePage
from pages.Menu.menu_locators import Menu
# from .src.src import HeaderSrc


class BurgerMenu(BasePage):

    @allure.step(f"{datetime.datetime.now()}.   Click button [Burger menu].")
    def burger_menu_click(self, d):
        
        menu1 = d.find_element(*Menu.MENU)

        self.element_is_clickable(menu1)
        menu1.click()

    @allure.step(f"{datetime.datetime.now()}.   Click 'Learn to trade' menu section.")
    def menu_section_learn_to_trade_click(self, d, test_language):
        
        if test_language == "":
            menu1 = d.find_element(*Menu.SUB_MENU_EN_LEARN_TO_TRADE)
        elif test_language == "de":
            menu1 = d.find_element(*Menu.SUB_MENU_DE_LEARN_TO_TRADE)
        elif test_language == "ru":
            menu1 = d.find_element(*Menu.SUB_MENU_RU_LEARN_TO_TRADE)
        elif test_language == "bg":
            menu1 = d.find_element(*Menu.SUB_MENU_BG_LEARN_TO_TRADE)
        elif test_language == "cs":
            menu1 = d.find_element(*Menu.SUB_MENU_CS_LEARN_TO_TRADE)
        elif test_language == "fr":
            menu1 = d.find_element(*Menu.SUB_MENU_FR_LEARN_TO_TRADE)
        else:
            pytest.fail(f"For '{test_language}' language test in development")

        self.element_is_clickable(menu1)
        menu1.click()

    @allure.step(f"{datetime.datetime.now()}.   Click 'Glossary' hyperlink.")
    def section_learn_to_trade_item_glossary_click(self, d, test_language):
        
        if test_language == "":
            menu1 = d.find_element(*Menu.SUB_MENU_EN_GLOSSARY)
        elif test_language == "de":
            menu1 = d.find_element(*Menu.SUB_MENU_DE_GLOSSARY)
        elif test_language == "ru":
            menu1 = d.find_element(*Menu.SUB_MENU_RU_GLOSSARY)
        elif test_language == "bg":
            menu1 = d.find_element(*Menu.SUB_MENU_BG_GLOSSARY)
        elif test_language == "cs":
            menu1 = d.find_element(*Menu.SUB_MENU_CS_GLOSSARY)
        elif test_language == "fr":
            menu1 = d.find_element(*Menu.SUB_MENU_FR_GLOSSARY)
        else:
            pytest.fail(f"For '{test_language}' language test in development")

        self.element_is_clickable(menu1)
        menu1.click()
