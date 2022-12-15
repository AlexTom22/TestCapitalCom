from .base_page import BasePage
# from .src import CapitalPageSrc
from .locators import (
    CapitalPageLocators,
    OnTrastLocators
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
