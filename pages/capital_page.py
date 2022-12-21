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

    #
    def click_button_accept_all_cookies(self):
        self.element_is_visible(OnTrastLocators.BUTTON_ACCEPT_ALL_COOKIE)
        # self.element_is_clickable(HeaderElementLocators.BUTTON_LOGIN)
        self.browser.find_element(*OnTrastLocators.BUTTON_ACCEPT_ALL_COOKIE).click()

    # Проверка, что на данной странице есть Header
    def check_that_cur_page_has_header(self):
        # assert self.element_is_located(*ProductsPageLocators.SHOP_CART_LINK)
        assert self.element_is_visible(CapitalPageLocators.HEADER_OF_CAPITAL_COM)

    def click_tab_0_on_main_banner(self):
        # self.element_is_visible(MainBaner.TAB_0)
        self.browser.find_element(*MainBaner.TAB_0).click()

    def click_tab_1_on_main_banner(self):
        # self.element_is_visible(MainBaner.TAB_1)
        self.browser.find_element(*MainBaner.TAB_1).click()

    def click_tab_2_on_main_banner(self):
        # self.element_is_visible(MainBaner.TAB_2)
        self.browser.find_element(*MainBaner.TAB_2).click()

    def click_tab_3_on_main_banner(self):
        # self.element_is_visible(MainBaner.TAB_3)
        self.browser.find_element(*MainBaner.TAB_3).click()

    # Click button on select tab
    def click_tab_0_button_open_account(self):
        self.element_is_visible(MainBaner.TAB_0_OPEN_ACCOUNT)
        self.browser.find_element(*MainBaner.TAB_0_OPEN_ACCOUNT).click()

    def click_tab_0_button_trade_now(self):
        self.element_is_visible(MainBaner.TAB_0_TRADE_NOW)
        self.browser.find_element(*MainBaner.TAB_0_TRADE_NOW).click()

    def click_tab_0_button_practise_for_free(self):
        self.element_is_visible(MainBaner.TAB_0_PRACTISE_FOR_FREE)
        self.browser.find_element(*MainBaner.TAB_0_PRACTISE_FOR_FREE).click()

    def click_tab_1_button_start_trading(self):
        self.element_is_visible(MainBaner.TAB_1_START_TRADING)
        self.browser.find_element(*MainBaner.TAB_1_START_TRADING).click()

    def click_tab_1_button_practise_for_free(self):
        self.element_is_visible(MainBaner.TAB_1_PRACTISE_FOR_FREE)
        self.browser.find_element(*MainBaner.TAB_1_PRACTISE_FOR_FREE).click()

    def click_tab_2_button_show_me_how(self):
        self.element_is_visible(MainBaner.TAB_2_SHOW_ME_HOW)
        self.browser.find_element(*MainBaner.TAB_2_SHOW_ME_HOW).click()

    def click_tab_3_button_explore_features(self):
        self.element_is_visible(MainBaner.TAB_3_EXPLORE_FEATURES)
        self.browser.find_element(*MainBaner.TAB_3_EXPLORE_FEATURES).click()

    def check_open_tradingview_page(self):
        self.should_be_link(TradingViewPageSrc.URL)

    def check_open_esg_page(self):
        self.should_be_link(ESGPageSrc.URL)

    def click_widget_still_looking_button_1_create_your_account(self):
        global half_size_screen
        loc_return = self.element_is_present(*WidgetStillLookingFor.BUT_CREATE_YOUR_ACCOUNT)
        assert loc_return, "Widget 'Still looking for a broker ...' are not present on this page"
        loc_button = self.browser.find_element(*WidgetStillLookingFor.BUT_CREATE_YOUR_ACCOUNT)
        self.browser.execute_script("return arguments[0].scrollIntoView(false);", loc_button)
        self.browser.execute_script(f"window.scrollBy(0, {half_size_screen});")
        loc_button.click()

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

    def click_button_tray_now_on_widget_explore_our_platform(self):
        global half_size_screen

        loc_return = self.element_is_present(*WidgetExploreOurPlatform.BUTTON_TRY_NOW)
        assert loc_return, "Widget 'Explore our platform' are not present on this page"
        button = self.browser.find_element(*WidgetExploreOurPlatform.BUTTON_TRY_NOW)
        self.browser.execute_script("return arguments[0].scrollIntoView(false);", button)
        self.browser.execute_script(f"window.scrollBy(0, {half_size_screen});")
        button.click()

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
