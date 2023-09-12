from selenium.webdriver import Chrome


class Cookies:
    def __init__(self, driver):
        self.driver = driver

    def getCookies(self, name):
        #self.driver.get('https://lordofboards.com.ua/komiksy-i-knigi/')
        return self.driver.get_cookie(name)
