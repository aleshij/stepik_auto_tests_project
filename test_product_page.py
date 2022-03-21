from .pages.product_page import ProductPage
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


@pytest.mark.skip
def test_should_see_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_see_product_description()


def test_add_product_in_cart(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_see_product_description()
    page.add_product_in_cart()
    page.solve_quiz_and_get_code()
    page.should_be_correct()
