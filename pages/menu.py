"""
-*- coding: utf-8 -*-
@Time    : 2023/01/27 10:00
@Author  : Alexander Tomelo
"""
import allure
import datetime
from pages.base_page import BasePage
from pages.menu_locators import Menu
# from .src.src import HeaderSrc


class MenuBurger(BasePage):

    @allure.step(f"{datetime.datetime.now()}.   Click Menu[Burger].")
    def click_menu_burger(self, d, test_language):
        
        if test_language == "":
            menu1 = d.find_element(*Menu.MENU)
        else:
            return

        self.element_is_clickable(menu1, 10)
        menu1.click()

    @allure.step(f"{datetime.datetime.now()}.   Click 'Learn to trade' submenu item.")
    def click_sub_menu_learn_to_trade(self, d, test_language):
        
        if test_language == "":
            menu1 = d.find_element(*Menu.SUB_MENU_EN_LEARN_TO_TRADE)
        elif test_language == "DE":
            menu1 = d.find_element(*Menu.SUB_MENU_DE_LEARN_TO_TRADE)
        else:
            return

        self.element_is_clickable(menu1, 10)
        menu1.click()

    @allure.step(f"{datetime.datetime.now()}.   Click 'Glossary' hyperlink.")
    def click_glossary_item(self, d, test_language):
        
        if test_language == "":
            menu1 = d.find_element(*Menu.SUB_MENU_EN_GLOSSARY)
        elif test_language == "de":
            menu1 = d.find_element(*Menu.SUB_MENU_DE_GLOSSARY)
        else:
            return

        self.element_is_clickable(menu1, 10)
        menu1.click()
