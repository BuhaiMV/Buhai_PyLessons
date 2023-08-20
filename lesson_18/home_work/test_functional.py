import pytest

test_data = {'params': 'line, expected',
             'data': [
                 ({'first_name': 'Adam', 'last_name': "First", 'age': 45, 'gender': 'Male', 'salary': 60000}, 4),
                 ({'first_name': 'Tom', 'last_name': "Cryiz", 'age': 99, 'gender': 'Male', 'salary': 100000}, 4)]}


@pytest.mark.parametrize(
    test_data['params'], test_data['data']
)
@pytest.mark.regression
def test_check_add_line(manager, delete_line, line, expected):
    manager.add_line(line)
    assert manager.count_lines() == expected


@pytest.mark.smoke
def test_check_delete_line(manager, add_line):
    manager.delete_line()
    assert manager.count_lines() == 3
