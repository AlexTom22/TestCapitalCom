import allure
import datetime
from pages.base_page import BasePage
from pages.Learn.learn_to_trade_locators import LearnToTradePageLocator


class LearnToTrade(BasePage):
    # Проверка текущего URL
    @allure.step(f"{datetime.datetime.now()}. Current_url.")
    def tc_03_current_url(self):
        current_url = self.browser.current_url
        check_current_url = "https://capital.com/learn-to-trade"
        assert current_url == check_current_url,  f'Text on UI {current_url} is not eq {check_current_url}'

    # Проверка наличия текста на странице
    @allure.step(f"{datetime.datetime.now()}. Should_be_learn_to_trade_text.")
    def tc_03_should_be_learn_to_trade_text(self):
        if self.element_is_present(*LearnToTradePageLocator.LOCATOR_LEARN_TO_TRADE_TEXT):
            learn_to_trade = self.browser.find_element(*LearnToTradePageLocator.LOCATOR_LEARN_TO_TRADE_TEXT)
            learn_to_trade_text = learn_to_trade.text
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                learn_to_trade)
            check_text = "Learn to trade"
            assert learn_to_trade_text == check_text, f'Text on UI {learn_to_trade_text} is not eq {check_text}'
            return True
        else:
            return False

    @allure.step(f"{datetime.datetime.now()}.   Click 'Log In' button.")
    def tc_03_01_click_button_login(self):
        if self.element_is_present(*LearnToTradePageLocator.LOCATOR_LEARN_TO_TRADE_LOGIN_BUTTON):
            button = self.browser.find_element(*LearnToTradePageLocator.LOCATOR_LEARN_TO_TRADE_LOGIN_BUTTON)
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                button)
            self.element_is_clickable(button, 5)
            button.click()
            return True
        else:
            return False

    @allure.step(F"{datetime.datetime.now()}. Click 'Trade Now' button.")
    def tc_03_02_click_button_trade_now(self):
        if self.element_is_present(*LearnToTradePageLocator.LOCATOR_LEARN_TO_TRADE_TRADE_NOW_BUTTON):
            button = self.browser.find_element(*LearnToTradePageLocator.LOCATOR_LEARN_TO_TRADE_TRADE_NOW_BUTTON)
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                button)
            self.element_is_clickable(button, 5)
            button.click()
            return True
        else:
            return False

    @allure.step(F"{datetime.datetime.now()}.Click '1.Create verify your account' button in "
                 F"'Three first steps' section")
    def tc_03_03_click_button_1_create_verify_your_account_button(self):
        if self.element_is_present(*LearnToTradePageLocator.LOCATOR_LEARN_TO_TRADE_CREATE_VERIFY_YOUR_ACCOUNT_BUTTON):
            button = self.browser.find_element(*LearnToTradePageLocator.
                                               LOCATOR_LEARN_TO_TRADE_CREATE_VERIFY_YOUR_ACCOUNT_BUTTON)
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                button)
            self.element_is_clickable(button, 5)
            button.click()
            return True
        else:
            return False
