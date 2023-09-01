class BaseLocators:
    def __init__(self):
        self.catalog = ('xpath', '//span[@class="site-menu__item"]//a[@href="/katalog/"]')
        self.novelty = ('xpath', '//span[@class="site-menu__item"]//a[@href="/novinki/"]')
        self.kikstarter_delux = ('xpath', '//span[@class="site-menu__item"]//a[@href="/kikstarter-deluxe/"]')
        self.sales = ('xpath', '//span[@class="site-menu__item"]//a[@href="/znizhki/"]')
        self.payment_and_delivery = ('xpath', '//span[@class="site-menu__item"]//a[@href="/oplata-i-dostavka/"]')
        self.exchange_and_return = ('xpath', '//span[@class="site-menu__item"]//a[@href="/obmen-i-vozvrat/"]')
