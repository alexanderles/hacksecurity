# Password Manager

## Disclaimer

The purpose of this project is to teach you about the thought process of creating a password manager, and not to replace a real, tested password manager. To avoid the risks associated with making inaccurate assumptions about the security of this program, please use a reputable industry solution, such as [Bitwarden](https://bitwarden.com/)

## What is a password manager?

A password manager is a tool that anyone can use to store, generate, and retrieve passwords from.

## Why is this important?

By taking the responsibility of memorizing different passwords away from you (the user!), a password manager greatly increases your security hygiene by reducing the risk of password reuse and choosing poor quality passwords. Users are less likely to use easily-guessed passwords for multiple important accounts.

## Creating a password manager

A basic password manager should be able to store and retrieve passwords for an authenticated user. This means when the program is started, a user has to be able to "log in" to the manager before doing anything.

When storing the root password, we should take care not to store the password in plaintext. This means we should never store the password as-is, so that if our password manager is hacked, the password stored isn't readable/usable. Instead, what we'll want to do is convert that password into something that can't be converted back to the password. We'll want to hash the password and store that hash! 

You might be wondering then, how will the pass manager check if a given password matches the root password?

When authenticating a user, we will take the password given and hash it, then compare it with the hash of the root password that we stored earlier on. If the hashes match, the passwords match! Our password is still protected, and attackers won't find anything useful. Please see the section below for more details on hashing.

When storing a password, we will encrypt the given password and store the encrypted version. We don't want to store our passwords in plaintext, but we can't use hashing, because otherwise we won't have a correct original password to return! Please see the section below for more details on encryption.

When retrieving a password, we will decrypt the encrypted password, and return the correct original password.

*For encryption, we'll need to generate a encryption/decryption key using a key generation algorithm with strong entropy. For this, we can use the Fernet library <https://cryptography.io/en/latest/fernet/> or the PBKDF2 library <https://www.dlitz.net/software/python-pbkdf2/>

## How does hashing work?

Data that is hashed cannot be unhashed; hashing is one-way and usually creates a code (hash) that is much shorter than the original message. 

The hash is usually used as a way to identify (fingerprint) the original message.

When you log in to a website, your password "a" is securely transmitted to website, which salts + hashes it into "b", then compares to a stored hash from when you first created your account. 

"b" can NOT be turned back into "a".

## How does encryption work?

Data that is encrypted is designed to be decrypted by only legitimate parties; you can have asymmetric or symmetric encryption. 

Asymmetric uses two keys, where each key can decrypt the other. Symmetric uses one key for encryption and decryption.

When a password manager stores your password "a", it encrypts it with an encryption key (that is kept secure!) and turns it into "b". When you ask the manager to retrieve your password, the manager decrypts "b" back into your password "a" before returning. 

"b" CAN be turned back into "a".

## How does this all differ from an ideal password manager?

 - Authentication serves a slightly different purpose in true password managers. The main password isn't just a way for the program to tell that you are an authorized user; it's also used to generate the encryption key itself.
 - Password managers actually shouldn't store the main password (even hashed) and instead, should store a salt (for the main user) and derive the encryption key using the salt + the main password when you pass it in, each time you log in. 
  - This means your manager doesn't need to know your main password or the encryption key, all it needs to know is what hashing algorithm and salt to use each time you authenticate.
 - Initialization Vectors should also be used when encrypting/decrypting data. For simplicity, we can leave that as a stretch goal. Please read this for more details: <https://www.bluespace.tech/blog/evolution-of-password-manager/second-generation-password-manager.html>

### Recommended Requirements

To follow along in this tutorial we recommend:

- intermediate/advanced knowledge of Python and how to use packages/libraries
- intermediate knowledge of cryptography and the ability to process relevant documentation
- the ability to know when to ask for help

### Windows Users

To install the necessary modules:
`pip install -r requirements.txt`
To run the file:
In the root project folder, run `python src/password_manager/main.py`

### MacOS/Linux Users

To install the necessary modules:
`python3 -m pip install -r requirements.txt`
To run the file:
In the root project folder, run `python3 ./src/password_manager/main.py`

### Exercises
- Make the label case-insensitive
- Allow the user to change the password for a label, if they confirm.
- Instead of authenticating the user every time they have to store/retrieve a password, make it possible for them to stay authenticated for 1, 5, and 10 minutes (they should be able to select which option).
- Implement a failed login timeout; if someone fails the login x times, they are locked out for y amount of time
 - Make this time exponential! If x increases, increase y exponentially to hinder brute-forcing.
- Implement an (authenticated) ultimate reset which prompts the user for a new main password (or generates it automatically) and wipes all previous data

#### Functional Milestones
 
1. Accept a main password as user input.
1. Implement salting + hashing on your main password before storing it.
1. Generate a secure encryption/decryption key.
1. Encrypt your stored passwords.
1. Decrypt your stored passwords before returning them to the user.

#### Bonus Milestones

- [OPTIONAL] Create the encryption/decryption key by hashing the main password and a saved salt. You will end up NOT having to save the key nor the main password in any form, not even hashed!
- [OPTIONAL] Implement password generation; the user should be able to request a strong password of length x-y, containing (or excluding) the lowercase alphabet, uppercase alphabet, numbers, and symbols/special characters.
- [OPTIONAL] Instead of allowing the user to create their own main password, generate it at the beginning for them to save and use later on.
