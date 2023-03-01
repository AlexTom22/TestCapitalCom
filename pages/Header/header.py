import allure
import datetime
from pages.base_page import BasePage
from pages.Capital.capital_locators import HeaderElementLocators
# from .src.src import HeaderSrc


class Header(BasePage):

    @allure.step(f"{datetime.datetime.now()}.   Click 'Log In' button.")
    def header_button_login_click(self):
        if self.element_is_present(*HeaderElementLocators.BUTTON_SIGNUP):
            button = self.browser.find_element(*HeaderElementLocators.BUTTON_LOGIN)
            self.element_is_clickable(button, 5)
            button.click()
            return True
        else:
            return False
    
    @allure.step(f"{datetime.datetime.now()}.   Click 'Trade Now' button.")
    def header_button_signup_click(self):
        if self.element_is_present(*HeaderElementLocators.BUTTON_SIGNUP):
            button = self.browser.find_element(*HeaderElementLocators.BUTTON_SIGNUP)
            self.element_is_clickable(button, 5)
            button.click()
            return True
        else:
            return False
