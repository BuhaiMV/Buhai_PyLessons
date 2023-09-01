import time


def test_go_to_books_and_comix(dashboard):
    dashboard.go_to_comix_and_books()
    time.sleep(2)


def test_search(dashboard):
    dashboard.write_to_search('pathfinder')

