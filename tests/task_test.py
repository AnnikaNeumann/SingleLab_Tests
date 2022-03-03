import unittest
from src.task import Tasks

class TaskTest(unittest.TestCase):
    def setUp(self):
        self.wash_dishes = Tasks("wash dishes", 10)
        self.cook_dinner = Tasks("cook dinner", 40)
        # self.clean_windows = Tasks("")



    def test_wash_dish_preferred_cook_dinner(self):
        self.assertEqual(True, Tasks.task_decider(self.wash_dishes, self.cook_dinner))
    def test_cook_dinner_not_preferred_wash_dishes(self):
        self.assertEqual(False, Tasks.task_decider(self.cook_dinner, self.wash_dishes))