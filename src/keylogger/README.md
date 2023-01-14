# Simple Python Key Logger

## Disclaimer

This source code is for educational purposes only. By participating in this workshop you agree to not use this code, use the ideas learned from this workshop, and extend this code in a malicious manner.

## What is a key logger?

A key logger is a program that covertly listens for key presses, used for the theft of confidential information like emails, passwords, and other sensitive information. Key loggers usually run as a background process transmitting the key presses of a victim's computer to an attacker's database/computer.

## Why is this important?

Knowledge of the existence and inner workings of a key logger will teach you about the risks of running untrusted code and the capabilities of programming exploits. Learning to think like a hacker is crucial to developing defensive security skills.

## Creating a key logger

This project uses the python module pynput for global keyboard hooks. Please refer to the documentation here: https://pynput.readthedocs.io/en/latest/index.html

### Recommended Requirements

To follow along in this tutorial we recommend:

- basic knowledge of Python
- readiness to self-troubleshoot
- having the ability to ask for help when really stuck

### Windows Users

To install the necessary modules:
`pip install -r requirements.txt`
To run the file:
In the root project folder, run `python src/keylogger/main.py`

### MacOS/Linux Users

To install the necessary modules:
`pip3 install -r requirements.txt`
To run the file:
In the root project folder, run `./src/keylogger/main.py`

### Exercises

#### Functional Milestones

1. Read main.py
1. First implement a mock database in mockdatabase.py. A database requires reading and writing is a way of storing information in an encapsulated manner. Consider how you want to store the key presses.
1. Hint: Order is important and you want to store multiple things, what data structure comes to mind?
1. Hint: What field do you want this class to have?
1. Hint: Start with the constructor of the database and have the methods work off the fields defined in the constructor.
1. Bonus: If you want to store more than one piece of information per key press, what data structure would be best?
1. Reasoning: A mock database simulates a real database. A malicious user would be able to track your keystrokes but without a way to view the information, they will not be able to access your keystroke data. A script that uploads the information to a database would be perfect to steal.
1. Attach the database to the key listener.
1. Hint: This can be done in the Key Listener constructor, what parameter should this class take?
1. Reasoning: attaching a database object as a field will allow the key listener methods/functions to work with the database.
1. Implement the key listener on press callback. This callback function describes what you want the listener to do when a key press happens, meaning this function runs when a key is pressed.
1. Hint: we want the listener to upload the information to the database.
1. Implement the key listener on release callback to stop the listener when the ESC key has been released. This callback function describes what you want the listener to do when a key is released (after pressing).
1. Hint: we want some kind of way to stop the listening like a kill switch while testing
1. Test your code by uncommenting the main function!

#### Bonus Milestones

1. Enhance your database by storing more information (date, special characters, hot keys)
1. Add query functions based on date/time pressed
1. Add query functions that splits on a specific character input. Hint: An "Enter" key would be useful to split upon since users usually press "Enter" in between username and passwords.
1. _ADVANCED_ Start local SQL server, create a new sql_database.py that can be used to store key entries into the SQL server.
