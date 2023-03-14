import allure
import datetime
from selenium.common.exceptions import (
    ElementClickInterceptedException
)
from pages.base_page import BasePage
from pages.Learn.learn_glossary_locators import (
    ItemFinancialDictionary,
    WidgetStillLookingFor
)
from pages.Signup_login.signup_login import SignupLogin


class ItemPage(BasePage):

    @allure.step(f"{datetime.datetime.now()}.   Check if the element is present on the page")
    def tc_05_03_video_in_frame_is_present(self):
        print(f"{datetime.datetime.now()}.   VIDEO_BANNER =>")
        if self.element_is_present(*ItemFinancialDictionary.VIDEO_IN_FRAME):
            print(f"{datetime.datetime.now()}.   => VIDEO_BANNER IS PRESENT")
            return True
        else:
            print(f"{datetime.datetime.now()}.   => VIDEO_BANNER IS NOT PRESENT")
            return False

    @allure.step(f"{datetime.datetime.now()}.   Click on frame with video")
    def tc_05_03_video_in_frame_click(self):
        button_list = self.browser.find_elements(*ItemFinancialDictionary.VIDEO_IN_FRAME)
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
            page_ = SignupLogin(self.browser, "")
            page_.close_signup_form()
            button_list[0].click()

        return True

    @allure.step(f"{datetime.datetime.now()}.   Check if the element is present on the page")
    def tc_05_04_button_trade_now_under_video_banner_is_present(self):
        print(f"{datetime.datetime.now()}.   BUTTON_UNDER_VIDEO_BANNER =>")
        if self.element_is_present(*ItemFinancialDictionary.BUTTON_UNDER_VIDEO_BANNER):
            print(f"{datetime.datetime.now()}.   => BUTTON_UNDER_VIDEO_BANNER IS PRESENT")
            return True
        else:
            print(f"{datetime.datetime.now()}.   => BUTTON_UNDER_VIDEO_BANNER IS NOT PRESENT")
            return False

    @allure.step(f"{datetime.datetime.now()}.   Click on button under video banner")
    def tc_05_04_button_trade_now_under_video_banner_click(self):
        button_list = self.browser.find_elements(*ItemFinancialDictionary.BUTTON_UNDER_VIDEO_BANNER)
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
            page_ = SignupLogin(self.browser, "")
            page_.close_signup_form()
            button_list[0].click()

        return True
    

    @allure.step(f"{datetime.datetime.now()}.   Check if the element is present on the page")
    def tc_05_05_vert_hor_banner_button_is_present(self):
        print(f"{datetime.datetime.now()}.   VER_HOR_BANNER_BUTTON =>")
        if self.element_is_present(*ItemFinancialDictionary.VER_HOR_BANNER_BUTTON):
            print(f"{datetime.datetime.now()}.   => VER_HOR_BANNER_BUTTON IS PRESENT")
            return True
        else:
            print(f"{datetime.datetime.now()}.   => VER_HOR_BANNER_BUTTON IS NOT PRESENT")
            return False

    @allure.step(f"{datetime.datetime.now()}.   Click on 'Create account' button on vertical banner")
    def tc_05_05_vert_hor_banner_button_click(self):
        button_list = self.browser.find_elements(*ItemFinancialDictionary.VER_HOR_BANNER_BUTTON)
        
        if len(button_list) == 0:
            return False

        print(f"{len(button_list)} checking element(s) with current CSS locator is(are) present(s) on this page")

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

    # @allure.step(f"{datetime.datetime.now()}.   Check if the element is present on the page")
    # def tc_05_05_vert_banner_practise_for_free_is_present(self):
    #     print(f"{datetime.datetime.now()}.   VER_BANNER_PRACTISE_FOR_FREE =>")
    #     if self.element_is_present(*ItemFinancialDictionary.VER_BANNER_PRACTISE_FOR_FREE):
    #         print(f"{datetime.datetime.now()}.   => VER_BANNER_PRACTISE_FOR_FREE IS PRESENT")
    #         return True
    #     else:
    #         print(f"{datetime.datetime.now()}.   => VER_BANNER_PRACTISE_FOR_FREE IS NOT PRESENT")
    #         return False
    #
    # @allure.step(f"{datetime.datetime.now()}.   Click on 'Practise for free' button on vertical banner")
    # def tc_05_05_vert_banner_practise_for_free_click(self):
    #     button_list = self.browser.find_elements(*ItemFinancialDictionary.VER_BANNER_PRACTISE_FOR_FREE)
    #     if len(button_list) == 0:
    #         return False
    #
    #     print(f"{len(button_list)} checking element(s) with current CSS locator is(are) present(s) on this page")
    #
    #     self.browser.execute_script(
    #         'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
    #         button_list[0]
    #     )
    #     self.element_is_clickable(button_list[0], 5)
    #     try:
    #         button_list[0].click()
    #     except ElementClickInterceptedException:
    #         print("'Sign up' form is auto opened")
    #         page_ = SignupLogin(self.browser)
    #         page_.close_signup_form()
    #         button_list[0].click()
    #
    #     return True

    # @allure.step(f"{datetime.datetime.now()}.   Check if the element is present on the page")
    # def tc_05_07_hor_banner_button_practise_for_free_is_present(self):
    #     print(f"{datetime.datetime.now()}.   HOR_BANNER_PRACTISE_FOR_FREE =>")
    #     if self.element_is_present(*ItemFinancialDictionary.HOR_BANNER_PRACTISE_FOR_FREE):
    #         print(f"{datetime.datetime.now()}.   => HOR_BANNER_PRACTISE_FOR_FREE IS PRESENT")
    #         return True
    #     else:
    #         print(f"{datetime.datetime.now()}.   => HOR_BANNER_PRACTISE_FOR_FREE IS NOT PRESENT")
    #         return False
    #
    # @allure.step(f"{datetime.datetime.now()}.   Click on 'Practise for free' button on horizontal banner")
    # def tc_05_07_hor_banner_button_practise_for_free_click(self):
    #     button_list = self.browser.find_elements(*ItemFinancialDictionary.HOR_BANNER_PRACTISE_FOR_FREE)
    #     if len(button_list) == 0:
    #         return False
    #
    #     print(f"{len(button_list)} checking element(s) with current CSS locator is(are) present(s) on this page")
    #
    #     self.browser.execute_script(
    #         'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
    #         button_list[0]
    #     )
    #
    #     self.element_is_clickable(button_list[0], 5)
    #
    #     try:
    #         button_list[0].click()
    #     except ElementClickInterceptedException:
    #         print("'Sign up' form is auto opened")
    #         page_ = SignupLogin(self.browser)
    #         page_.close_signup_form()
    #         button_list[0].click()
    #
    #     return True

    @allure.step(f"{datetime.datetime.now()}.   Check if the element is present on the page")
    def tc_05_06_button_create_your_account_is_present(self):
        print(f"{datetime.datetime.now()}.   BUT_CREATE_YOUR_ACCOUNT =>")
        if self.element_is_present(*WidgetStillLookingFor.BUT_CREATE_YOUR_ACCOUNT):
            print(f"{datetime.datetime.now()}.   => BUT_CREATE_YOUR_ACCOUNT IS PRESENT")
            return True
        else:
            print(f"{datetime.datetime.now()}.   => BUT_CREATE_YOUR_ACCOUNT IS NOT PRESENT")
            return False

    @allure.step(f"{datetime.datetime.now()}.   Click '1. Create your accaunt' button in 'Three first steps' section")
    def tc_05_06_button_create_your_account_click(self):
        button_list = self.browser.find_elements(*WidgetStillLookingFor.BUT_CREATE_YOUR_ACCOUNT)
        if len(button_list) == 0:
            return False
        print(f"{len(button_list)} checking element(s) with current CSS locator is(are) present(s) on this page")
        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )
        self.element_is_clickable(button_list[0], 5)
        try:
            button_list[0].click()
        except ElementClickInterceptedException:
            print("'Sign up' form is auto opened")
            page_ = SignupLogin(self.browser, "")
            page_.close_signup_form()
            button_list[0].click()
        return True
