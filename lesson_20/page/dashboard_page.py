from lesson_20.page.base_page import BasePage
from lesson_20.page.category_page import CategoryPage
from lesson_20.core.Locators import DashboardLocators


class Dashboard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = DashboardLocators()

    def go_to_comix_and_books(self):
        self.click_on_element(self.locators.go_to_comix_and_books_locator)
        return CategoryPage(self._driver)

    def go_to_login_form(self):
        self.click_on_element(self.locators.login)

    def write_to_search(self, message):
        self.send_keys_into_field(self.locators.search, message)
        self.wait_until_element_appears(self.locators.first_search_result)
        self.press_enter(self.locators.search)
