from passGen import PasswordGenerator
from passTest import PasswordTest


def main():
    
    ## Password Generator
    passGen = PasswordGenerator(10)
    print(passGen.get_pass())


    ## Passwrord Test
    # Get password input
    password = input("Enter your password: ")

    # Calculate and print password entropy
    password_test = PasswordTest(password)
    tess_pass = password_test.test_password()
    print(f"Password Entropy: {tess_pass[0]} bits\nStrength Level: {tess_pass[1]}")

    def countElements(lst):
        # Count the occurrences of each element in the list
        count_dict = {}
        for element in lst:
            count_dict[element] = count_dict.get(element, 0) + 1
        
        # Filter the elements with even count and remove duplicates
        result = []
        for element, count in count_dict.items():
            if count % 2 == 0 and element not in result:
                result.append(element)
        
        return result

if __name__ == "__main__":
    main()