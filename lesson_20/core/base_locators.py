class BaseLocator:
    def __init__(self):
        self.login = ('xpath', '//a[@class="userbar__button __active"]')
        self.catalog = ('xpath', '//a[text()="Каталог"]')
        self.go_to_comix_and_books_locator = (
        'xpath', '//div[@class="products-menu__title"]//a[@href="/komiksy-i-knigi/"]')
        self.search = ('xpath', '//input[@class="search__input"]')
        self.first_search_result = ('xpath', '//li[@class="search-results__item"]')
