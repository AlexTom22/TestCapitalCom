import time

import allure
from selenium.webdriver import ActionChains
from ..base_page import BasePage
from src.src import (
    TradingViewPageSrc,
    ESGPageSrc,
)
from .locators import (
    CapitalPageLocators,
    OnTrastLocators,
    MainBaner,
    WidgetStillLookingFor,
    WidgetPromoMarket,
    WidgetTradingInstrument,
    WidgetExploreOurPlatform,
    WidgetNewToTrading,
    WidgetTradingCalculator,
    WidgetTradersDashboard,
    BannerOfCounters,
    MainBannerDe,
    WhyCapitalDe,
    BannerNewToTradingDe,
)

half_size_screen = int(1080 / 2)


class CapitalPage(BasePage):

    @allure.step("Принять все куки")
    def button_accept_all_cookies_click(self):
        self.element_is_visible(OnTrastLocators.BUTTON_ACCEPT_ALL_COOKIE, 15)
        # self.element_is_clickable(HeaderElementLocators.BUTTON_LOGIN)
        time.sleep(1)
        self.browser.find_element(*OnTrastLocators.BUTTON_ACCEPT_ALL_COOKIE).click()

    # Проверка, что на данной странице есть Header
    @allure.step("Проверка, что на данной странице есть Header")
    def check_that_cur_page_has_header(self):
        # assert self.element_is_located(*ProductsPageLocators.SHOP_CART_LINK)
        assert self.element_is_visible(CapitalPageLocators.HEADER_OF_CAPITAL_COM)

    @allure.step("Click tab 'Spread betting'(tab1) on banner 'Main'")
    def banner_main_tab1_click(self):
        # self.element_is_visible(MainBaner.TAB1)
        self.browser.find_element(*MainBaner.TAB1).click()

    @allure.step("Click button 'Open account' on banner 'Main' tab 'Spread betting'(tab1)")
    # Click button on select tab
    def banner_main_tab1_button_open_account_click(self):
        self.element_is_visible(MainBaner.TAB1_OPEN_ACCOUNT)
        self.browser.find_element(*MainBaner.TAB1_OPEN_ACCOUNT).click()

    @allure.step("Click button 'Trade now' on banner 'Main' tab '1'")
    def banner_main_tab1_button_trade_now_click(self):
        self.element_is_visible(MainBaner.TAB1_TRADE_NOW)
        self.browser.find_element(*MainBaner.TAB1_TRADE_NOW).click()

    @allure.step("Click button 'Practise for free' on banner 'Main' tab '1'")
    def banner_main_tab1_button_practise_for_free_click(self):
        self.element_is_visible(MainBaner.TAB1_PRACTISE_FOR_FREE)
        self.browser.find_element(*MainBaner.TAB1_PRACTISE_FOR_FREE).click()

    @allure.step("Click tab '2' on banner 'Main'")
    def banner_main_tab2_click(self):
        # self.element_is_visible(MainBaner.TAB2)
        self.browser.find_element(*MainBaner.TAB2).click()

    @allure.step("Click button 'Start trading' on banner 'Main' tab '2'")
    def banner_main_tab2_button_start_trading_click(self):
        self.element_is_visible(MainBaner.TAB2_START_TRADING)
        self.browser.find_element(*MainBaner.TAB2_START_TRADING).click()

    @allure.step("Click button 'Practise for free' on banner 'Main' tab '2'")
    def banner_main_tab2_button_practise_for_free_click(self):
        self.element_is_visible(MainBaner.TAB2_PRACTISE_FOR_FREE)
        self.browser.find_element(*MainBaner.TAB2_PRACTISE_FOR_FREE).click()

    @allure.step("Click button 'Take me there' on banner 'Main' tab '2'")
    def banner_main_tab2_button_take_me_there_click(self):
        self.element_is_visible(MainBaner.TAB2_TAKE_ME_THERE)
        self.browser.find_element(*MainBaner.TAB2_TAKE_ME_THERE).click()

    @allure.step("Click tab '3' on banner 'Main'")
    def banner_main_tab3_click(self):
        # self.element_is_visible(MainBaner.TAB3)
        data_type = self.get_attribute("data-type", *MainBaner.TAB3)
        self.browser.find_element(*MainBaner.TAB3).click()
        print(f"data_type = {data_type}")
        if data_type == "topbanner_pro_au_slider":
            layout = 1
        elif data_type == "topbanner_best_platform_22_slider":
            layout = 2
        else:
            layout = 0
        print(f"layout = {layout}")
        return layout

    @allure.step("Click button 'Learn more' on banner 'Main' tab '3' (l1: asic)")
    def banner_main_tab3_l1_button_learn_more_asic_click(self):
        self.element_is_visible(MainBaner.TAB3_L1_LEARN_MORE_ASIC)
        self.browser.find_element(*MainBaner.TAB3_L1_LEARN_MORE_ASIC).click()

    @allure.step("Click button 'Start trading' on banner 'Main' tab '3' (l1: asic)")
    def banner_main_tab3_l1_button_start_trading_asic_click(self):
        self.element_is_visible(MainBaner.TAB3_L1_START_TRADING_ASIC)
        self.browser.find_element(*MainBaner.TAB3_L1_START_TRADING_ASIC).click()

    @allure.step("Click button 'Start trading' on banner 'Main' tab '3' (l2: All, axcept ASIC)")
    def banner_main_tab3_l2_button_start_trading_fca_click(self):
        self.element_is_visible(MainBaner.TAB3_L2_START_TRADING_FCA)
        self.browser.find_element(*MainBaner.TAB3_L2_START_TRADING_FCA).click()

    @allure.step("Click button 'Practise for free 'Main' tab '3' (l2: All, except ASIC)")
    def banner_main_tab3_l2_button_practise_for_free_fca_click(self):
        self.element_is_visible(MainBaner.TAB3_L2_PRACTISE_FOR_FREE_FCA)
        self.browser.find_element(*MainBaner.TAB3_L2_PRACTISE_FOR_FREE_FCA).click()

    # @allure.step("Click button 'Start trading' on banner 'Main' tab '3' (l2: All, except ASIC)")
    # def banner_main_tab3_button_practise_for_free_fca_click(self):
    #     self.element_is_visible(MainBaner.TAB3_L2_PRACTISE_FOR_FREE_FCA)
    #     self.browser.find_element(*MainBaner.TAB3_L2_PRACTISE_FOR_FREE_FCA).click()
    #
    @allure.step("Click button 'Show me now' on banner 'Main' tab '3'")
    def banner_main_tab3_button_show_me_how_click(self):
        self.element_is_visible(MainBaner.TAB3_SHOW_ME_HOW)
        self.browser.find_element(*MainBaner.TAB3_SHOW_ME_HOW).click()

    @allure.step("Click tab '4' on banner 'Main'")
    def banner_main_tab4_click(self):
        self.element_is_visible(MainBaner.TAB4)
        self.browser.find_element(*MainBaner.TAB4).click()

    @allure.step("Click button 'Explore features' on banner 'Main' tab '4'")
    def banner_main_tab4_button_explore_features_click(self):
        self.element_is_visible(MainBaner.TAB4_EXPLORE_FEATURES)
        self.browser.find_element(*MainBaner.TAB4_EXPLORE_FEATURES).click()

    @allure.step("What is the current layout Widget 'Trading instrument'?")
    def what_is_the_current_layout(self, language):
        layout = 0

        if language in [""]:
            len_list_1 = len(self.browser.find_elements(*WidgetTradingInstrument.LIST_TABS_1))
            if len_list_1 > 0:
                layout = 1

            len_list_2 = len(self.browser.find_elements(*WidgetTradingInstrument.LIST_TABS_2))
            if len_list_2 > 0:
                layout = 2
        elif language not in [""]:
            len_list_2 = len(self.browser.find_elements(*WidgetTradingInstrument.LIST_TABS_2_DE))
            if len_list_2 > 0:
                layout = 2

        print(f"Current layout: {layout}")
        return layout

    @allure.step("Click tab '{tab_name}' on Widget 'Trading instrument' (layout: {layout})")
    def widget_trading_instrument_cur_tab_click(self, language, layout, tab_name):
        list_tabs = None
        x = None

        if language not in [""]:
            if layout == 2:
                list_tabs = self.browser.find_elements(*WidgetTradingInstrument.LIST_TABS_2_DE)
        elif language in [""]:
            if layout == 2:
                list_tabs = self.browser.find_elements(*WidgetTradingInstrument.LIST_TABS_2)
            elif layout == 1:
                list_tabs = self.browser.find_elements(*WidgetTradingInstrument.LIST_TABS_1)

        qty_tabs = len(list_tabs)
        if qty_tabs == 6:
            if tab_name == "Most traded":
                x = 0
            elif tab_name == "Commodities":
                x = 1
            elif tab_name == "Indices":
                x = 2
            elif tab_name == "Shares":
                x = 3
            elif tab_name == "Forex":
                x = 4
            elif tab_name == "ETFs":
                x = 5
        elif qty_tabs == 7:
            if tab_name == "Most traded":
                x = 0
            elif tab_name == "Commodities":
                x = 1
            elif tab_name == "Indices":
                x = 2
            elif tab_name == "Cryptocurrencies":
                x = 3
            elif tab_name == "Shares":
                x = 4
            elif tab_name == "Forex":
                x = 5
            elif tab_name == "ETFs":
                x = 6

        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            list_tabs[x]
        )
        # self.browser.execute_script(f"window.scrollBy(0, {half_size_screen});")
        list_tabs[x].click()

    @allure.step("Get list of lines with buttons in {tab_name} tab. (Layout: {layout}")
    def get_list_lines_cur_tab(self, language, layout, tab_name):
        list_buttons = None

        if layout == 1 and language in [""]:
            if tab_name == "Most traded":
                list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_MTR_1)
            elif tab_name == "Commodities":
                list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_COM_1)
            elif tab_name == "Indices":
                list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_IND_1)
            elif tab_name == "Cryptocurrencies":
                list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_CRY_1)
            elif tab_name == "Shares":
                list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_SHAR_1)
            elif tab_name == "Forex":
                list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_FX_1)
            elif tab_name == "ETFs":
                list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_ETF_1)
        elif layout == 2:
            if tab_name == "Most traded":
                list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_MTR_2)
            elif tab_name == "Commodities":
                list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_COM_2)
            elif tab_name == "Indices":
                list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_IND_2)
            elif tab_name == "Cryptocurrencies":
                list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_CRY_2)
            elif tab_name == "Shares":
                list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_SHAR_2)
            elif tab_name == "Forex":
                list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_FX_2)
            elif tab_name == "ETFs":
                list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_ETF_2)
        else:
            return
        return list_buttons

    @allure.step("Click button 'Trade' on the '{y}' line selected tab.")
    def selected_tab_and_line_button_trade_click(self, list_buttons, y):

        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            list_buttons[y]
        )
        list_buttons[y].click()

    @allure.step
    def check_open_tradingview_page(self):
        self.should_be_link(TradingViewPageSrc.URL)

    @allure.step
    def check_open_esg_page(self):
        self.should_be_link(ESGPageSrc.URL)

    @allure.step("Click 'Create your account and send ...' in widget 'Still looking for ...'")
    def widget_still_looking_button_1_create_your_account_click(self, language):
        loc_button = None
        if language in [""]:
            loc_return = self.element_is_present(*WidgetStillLookingFor.BUT_CREATE_YOUR_ACCOUNT_EN)
            assert loc_return, "Widget 'Still looking for a broker ...' are not present on this page"
            loc_button = self.browser.find_element(*WidgetStillLookingFor.BUT_CREATE_YOUR_ACCOUNT_EN)
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                loc_button
            )
        elif language not in [""]:
            loc_return = self.element_is_present(*WidgetStillLookingFor.BUT_CREATE_YOUR_ACCOUNT_DE)
            assert loc_return, "Widget 'Still looking for a broker ...' are not present on this page"
            loc_button = self.browser.find_element(*WidgetStillLookingFor.BUT_CREATE_YOUR_ACCOUNT_DE)
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                loc_button
            )
        loc_button.click()

    @allure.step("How many different buttons 'Trade Now' on widget 'Promo Market'")
    def how_many_dif_buttons_trade_now_on_widget_promo_market(self):
        list_but = self.browser.find_elements(*WidgetPromoMarket.LIST_BUTs_TRADE_NOW_2)
        qty = len(list_but)
        if qty != 0:
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                list_but[0]
            )
        return qty

    @allure.step("Click button 'Trade Now({i})' on widget 'Promo Market'")
    def widget_promo_market_button_trade_now_click(self, i):
        if i == 0:
            self.element_is_clicable(WidgetPromoMarket.BUT_1_TRADE_NOW_ACTIVE, 20)
            self.browser.find_element(*WidgetPromoMarket.BUT_1_TRADE_NOW_ACTIVE).click()
        elif i == 1:
            self.element_is_clicable(WidgetPromoMarket.BUT_2_TRADE_NOW_ACTIVE, 10)
            self.browser.find_element(*WidgetPromoMarket.BUT_2_TRADE_NOW_ACTIVE).click()
        elif i == 2:
            self.element_is_clicable(WidgetPromoMarket.BUT_3_TRADE_NOW_ACTIVE, 10)
            self.browser.find_element(*WidgetPromoMarket.BUT_3_TRADE_NOW_ACTIVE).click()
        elif i == 3:
            self.element_is_clicable(WidgetPromoMarket.BUT_4_TRADE_NOW_ACTIVE, 10)
            self.browser.find_element(*WidgetPromoMarket.BUT_4_TRADE_NOW_ACTIVE).click()

    @allure.step("Click button 'Trade Now' on widget 'Explore our platform'")
    def widget_explore_our_platform_button_tray_now_click(self, language):
        button = None
        if language in [""]:
            loc_return = self.element_is_present(*WidgetExploreOurPlatform.BUTTON_TRY_NOW_EN)
            assert loc_return, "Widget 'Explore our platform' are not present on this page"
            button = self.browser.find_element(*WidgetExploreOurPlatform.BUTTON_TRY_NOW_EN)
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                button
            )
        elif language not in [""]:
            loc_return = self.element_is_present(*WidgetExploreOurPlatform.BUTTON_TRY_NOW_DE)
            assert loc_return, "Widget 'Explore our platform' are not present on this page"
            button = self.browser.find_element(*WidgetExploreOurPlatform.BUTTON_TRY_NOW_DE)
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                button
        )
        button.click()

    @allure.step("Click button 'Practise for free' on widget 'New to trading?'")
    def widget_new_to_trading_button_practise_for_free_click(self, language):
        button = None

        if language in [""]:
            section_new_to_trading = self.browser.find_element(*WidgetNewToTrading.SECTION_NEW_TO_TRADING_EN)
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                section_new_to_trading
            )
            button = self.browser.find_element(*WidgetNewToTrading.BUTTON_PRACTISE_FOR_FREE_EN)
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                button
            )
        elif language not in [""]:
            button = self.browser.find_element(*WidgetNewToTrading.BUTTON_PRACTISE_FOR_FREE_DE)
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                button
            )
        button.click()
        return True

    @allure.step("Click button 'Start trading' on widget 'Trading calculator'")
    def widget_trading_calculator_button_start_trading_click(self):
        loc_return = self.element_is_present(*WidgetTradingCalculator.BUTTON_START_TRADING)
        assert loc_return, "Widget 'Trading calculator' are not present on this page"
        button = self.browser.find_element(*WidgetTradingCalculator.BUTTON_START_TRADING)
        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button
        )
        time.sleep(1)
        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button
        )
        button.click()

    @allure.step("How many lines with buttons 'Trade' on widget 'Trader's Dashboard'?")
    def how_many_buttons_trade_on_widget_traders_dashboard(self):
        list_but = self.browser.find_elements(*WidgetTradersDashboard.LIST_BUTTONS_TRADE)
        qty = len(list_but)
        # if qty != 0:
        #     self.browser.execute_script("return arguments[0].scrollIntoView(false);", list_but[qty-1])
        print(f"Trader's Dashboard widget has {qty} lines")
        return qty

    @allure.step("Click 'Trade' button {i} line on widget 'Trader's Dashboard'")
    def widget_traders_dashboard_button_trade_click(self, i):
        list_buttons = self.browser.find_elements(*WidgetTradersDashboard.LIST_BUTTONS_TRADE)
        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            list_buttons[i]
        )
        time.sleep(1)
        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            list_buttons[i]
        )
        list_buttons[i].click()

    @allure.step("Click 'Try now' button on 'Why choose Capital.com? ...' banner")
    def banner_of_counters_button_try_now_click(self):
        list_buttons = self.browser.find_elements(*BannerOfCounters.BUTTON_TRY_NOW)
        qty = len(list_buttons)
        if qty != 0:
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                list_buttons[0]
            )
            list_buttons[0].click()
        return bool(qty)

    @allure.step("Click 'Jetzt traden' button on 'Main' banner")
    def de_banner_main_button_left_click(self):
        list_buttons = self.browser.find_elements(*MainBannerDe.BUTTON_LEFT)
        qty = len(list_buttons)
        if qty != 0:
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                list_buttons[0]
            )
            list_buttons[0].click()
        return bool(qty)

    @allure.step("Click 'Kostenloses Demokonto' button on 'Main' banner")
    def de_banner_main_button_righ_click(self):
        list_buttons = self.browser.find_elements(*MainBannerDe.BUTTON_RIGH)
        qty = len(list_buttons)
        if qty != 0:
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                list_buttons[0]
            )
            list_buttons[0].click()
        return bool(qty)

    @allure.step("Click 'Jetzt traden' button on 'Warum Capital.com?' banner")
    def de_banner_why_capital_button_trade_now_click(self):
        list_buttons = self.browser.find_elements(*WhyCapitalDe.BUTTON_TRADE_NOW_DE)
        qty = len(list_buttons)
        if qty != 0:
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                list_buttons[0]
            )
            list_buttons[0].click()
        return bool(qty)

    @allure.step("Click 'Practise for free' button on the 'New to trading?' banner (de)")
    def de_banner_new_to_trading_button_practise_fo_free_click(self):
        list_buttons = self.browser.find_elements(*BannerNewToTradingDe.BUTTON_PRACTISE_FOR_FREE)
        qty = len(list_buttons)
        if qty != 0:
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                list_buttons[0]
            )
            list_buttons[0].click()
        return bool(qty)
