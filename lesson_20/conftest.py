import pytest
from selenium.webdriver import Chrome
from lesson_20.page.dashboard_page import Dashboard


@pytest.fixture(scope='session')
def driver():
    driver = Chrome()
    driver.get('https://lordofboards.com.ua/')
    driver.maximize_window()

    yield driver
    driver.close()


@pytest.fixture(scope='function')
def dashboard(driver):
    yield Dashboard(driver)
