from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_items_form_is_not_presented(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_FORM), \
            "Basket items form is presented, but should not be"
    def should_be_empty_basket_message(self):
        basket_message = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text
        print(basket_message)
        assert len(basket_message) > 0, 'Missing message of empty basket'
