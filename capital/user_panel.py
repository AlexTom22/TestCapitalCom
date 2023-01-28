import allure
import datetime
from base_page import BasePage
from capital_locators import UserPanel
# from .src.src import HeaderSrc


class UserPanel(BasePage):

    @allure.step(f"{datetime.datetime.now()}.   Click 'Logout'")
    def click_logout(self):
        button = self.browser.find_element(*UserPanel.LOGOUT)
        self.element_is_clicable(button, 10)
        button.click()

    @allure.step(f"{datetime.datetime.now()}.   Click 'Trading Platform' button")
    def click_button_trading_platform(self):
        button = self.browser.find_element(*UserPanel.TRADING_PLATFORM)
        self.element_is_clicable(button, 10)
        button.click()

    @allure.step(f"{datetime.datetime.now()}.   Click 'Close User panel'")
    def click_close_user_panel(self):
        button = self.browser.find_element(*UserPanel.CLOSE)
        self.element_is_clicable(button, 10)
        button.click()
