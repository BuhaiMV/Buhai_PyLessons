import time


def test_go_to_product_page_and_back(dashboard):
    category_page = dashboard.go_to_comix_and_books()
    product_page = category_page.return_to_dashboard_page()
    time.sleep(2)
