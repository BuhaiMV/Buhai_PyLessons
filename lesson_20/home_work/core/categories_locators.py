from lesson_20.home_work.core.base_locators import BaseLocators


class CategoriesLocator(BaseLocators):
    def __init__(self):
        super().__init__()
        self.checkbox_new = ('xpath', "//span[text()='Новинка']/../span[1]")
        self.home = ('xpath', '//a[@class="header__logo-link"]')
