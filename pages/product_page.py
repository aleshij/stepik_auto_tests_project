from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import ProductPageLocators
import time


class ProductPage(BasePage): # наследует все методы от BasePage
    def should_see_product_description(self):
        assert self.browser.find_element(By.ID, 'product_description')

    def add_product_in_cart(self):
        button_add_in_cart = self.browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
        button_add_in_cart.click()

    def should_be_correct(self):
        try:
            # Задаем счетчик ожидания в 10 секунд и отслеживаем изменение, сравнивая его с текстом
            WebDriverWait(self.browser, 10).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.alertinner'),
                                                 "The shellcoder's handbook has been added to your basket."))
            message = self.browser.find_elements(By.CSS_SELECTOR, 'div.alertinner')

            title = self.browser.find_element(*ProductPageLocators.TITLE_PRODUCT)
            title = title.text

            message_title = message[0].text

            assert title in message_title, "Error title in the cart"

            price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
            price = price.text

            message_price = message[2].text

            assert price in message_price, "Error price in the cart"

        finally:
            pass


