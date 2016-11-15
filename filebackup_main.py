# Python Ver:   3.5.2
#
# Author:   Samuel Sanseri
#
# Purpose:  Filebackup Demo. Demonstrating OOP, Tkinter GUI module,
#           using Tkinter Parent and Child relationships.
#
# Tested OS:    This code was written and tested with Windows 10
##
##Scenario: You recently created a script that will check a folder for new or modified files, and then
##copy those new or modified files to another location. You also created a UI that makes using the script
##easier and more versatile.
##Users are reporting issues with the current system you've made. Specifically, they are having to manually
##initiate the 'file check' script at the same time each day. Because they aren't doing this at the EXACT
##same time each day, some files that were edited right around the time the script was meant to be run were
##missed, and weren't copied to the outgoing files destination.
##This means you will have to provide for recording the last time the 'file check' process was performed,
##so that you can be sure to cover the entire time period in which new or edited files could occur.
##To do this, you will need to create a database with a table that can store the date and time of the last 'file
##check' process. That way, you can use that date/time as a reference point in terms of finding new or
##modified files.
##As part of this project, the users are asking that their UI display the date and time of the last 'file check'
##process.
##You have been asked to implement this functionality. This means that you will need to
##• create a database and a table
##• modify your script to both record date/time of 'file check' runs and to retrieve that data for use in
##the 'file check' process, and
##• modify the UI to display the last 'file check' date/time
##

from tkinter import *
import tkinter as tk

# Be sure to import our other modules
# so we can have access to them
import filebackup_gui
import filebackup_func

# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,300) #(Height, width
        self.master.maxsize(500,300)
        # This CenterWindow method will center our app on the user's screen
        filebackup_func.center_window(self, 500, 300)
        self.master.title("The Tkinter filebackup Demo")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: filebackup_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module,
        # keeping your code compartmentalized and clutter free
        filebackup_gui.load_gui(self, master)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
