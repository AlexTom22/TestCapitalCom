# import time
# import allure

# from datetime import datetime
# from selenium.webdriver import ActionChains
# from capital.base_page import BasePage
# from capital.header import Header
# from src.src import (
#     TradingViewPageSrc,
#     ESGPageSrc,
# )
# from capital.learn.learn_glossary_locators import (
#     FinancialDictionary,
# )


# class Glossary(BasePage):
#  @allure.step(f"{datetime.now()}. Checking if the page has a Header.")
# def get_list_letters(self, language):
#     list_letters = None
#     if language in [""]:
#         list_letters = self.browser.find_elements(*FinancialDictionary.ALPHABET_LIST_EN)
#     return list_letters
#
#
# @allure.step(f"{datetime.now()}.   Click button 'Trade Now({{i}})' on widget 'Promo Market'.")
# def tc1001_widget_promo_market_button_trade_now_click(self, i):
#     button = None
#
#     if i == 0:
#         button = self.browser.find_element(*WidgetPromoMarket.BUT_1_TRADE_NOW_ACTIVE)
#     elif i == 1:
#         button = self.browser.find_element(*WidgetPromoMarket.BUT_2_TRADE_NOW_ACTIVE)
#     elif i == 2:
#         button = self.browser.find_element(*WidgetPromoMarket.BUT_3_TRADE_NOW_ACTIVE)
#     elif i == 3:
#         button = self.browser.find_element(*WidgetPromoMarket.BUT_4_TRADE_NOW_ACTIVE)
#
#     self.browser.execute_script(
#         'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
#         button
#     )
#     self.element_is_clickable(button, 30)
#     button.click()
