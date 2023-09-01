from lesson_20.page.base_page import BasePage
from lesson_20.page.product_page import ProductPage


class CategoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def return_to_dashboard_page(self):
        locator = ('xpath', '//div[@class="catalogCard-view"]')
        self.click_on_element(locator)
        return ProductPage(self._driver)
