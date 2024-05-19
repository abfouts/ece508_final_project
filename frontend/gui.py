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
from tkinter import Button, Label, Canvas
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

matplotlib.use("TkAgg")


class Backend:
    """Backend class."""

    def __init__(self):
        pass

    @staticmethod
    def upload_csv_file():
        """Upload a CSV file."""
        print("Upload a CSV file.")

    @staticmethod
    def reset():
        """Reset the application."""
        print("Reset the application.")

    @staticmethod
    def generate_report():
        """Generate a report."""
        print("Generate a report.")

    @staticmethod
    def add_new_transaction():
        """Add a new transaction."""
        print("Add a new transaction.")


class Plot(Canvas):
    """Chart class."""

    def __init__(self, balance, transactions, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.balance = balance
        self.transactions = transactions
        self.configure(bg="#adbce6")

        # Create a matplotlib figure1
        self.balance_df = pd.DataFrame(self.balance)
        # Create a Figure object
        self.figure1 = Figure(figsize=(6, 5), dpi=100)
        # Create an Axes object
        self.ax1 = self.figure1.add_subplot(111)
        # Plot the data
        self.bar1 = FigureCanvasTkAgg(self.figure1, self)
        # Add the toolbar
        self.bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        # Group the data by category
        self.ax1.bar(self.balance_df["day_of_the_month"],
                     self.balance_df["balance"])
        # Add a title to the plot
        self.ax1.set_title("Balance")
        self.ax1.set_facecolor('#cfcfcf')

        # Create a matplotlib figure2
        self.transactions_df = pd.DataFrame(self.transactions)
        # Create a Figure object
        self.figure2 = Figure(figsize=(5, 4), dpi=100)
        # Create an Axes object
        self.ax2 = self.figure2.add_subplot(111)
        # Plot the data
        self.line2 = FigureCanvasTkAgg(self.figure2, self)
        # Add the toolbar
        self.line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        # Group the data by date
        self.ax2.plot(self.transactions_df["amount"],
                      self.transactions_df["item"])
        # Add a title to the plot
        self.ax2.set_title("Transactions")
        self.ax2.set_facecolor('#cfcfcf')


class Buttons(Button):
    """Buttons class."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Upload a csv file button
        self.upload_csv_button = Button(
            self,
            text="Upload CSV File",
            command=Backend.upload_csv_file,
            width=30,
            activebackground="#ffdf4f",
            bg="#e2ff00",
            fg="black",
            activeforeground="black",
            font=("Roboto", 12),
            borderwidth=2,
        )
        self.upload_csv_button.grid(
            row=10, column=1, sticky="NSEW", padx=5, pady=5, ipadx=5, ipady=5
        )

        # Reset the application button
        self.reset_button = Button(
            self,
            text="Reset",
            command=Backend.reset,
            width=30,
            bg="#ff0000",
            activebackground="#e23a08",
            fg="white",
            font=("Roboto", 12),
            borderwidth=2,
        )
        self.reset_button.grid(
            row=10, column=2, sticky="NSEW", padx=5, pady=5, ipadx=5, ipady=5
        )

        # Generate a report button
        self.generate_report_button = Button(
            self,
            text="Generate Report",
            command=Backend.generate_report,
            width=30,
            bg="#23a08e",
            activebackground="#a3ffb4",
            fg="white",
            font=("Roboto", 12),
            borderwidth=2,
        )
        self.generate_report_button.grid(
            row=10, column=3, sticky="NSEW", padx=5, pady=5, ipadx=5, ipady=5
        )
        # Add a new transaction button
        self.add_new_transaction_button = Button(
            self,
            text="Add New Transaction",
            command=Backend.add_new_transaction,
            width=30,
            bg="#6e57d2",
            activebackground="#7a49a5",
            fg="white",
            font=("Roboto", 12),
            borderwidth=2,
        )
        self.add_new_transaction_button.grid(
            row=10, column=4, sticky="NSEW", padx=5, pady=5, ipadx=5, ipady=5
        )


class Application(tk.Tk):
    """Application root window."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Budget Spreadsheet Tracker")
        self.geometry("1280x640")
        self.resizable(True, True)
        self.configure(bg='#add8e6')

        # Create the application's label
        Label(
            self,
            text="Budget Spreadsheet Tracker",
            font=("TkDefaultFont", 16),
        ).grid(row=0)

        # Chart
        self.balance_per_day = self.get_balance_per_day()
        self.highest_transactions = self.get_transactions()

        chart = Plot(self.balance_per_day, self.highest_transactions)
        chart.grid(row=0, sticky="NSEW")

        # Buttons
        buttons = Buttons()
        buttons.grid(row=2, sticky="NSEW")
        buttons.columnconfigure(2, weight=1)
        buttons.rowconfigure(2, weight=1)

    # Function to fetch the data for the chart
    def get_balance_per_day(self):
        """Get the data for the chart."""
        balance_per_month = {
            "balance": [1000, 2000, 3000, 4000],
            "day_of_the_month": ["1st", "2nd", "3rd", "4th"],
        }

        return balance_per_month

    def get_transactions(self):
        """Get the data for the chart."""
        transactions_per_day = {
            "item": ["item1", "item2", "item3", "item4"],
            "amount": [100, 200, 300, 400],
        }

        return transactions_per_day


if __name__ == "__main__":
    app = Application()
    app.mainloop()
