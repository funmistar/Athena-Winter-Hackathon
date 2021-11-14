# Hi markers, this was out first ever attempt at a kivy file, we are extremely proud of the progress we were able to make in less than 48 hours
import kivy
from kivy.app import App
from kivy.uix.label import Label

# Replace this with your
# current version
kivy.require('1.11.1')

# Defining a class
class MyFirstKivyApp(App):
    # Function that returns
    # the root widget
    def build(self):
        # Label with text Hello World is
        # returned as root widget
        return Label(text ="Hello World !")


# Here our class is initialized
# and its run() method is called.
# This initializes and starts
# our Kivy application.
MyFirstKivyApp().run()