class StringCalculator():
    def add(numbers: str) -> int:
        if numbers == '':
            return 0
        else:
            numbersArray = [int(number) for number in numbers.split(',')]
            sum = 0
            for number in numbersArray:
                sum += number
            return sum
