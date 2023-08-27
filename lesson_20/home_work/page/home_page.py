from lesson_20.home_work.page.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_catalog(self):
        locator = ('xpath', '//span[@class="site-menu__item"]//a[@href="/katalog/"]')
        element = self.wait_until_element_appears(locator)
        element.click()

    def go_to_novelty(self):
        locator = ('xpath', '//span[@class="site-menu__item"]//a[@href="/novinki/"]')
        element = self.wait_until_element_appears(locator)
        element.click()

    def go_to_kikstarter_deluxe(self):
        locator = ('xpath', '//span[@class="site-menu__item"]//a[@href="/kikstarter-deluxe/"]')
        element = self.wait_until_element_appears(locator)
        element.click()

    def go_to_sales(self):
        locator = ('xpath', '//span[@class="site-menu__item"]//a[@href="/znizhki/"]')
        element = self.wait_until_element_appears(locator)
        element.click()

    def go_to_payment_and_delivery(self):
        locator = ('xpath', '//span[@class="site-menu__item"]//a[@href="/oplata-i-dostavka/"]')
        element = self.wait_until_element_appears(locator)
        element.click()

    def go_to_exchange_and_return(self):
        locator = ('xpath', '//span[@class="site-menu__item"]//a[@href="/obmen-i-vozvrat/"]')
        element = self.wait_until_element_appears(locator)
        element.click()

    def check_text_in_catalog_header(self, value):
        locator = ('xpath', '//h1[@class="main-h"]')
        element = self.wait_until_element_appears(locator)
        assert element.text == value

    def check_catalog_tabs_nav(self):
        test_data = ['Хіти продажу', 'Розпродаж', 'Новинки']
        for i in range(len(test_data)):
            locator = ('xpath', f'//ul[@class="catalogTabs-nav-box"]//li[{i + 1}]')
            element = self.wait_until_element_appears(locator)
            assert element.text == test_data[i]
