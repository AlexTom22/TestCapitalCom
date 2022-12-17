from .base_page import BasePage
from src.src import (
    TradingViewPageSrc,
    ESGPageSrc,
)
from .locators import (
    CapitalPageLocators,
    OnTrastLocators,
    MainBaner
)


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

    # Проверка всех кнопок Trade на вкладке tab_instrument
    def check_buttons_trade_on_select_tab(self, tab_instrument):
        pass

# Click on Tab0, Tab1, Tab2 or Tab3
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

    #
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
