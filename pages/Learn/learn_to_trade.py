import allure
import datetime
from pages.base_page import BasePage
from pages.Learn.learn_to_trade_locators import LearnToTradePageLocator


class LearnToTrade(BasePage):

    # Проверка наличия текста на странице
    def tc_03_should_be_learn_to_trade_text(self):
        if self.element_is_present(LearnToTradePageLocator.LOCATOR_LEARN_TO_TRADE_TEXT):
            learn_to_trade_text = self.browser.find_element(LearnToTradePageLocator.LOCATOR_LEARN_TO_TRADE_TEXT)
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                learn_to_trade_text)
            check_text = "Learn to trade"
            assert learn_to_trade_text == check_text, f'Text on UI {learn_to_trade_text} is not eq {check_text}'
            return True
        else:
            return False

    @allure.step(f"{datetime.datetime.now()}.   Click 'Log In' button.")
    def tc_03_01_click_button_login(self):
        button = self.browser.find_element(LearnToTradePageLocator.LOCATOR_LEARN_TO_TRADE_LOGIN_BUTTON)
        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button
        )
        self.element_is_clickable(button, 5)
        button.click()
        return True

    @allure.step(F"{datetime.datetime.now()}. Click 'Trade Now' button.")
    def tc_03_02_click_button_trade_now(self):
        button = self.browser.find_element(LearnToTradePageLocator.LOCATOR_LEARN_TO_TRADE_TRADE_NOW_BUTTON)
        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button
        )
        self.element_is_clickable(button, 5)
        button.click()
        return True

    @allure.step(F"{datetime.datetime.now()}.Click '1.Create verify your account' button in "
                 F"'Three first steps' section")
    def tc_03_03_click_button_1_create_verify_your_account_button(self):
        button = self.browser.find_element(LearnToTradePageLocator.
                                           LOCATOR_LEARN_TO_TRADE_CREATE_VERIFY_YOUR_ACCOUNT_BUTTON)
        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button
        )
        self.element_is_clickable(button, 5)
        button.click()
        return True
