from lesson_20.home_work.page.base_page import BasePage
from lesson_20.home_work.core.catalog_locators import CatalogLocator


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CatalogLocator()

    def go_to_catalog(self):
        self.click_on_element(self.locators.catalog)

    def go_to_novelty(self):
        self.click_on_element(self.locators.novelty)

    def go_to_kikstarter_deluxe(self):
        self.click_on_element(self.locators.kikstarter_delux)

    def go_to_sales(self):
        self.click_on_element(self.locators.sales)

    def go_to_payment_and_delivery(self):
        self.click_on_element(self.locators.payment_and_delivery)

    def go_to_exchange_and_return(self):
        self.click_on_element(self.locators.exchange_and_return)

    def check_text_in_catalog_header(self, value):
        self.check_text_in_element(self.locators.text_in_catalog_header, value)

    def check_catalog_tabs_nav(self):
        test_data = ['Хіти продажу', 'Розпродаж', 'Новинки']
        for i in range(len(test_data)):
            element = self.wait_until_element_appears(self.locators.catalog_tabs_nav(i + 1))
            assert element.text == test_data[i]
