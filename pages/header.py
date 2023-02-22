import allure
import datetime
from pages.base_page import BasePage
from pages.capital_locators import HeaderElementLocators
# from .src.src import HeaderSrc


class Header(BasePage):

    @allure.step(f"{datetime.datetime.now()}.   Click 'Log In' button.")
    def click_button_login_on_header(self):
        button = self.browser.find_element(*HeaderElementLocators.BUTTON_LOGIN)
        self.element_is_clickable(button, 5)
        button.click()
        return True
    
    @allure.step(f"{datetime.datetime.now()}.   Click 'Trade Now' button.")
    def click_button_signup_on_header(self):
        button = self.browser.find_element(*HeaderElementLocators.BUTTON_SIGNUP)
        self.element_is_clickable(button, 5)
        button.click()
        return True
    