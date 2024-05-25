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

import os
import tkinter as tk
from tkinter import Button, Canvas, filedialog

import matplotlib
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import csv_reader as my_csv_reader

matplotlib.use("TkAgg")


class Backend:
    """Backend class for the Budget Spreadsheet Tracker application"""

    def __init__(self, csv_path=None):
        self.csv_path = csv_path
        self.csv_reader = my_csv_reader.CSVReader(self.csv_path)
        self.balance_per_day = None
        self.highest_transactions = None
        self.chart_top = None
        self.chart_bottom = None
        self.buttons = None
        self.chart = None

    def upload_csv_file(self):
        """Uploads a csv file"""
        self.csv_path = filedialog.askopenfilename(initialdir=os.getcwd())

    def reset(self):
        """Resets the application to its initial state"""
        if self.chart_top and self.chart_bottom:
            self.chart_top.destroy()
            self.chart_bottom.destroy()

        self.chart_top = PlotTop(self.balance_per_day, self.highest_transactions)
        self.chart_bottom = PlotBottom(self.balance_per_day, self.highest_transactions)

    def generate_report(self):
        """Generates a report"""
        self.csv_reader.read_csv()
        self.balance_per_day = self.get_balance_per_day()
        self.highest_transactions = self.get_ten_highest_transactions()
        self.chart = PlotTop(self.balance_per_day, self.highest_transactions)
        self.chart.grid(row=0, column=0)

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


class PlotTop(Canvas):
    """Plot class for the Budget Spreadsheet Tracker application"""

    def __init__(self, balance_per_day, ten_highest_transactions, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if balance_per_day is None or ten_highest_transactions is None:
            return

        self.balance = balance_per_day
        self.transactions = ten_highest_transactions
        self.configure(bg="#adbce6")

        self.create_figure1()
        self.create_figure2()

    def create_figure1(self):
        """Creates the first figure"""
        # Create figure 1
        transaction_df = pd.DataFrame(self.transactions)
        self.figure1 = Figure(figsize=(3, 3), dpi=80)
        self.ax1 = self.figure1.add_subplot(111)
        self.bar1 = FigureCanvasTkAgg(self.figure1, self)

        self.ax1.bar(transaction_df["date"], transaction_df["amount"])
        self.ax1.set_title("10 Highest Transactions")
        self.ax1.set_facecolor("#cfcfcf")
        self.ax1.set_xlabel("Date")
        self.ax1.set_ylabel("Amount in Dollars")
        self.ax1.set_xticks(transaction_df["date"])
        self.ax1.set_xticklabels(transaction_df["date"], rotation=90)
        self.bar1.get_tk_widget().pack(expand=False, side=tk.TOP, ipadx=50, ipady=50)

    def create_figure2(self):
        """Creates the second figure"""

        balance_df = pd.DataFrame(self.balance)
        self.figure2 = Figure(figsize=(3, 3), dpi=80)
        self.ax2 = self.figure2.add_subplot()
        self.line2 = FigureCanvasTkAgg(self.figure2, self)

        self.ax2.plot(balance_df["date"], balance_df["balance"], "b", label="Balance")
        self.ax2.set_title("Balance in Dollars")
        self.ax2.set_facecolor("#cfcfcf")
        self.ax2.set_xlabel("Date")
        self.ax2.set_ylabel("Dollars")
        self.ax2.set_xticks(balance_df["date"])
        self.ax2.set_xticklabels(balance_df["date"], rotation=90)
        self.line2.get_tk_widget().pack(expand=False, side=tk.TOP, ipadx=50, ipady=50)


class PlotBottom(Canvas):
    """Plot class for the Budget Spreadsheet Tracker application"""

    def __init__(self, balance_per_day, ten_highest_transactions, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if balance_per_day is None or ten_highest_transactions is None:
            return

        self.balance = balance_per_day
        self.transactions = ten_highest_transactions
        self.configure(bg="#adbce6")

        self.create_figure1()
        self.create_figure2()

    def create_figure1(self):
        """Creates the first figure"""
        # Create figure 1
        transaction_df = pd.DataFrame(self.transactions)
        self.figure1 = Figure(figsize=(3, 3), dpi=80)
        self.ax1 = self.figure1.add_subplot(111)
        self.bar1 = FigureCanvasTkAgg(self.figure1, self)

        self.ax1.bar(transaction_df["date"], transaction_df["amount"])
        self.ax1.set_title("10 Highest Transactions")
        self.ax1.set_facecolor("#cfcfcf")
        self.ax1.set_xlabel("Date")
        self.ax1.set_ylabel("Amount in Dollars")
        self.ax1.set_xticks(transaction_df["date"])
        self.ax1.set_xticklabels(transaction_df["date"], rotation=90)
        self.bar1.get_tk_widget().pack(expand=False, side=tk.LEFT, ipadx=50, ipady=50)

    def create_figure2(self):
        """Creates the second figure"""

        balance_df = pd.DataFrame(self.balance)
        self.figure2 = Figure(figsize=(3, 3), dpi=80)
        self.ax2 = self.figure2.add_subplot()
        self.line2 = FigureCanvasTkAgg(self.figure2, self)

        self.ax2.plot(balance_df["date"], balance_df["balance"], "b", label="Balance")
        self.ax2.set_title("Balance in Dollars")
        self.ax2.set_facecolor("#cfcfcf")
        self.ax2.set_xlabel("Date")
        self.ax2.set_ylabel("Dollars")
        self.ax2.set_xticks(balance_df["date"])
        self.ax2.set_xticklabels(balance_df["date"], rotation=90)
        self.line2.get_tk_widget().pack(expand=False, side=tk.LEFT, ipadx=50, ipady=50)


class Buttons(Button):
    """Button class for the Budget Spreadsheet Tracker application"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.csv_path = ""
        self.csv_path = ""
        self.backend = Backend(self.csv_path)

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
            row=3, column=0, sticky="nsew", padx=10, pady=5, ipadx=50, ipady=5
        )

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
            row=3, column=1, padx=10, sticky="nsew", pady=5, ipadx=50, ipady=5
        )

        self.generate_report_button = Button(
            self,
            text="Generate Report",
            command=self.backend.generate_report,
            width=20,
            activeforeground="black",
            bg="#23a08e",
            activebackground="#a3ffb4",
            fg="black",
            font=("Roboto", 14),
            borderwidth=2,
        )
        self.generate_report_button.grid(
            row=3,
            column=23,
            padx=10,
            sticky="we",
            pady=5,
            ipadx=50,
            ipady=5,
            rowspan=3,
            columnspan=3,
        )

        self.generate_report_button.grid_columnconfigure(3, weight=1)


class MyCanvas(Canvas):
    """Canvas class for the Budget Spreadsheet Tracker application"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.bg = tk.PhotoImage(file="Designer.png")
        self.my_canvas = Canvas(self, width=1000, height=600)

        self.my_canvas.create_image(0, 0, image=self.bg, anchor="nw")
        self.my_canvas.pack(
            fill="both", expand=True, padx=10, pady=10, ipadx=5, ipady=5, side="top"
        )


class Application(tk.Tk):
    """Application class for the Budget Spreadsheet Tracker application"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create the ccanvas, and the background image
        self.my_canvas = MyCanvas()
        self.my_canvas.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.my_canvas.grid_columnconfigure(0, weight=1)

        # Create the button structure
        self.my_buttons = Buttons()
        self.my_buttons.grid(
            sticky="nsew",
            columnspan=3,
            rowspan=3,
        )


if __name__ == "__main__":
    app = Application()
    app.title("Budget Spreadsheet Tracker")
    app.configure(bg="white")
    app.geometry("1100x800")
    app.grid()

    app.mainloop()
