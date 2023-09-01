from lesson_20.core.base_locators import BaseLocator


class DashboardLocators(BaseLocator):
    def __init__(self):
        super().__init__()
        self.banner = ('xpath', '//li[@class="frontCategories-i swiper-slide-active"]//a[@href="/komiksy/"]')

