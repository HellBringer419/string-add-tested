class StringCalculator():
    def hello_world():
        return "Hello World"

    def add(numbers: str) -> int:
        [number1, number2] = [ int(number) for number in numbers.split(',')]
        return number1 + number2
