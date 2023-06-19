import random
import string 

'''
    NOTE:
    This function is a disaster for moving to a 
    GUI. Furthermore, it is not well suited for 
    being a Object oriented function either. 
    You need to change the way this function
    processes the users choices, how will you 
    add choices? are you going to modify this 
    function and all the user interfaces that 
    will depend on it every time?
    You also have a nightmare of loops and IF
    statements which are going to make it hard 
    to debug this code.
    You should plan this out more, and see me about 
    modifying it for OO.
'''

class PasswordGenerator:
    def __init__(self):
        self.length = 0
        self.include_special = False  # set default values for each variable
        self.include_numbers = False
        self.include_normal = False

    def password_options(self):  # let the user choose what options they want
        while (  # loops until at least 1 category of characters is selected
            not self.include_special
            and not self.include_numbers
            and not self.include_normal
        ):
            while True:
                length_input = input(
                    "Enter the desired password length: "
                )  # get password length
                if length_input.isdigit():  # input validation
                    self.length = int(length_input)
                    break
                else:
                    print(
                        "Invalid input. Please enter a positive integer."
                    )  # input validation

            while True:
                include_special_input = input(
                    "Include special characters? (y/n): "
                ).lower()  # want special characters?
                if include_special_input in ["y", "n"]:  # input validation
                    self.include_special = (
                        include_special_input == "y"
                    )  # check the input
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")  # input validation

            while True:
                include_numbers_input = input(
                    "Include numbers? (y/n): "
                ).lower()  # want numbers?
                if include_numbers_input in ["y", "n"]:  # input validaton
                    self.include_numbers = (
                        include_numbers_input == "y"
                    )  # check the input
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")

            while True:
                include_normal_input = input(
                    "Include normal characters? (y/n): "
                ).lower()  # want lowercase + uppercase?
                if include_normal_input in ["y", "n"]:  # input validation
                    self.include_normal = include_normal_input == "y"  # check the input
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
            if (  # Checks whether no options were selected and gives error if so
                not self.include_special
                and not self.include_numbers
                and not self.include_normal
            ):
                print(
                    "At least one character type must be included. Please re-enter the details."
                )

    def generate_password(self):
        characters = ""

        if self.include_special:
            characters += string.punctuation
        if self.include_numbers:
            characters += string.digits
        if self.include_normal:
            characters += string.ascii_letters
        """if not characters:
            print("You need to select some characters!")
            self.password_options()
            self.generate_password()"""
        password = "".join(
            random.choice(characters) for i in range(self.length)
        )  # concatenate all the randomly generated characters from the valid characters
        return password
