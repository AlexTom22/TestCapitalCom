import allure
import datetime
from selenium.common.exceptions import (
    ElementClickInterceptedException
)
from pages.base_page import BasePage
from pages.Signup_login.signup_login import SignupLogin
from pages.Header.header_locators import HeaderElementLocators
# from .src.src import HeaderSrc


class Header(BasePage):

    @allure.step(f"{datetime.datetime.now()}.   Check if the element is present on the page")
    def header_button_login_is_present(self):
        if self.element_is_present(*HeaderElementLocators.BUTTON_LOGIN):
            return True
        else:
            return False

    @allure.step(f"{datetime.datetime.now()}.   Click 'Log In' button.")
    def header_button_login_click(self):
        button_list = self.browser.find_elements(*HeaderElementLocators.BUTTON_LOGIN)
        if len(button_list) == 0:
            return False

        self.browser.execute_script(
        'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
        button_list[0]
        )

        self.element_is_clickable(button_list[0], 5)

        try:
            button_list[0].click()
        except ElementClickInterceptedException:
            print("'Login' form is auto opened")
            page_ = SignupLogin(self.browser)
            page_.close_login_form()
            button_list[0].click()

        return True

    @allure.step(f"{datetime.datetime.now()}.   Check if the element is present on the page")
    def header_button_signup_is_present(self):
        if self.element_is_present(*HeaderElementLocators.BUTTON_SIGNUP):
            return True
        else:
            return False

    @allure.step(f"{datetime.datetime.now()}.   Click 'Trade Now' button.")
    def header_button_signup_click(self):
        button_list = self.browser.find_elements(*HeaderElementLocators.BUTTON_SIGNUP)
        if len(button_list) == 0:
            return False

        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )

        self.element_is_clickable(button_list[0], 5)

        try:
            button_list[0].click()
        except ElementClickInterceptedException:
            print("'Sign up' form is auto opened")
            page_ = SignupLogin(self.browser)
            page_.close_signup_form()
            button_list[0].click()

        return True
