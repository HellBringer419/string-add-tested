import unittest
from string_calculator import StringCalculator

class FirstTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(StringCalculator.add("1,2"), 3)
    
    def test_add_1(self):
        self.assertEqual(StringCalculator.add("1"), 1)
    
    def test_add_0(self):
        self.assertEqual(StringCalculator.add(""), 0)

if __name__ == '__main__':
    unittest.main()
