def test_go_to_catalog(home_page):
    home_page.go_to_catalog()
    home_page.check_text_in_catalog_header('Всі настільні ігри')


def test_go_to_novelty(home_page):
    home_page.go_to_novelty()
    home_page.check_text_in_catalog_header('Новинки')


def test_go_to_kikstarter_deluxe(home_page):
    home_page.go_to_kikstarter_deluxe()
    home_page.check_text_in_catalog_header('Kickstarter/Deluxe')


def test_go_to_sales(home_page):
    home_page.go_to_sales()
    home_page.check_text_in_catalog_header('Настільні ігри зі знижкою')


def test_go_to_payment_and_delivery(home_page):
    home_page.go_to_payment_and_delivery()
    home_page.check_text_in_catalog_header('Оплата і доставка')


def test_go_to_exchange_and_return(home_page):
    home_page.go_to_exchange_and_return()
    home_page.check_text_in_catalog_header('Обмін та повернення')


def test_catalog_tabs_nav(home_page):
    home_page.check_catalog_tabs_nav()
