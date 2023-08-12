from lesson_16.factory_example.drivers.browser_base_class_example import Browser
from lesson_16.factory_example.drivers.chrome_browser import ChromeBrowser
from lesson_16.factory_example.drivers.firefox_browser import FireFox


class BrowserFactory:
    def __init__(self):
        self.last_browser = None

    def get_browser(self, name):
        self.last_browser = name
        if name == 'chrome':
            return ChromeBrowser()
        elif name == 'firefox':
            return FireFox()
        else:
            raise Exception('wrong browser type')


our_browser_factory = BrowserFactory()
chrome1 = our_browser_factory.get_browser('chrome')
chrome2 = our_browser_factory.get_browser('chrome')
firefox1 = our_browser_factory.get_browser('firefox')
print()