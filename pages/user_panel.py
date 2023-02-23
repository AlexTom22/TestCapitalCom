import allure
import datetime
from pages.base_page import BasePage
from pages.Capital.capital_locators import UserPanelLocator
# from .src.src import HeaderSrc


class UserPanel(BasePage):

    @allure.step(f"{datetime.datetime.now()}.   Click 'Logout'")
    def click_logout(self):
        button = self.browser.find_element(*UserPanelLocator.LOGOUT)
        self.element_is_clicable(button, 10)
        button.click()

    @allure.step(f"{datetime.datetime.now()}.   Click 'Trading Platform' button")
    def click_button_trading_platform(self):
        button = self.browser.find_element(*UserPanelLocator.TRADING_PLATFORM)
        self.element_is_clicable(button, 10)
        button.click()

    @allure.step(f"{datetime.datetime.now()}.   Click 'Close User panel'")
    def click_close_user_panel(self):
        button = self.browser.find_element(*UserPanelLocator.CLOSE)
        self.element_is_clicable(button, 10)
        button.click()
