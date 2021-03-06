from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators


class MainPage(BasePage): # наследует все методы от BasePage
    # task 4.3.8
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    # task 4.2.3
    # перенесли в base_page.py
    # def go_to_login_page(self):
    #     login_link = self.browser.find_element(By.CSS_SELECTOR, '#login_link')
    #     login_link.click()

    # task 4.2.6 - 4.2.7
    # def should_be_login_link(self):
    #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented" # смотреть файл locators.py


