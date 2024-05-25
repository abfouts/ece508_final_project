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
from textwrap import fill
import tkinter as tk
from tkinter import Button, Label, Canvas, filedialog
import os
from turtle import pos
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import csv_reader as my_csv_reader


matplotlib.use("TkAgg")


class Backend:
    """Backend class."""

    def __init__(self, csv_path=None):
        """Initialize the backend."""
        self.csv_path = csv_path
        self.csv_reader = my_csv_reader.CSVReader(self.csv_path)
        self.csv_balance_per_day = self.csv_reader.get_balance_per_day()
        self.csv_ten_highest_transactions = (
            self.csv_reader.get_ten_highest_transactions()
        )
        self.balance_per_day = None
        self.highest_transactions = None
        self.chart = Plot(None, None)

    def upload_csv_file(self):
        """Upload a CSV file."""
        print("Upload a CSV file.")
        self.csv_path = filedialog.askopenfilename(initialdir=os.getcwd())

    def reset(self):
        """Reset the application."""
        print("Reset the application.")
        self.chart.destroy()
        self.chart.grid(row=0, sticky="NSEW")

    def generate_report(self):
        """Generate a report."""
        print("Generate a report.")

        # Chart
        self.balance_per_day = self.get_balance_per_day()
        self.highest_transactions = self.get_ten_highest_transactions()
        self.chart = Plot(self.balance_per_day, self.highest_transactions)
        self.chart.grid(row=0, sticky="NSEW", fill=tk.BOTH, expand=True)
        self.chart.columnconfigure(0, weight=1, minsize=100)
        self.chart.rowconfigure(0, weight=1, minsize=100)

    def add_new_transaction(self):
        """Add a new transaction."""
        print("Add a new transaction.")

    def get_balance_per_day(self):
        """Get the balance per day."""

        self.csv_balance_per_day = self.csv_reader.get_balance_per_day()

        return self.csv_balance_per_day

    def get_ten_highest_transactions(self):
        """Get the ten highest transactions."""

        self.csv_ten_highest_transactions = (
            self.csv_reader.get_ten_highest_transactions()
        )

        return self.csv_ten_highest_transactions

    def update_csv_path(self, new_path):
        """Update the CSV path."""
        self.csv_path = new_path


class Plot(Canvas):
    """Chart class."""

    def __init__(self, balance_per_day, ten_highest_transactions, *args, **kwargs):
        """Initialize the charts"""
        super().__init__(*args, **kwargs)

        if balance_per_day is None:
            return
        if ten_highest_transactions is None:
            return

        # Balance array
        self.balance = balance_per_day
        # Transactions array
        self.transactions = ten_highest_transactions
        # Configure the background color
        self.configure(bg="#adbce6")
        # -----------------------------------------
        # Create a matplotlib figure1
        # -----------------------------------------
        self.transaction_df = pd.DataFrame(self.transactions)
        # Create a Figure object
        self.figure1 = Figure(
            figsize=(4, 3),
            dpi=100,
        )
        # Create an Axes object
        self.ax1 = self.figure1.add_subplot(111)
        # Plot the data
        self.bar1 = FigureCanvasTkAgg(self.figure1, self)
        # Add the toolbar
        self.bar1.get_tk_widget().pack()
        # Group the data by category

        self.ax1.bar(self.transaction_df["date"], self.transaction_df["amount"])
        # Add a title to the plot
        self.ax1.set_title("10 Highest Transactions")
        self.ax1.set_facecolor("#cfcfcf")
        self.ax1.set_xlabel("Date")
        self.ax1.set_ylabel("Amount in Dollars")
        self.ax1.set_xticks(self.transaction_df["date"])
        self.ax1.set_xticklabels(self.transaction_df["date"], rotation=90)

        self.ax1.set_autoscaley_on(True)
        self.ax1.set_autoscalex_on(True)
        self.ax1.minorticks_on()
        self.ax1.legend("$", fontsize=10)
        self.ax1.yaxis_date()
        self.ax1.violinplot(self.transaction_df["amount"])
        self.ax1.indicate_inset_zoom(self.ax1, edgecolor="black")
        self.ax1.set_ylim(0, 20000)
        self.ax1.set_autoscale_on(True)

        # -----------------------------------------
        # Create a matplotlib figure2
        # -----------------------------------------
        self.balance_df = pd.DataFrame(self.balance)
        # Create a Figure object
        self.figure2 = Figure(figsize=(4, 3), dpi=120)
        # Create an Axes object
        self.ax2 = self.figure2.add_subplot(111)
        # Plot the data
        self.line2 = FigureCanvasTkAgg(self.figure2, self)
        # Add the toolbar
        self.line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        # Group the data by date
        self.ax2.plot(
            self.balance_df["date"], self.balance_df["balance"], "b", label="Balance"
        )
        # Add a title to the plot
        self.ax2.set_title("Balance in Dollars")
        self.ax2.set_facecolor("#cfcfcf")
        self.ax2.set_xlabel("Date")
        self.ax2.set_ylabel("Dollars")
        self.ax2.set_xticks(self.balance_df["date"])
        self.ax2.set_xticklabels(self.balance_df["date"], rotation=90)

        self.ax2.set_autoscaley_on(True)
        self.ax2.set_autoscalex_on(True)
        self.ax2.minorticks_on()
        self.ax2.legend("$", fontsize=8)

        self.ax2.violinplot(self.balance_df["balance"])
        self.ax2.indicate_inset_zoom(self.ax2, edgecolor="black")
        self.ax2.set_autoscale_on(True)

        # Create a matplotlib figure3

        self.spending = pd.DataFrame(self.balance)
        # Create a Figure object
        self.figure3 = Figure(figsize=(4, 3), dpi=120)
        # Create an Axes object
        self.ax3 = self.figure3.add_subplot(111)
        # Plot the data
        self.line3 = FigureCanvasTkAgg(self.figure3, self)
        # Add the toolbar
        self.line3.get_tk_widget().pack()
        # Group the data by date
        self.ax3.plot(
            self.balance_df["date"], self.balance_df["balance"], "b", label="Balance"
        )
        # Add a title to the plot
        self.ax3.set_title("Balance in Dollars")
        self.ax3.set_facecolor("#cfcfcf")
        self.ax3.set_xlabel("Date")
        self.ax3.set_ylabel("Dollars")
        self.ax3.set_xticks(self.balance_df["date"])
        self.ax3.set_xticklabels(self.balance_df["date"], rotation=90)

        self.ax3.set_autoscaley_on(True)
        self.ax3.set_autoscalex_on(True)
        self.ax3.minorticks_on()
        self.ax3.legend("$", fontsize=8)

        self.ax3.violinplot(self.balance_df["balance"])
        self.ax3.indicate_inset_zoom(self.ax3, edgecolor="black")
        self.ax3.set_autoscale_on(True)

        # Create a matplotlib figure3

        self.inflow = pd.DataFrame(self.balance)
        # Create a Figure object
        self.figure4 = Figure(figsize=(4, 3), dpi=120)
        # Create an Axes object
        self.ax4 = self.figure4.add_subplot(111)
        # Plot the data
        self.line4 = FigureCanvasTkAgg(self.figure3, self)
        # Add the toolbar
        self.line4.get_tk_widget().pack()
        # Group the data by date
        self.ax4.plot(
            self.balance_df["date"], self.balance_df["balance"], "b", label="Balance"
        )
        # Add a title to the plot
        self.ax4.set_title("Balance in Dollars")
        self.ax4.set_facecolor("#cfcfcf")
        self.ax4.set_xlabel("Date")
        self.ax4.set_ylabel("Dollars")
        self.ax4.set_xticks(self.balance_df["date"])
        self.ax4.set_xticklabels(self.balance_df["date"], rotation=90)

        self.ax4.set_autoscaley_on(True)
        self.ax4.set_autoscalex_on(True)
        self.ax4.minorticks_on()
        self.ax4.legend("$", fontsize=8)

        self.ax4.violinplot(self.balance_df["balance"])
        self.ax4.indicate_inset_zoom(self.ax4, edgecolor="black")
        self.ax4.set_autoscale_on(True)


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


class Application(tk.Tk):
    """Application root window."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Budget Spreadsheet Tracker")
        self.geometry("1100x600")
        self.resizable(True, True)
        self.configure(bg="#add8e6")
        # Empty means we will use the default path
        self.backend = Backend("")

        # Create the application's label
        Label(
            self,
            text="Budget Spreadsheet Tracker",
            font=("TkDefaultFont", 14),
        ).grid(row=0)

        # Buttons
        buttons = Buttons()
        buttons.grid(row=2, sticky="NSEW")
        buttons.columnconfigure(2, weight=1)
        buttons.rowconfigure(2, weight=1)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
