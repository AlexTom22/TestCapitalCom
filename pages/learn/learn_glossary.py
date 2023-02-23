import allure
import datetime
from pages.base_page import BasePage
from pages.Learn.learn_glossary_locators import (
    ItemFinancialDictionary,
    WidgetStillLookingFor
)


class ItemPage(BasePage):

    @allure.step(f"{datetime.datetime.now()}.   Click on frame with video.")
    def tc_05_03_video_in_frame_click(self):
        button = self.browser.find_element(*ItemFinancialDictionary.VIDEO_IN_FRAME)
        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button
        )
        self.element_is_clickable(button)
        button.click()

    @allure.step(f"{datetime.datetime.now()}.   Click on 'Trade Now' button.")
    def tc_05_04_button_trade_now_in_frame_click(self):
        button = self.browser.find_element(*ItemFinancialDictionary.BUTTON_IN_FRAME)
        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button
        )
        self.element_is_clickable(button)
        button.click()

    @allure.step(f"{datetime.datetime.now()}.   Click on 'Trade Now' button.")
    def tc_05_05_button_practise_for_free_click(self):
        button = self.browser.find_element(*ItemFinancialDictionary.PRACTISE_FOR_FREE)
        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button
        )
        self.element_is_clickable(button)
        button.click()

    @allure.step(f"{datetime.datetime.now()}.   Click on 'Trade Now' button.")
    def tc_05_06_button_create_and_verify_account_click(self):
        button = self.browser.find_element(*WidgetStillLookingFor.BUT_CREATE_YOUR_ACCOUNT)
        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button
        )
        self.element_is_clickable(button)
        button.click()
