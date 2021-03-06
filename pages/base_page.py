from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .locators import BasePageLocators
import math
import time

# task 4.2.2
# task 4.2.6
class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # task 4.2.2
    def open(self):
        self.browser.get(self.url)

    # task 4.3.8
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"


    # task 4.3.13
    def should_be_authorized_user(self):
        # Задаем счетчик ожидания в 10 секунд и отслеживаем изменение, сравнивая его с текстом
        WebDriverWait(self.browser, 15).until(lambda l: l.find_element(By.LINK_TEXT, "Logout"))
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    # task 4.3.10
    def should_be_basket_link(self):
        assert self.is_element_present(*BasePageLocators.BASKET_LINK), "Basket link is not presented"

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    # task 4.2.6
    def is_element_present(self, how, what): # перехватывает исключение, существуют ли запрашиваемые поля
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # task 4.3.5
    # is_not_element_present: упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый.
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    # is_disappeared: будет ждать до тех пор, пока элемент не исчезнет.
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    # task 4.3.2
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        time.sleep(2)
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
