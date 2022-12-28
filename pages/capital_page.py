import time

import allure
from selenium.webdriver import ActionChains
from .base_page import BasePage
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

    @allure.step
    def check_open_tradingview_page(self):
        self.should_be_link(TradingViewPageSrc.URL)

    @allure.step
    def check_open_esg_page(self):
        self.should_be_link(ESGPageSrc.URL)

    @allure.step
    def click_widget_still_looking_button_1_create_your_account(self):
        global half_size_screen
        loc_return = self.element_is_present(*WidgetStillLookingFor.BUT_CREATE_YOUR_ACCOUNT)
        assert loc_return, "Widget 'Still looking for a broker ...' are not present on this page"
        loc_button = self.browser.find_element(*WidgetStillLookingFor.BUT_CREATE_YOUR_ACCOUNT)
        self.browser.execute_script("return arguments[0].scrollIntoView(false);", loc_button)
        self.browser.execute_script(f"window.scrollBy(0, {half_size_screen});")
        loc_button.click()

    @allure.step
    def click_widget_promo_market_button_trade_now(self):
        global half_size_screen

        loc_return = self.element_is_present(*WidgetPromoMarket.SLIDER_FADE)
        assert loc_return, "Widget 'Promo Market' are not present on this page"
        slider_element = self.browser.find_element(*WidgetPromoMarket.SLIDER_FADE)
        self.browser.execute_script("return arguments[0].scrollIntoView(false);", slider_element)
        self.browser.execute_script(f"window.scrollBy(0, {half_size_screen});")

        list_items_trade_now = self.elements_are_present(*WidgetPromoMarket.LIST_SLIDER_FADE_ITEMS)
        for item in list_items_trade_now:
            item.element_is_clicable(WidgetPromoMarket.BUTTON_ON_ITEM, 15)
            item.find_element(*WidgetPromoMarket.BUTTON_ON_ITEM).click()

    @allure.step
    def select_tab_on_widget_trading_instrument(self, tab_name):
        global half_size_screen
        x = None
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

        # loc_return = self.element_is_present(*WidgetTradingInstrument.TABS_NAVIGATOR)
        # assert loc_return, "Widget 'Trading instrument' are not present on this page"
        list_tabs = self.browser.find_elements(*WidgetTradingInstrument.LIST_TABS)
        # for chromium only
        ActionChains(self.browser).scroll_to_element(list_tabs[x])
        ActionChains(self.browser).perform()
        ActionChains(self.browser).scroll_by_amount(0, half_size_screen)
        ActionChains(self.browser).perform()
        ActionChains(self.browser).click(list_tabs[x])
        ActionChains(self.browser).perform()
        # self.browser.execute_script("return arguments[0].scrollIntoView(false);", list_tabs[x])
        # self.browser.execute_script(f"window.scrollBy(0, {half_size_screen});")
        # list_tabs[x].click()

    @allure.step
    def click_button_trade_on_selected_line(self, tab_name, y):
        global half_size_screen
        list_buttons = None
        if tab_name == "Most traded":
            list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_MTR)
        elif tab_name == "Commodities":
            list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_COM)
        elif tab_name == "Indices":
            list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_IND)
        elif tab_name == "Shares":
            list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_SHAR)
        elif tab_name == "Forex":
            list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_FX)
        elif tab_name == "ETFs":
            list_buttons = self.browser.find_elements(*WidgetTradingInstrument.LIST_BUTTONS_TRADE_FOR_ETF)

        # for chromium only
        ActionChains(self.browser).scroll_to_element(list_buttons[y])
        ActionChains(self.browser).perform()
        ActionChains(self.browser).scroll_by_amount(0, half_size_screen)
        ActionChains(self.browser).perform()
        ActionChains(self.browser).click(list_buttons[y])
        ActionChains(self.browser).perform()

        # self.browser.execute_script("return arguments[0].scrollIntoView(false);", list_buttons[y])
        # # self.browser.execute_script(f"window.scrollBy(0, {half_size_screen});")
        # list_buttons[y].click()

    @allure.step
    def click_button_tray_now_on_widget_explore_our_platform(self):
        global half_size_screen

        loc_return = self.element_is_present(*WidgetExploreOurPlatform.BUTTON_TRY_NOW)
        assert loc_return, "Widget 'Explore our platform' are not present on this page"
        button = self.browser.find_element(*WidgetExploreOurPlatform.BUTTON_TRY_NOW)
        self.browser.execute_script("return arguments[0].scrollIntoView(false);", button)
        self.browser.execute_script(f"window.scrollBy(0, {half_size_screen});")
        button.click()

    @allure.step
    def click_button_practise_for_free_on_widget_new_to_trading(self):
        global half_size_screen

        loc_return = self.element_is_present(*WidgetNewToTrading.BUTTON_PRACTISE_FOR_FREE)
        assert loc_return, "Widget 'Explore our platform' are not present on this page"
        button = self.browser.find_element(*WidgetNewToTrading.BUTTON_PRACTISE_FOR_FREE)
        # for chromium only
        ActionChains(self.browser).scroll_to_element(button).click(button).perform()


#
#
#
#
#
        # list_slider_items = self.elements_are_present(*WidgetPromoMarket.LIST_SLIDER_FADE_ITEMS)
        # for elem in list_slider_items:
        #     elem.element_is_clicable(WidgetPromoMarket.ACTIVE_BUTTON_TRADE_NOW, 15).click()
            # self.browser.find_element(*WidgetPromoMarket.ACTIVE_BUTTON_TRADE_NOW).click()

        # self.element_is_visible(WidgetStillLookingFor.BUT_CREATE_YOUR_ACCOUNT)
        # self.browser.find_element(*WidgetStillLookingFor.BUT_CREATE_YOUR_ACCOUNT).click()

    # button = browser.find_element_by_tag_name("button")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # button.click()
    # # Checks the products on the page meet the requirements
    # def should_be_products_page_inventory_list(self):
    #     # Gets the list of elements on the page
    #     list_el = self.browser.find_element(*ProductsPageLocators.INVENT_LIST)
    #     assert len(list_el.get_property("children")) != 0, "there is no products"
    #
    #
    # # Goes to the Cart page
    # def go_to_basket_page(self):
    #     self.click_button(*ProductsPageLocators.SHOP_CART_LINK)
    #
    # # Check the cart icon on the current page doesn't display any products
    # def should_be_empty_shopping_cart_badge(self):
    #     el = self.browser.find_element(*ProductsPageLocators.SHOP_CART_LINK)
    #     assert (el.get_property("children")) == [], "there is some items in cart"
    #
    # # Checks the link Privacy Policy
    # def check_privacy_link(self):
    #     assert self.element_is_present(*PageLocators.ROBOT_IMG), "something went wrong"
    #     # self.browser.find_element(*PageLocators.PRIVACY)
    #     self.click_button(*PageLocators.PRIVACY)
    #
    # def go_to_product_page(self):
    #     self.click_button(*ProductsPageLocators.PRODUCT_IMG)
