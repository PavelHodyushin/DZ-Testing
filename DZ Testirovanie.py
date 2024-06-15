from testirovanie import Student
import unittest

class Test_student(unittest.TestCase):

    def setUp(self):
        self.student_1 = Student('Vasiya')
        self.student_2 = Student('Alesha')

    def test_walk(self):
        for i in range(10):
            self.student_1.walk()
        self.assertEqual(self.student_1.distance, 500,
                         f'Дистанции не равны[дистанция человека {self.student_1}] !=500')

    # def assertEqual(self, first, second, msg = None):
    #     """Завершится неудачей, если два объекта неравнозначны, как определено '=='оператор."""
    #     assertion_func = self._getAssertEqualityFunc(first, second)
    #     assertion_func(first, second, msg=msg)

    def test_run(self):
        for i in range(10):
            self.student_2.run()
        self.assertEqual(self.student_2.distance, 1000,
                         f'Дистанции не равны[дистанция человека {self.student_2}] !=1000')

    def student_competition(self):
        for i in range(10):
            self.student_1.walk()
            self.student_2.run()
            self.assertTrue(self.student_1.distance < self.student_2.distance,
                            f'[бегущий человек] должен преодолеть дистанцию больше, чем [идущий человек].')

if __name__ == '__main__':
    unittest.main()



