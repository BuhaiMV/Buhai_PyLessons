#1
from lesson_23.home_work.basePage import BasePage
from selenium.webdriver import Chrome
driver = Chrome()

basePage = BasePage(driver)

basePage.open('https://takagra.com.ua/')
print(basePage.cookies.getCookies('uuid'))
print(basePage.localStorage.getLocalStorage('inlineSVGrev'))

