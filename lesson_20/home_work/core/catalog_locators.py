from lesson_20.home_work.core.base_locators import BaseLocators


class CatalogLocator(BaseLocators):
    def __init__(self):
        super().__init__()
        self.text_in_catalog_header = ('xpath', '//h1[@class="main-h"]')
        self.catalog_tabs_nav = lambda i: ('xpath', f'//ul[@class="catalogTabs-nav-box"]//li[{i}]')
