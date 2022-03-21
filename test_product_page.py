from .pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('url', [
                                "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"])

# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


@pytest.mark.skip
def test_should_see_product_page(browser, url):
    link = f"{url}"
    page = ProductPage(browser, link)
    page.open()
    page.should_see_product_description()


# @pytest.mark.parametrize('url', [
#                                 "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
#                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"])
# @pytest.mark.parametrize(
#     "url",
#     [
#         f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}" for i in range(10)
#     ]
# )
@pytest.mark.parametrize('url', [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}" if i != 7
            else pytest.param(f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}", marks=pytest.mark.xfail)
            for i in range(10)])
def test_add_product_in_cart(browser, url):
    link = f"{url}"
    page = ProductPage(browser, link)
    page.open()
    page.should_see_product_description()
    page.add_product_in_cart()
    page.solve_quiz_and_get_code()
    page.should_be_correct()
