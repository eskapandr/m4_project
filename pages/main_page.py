from .base_page import BasePage
from .locators import BasePageLocators


class MainPage(BasePage):
    def go_to_basket(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()