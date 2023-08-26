from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


class Lords:
    driver = Chrome()

    first_element_in_menu_locator = '//div[@class="products-menu__title"]'
    second_element_in_menu_locator = '//li[@class="products-menu__item j-submenu-item"][2]'
    third_element_in_menu_locator = '//li[@class="products-menu__item j-submenu-item"][3]'
    catalog_header_locator = '//h1[@class="main-h"]'
    search_locator = '//input[@class="search__input"]'
    search_result_locator = '//ul[@class="search-results__list"]'

    def enter_page(self):
        self.driver.get('https://lordofboards.com.ua/')

    def find_first_element_in_menu(self):
        first_element_menu = self.driver.find_element(by='xpath', value=self.first_element_in_menu_locator)
        return first_element_menu

    def find_second_element_in_menu(self):
        second_element_menu = self.driver.find_element(by='xpath', value=self.second_element_in_menu_locator)
        return second_element_menu

    def find_third_element_in_menu(self):
        third_element_menu = self.driver.find_element(by='xpath', value=self.third_element_in_menu_locator)
        return third_element_menu

    def find_catalog_header(self):
        catalog_header = self.driver.find_element(by='xpath', value=self.catalog_header_locator)
        return catalog_header

    def find_search(self):
        search = self.driver.find_element(by='xpath', value=self.search_locator)
        return search

    def find_search_result(self):
        search_result = self.driver.find_element(by='xpath', value=self.search_result_locator)
        return search_result

    def click_first_element_in_menu(self):
        self.find_first_element_in_menu().click()

    def click_second_element_in_menu(self):
        self.find_second_element_in_menu().click()

    def click_third_element_in_menu(self):
        self.find_third_element_in_menu().click()

    def type_text_to_search(self, text):
        self.find_search().send_keys(text)

    @staticmethod
    def check_text_in_element(value, element):
        assert element.text == value

    def check_search_result_contain_text(self, value):
        self.driver.implicitly_wait(5)
        assert value in self.find_search_result().text
