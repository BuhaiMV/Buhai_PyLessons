from lesson_17.home_work.home_work_test.adapter_for_test import CsvManager

class TestManager:
    def setup(self):
        self.csvManager = CsvManager()
    def test_check_add_line(self):
        self.csvManager.add_line({'first_name': 'Adam', 'last_name': "First", 'age': 45, 'gender': 'Male', 'salary': 60000})
        assert self.csvManager.count_lines() == 4

    def test_check_delete_line(self):
        self.csvManager.delete_line()
        assert self.csvManager.count_lines() == 3