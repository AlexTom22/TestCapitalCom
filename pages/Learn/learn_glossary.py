import allure
import datetime
from pages.base_page import BasePage
from pages.Learn.learn_glossary_locators import (
    ItemFinancialDictionary,
    WidgetStillLookingFor
)


class ItemPage(BasePage):

    @allure.step(f"{datetime.datetime.now()}.   Click on frame with video")
    def tc_05_03_video_in_frame_click(self):
        if self.element_is_present(*ItemFinancialDictionary.VIDEO_IN_FRAME):
            button = self.browser.find_element(*ItemFinancialDictionary.VIDEO_IN_FRAME)
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                button
            )
            self.element_is_clickable(button, 5)
            button.click()
            return True
        else:
            return False

    @allure.step(f"{datetime.datetime.now()}.   Click on 'Trade Now' button under frame with video")
    def tc_05_04_button_trade_now_in_frame_click(self):
        if self.element_is_present(*ItemFinancialDictionary.BUTTON_IN_FRAME):
            button = self.browser.find_element(*ItemFinancialDictionary.BUTTON_IN_FRAME)
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                button
            )
            self.element_is_clickable(button, 5)
            button.click()
            return True
        else:
            return False

    @allure.step(f"{datetime.datetime.now()}.   Click on 'Practise for free' button on vertical banner")
    def tc_05_05_vert_banner_practise_for_free_click(self):
        if self.element_is_present(*ItemFinancialDictionary.VER_BANNER_PRACTISE_FOR_FREE):
            button = self.browser.find_element(*ItemFinancialDictionary.VER_BANNER_PRACTISE_FOR_FREE)
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                button
            )
            self.element_is_clickable(button, 5)
            button.click()
            return True
        else:
            return False

    @allure.step(f"{datetime.datetime.now()}.   Click on 'Practise for free' button on horizontal banner")
    def tc_05_06_hor_banner_button_practise_for_free_click(self):
        if self.element_is_present(*ItemFinancialDictionary.HOR_BANNER_PRACTISE_FOR_FREE):
            button = self.browser.find_element(*ItemFinancialDictionary.HOR_BANNER_PRACTISE_FOR_FREE)
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                button
            )
            self.element_is_clickable(button, 5)
            button.click()
            return True
        else:
            return False
        
    @allure.step(f"{datetime.datetime.now()}.   Click '1. Create your accaunt' button in 'Three first steps' section")
    def tc_05_07_button_create_your_account_click(self):
        if self.element_is_present(*WidgetStillLookingFor.BUT_CREATE_YOUR_ACCOUNT):
            button = self.browser.find_element(*WidgetStillLookingFor.BUT_CREATE_YOUR_ACCOUNT)
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                button
            )
            self.element_is_clickable(button, 5)
            button.click()
            return True
        else:
            return False
        