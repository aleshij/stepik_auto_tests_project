import pytest
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='Choose language, default english')


# useragent = UserAgent()
# options.set_preference('general.useragent.override', useragent.firefox)

options = webdriver.FirefoxOptions()

options.set_preference('general.useragent.override',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0')
options.set_preference('dom.webdriver.enable', False)

service = Service("D:\\Dropbox\\GitHub\\geckodriver.exe")

# Запустить в фоне
# options.headless = True


@pytest.fixture(scope="function")
def browser(request):

    user_language = request.config.getoption('language')
    options.set_preference('intl.accept_languages', user_language)

    browser = webdriver.Firefox(
        service=service,
        options=options
    )
    # return browser
    # этот код выполнится после завершения теста
    yield browser
    time.sleep(5)
    browser.quit()