import unittest
from string_calculator import StringCalculator

class FirstTest(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(StringCalculator.hello_world(), 'Hello World')
    
    def test_add(self):
        self.assertEqual(StringCalculator.add("1,2"), 3)

if __name__ == '__main__':
    unittest.main()
