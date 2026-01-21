import pytest
from .pages.product_page import ProductPage
import time


@pytest.mark.parametrize('num', ['1', '2', '3', '4', '5', '6',
                                 pytest.param("7", marks=pytest.mark.xfail), '8', '9'])
def  test_guest_can_add_product_to_basket(browser, num):
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
    #print(added_product_name, added_product_price)


