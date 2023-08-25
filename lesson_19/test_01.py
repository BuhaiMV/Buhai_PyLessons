from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


def test_01():
    driver = Chrome()
    driver.get('https://google.com')
    search_field_locator = '//textarea[@type="search"]'
    element = driver.find_element(by='xpath', value=search_field_locator)
    element.send_keys('how to use webdriver')
    element.send_keys(Keys.ENTER)
    second_page = driver.find_element(by='xpath', value=search_field_locator)
    assert second_page.text == 'how to use webdriver'


def test_02():
    driver = Chrome()
    driver.get('https://google.com')
    search_field_locator = '//textarea[@type="search"]'
    element = driver.find_element(by='xpath', value=search_field_locator)
    element.send_keys('how to use webdriver')
    element.send_keys(Keys.ENTER)
    first_link_locator = '//h3[text()="Selenium Webdriver Tutorial with Examples - BrowserStack"]'
    first_link = driver.find_element(by='xpath', value=first_link_locator)
    first_link.click()
    desired_text_locator = '//h1'
    desired_text = driver.find_element(by='xpath', value=desired_text_locator)
    assert desired_text.text == 'Selenium WebDriver Tutorial : Getting Started with Test Automation'


def test_03():
    driver = Chrome()
    driver.get('https://geekach.com.ua/')
    first_element_menu_locator = '//div[@class="products-menu__title"]'
    first_element_menu = driver.find_element(by='xpath', value=first_element_menu_locator)
    first_element_menu.click()
    products_locator = '//li[@class="catalog-grid__item"]'
    products = driver.find_elements(by='xpath', value=products_locator)
    assert len(products) == 20


def test_04():
    driver = Chrome()
    driver.get('https://geekach.com.ua/')
    first_element_menu_locator = '//div[@class="products-menu__title"]'
    first_element_menu = driver.find_element(by='xpath', value=first_element_menu_locator)
    first_element_menu.click()
    products_locator = '//li[@class="catalog-grid__item"]'
    products = driver.find_elements(by='xpath', value=products_locator)
    for element in products:
        assert 'В наявності' in element.text


def test_05():
    driver = Chrome()
    driver.get('https://google.com')
    search_field_locator = '//textarea[@type="search"]'
    element = driver.find_element(by='xpath', value=search_field_locator)
    element.send_keys('how to use webdriver')
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).send_keys('a').send_keys('x').key_up(Keys.CONTROL).perform()
