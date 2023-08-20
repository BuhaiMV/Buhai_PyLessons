import pytest
from lesson_18.code_for_testing import Human

test_data = {'params': 'color, expected',
             'data': [('black', 'black'), ('white', 'white')],
             'ids': ['change to black', 'change to white']}

'''
@pytest.mark.xfail(reason='failed due to know bug @83483289')
def test_change_hair_color():
    human = Human('Alnert', 80, 'pink')
    human.change_color('black')
    assert human.hair_color == 'black'''


@pytest.mark.parametrize(
    test_data['params'], test_data['data'], ids=test_data['ids']
)
def test_change_hair_color2(human, color, expected):
    human.change_color(color)
    assert human.hair_color == expected


@pytest.mark.smoke
@pytest.mark.regression
def test_age_grow(human):
    human.grow()
    assert human.age == 26


def test_check_raise_for_exception(human):
    with pytest.raises(Exception):
        human.change_color('pink')
    