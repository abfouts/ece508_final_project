#!python
# -*- coding: utf-8 -*-
"""

ECE508 - Python & Scripting Wksp
Final Project - Budget Spreadsheet Tracker
Spring 2024 Jean Paul Mugisha
Abram Fouts, Niko Nikolov
--------------------------------
This is the GUI for the Budget Spreadsheet Tracker.
It is a simple Tkinter-based GUI.
https://docs.python.org/3/library/tkinter.html
"""

# Import the necessary modules
import tkinter as tk
from tkinter import Button, Label, Canvas, filedialog
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import csv_reader as my_csv_reader
import os

matplotlib.use("TkAgg")


class Backend:
    """Backend class."""

    def __init__(self, csv_path=None):
        """Initialize the backend."""
        self.csv_path = csv_path
        self.csv_reader = my_csv_reader.CSVReader(self.csv_path)
        self.csv_balance_per_day = self.csv_reader.get_balance_per_day()
        self.csv_ten_highest_transactions = self.csv_reader.get_ten_highest_transactions()

    def upload_csv_file(self):
        """Upload a CSV file."""
        print("Upload a CSV file.")
        self.csv_path = filedialog.askopenfilename(initialdir = os.getcwd())

    def reset(self):
        """Reset the application."""
        print("Reset the application.")

    def generate_report(self):
        """Generate a report."""
        print("Generate a report.")

    def add_new_transaction(self):
        """Add a new transaction."""
        print("Add a new transaction.")

    def get_balance_per_day(self):
        """Get the balance per day."""

        self.csv_balance_per_day = self.csv_reader.get_balance_per_day()

        return self.csv_balance_per_day

    def get_ten_highest_transactions(self):
        """Get the ten highest transactions."""

        self.csv_ten_highest_transactions = self.csv_reader.get_ten_highest_transactions()

        return self.csv_ten_highest_transactions

    def update_csv_path(self, new_path):
        """Update the CSV path."""
        self.csv_path = new_path


class Plot(Canvas):
    """Chart class."""

    def __init__(self, balance_per_day, ten_highest_transactions, *args, **kwargs):
        """Initialize the charts"""
        super().__init__(*args, **kwargs)

        # Balance array
        self.balance = balance_per_day
        # Transactions array
        self.transactions = ten_highest_transactions
        # Configure the background color
        self.configure(bg="#adbce6")

        # Create a matplotlib figure1
        self.transaction_df = pd.DataFrame(self.transactions)
        # Create a Figure object
        self.figure1 = Figure(figsize=(6, 5), dpi=120)
        # Create an Axes object
        self.ax1 = self.figure1.add_subplot(111)
        # Plot the data
        self.bar1 = FigureCanvasTkAgg(self.figure1, self)
        # Add the toolbar
        self.bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        # Group the data by category
        print(self.transaction_df)
        self.ax1.bar(self.transaction_df["date"],
                     self.transaction_df["amount"])
        # Add a title to the plot
        self.ax1.set_title("10 Highest Transactions")
        self.ax1.set_facecolor('#cfcfcf')

        # Create a matplotlib figure2
        self.balance_df = pd.DataFrame(self.balance)
        # Create a Figure object
        self.figure2 = Figure(figsize=(5, 4), dpi=120)
        # Create an Axes object
        self.ax2 = self.figure2.add_subplot(111)
        # Plot the data
        self.line2 = FigureCanvasTkAgg(self.figure2, self)
        # Add the toolbar
        self.line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        # Group the data by date
        self.ax2.plot(self.balance_df["date"],
                      self.balance_df["balance"])
        # Add a title to the plot
        self.ax2.set_title("Balance in Dollars")
        self.ax2.set_facecolor('#cfcfcf')


class Buttons(Button):
    """Buttons class."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Empty string means default path
        self.csv_path = ""
        self.backend = Backend(self.csv_path)

        # Upload a csv file button
        self.upload_csv_button = Button(
            self,
            text="Upload CSV File",
            command=self.backend.upload_csv_file,
            width=20,
            activebackground="#ffdf4f",
            bg="#e2ff00",
            fg="black",
            activeforeground="black",
            font=("Roboto", 14),
            borderwidth=2,
        )
        self.upload_csv_button.grid(
            row=10, column=0, sticky="NSEW", padx=5, pady=5, ipadx=5, ipady=5
        )

        # Reset the application button
        self.reset_button = Button(
            self,
            text="Reset",
            command=self.backend.reset,
            width=20,
            bg="#ff0000",
            activebackground="#e23a08",
            fg="black",
            font=("Roboto", 14),
            borderwidth=2,
        )
        self.reset_button.grid(
            row=10, column=1, sticky="NSEW", padx=5, pady=5, ipadx=5, ipady=5
        )

        # Generate a report button
        self.generate_report_button = Button(
            self,
            text="Generate Report",
            command=self.backend.generate_report,
            width=20,
            bg="#23a08e",
            activebackground="#a3ffb4",
            fg="black",
            font=("Roboto", 14),
            borderwidth=2,
        )
        self.generate_report_button.grid(
            row=10, column=2, sticky="NSEW", padx=5, pady=5, ipadx=5, ipady=5
        )
        # Add a new transaction button
        self.add_new_transaction_button = Button(
            self,
            text="Add New Transaction",
            command=self.backend.add_new_transaction,
            width=20,
            bg="#6e57d2",
            activebackground="#7a49a5",
            fg="black",
            font=("Roboto", 14),
            borderwidth=2,
        )
        self.add_new_transaction_button.grid(
            row=10, column=3, sticky="NSEW", padx=5, pady=5, ipadx=5, ipady=5
        )


class Application(tk.Tk):
    """Application root window."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Budget Spreadsheet Tracker")
        self.geometry("1400x700")
        self.resizable(True, True)
        self.configure(bg='#add8e6')
        # Empty means we will use the default path
        self.backend = Backend('')

        # Create the application's label
        Label(
            self,
            text="Budget Spreadsheet Tracker",
            font=("TkDefaultFont", 14),
        ).grid(row=0)

        # Chart
        self.balance_per_day = self.backend.get_balance_per_day()
        self.highest_transactions = self.backend.get_ten_highest_transactions()

        chart = Plot(self.balance_per_day, self.highest_transactions)
        chart.grid(row=0, sticky="NSEW")

        # Buttons
        buttons = Buttons()
        buttons.grid(row=2, sticky="NSEW")
        buttons.columnconfigure(2, weight=1)
        buttons.rowconfigure(2, weight=1)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
