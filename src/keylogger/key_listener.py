from pynput import keyboard
from database import MockDatabaseDAO

'''
    A key listener with customizable listening properties through the on_press and on_release callback functions.
'''


class KeyListener():

    '''
        Constructs an instance of this class, taking in a database as a field.
    '''

    def __init__(self, database_connection):
        self.database = database_connection
        self.listener = keyboard.Listener(
            on_press=self.on_press, on_release=self.on_release)
        self.listener.start()
        self.listening = True

    '''
        Defines the behavior when a key is pressed.
    '''

    def on_press(self, key):
        self.database.write(key)

    '''
        Defines the behavior when a key is released. Note: When a key is typed, it is both pressed and released. 
        Theoretically, you can not use this function at all and just use on_press. But if you want more fine tuned control, you can 
        make edits here too.
    '''

    def on_release(self, key):
        if key == keyboard.Key.esc:  # Stop listener when the Esc key is pressed
            strokes = self.database.query()
            print("Printing keystrokes...")
            for stroke in strokes:
                print(stroke.key_pressed)
            self.listening = False

    '''
        Stops the listener from listening.
    '''

    def stop_listening(self):
        keyboard.Listener.stop(self.listener)
