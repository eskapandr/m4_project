from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_item_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def find_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def find_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def find_added_product_name(self):
        return self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text

    def find_added_product_price(self):
        return self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text
