from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasePageLocators

class ProductPage(BasePage):

    def test_guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def add_item_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def go_to_basket(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def success_message_is_not_presented(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"


    def check_product_name_after_adding_item_to_basket(self):
        assert (self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text ==
         self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text), \
        "product name doesn't match added product name"

    def check_product_price_after_adding_item_to_basket(self):
        assert (self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text ==
         self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text), \
        "product price doesn't match added product name"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success is not disappeared, but should be"
