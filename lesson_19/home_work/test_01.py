from lesson_19.home_work.lords_class import Lords
lords = Lords()


def test_01():
    lords.enter_page()
    lords.click_first_element_in_menu()
    lords.check_text_in_element('Комікси та книги', lords.find_catalog_header())


def test_02():
    lords.enter_page()
    lords.click_second_element_in_menu()
    lords.check_text_in_element('Настільні ігри всіх видів', lords.find_catalog_header())


def test_03():
    lords.enter_page()
    lords.click_third_element_in_menu()
    lords.check_text_in_element('Рольові ігри', lords.find_catalog_header())


def test_04():
    lords.enter_page()
    lords.type_text_to_search('звір')
    lords.check_search_result_contain_text('Звір')


def test_05():
    lords.enter_page()
    lords.type_text_to_search('дюна')
    lords.check_search_result_contain_text('Настільна гра Дюна: Імперіум (Dune: Imperium)')
