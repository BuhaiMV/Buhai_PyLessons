import pytest
from selenium.webdriver import Chrome
from lesson_20.home_work.page.home_page import HomePage


@pytest.fixture(scope='session')
def driver():
    driver = Chrome()

    yield driver
    driver.close()


@pytest.fixture(scope='function')
def home_page(driver):
    driver.get('https://takagra.com.ua/')
    driver.maximize_window()
    yield HomePage(driver)
