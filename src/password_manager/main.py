#!/usr/bin/env python3

from hash import HashAlgos
from manager import PasswordManager
import getpass


def main():
    algorithms = HashAlgos() # hash.py contains this class
    user = input("Main Username: ")
    password = getpass.getpass(prompt="Main Password: ")
    hash_type = input(
        "Choose the hash algorithm for your main password: (1) SHA256 (2) SHA512 (3) ARGON2 (4) BCRYPT: ")
    while hash_type not in algorithms.number_codes():
        print("Your algorithm of choice is not supported, please try again.")
        hash_type = input(
            "Choose the hash algorithm for your main password: (1) SHA256 (2) SHA512 (3) ARGON2 (4) BCRYPT: ")

    manager = PasswordManager(user) # TODO: What else should your Password Manager take in? Make changes to manager.py
    manager.run()


if __name__ == "__main__":
    main()
