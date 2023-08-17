from lesson_17.code_for_testing import Human


class TestHuman:
    def setup_class(self):
        print('\nit`s setup class')

    def setup(self):
        print('\nsetup for each test')
        self.human = Human('Alfred', 78, 'grey')

    def test_check_age(self):
        self.human.grow()
        assert self.human.age == 79

    def test_check_hair_color(self):
        self.human.change_color('black')
        assert self.human.hair_color == 'black'

    def teardown(self):
        print('\nteardown for each test')

    def teardown_class(self):
        print('it`s teardown class')
