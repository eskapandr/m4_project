from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def test_guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def add_item_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def success_message_is_not_presented(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def find_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def find_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def find_added_product_name(self):
        return self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text

    def find_added_product_price(self):
        return self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success is not disappeared, but should be"
