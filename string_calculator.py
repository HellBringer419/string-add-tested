class StringCalculator():
    def hello_world():
        return "Hello World"

    def add(numbers: str) -> int:
        numbersArray = [ int(number) for number in numbers.split(',')]
        number1 = 0
        number2 = 0
        if numbersArray.__len__() == 2:
            [number1, number2] = numbersArray
        return number1 + number2
