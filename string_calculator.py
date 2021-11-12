class StringCalculator():
    def add(numbers: str) -> int:
        numbersArray = numbers.split(',')
        number1 = 0
        number2 = 0
        if numbersArray.__len__() == 2:
            [number1, number2] = [ int(number) for number in numbersArray]
        if numbersArray.__len__() == 1:
            [number1] = numbersArray
        return number1 + number2
