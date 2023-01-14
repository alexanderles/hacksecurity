import getpass
from enum import Enum

# Class which represents our password manager, which we can use to authenticate ourself (log in) and store/retrieve passwords.
class PasswordManager():
    """

    For any methods with the keyword pass in them, please place the code you'd like to run above the statement, and remove pass completely after doing so.

    """

    def __init__(self, user,):
        """
        Add other fields for data you think your password manager will need to store.
        
        :param user: the username for the main user
        """
        self.username = user
        self.password_storage = {
            "gmail": "plaintext_password"
        }

    def hash_input(self, input, salt, hash_algo):
        """
        Returns the hash for the given input + salt using the given hashing algorithm.
        """
        # TODO: How will you hash your input before returning it?
        pass

    def encrypt(to_encrypt,):
        """
        Encrypts the given input.
        """
        pass

    def decrypt(to_decrypt,):
        """
        Decrypts the given input.
        """
        pass

    def save_password_for_label(self):
        """
        Stores the given password, associating it with the given label.
        """
        # FIXME: add encryption so that the password doesn't get stored in plaintext!
        label = input("What account are you trying to store this password for? ")
        password = getpass.getpass("Please enter the associated password to store: ")
        # FIXME: what should happen if you're trying to store the password for a label that's already taken?
        self.password_storage[label] = password
        print(f"Password stored for account {label}.")
        pass

    def retrieve_password_for_label(self):
        """
        Retrieves password for the given label.
        """
        # FIXME: add decryption so that the encrypted password can be decrypted!
        label = input("What account are you trying to retrieve the password for? ")
        print(f"Your password for account {label} is: {self.password_storage[label]}")

    def authenticate(self, ):
        """
        Authenticate the current user, essentially logging them in. You may need to ask the current user some questions!
        """
        return True # FIXME

    def run(self):
        """
        For our simple password manager, we want to be able to authenticate (log in), save passwords, and retrieve passwords.
        """
        while True:
            if self.authenticate() == True:
                number = input("-------------Please select from the following options-------------\n1) Save Password\n2) Retrieve Password\n3)Reset Main Password\n4)Reset All\n")
                if number == "1":
                    # FIXME: add encryption so that the password doesn't get stored in plaintext!
                    self.save_password_for_label()
                elif number == "2":
                    # FIXME: add decryption so that the encrypted password can be decrypted!
                    self.retrieve_password_for_label()
                    pass
                elif number == "3":
                    pass
                elif number == "4":
                    pass
                else:
                    print("The input you provided is not a supported option. Please try again!")
        return
