from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "Non login url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "Field Username is not presented" # смотреть файл locators.py
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Field Password is not presented"  # смотреть файл locators.py

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Field Registration Email is not presented"  # смотреть файл locators.py
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_1), "Field Password is not presented"  # смотреть файл locators.py
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_2), "Field Password check is not presented"  # смотреть файл locators.py