import pytest
from selenium.webdriver import Chrome
from lesson_20.home_work.page.home_page import HomePage
from lesson_20.home_work.page.category_page import CategoryPage


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


@pytest.fixture(scope='function')
def category_page(driver):
    driver.get('https://takagra.com.ua/strategichni/1069/')
    driver.maximize_window()
    yield CategoryPage(driver)
