import datetime
from dataclasses import dataclass


'''
    Represents a connection to a mock database from which you can read (query) and write to. 
    DAO = Data Access Object, a technique to abstract a database into an object with defined functions.
'''


class MockDatabaseDAO:

    '''
        Initalizes the mock database to empty.
    '''

    def __init__(self) -> None:
        self.keystrokes = []

    '''
        Writes to the database, storing information.
    '''

    def write(self, key_pressed):
        key_dict = {
            "key": key_pressed,
            "timestamp": datetime.datetime 
        }
        self.keystrokes.append(key_dict)

    '''
        Read every entry from the database with no formatting.
    '''

    def query(self):
        return self.keystrokes

    '''
        Read entries from the database from a certain date.
    '''

    def query_by_date(self, date_requested):
        return filter(lambda stroke: stroke.timestamp.date == date_requested, self.keystrokes)
