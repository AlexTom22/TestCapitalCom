from .base_page import BasePage
from .locators import HeaderElementLocators
# from .src import HeaderSrc


class HeaderElement(BasePage):

    def click_button_login_on_header(self):
        self.element_is_visible(HeaderElementLocators.BUTTON_LOGIN_LOCATOR)
        # self.element_is_clickable(HeaderElementLocators.BUTTON_LOGIN)
        self.browser.find_element(*HeaderElementLocators.BUTTON_LOGIN).click()

    def click_button_signup_on_header(self):
        self.element_is_visible(HeaderElementLocators.BUTTON_SIGNUP_LOCATOR)
        # self.element_is_clickable(HeaderElementLocators.BUTTON_SIGNUP)
        self.browser.find_element(*HeaderElementLocators.BUTTON_SIGNUP).click()
