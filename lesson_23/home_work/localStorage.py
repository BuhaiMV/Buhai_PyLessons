from selenium.webdriver import Chrome


class LocalStorage:
    def __init__(self, driver):
        self.driver = driver

    def getLocalStorage(self, name):
        #self.driver.get('https://lordofboards.com.ua/komiksy-i-knigi/')
        return self.driver.execute_script(f"return window.localStorage['{name}'];")
