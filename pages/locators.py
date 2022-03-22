from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini a.btn")


class BasketPageLocators():
    BASKET_TITLE = (By.CSS_SELECTOR, "div.basket-title")
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "div#content_inner")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_USERNAME = (By.NAME, "login-username")
    LOGIN_PASSWORD = (By.NAME, "login-password")

    REGISTRATION_EMAIL = (By.NAME, "registration-email")
    REGISTRATION_PASSWORD_1 = (By.NAME, "registration-password1")
    REGISTRATION_PASSWORD_2 = (By.NAME, "registration-password2")


class ProductPageLocators():
    TITLE_PRODUCT = (By.CSS_SELECTOR, 'div.product_main>h1')
    PRICE_PRODUCT = (By.CSS_SELECTOR, 'div.product_main p.price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner strong')
