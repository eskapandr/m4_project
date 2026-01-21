import pytest
from .pages.product_page import ProductPage


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

@pytest.mark.xfail(reason='success message should not appear')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.success_message_is_not_presented()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.success_message_is_not_presented()

@pytest.mark.xfail(reason='bug is not fixed')
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.success_message_is_disappeared()