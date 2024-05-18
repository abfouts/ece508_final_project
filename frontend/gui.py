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


class GUI(Tk):
    """
    This class is the GUI for the Budget Spreadsheet Tracker. It is a simple
    Tkinter-based GUI.
    """

    def __init__(self, title: str, width: int, height: int, background_color: str):
        """
        This function initializes the GUI.
        """
        # Call the parent class constructor
        super().__init__()
        # Set the title of the window
        self.title(title)
        # Set the size of the window
        self.geometry(f"{width}x{height}")
        # Set the background color of the window
        self.configure(bg=background_color)


def gui():
    """
    This function is the main function of the GUI. It creates the GUI window and
    calls the other functions to create the GUI elements.
    """
    # Import the necessary modules

    # Create the GUI object
    app = GUI("Budget Spreadsheet Tracker", 800, 600, "white")

    app.mainloop()


if __name__ == "__main__":
    gui()
