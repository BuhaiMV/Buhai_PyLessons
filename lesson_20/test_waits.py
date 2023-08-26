from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def test_01():
    driver = Chrome()
    driver.implicitly_wait(10)
    driver.get('https://google.com')
    search_field_locator = '//textarea[@type="search"]'
    element = driver.find_element(by='xpath', value=search_field_locator)
    element.send_keys('how to use webdriver')
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).send_keys('a').send_keys('x').key_up(Keys.CONTROL).perform()
