from lesson_23.home_work.cookies import Cookies
from lesson_23.home_work.localStorage import LocalStorage



class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.cookies = Cookies(self.driver)
        self.localStorage = LocalStorage(self.driver)


    def open(self, page):
        self.driver.get(page)
