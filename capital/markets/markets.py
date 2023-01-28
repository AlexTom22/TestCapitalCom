import allure
import time
import datetime
from ..base_page import BasePage
from markets_locators import HeaderElementLocators
from src.src import (
    CapitalComPageSrc,
    MarketsSrc,
)


class Markets(BasePage):

    @allure.step(f"{datetime.datetime.now()}.   Click 'Log In' button.")
    def click_button_login_on_header(self):
        button = self.browser.find_element(*HeaderElementLocators.BUTTON_LOGIN)
        self.element_is_clickable(button, 10)
        button.click()

    @allure.step(f"{datetime.datetime.now()}.   Click 'Trade Now' button.")
    def click_button_signup_on_header(self):
        button = self.browser.find_element(*HeaderElementLocators.BUTTON_SIGNUP)
        self.element_is_clickable(button, 10)
        button.click()
