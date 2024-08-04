import random
class PasswordGenerator:
    '''
    A class to generate random passwords of a specified length.
    The password generated will contain alphanumeric characters (A-Z, a-z, 0-9), underscore (_), and period (.).
    '''

    def __init__(self, pass_len : int = 10) -> None:
        '''
        Initialize the PasswordGenerator class with a default password length of 10 characters.
        '''
        self.pass_len = pass_len

    def __generate_password(self, n: int) -> str:
        
        # Define ranges for alphanumeric characters: A-Z, a-z, 0-9, underscore (_), and period (.)
        char_ranges: list = [range(48, 58), range(65, 91), range(97, 123), [95], [46]]
        # Flatten the list of ranges into a single list of characters
        valid_chars: list = [chr(code) for r in char_ranges for code in r]
        # Generate the password
        random_password: list = [random.choice(valid_chars) for _ in range(n)]
        return ''.join(random_password)

    def get_pass(self) -> str:
        '''
        Gets randomly generated password of length pass_len.
        :return: A string representing the generated password.
        '''
        return self.__generate_password(self.pass_len)

