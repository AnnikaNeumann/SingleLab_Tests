import unittest
from src.task import Tasks

class TaskTest(unittest.TestCase):
    def setUp(self):
        self.wash_dishes = Tasks("wash dishes", 10)
        self.cook_dinner = Tasks("cook dinner", 40)
        self.clean_windows = Tasks("clean windows", 30)


#Tests to compare wash dishes and cook dinner
    def test_wash_dish_preferred_cook_dinner(self):
        self.assertEqual(True, Tasks.task_decider(self.wash_dishes, self.cook_dinner))
    def test_cook_dinner_not_preferred_wash_dishes(self):
        self.assertEqual(False, Tasks.task_decider(self.cook_dinner, self.wash_dishes))
#Tests to compare clean windows and wash_dishes
    def test_clean_windows_preferred_wash_dishes(self):
        self.assertEqual(True, Tasks.task_decider(self.clean_windows, self.wash_dishes))
    def test_wash_dishes_not_preferred_clean_windows(self):
        self.assertEqual(False, Tasks.task_decider(self.wash_dishes, self.clean_windows))
#CLEAN WINDOWS VS COOK DINNER
    def test_cook_dinner_preferred_clean_windows(self):
        self.assertEqual(True, Tasks.task_decider(self.cook_dinner, self.clean_windows))
    def test_clean_windows_not_preferred_cook_dinner(self):
        self.assertEqual(False, Tasks.task_decider(self.clean_windows, self.cook_dinner))

