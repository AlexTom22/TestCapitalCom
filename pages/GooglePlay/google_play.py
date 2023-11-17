"""
-*- coding: utf-8 -*-
@Time    : 2023/06/20 11:00
@Author  : Andrey Bozhko
"""

import allure
from datetime import datetime

import pytest

from pages.base_page import BasePage
from pages.GooglePlay.google_play_locators import GooglePlayLocators
from test_data.google_play_data import data


class GooglePlay(BasePage):
    @allure.step("Checking that the Google Play page has opened")
    def should_be_google_play_page(self, cur_link):
        """Check if the page is open"""
        print(f"{datetime.now()}   Checking that the Google Play page has opened")
        self.wait_for_change_url(cur_link, 10)
        # Следующие две строки только для проверки работоспособности asserts, тк в данный момент баг в url кнопки
        # self.link = "https://play.google.com/store/apps/details?id=com.capital.trading"
        # self.open_page()
        if self.current_page_url_contain_the(data["APP_URL"]):
            self.should_be_page_title_v2(data["PAGE_TITLE"])
            self.should_be_google_play_app_title(data["APP_TITLE"])
            self.should_be_google_play_specifies_provider(data["PROVIDER"])
            self.open_page()
            assert True
        else:
            current_page = self.browser.current_url
            self.open_page()
            pytest.fail(f'Bug!!! Loaded page {current_page} with not {data["APP_URL"]} url')

    @allure.step("Checking that the Google Play app title")
    def should_be_google_play_app_title(self, app_title):
        """Check if the app title"""
        print(f"{datetime.now()}   Checking that the Google Play app title")
        assert self.get_text(0, *GooglePlayLocators.APP_TITLE) == app_title

    @allure.step("Checking that the Google Play specifies provider")
    def should_be_google_play_specifies_provider(self, provider):
        """Check if the specifies provider"""
        print(f"{datetime.now()}   Checking that the App Store specifies provider")
        assert self.get_text(0, *GooglePlayLocators.PROVIDER) == provider
