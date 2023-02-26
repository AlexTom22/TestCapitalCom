import time
import allure

from datetime import datetime
from pages.base_page import BasePage
from pages.header import Header
from src.src import (
    TradingViewPageSrc,
    ESGPageSrc,
)
from pages.Capital.capital_locators import (
    CapitalPageLocators,
    MainBanner,
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
from pages.Signup_login.signup_login_locators import (
    SignupLoginFormLocators,
)

class Capital(BasePage):

    # Check that this page has a Header
    @allure.step(f"{datetime.now()}. Checking if the page has a Header.")
    def check_that_cur_page_has_header(self):
        # assert self.element_is_located(*ProductsPageLocators.SHOP_CART_LINK)
        assert self.element_is_visible(CapitalPageLocators.HEADER_OF_CAPITAL_COM)

    # авторизация пользователя
    @allure.step(f"{datetime.now()}. Checking if the page has a Header.")
    def to_do_authorization(self, d, test_link, test_login, test_password):

        assert test_login != "", "Авторизация невозможна. Не указан e-mail"
        assert test_password != "", "Авторизация невозможна. Не указан пароль"
        # нажать в хедере на кнопку "Log in"
        page = Header(d, test_link)
        page.click_button_login_on_header()

        # User's name is passed to the text element on the login page
        self.send_keys(test_login, *SignupLoginFormLocators.LOGIN_INPUT_EMAIL)
        # Password is passed to the text element on the login page
        self.send_keys(test_password, *SignupLoginFormLocators.LOGIN_INPUT_PASSWORD)
        self.click_button(*SignupLoginFormLocators.LOGIN_CONTINUE)
        time.sleep(2)

    @allure.step(f"{datetime.now()}. Click tab 'Spread betting'(tab1) on banner 'Main'.")
    def banner_main_tab1_click(self):
        self.element_is_clickable(MainBanner.TAB1, 10)
        self.browser.find_element(*MainBanner.TAB1).click()

    @allure.step(f"{datetime.now()}. "
                 f"Click button 'Open account' on banner 'Main' tab 'Spread betting'(tab1).")
    # Click button on select tab
    def banner_main_tab1_button_open_account_click(self):
        self.element_is_clickable(MainBanner.TAB1_OPEN_ACCOUNT, 10)
        self.browser.find_element(*MainBanner.TAB1_OPEN_ACCOUNT).click()

    @allure.step(f"{datetime.now()}.   Click button 'Trade now' on banner 'Main' tab '1'.")
    def banner_main_tab1_button_trade_now_click(self):
        self.element_is_clickable(MainBanner.TAB1_TRADE_NOW, 10)
        self.browser.find_element(*MainBanner.TAB1_TRADE_NOW).click()

    @allure.step(f"{datetime.now()}.   Click button 'Practise for free' on banner 'Main' tab '1'.")
    def banner_main_tab1_button_practise_for_free_click(self):
        self.element_is_clickable(MainBanner.TAB1_PRACTISE_FOR_FREE, 10)
        self.browser.find_element(*MainBanner.TAB1_PRACTISE_FOR_FREE).click()

    @allure.step(f"{datetime.now()}.   Click button 'Start trading' on banner 'Main' tab '1'.")
    def banner_main_tab1_button_start_trading_click(self):
        self.element_is_clickable(MainBanner.TAB1_START_TRADING, 10)
        self.browser.find_element(*MainBanner.TAB1_START_TRADING).click()

    @allure.step(f"{datetime.now()}.   Click tab '2' on banner 'Main'.")
    def banner_main_tab2_click(self):
        self.element_is_clickable(MainBanner.TAB2, 10)
        self.browser.find_element(*MainBanner.TAB2).click()

    @allure.step(f"{datetime.now()}.   Click button 'Start trading' on banner 'Main' tab '2'.")
    def banner_main_tab2_button_start_trading_click(self):
        self.element_is_clickable(MainBanner.TAB2_START_TRADING, 10)
        self.browser.find_element(*MainBanner.TAB2_START_TRADING).click()

    @allure.step(f"{datetime.now()}.   Click button 'Practise for free' on banner 'Main' tab '2'.")
    def banner_main_tab2_button_practise_for_free_click(self):
        self.element_is_clickable(MainBanner.TAB2_PRACTISE_FOR_FREE, 10)
        self.browser.find_element(*MainBanner.TAB2_PRACTISE_FOR_FREE).click()

    @allure.step(f"{datetime.now()}.   Click button 'Take me there' on banner 'Main' tab '2'.")
    def banner_main_tab2_button_take_me_there_click(self):
        self.element_is_clickable(MainBanner.TAB2_TAKE_ME_THERE, 10)
        self.browser.find_element(*MainBanner.TAB2_TAKE_ME_THERE).click()

    @allure.step(f"{datetime.now()}.   Click tab '3' on banner 'Main'.")
    def banner_main_tab3_click(self):
        data_type = self.get_attribute("data-type", *MainBanner.TAB3)
        self.browser.find_element(*MainBanner.TAB3).click()
        print(f"data_type = {data_type}")
        if data_type == "topbanner_pro_au_slider":
            layout = 1
        elif data_type == "topbanner_best_platform_22_slider":
            layout = 2
        else:
            layout = 0
        print(f"layout = {layout}")
        return layout

    @allure.step(f"{datetime.now()}.   Click button 'Learn more' on banner 'Main' tab '3' (l1: ASIC).")
    def banner_main_tab3_l1_button_learn_more_asic_click(self):
        self.element_is_clickable(MainBanner.TAB3_L1_LEARN_MORE_ASIC, 10)
        self.browser.find_element(*MainBanner.TAB3_L1_LEARN_MORE_ASIC).click()

    @allure.step(f"{datetime.now()}.   Click button 'Start trading' on banner 'Main' tab '3' (l1: ASIC).")
    def banner_main_tab3_l1_button_start_trading_asic_click(self):
        self.element_is_clickable(MainBanner.TAB3_L1_START_TRADING_ASIC, 10)
        self.browser.find_element(*MainBanner.TAB3_L1_START_TRADING_ASIC).click()

    @allure.step(f"{datetime.now()}.   "
                 f"Click button 'Start trading' on banner 'Main' tab '3' (l2: All, except ASIC).")
    def banner_main_tab3_l2_button_start_trading_fca_click(self):
        self.element_is_clickable(MainBanner.TAB3_L2_START_TRADING_FCA, 10)
        self.browser.find_element(*MainBanner.TAB3_L2_START_TRADING_FCA).click()

    @allure.step(f"{datetime.now()}.   Click button 'Practise for free 'Main' tab '3' (l2: All, except ASIC).")
    def banner_main_tab3_l2_button_practise_for_free_fca_click(self):
        self.element_is_clickable(MainBanner.TAB3_L2_PRACTISE_FOR_FREE_FCA, 10)
        self.browser.find_element(*MainBanner.TAB3_L2_PRACTISE_FOR_FREE_FCA).click()

    @allure.step(f"{datetime.now()}.   Click button 'Show me now' on banner 'Main' tab '3'.")
    def banner_main_tab3_button_show_me_how_click(self):
        self.element_is_clickable(MainBanner.TAB3_SHOW_ME_HOW, 10)
        self.browser.find_element(*MainBanner.TAB3_SHOW_ME_HOW).click()

    @allure.step(f"{datetime.now()}.   Click tab '4' on banner 'Main'.")
    def tc0601_banner_main_tab4_click(self):
        self.element_is_clickable(MainBanner.TAB4, 10)
        self.browser.find_element(*MainBanner.TAB4).click()

    @allure.step(f"{datetime.now()}.   Click button 'Explore features' on banner 'Main' tab '4'.")
    def tc0601_banner_main_tab4_button_explore_features_click(self):
        self.element_is_clickable(MainBanner.TAB4_EXPLORE_FEATURES, 10)
        self.browser.find_element(*MainBanner.TAB4_EXPLORE_FEATURES).click()

    @allure.step(f"{datetime.now()}.   What is the current layout Widget 'Trading instrument'?")
    def tc08_what_is_the_current_layout(self):
        layout = 0

        len_list_1 = len(self.browser.find_elements(*WidgetTradingInstrument.LIST_TABS_1))
        if len_list_1 > 0:
            layout = 1

        len_list_2 = len(self.browser.find_elements(*WidgetTradingInstrument.LIST_TABS_2))
        if len_list_2 > 0:
            layout = 2

        print(f"Current layout: {layout}")
        return layout

    @allure.step(f"{datetime.now()}.   "
                 f"Click '{{tab_name}}' tab on 'Trading instrument' widget (layout: {{layout}}).")
    def tc08_widget_trading_instrument_tab_click(self, layout, tab_name):
        button_tab = None

        print(f"Current kayout - {layout}")

        if layout == 1:
            if tab_name == "Most":
                button_tab = self.browser.find_element(*WidgetTradingInstrument.BUT_MOST_1)
            elif tab_name == "Commodities":
                button_tab = self.browser.find_element(*WidgetTradingInstrument.BUT_COMMOD_1)
            elif tab_name == "Indices":
                button_tab = self.browser.find_element(*WidgetTradingInstrument.BUT_INDICES_1)
            elif tab_name == "Crypto":
                button_tab = self.browser.find_element(*WidgetTradingInstrument.BUT_CRYPTO_1)
            elif tab_name == "Shares":
                button_tab = self.browser.find_element(*WidgetTradingInstrument.BUT_SHARES_1)
            elif tab_name == "Forex":
                button_tab = self.browser.find_element(*WidgetTradingInstrument.BUT_FOREX_1)
            elif tab_name == "ETFs":
                button_tab = self.browser.find_element(*WidgetTradingInstrument.BUT_ETFS_1)
        elif layout == 2:
            if tab_name == "Most":
                button_tab = self.browser.find_element(*WidgetTradingInstrument.BUT_MOST_2)
            elif tab_name == "Commodities":
                button_tab = self.browser.find_element(*WidgetTradingInstrument.BUT_COMMOD_2)
            elif tab_name == "Indices":
                button_tab = self.browser.find_element(*WidgetTradingInstrument.BUT_INDICES_2)
            elif tab_name == "Crypto":
                button_tab = self.browser.find_element(*WidgetTradingInstrument.BUT_CRYPTO_2)
            elif tab_name == "Shares":
                button_tab = self.browser.find_element(*WidgetTradingInstrument.BUT_SHARES_2)
            elif tab_name == "Forex":
                button_tab = self.browser.find_element(*WidgetTradingInstrument.BUT_FOREX_2)
            elif tab_name == "ETFs":
                button_tab = self.browser.find_element(*WidgetTradingInstrument.BUT_ETFS_2)

        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_tab
        )
        self.element_is_clickable(button_tab, 20)
        button_tab.click()

    @allure.step(f"{datetime.now()}.   "
                 f"Get list of lines with buttons in {{tab_name}} tab. (Layout: {{layout}}).")
    def tc08_get_list_lines_from_tab(self, language, layout, tab_name):
        list_buttons = None

        print(language)

        if layout == 1:
            if tab_name == "Most":
                list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_MTR_1)
            elif tab_name == "Commodities":
                list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_COM_1)
            elif tab_name == "Indices":
                list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_IND_1)
            elif tab_name == "Crypto":
                list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_CRY_1)
            elif tab_name == "Shares":
                list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_SHAR_1)
            elif tab_name == "Forex":
                list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_FX_1)
            elif tab_name == "ETFs":
                list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_ETF_1)
        elif layout == 2:
            if tab_name == "Most":
                list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_MTR_2)
            elif tab_name == "Commodities":
                list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_COM_2)
            elif tab_name == "Indices":
                list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_IND_2)
            elif tab_name == "Crypto":
                list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_CRY_2)
            elif tab_name == "Shares":
                list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_SHAR_2)
            elif tab_name == "Forex":
                list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_FX_2)
            elif tab_name == "ETFs":
                list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_ETF_2)
        else:
            return
        print(f"{tab_name} tab has {len(list_buttons)} lines with ' Trade' button")

        return list_buttons

    @allure.step(f"{datetime.now()}.   Click button 'Trade' on the '{{y}}' line selected tab.")
    def tc08_selected_tab_and_line_button_trade_click(self, list_buttons, y):

        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            list_buttons[y]
        )
        self.element_is_clickable(list_buttons[y], 15)
        list_buttons[y].click()

    @allure.step(f"{datetime.now()}.   Check that TradingView page is open")
    def check_open_tradingview_page(self):
        self.should_be_link(TradingViewPageSrc.URL)

    @allure.step(f"{datetime.now()}.   Check, that ESG page is open")
    def check_open_esg_page(self):
        self.should_be_link(ESGPageSrc.URL)

    @allure.step(f"{datetime.now()}.   "
                 f"Click 'Create your account and send ...' in widget 'Still looking for ...'")
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
        self.element_is_clickable(loc_button, 10)
        loc_button.click()

    @allure.step(f"{datetime.now()}.   How many different buttons 'Trade Now' on widget 'Promo Market'.")
    def tc1001_how_many_dif_buttons_trade_now_on_widget_promo_market(self):
        list_but = self.browser.find_elements(*WidgetPromoMarket.LIST_BUTs_TRADE_NOW_2)
        qty = len(list_but)
        print(f"This widget has {qty} different slider lines with 'Trade Now' button")
        return qty

    @allure.step(f"{datetime.now()}.   Click button 'Trade Now({{i}})' on widget 'Promo Market'.")
    def tc1001_widget_promo_market_button_trade_now_click(self, i):
        button = None

        if i == 0:
            button = self.browser.find_element(*WidgetPromoMarket.BUT_1_TRADE_NOW_ACTIVE)
        elif i == 1:
            button = self.browser.find_element(*WidgetPromoMarket.BUT_2_TRADE_NOW_ACTIVE)
        elif i == 2:
            button = self.browser.find_element(*WidgetPromoMarket.BUT_3_TRADE_NOW_ACTIVE)
        elif i == 3:
            button = self.browser.find_element(*WidgetPromoMarket.BUT_4_TRADE_NOW_ACTIVE)

        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button
        )
        self.element_is_clickable(button, 30)
        button.click()

    @allure.step(f"{datetime.now()}.   Click button 'Trade Now' on widget 'Explore our platform'.")
    def tc1101_widget_explore_our_platform_button_tray_now_click(self, language):
        button = None
        if language in [""]:
            button = self.element_is_present(*WidgetExploreOurPlatform.BUTTON_TRY_NOW_EN)
            assert button, "Widget 'Explore our platform' are not present on this page"
            button = self.browser.find_element(*WidgetExploreOurPlatform.BUTTON_TRY_NOW_EN)
        elif language not in [""]:
            button = self.element_is_present(*WidgetExploreOurPlatform.BUTTON_TRY_NOW_DE)
            assert button, "Widget 'Explore our platform' are not present on this page"
            button = self.browser.find_element(*WidgetExploreOurPlatform.BUTTON_TRY_NOW_DE)

        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button
        )
        self.element_is_clickable(button, 25)
        button.click()

    @allure.step(f"{datetime.now()}.   Click 'Practise for free' button on the 'New to trading?' banner (de).")
    def tc1201_de_banner_new_to_trading_button_practise_fo_free_click(self):
        list_buttons = self.browser.find_elements(*BannerNewToTradingDe.BUTTON_PRACTISE_FOR_FREE)
        qty = len(list_buttons)
        if qty != 0:
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                list_buttons[0]
            )
            # self.element_is_visible(list_buttons[0], 15)
            self.element_is_clickable(list_buttons[0], 15)
            list_buttons[0].click()
        return bool(qty)

    @allure.step(f"{datetime.now()}.   Click button 'Practise for free' on widget 'New to trading?'.")
    def tc1301_widget_new_to_trading_button_practise_for_free_click(self, language):
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
        
        self.element_is_clickable(button, 15)
        button.click()
      
        return True

    @allure.step(f"{datetime.now()}.   Click button 'Start trading' on widget 'Trading calculator'.")
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
        self.element_is_clickable(button, 10)
        button.click()

    @allure.step(f"{datetime.now()}.   How many lines with buttons 'Trade' on widget 'Trader's Dashboard'?.")
    def how_many_buttons_trade_on_widget_traders_dashboard(self):
        list_but = self.browser.find_elements(*WidgetTradersDashboard.LIST_BUTTONS_TRADE)
        qty = len(list_but)
        print(f"This tab Trader's Dashboard widget has {qty} lines with 'Trade' button")
        return qty

    @allure.step(f"{datetime.now()}.   Click 'Trade' button {{i}} line on widget 'Trader's Dashboard'.")
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
        self.element_is_clickable(list_buttons[i], 10)
        list_buttons[i].click()

    @allure.step(f"{datetime.now()}.   Click 'Try now' button on 'Why choose Capital.com? ...' banner.")
    def tc1601_banner_of_counters_button_try_now_click(self):
        button = None
        layout = 0

        list_buttons = self.browser.find_elements(*BannerOfCounters.BUTTON_1)
        if len(list_buttons) != 0:
            layout = 1
            button = list_buttons[0]

        list_buttons = self.browser.find_elements(*BannerOfCounters.BUTTON_2)
        if len(list_buttons) != 0:
            layout = 2
            button = list_buttons[0]

        print(f"Current layout = {layout}")

        if layout != 0:
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                button
            )
            self.element_is_clickable(button, 10)
            button.click()

        return layout

    @allure.step(f"{datetime.now()}.   Click 'Jetzt traden' button on 'Main' banner.")
    def tc0201_de_banner_main_button_left_click(self):
        list_buttons = self.browser.find_elements(*MainBannerDe.BUTTON_LEFT)
        qty = len(list_buttons)
        if qty != 0:
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                list_buttons[0]
            )
            self.element_is_clickable(list_buttons[0], 15)
            list_buttons[0].click()
        return bool(qty)

    @allure.step(f"{datetime.now()}.   Click 'Kostenloses Demokonto' button on 'Main' banner.")
    def tc0202_de_banner_main_button_right_click(self):
        list_buttons = self.browser.find_elements(*MainBannerDe.BUTTON_RIGH)
        qty = len(list_buttons)
        if qty != 0:
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                list_buttons[0]
            )
            self.element_is_clickable(list_buttons[0], 15)
            list_buttons[0].click()
        return bool(qty)

    @allure.step(f"{datetime.now()}.   Click 'Jetzt traden' button on 'Warum Capital.com?' banner.")
    def tc0701_de_banner_why_capital_button_trade_now_click(self):
        list_buttons = self.browser.find_elements(*WhyCapitalDe.BUTTON_TRADE_NOW_DE)
        qty = len(list_buttons)
        if qty != 0:
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                list_buttons[0]
            )
            # self.element_is_visible(list_buttons[0], 15)
            self.element_is_clickable(list_buttons[0], 15)
            list_buttons[0].click()
        return bool(qty)
