class StringCalculator():
    def add(numbers: str) -> int:
        if numbers is '':
            return 0
        else:
            # splitting manually
            # Keep a buffer to store all characters before delimiters 
            # have a list to collect all numbers (after splitting using dilimiters)
            buffer = ''
            numbersArray = list()
            for char in numbers:
                if char is ',' or char is '\n':
                    numbersArray.append(int(buffer))
                    buffer = ''
                else:
                    buffer += char
            
            # flush all remaining in buffer to the array
            if buffer is not '':
                numbersArray.append(int(buffer))
            sum = 0
            for number in numbersArray:
                sum += number
            return sum
