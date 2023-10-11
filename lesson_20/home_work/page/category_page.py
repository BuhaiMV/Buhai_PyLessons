from lesson_20.home_work.page.base_page import BasePage
from lesson_20.home_work.page.home_page import HomePage
from lesson_20.home_work.core.categories_locators import CategoriesLocator

class CategoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CategoriesLocator()

    def go_to_home_page(self):
        self.click_on_element(self.locators.home)
        return HomePage(self._driver)

    def filter_new(self):
        self.click_on_element(self.locators.checkbox_new)