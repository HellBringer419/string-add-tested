import unittest
from random import randint
from string_calculator import StringCalculator

class FirstTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(StringCalculator.add("1,2"), 3)
    
    def test_add_1(self):
        self.assertEqual(StringCalculator.add("1"), 1)
    
    def test_add_0(self):
        self.assertEqual(StringCalculator.add(""), 0)

class SecondTest(unittest.TestCase):

    def test_add_n(self):
        # To simulate unknown amount of numbers, we generate a random whole number
        # then used that to pass arguments as "0, 1, ... (n-1)" to add function
        # random_number = randint(0, 500)
        random_number = 2
        argument_string = ""
        for i in range(0, random_number):
            if(i == random_number-1):
                argument_string += str(i)
            else:
                argument_string += str(i) + ","
        
        ## sum of (n-1) natural numbers: n * (n-1) / 2
        expected_result = int(random_number * (random_number - 1) / 2)

        self.assertEqual(StringCalculator.add(argument_string), expected_result)

if __name__ == '__main__':
    unittest.main()
