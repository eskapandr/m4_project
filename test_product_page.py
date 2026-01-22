import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95"

@pytest.mark.skip(reason='test is not needed to check')
@pytest.mark.parametrize('num', ['1', '2', '3', '4', '5', '6',
                                 pytest.param("7", marks=pytest.mark.xfail), '8', '9'])
def test_guest_can_add_product_to_basket(browser, num):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open() # открываем страницу
    product_name = page.find_product_name()
    product_price = page.find_product_price()
    #print(product_name, product_price)
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(5)
    added_product_name = page.find_added_product_name()
    added_product_price = page.find_added_product_price()
    assert product_name == added_product_name, "product name doesn't match added product name"
    assert product_price == added_product_price, "product name doesn't match added product price"

@pytest.mark.skip(reason='test is not needed to check')
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip(reason='test is not needed to check')
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.skip(reason='test is not needed to check')
@pytest.mark.xfail(reason='success message should not appear')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.success_message_is_not_presented()

@pytest.mark.skip(reason='test is not needed to check')
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.success_message_is_not_presented()

@pytest.mark.skip(reason='test is not needed to check')
@pytest.mark.xfail(reason='bug is not fixed')
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.success_message_is_disappeared()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_items_form_is_not_presented()
    basket_page.should_be_empty_basket_message()
