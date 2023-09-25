import sys
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

class MainWindow(Gtk.ApplicationWindow):  # Class that inherits from Gtk.ApplicationWindow
    def __init__(self, *args, **kwargs):  # Constructor
        super().__init__(*args, **kwargs)  # Call GtkApplicationWindow constructor
        # Things will go here

class MyApp(Gtk.Application):  # Class that represents the app
    def __init__(self, **kwargs):  # Constructor
        super().__init__(**kwargs)  # Call GtkApplication constructor
        self.connect('activate', self.on_activate)  # Initialize the app with 'activate' signal

    def on_activate(self, app):
        self.win = MainWindow(application=app)  # Creates an instance of the window
        self.win.present()  # Show the window

app = MyApp(application_id="com.example.GtkApplication")  # Creates an instance of the app
app.run(sys.argv)  # Run the code
