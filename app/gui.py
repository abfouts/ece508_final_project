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

from csv_reader import CSVReader

matplotlib.use("TkAgg")


class Backend:
    """Backend class for the Budget Spreadsheet Tracker application"""

    def __init__(self, csv_path=None):
        self.csv_path = csv_path
        self.csv_reader = None
        self.balance_per_day = None
        self.highest_transactions = None
        self.chart_top = None
        self.chart_bottom = None
        self.buttons = None
        self.chart = None
        self.category_sum = None
        self.category_count = None

    def upload_csv_file(self):
        """Uploads a csv file"""
        self.csv_path = filedialog.askopenfilename(initialdir=os.getcwd())
        self.update_csv_path(self.csv_path)
        self.csv_reader = CSVReader(self.csv_path)
        return self.generate_report()

    def reset(self):
        """Resets the application to its initial state"""
        if self.chart_top is None or self.chart_bottom is None:
            return

        return self.chart_top.destroy(), self.chart_bottom.destroy()

    def generate_report(self):
        """Generates a report"""
        self.csv_reader = CSVReader(self.csv_path)
        self.balance_per_day = self.get_balance_per_day()
        self.highest_transactions = self.get_ten_highest_transactions()
        self.category_sum = self.get_category_sum()
        self.category_count = self.get_category_count()

        if self.chart_top is not None or self.chart_bottom is not None:
            self.chart_top.destroy()
            self.chart_bottom.destroy()

        self.chart_top = PlotTop(self.balance_per_day, self.highest_transactions)
        self.chart_top.grid(
            row=0,
            column=0,
            sticky="nw",
        )
        self.chart_bottom = PlotBottom(self.category_sum, self.category_count)
        self.chart_bottom.grid_rowconfigure(0, weight=1)
        self.chart_bottom.grid(row=0, column=0, sticky="se", ipady=25)

        return self.chart_top, self.chart_bottom

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
        return self.csv_path

    def get_category_sum(self):
        self.category_sum = self.csv_reader.get_category_sum()
        return self.category_sum

    def get_category_count(self):
        self.category_count = self.csv_reader.get_category_count()
        return self.category_count


class PlotTop(Canvas):
    """Plot class for the Budget Spreadsheet Tracker application"""

    def __init__(self, balance_per_day, ten_highest_transactions, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if balance_per_day is None or ten_highest_transactions is None:
            return

        self.balance = balance_per_day
        self.transactions = ten_highest_transactions
        self.configure(bg="#020101")

        self.create_figure1()
        self.create_figure2()

    def create_figure1(self):
        """Creates the first figure"""
        # Create figure 1
        transaction_df = pd.DataFrame(self.transactions)
        self.figure1 = Figure(figsize=(6, 4), dpi=65)
        self.ax1 = self.figure1.add_subplot()
        self.bar1 = FigureCanvasTkAgg(self.figure1, self)
        self.figure1.set_layout_engine("compressed")
        y_values = transaction_df["amount"]
        facecolors = [
            "red" if y > transaction_df["amount"].mean() else "green" for y in y_values
        ]
        edgecolors = facecolors
        self.ax1.bar(
            transaction_df["date"],
            transaction_df["amount"],
            color=facecolors,
            edgecolor=edgecolors,
        )

        self.ax1.tick_params(
            axis="x", labelcolor="tab:red", labelrotation=45, labelsize=16
        )
        self.ax1.tick_params(axis="y", color="tab:green", size=25, width=3)
        self.ax1.set_title("10 Highest Purchases")
        self.ax1.set_facecolor("#00ffff")

        self.ax1.tick_params(axis="both", which="minor", labelsize=10)
        self.ax1.set_xlabel("Date")
        self.ax1.set_ylabel("Amount in Dollars")
        self.ax1.set_xticks(transaction_df["date"])
        self.ax1.set_xticklabels(transaction_df["date"], rotation=90)

        self.bar1.get_tk_widget().pack(
            expand=False, side=tk.TOP, ipadx=60, ipady=92, anchor="w", fill="both"
        )

    def create_figure2(self):
        """Creates the second figure"""

        balance_df = pd.DataFrame(self.balance)
        self.figure2 = Figure(figsize=(6, 4), dpi=65)
        self.figure2.set_layout_engine("compressed")

        self.ax2 = self.figure2.add_subplot()
        self.line2 = FigureCanvasTkAgg(self.figure2, self)

        self.ax2.plot(balance_df["date"], balance_df["balance"], "b", label="Balance")
        self.ax2.set_title("Balance the Last 30 Days")

        self.ax2.set_facecolor("#e6e600")
        self.ax2.set_xlabel("Date")
        self.ax2.set_ylabel("Dollars")
        self.ax2.tick_params(axis="both", which="minor", labelsize=10)
        self.ax2.tick_params(
            axis="x", labelcolor="tab:red", labelrotation=45, labelsize=16
        )
        self.ax2.tick_params(axis="y", color="tab:green", size=25, width=3)
        self.ax2.yaxis.set_major_formatter("${x:1.2f}")

        self.ax2.yaxis.set_tick_params(
            which="major", labelcolor="green", labelleft=False, labelright=True
        )
        self.ax2.set_xticks(balance_df["date"])
        self.ax2.set_xticklabels(
            balance_df["date"],
            rotation=90,
        )

        self.line2.get_tk_widget().pack(
            expand=False, side=tk.TOP, ipadx=60, ipady=93, anchor="w", fill="both"
        )


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
        self.figure1 = Figure(figsize=(6, 4), dpi=60)
        self.ax1 = self.figure1.add_subplot()

        y_values = transaction_df.iloc[:, 1]
        facecolors = [
            "red" if y > transaction_df.iloc[:, 1].median() else "green"
            for y in y_values
        ]
        edgecolors = facecolors

        self.bar1 = FigureCanvasTkAgg(self.figure1, self)

        self.figure1.set_layout_engine("compressed")
        self.ax1.bar(
            transaction_df.iloc[:, 0],
            transaction_df.iloc[:, 1],
            color=facecolors,
            edgecolor=edgecolors,
        )
        self.ax1.set_title("Total Number of Transactions Per Category")
        self.ax1.set_facecolor("#f7d7e7")
        self.ax1.set_xlabel("Category")
        self.ax1.set_ylabel("Count")
        self.ax1.tick_params(axis="both", which="minor", labelsize=10)

        self.ax1.set_xticks(transaction_df.iloc[:, 0])
        self.ax1.set_xticklabels(transaction_df.iloc[:, 0], rotation=40)

        self.bar1.get_tk_widget().pack(
            expand=True, side=tk.TOP, ipadx=70, ipady=90, anchor="e", fill="both"
        )

    def create_figure2(self):
        """Creates the second figure"""

        balance_df = pd.DataFrame(self.balance)
        self.figure2 = Figure(figsize=(6, 4), dpi=60)
        self.ax2 = self.figure2.add_subplot()
        self.line2 = FigureCanvasTkAgg(self.figure2, self)
        self.figure2.set_layout_engine("compressed")
        bar_colors = [
            "tab:red",
            "tab:blue",
            "tab:red",
            "tab:orange",
            "tab:green",
            "tab:purple",
            "tab:brown",
            "tab:pink",
            "tab:gray",
            "tab:olive",
        ]
        self.ax2.bar(balance_df.iloc[:, 0], balance_df.iloc[:, 1], color=bar_colors)
        self.ax2.set_title("Sum Spent Per Category")
        self.ax2.set_facecolor("#e6e0e3")
        self.ax2.set_xlabel("Category")
        self.ax2.set_ylabel("Dollars")
        self.ax2.tick_params(axis="both", which="minor", labelsize=10)
        self.ax2.set_xticks(balance_df.iloc[:, 0])
        self.ax2.set_xticklabels(balance_df.iloc[:, 0], rotation=40)
        self.line2.get_tk_widget().pack(
            expand=True,
            side=tk.TOP,
            ipadx=70,
            ipady=90,
            anchor="e",
            fill="both",
        )


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
            column=2,
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
        self.my_canvas = Canvas(self, width=950, height=650)

        self.my_canvas.create_image(0, 0, image=self.bg, anchor="nw")
        self.my_canvas.pack(
            fill="both", expand=True, padx=10, pady=10, ipadx=10, ipady=10, side="top"
        )
        self.my_canvas.pack_configure(fill="both", expand=True)


class Application(tk.Tk):
    """Application class for the Budget Spreadsheet Tracker application"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create the ccanvas, and the background image
        self.my_canvas = MyCanvas()
        self.my_canvas.grid(row=0, column=0, sticky="nsew")
        self.my_canvas.grid_columnconfigure(0, weight=1)
        self.my_canvas.grid_rowconfigure(0, weight=1)

        # Create the button structure
        self.my_buttons = Buttons()
        self.my_buttons.grid(sticky="nsew")


if __name__ == "__main__":
    app = Application()
    app.title("Budget Spreadsheet Tracker")
    app.configure(bg="white")
    app.geometry("900x750")
    app.grid()

    app.mainloop()
