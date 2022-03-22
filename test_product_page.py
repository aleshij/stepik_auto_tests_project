from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time
import random




link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


# lesson 4.3.13

email = str(time.time()) + "@fakemail.org"
count = random.randint(1, 100)
password = str(time.time() + count)


@pytest.mark.user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        login_page = LoginPage(browser, login_link)
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        page.add_product_in_cart()
        page.should_be_correct()


# lesson 4.3.10
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    # получить текущий url страницы lesson 4.2.9
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_message_empty_basket()


# тест сразу падает
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_cart()
    page.should_not_be_success_message()


# тест ждет 4 секунды и проходит
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


# тест ждет 4 секунды и падает
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_cart()
    page.should_not_be_success_message_is_disappeared()


# маркерованные тест start, маркеры стоят в pytest.nin
@pytest.mark.start
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.start
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page() #авдает так как в locators.py указан не верный селектор


@pytest.mark.skip
@pytest.mark.parametrize('url', [
                                "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"])
def test_should_see_product_page(browser, url):
    link = f"{url}"
    page = ProductPage(browser, link)
    page.open()
    page.should_see_product_description()


# @pytest.mark.parametrize(
#     "url",
#     [
#         f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}" for i in range(10)
#     ]
# )

@pytest.mark.skip
@pytest.mark.parametrize('url', [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}" if i != 7
            else pytest.param(f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}", marks=pytest.mark.xfail)
            for i in range(10)])
def test_guest_can_add_product_to_basket(browser, url):
    link = f"{url}"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    page.should_see_product_description()
    page.add_product_in_cart()
    page.solve_quiz_and_get_code()
    page.should_be_correct()
