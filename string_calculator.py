import sys
from negative_number_error import NegativeNumberException


class StringCalculator:
    def add(numbers: str) -> int:
        if numbers == "":
            return 0
        else:
            delimiters = {",", "\n"}  # Set
            if numbers.startswith("//"):
                delimiters.add(numbers[2])
                numbers = numbers.strip(f"//{numbers[2]}\n")

            # splitting manually
            # Keep a buffer to store all characters before delimiters
            # have a list to collect all numbers (after splitting using dilimiters)
            buffer = ""
            numbersArray = list()
            for char in numbers:
                if char in delimiters:
                    numbersArray.append(int(buffer))
                    buffer = ""
                else:
                    buffer += char

            # flush all remaining in buffer to the array
            if buffer != "":
                numbersArray.append(int(buffer))

            negativeNumbers = list()
            for number in numbersArray:
                if number < 0:
                    negativeNumbers.append(number)

            if len(negativeNumbers) > 0:
                raise NegativeNumberException(negativeNumbers)

            sum = 0
            for number in numbersArray:
                sum += number
            return sum


if __name__ == "__main__":
    print(sys.argv[1])
    print(type(sys.argv[1]))
    print(StringCalculator.add(sys.argv[1]))
