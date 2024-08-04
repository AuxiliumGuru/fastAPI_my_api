import math
class PasswordTest:
    '''
    A class to test the strength of a password based on its entropy.
    '''
    def __init__(self, password) -> None:
       self.password = password
    
    def __calculate_entropy(self) -> int:
      
      """
      Calculates the estimated entropy of a password.

      :param password: A string representing the password to be tested.

      :return A float representing the password's entropy in bits.
      """
      
      # Check for empty password
      if not self.password:
        return 0

      # Get the number of unique characters in the password
      possible_number_char = 64

      # Calculate entropy based on character set size and password length
      entropy = math.log2(possible_number_char ** len(self.password)) 

      return int(entropy)
    
    def __get_password_strength(self, entropy: float) -> tuple:
        '''
        Assigns a strength level to a password based on its entropy.
        '''
        # Define entropy ranges and corresponding strength levels
        strength_levels = {
            0: "Empty Password",
            25: "Very Weak",
            30: "Weak",
            40: "Moderate",
            60: "Strong",
            128: "Very Strong"  # Upper limit for practical password lengths
        }
        # Initialize variables to store the best match found so far
        best_match_entropy = -1
        best_match_level = "Unknown"

        # Assign strength level based on entropy
        for bits, level in strength_levels.items():
            if entropy >= bits and bits > best_match_entropy:
                best_match_entropy = bits
                best_match_level = level

        return entropy, best_match_level
    
    def test_password(self) -> tuple:
      '''
      Test the strength of a password and return the entropy and strength level.
      :return: A tuple containing the password's entropy and strength level.
      '''
      return self.__get_password_strength(self.__calculate_entropy())

