#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Budget Spreadsheet Tracker
ECE508 - Python & Scripting Wksp
Final Project
Spring 2024 Jean Paul Mugisha
April 21, 2024
Abram Fouts, Niko Nikolov
--------------------------------
This is the GUI for the Budget Spreadsheet Tracker. It is a simple Tkinter-based
GUI. https://docs.python.org/3/library/tkinter.html
"""

# Import the necessary modules
from tkinter import Tk, Label
from tkinter import ttk


class GUI:
    """
    This class is the GUI for the Budget Spreadsheet Tracker. It is a simple
    Tkinter-based GUI.
    """

    def __init__(self, root: Tk):
        """
        This function initializes the GUI.
        """
        # Set the title of the GUI window
        root.title("Budget Spreadsheet Tracker")
        # Set the size of the GUI window
        root.geometry("800x600")

        def create_label(text: str, x: int, y: int):
            """
            This function creates a label with the given text and position.
            """
            # Create the label
            label = Label(root, text=text)
            # Set the position of the label
            label.place(x=x, y=y)

        # Run the GUI
        root.mainloop()


def gui():
    """
    This function is the main function of the GUI. It creates the GUI window and
    calls the other functions to create the GUI elements.
    """
    # Import the necessary modules

    # Create the GUI window
    root = Tk()
    # Create the GUI object
    app = GUI(root)
    app.create_label("Hello World!", 100, 100)


if __name__ == "__main__":
    gui()
