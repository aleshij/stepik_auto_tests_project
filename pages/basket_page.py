from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

# task 4.3.10
class BasketPage(BasePage): # наследует все методы от BasePage
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TITLE), \
            "Success message is presented BASKET_TITLE, but should not be"

    def should_be_message_empty_basket(self):
        # реализуйте проверку, что есть сообщение корзина пуста
        assert 'Your basket is empty' in self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE).text, "Non empty message"
