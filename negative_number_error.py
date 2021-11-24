class NegativeNumberException(Exception):
    """ Exception raised when you try adding negative numbers in String Calculator 
    Attributes:
        negative_numbers -- list of negative numbers found in the 'numbers' 
    """
    def __init__(self, negative_numbers):
        self.message = f"negative not allowed {negative_numbers}"
        super().__init__(self.message)
