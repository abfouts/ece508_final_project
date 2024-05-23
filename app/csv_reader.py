#!python
# -*- coding: utf-8 -*-
"""
##############################################################################
# Class      : CSVReader
# Description: Creates an object that uses a method that takes in a CSV and
#               parses the CSVs first row into unique column entry lists
#
# Date  : 05/18/2024
# Author: Abram Fouts, Niko Nikolov
##############################################################################
"""

from pathlib import Path
import os
import pandas as pd


class CSVReader:
    """The proper way to access the data is to use the dictionary
    mycsv = CSVReader()
    mycsv.read_csv('credit_card_statement.csv'
    """

    def __init__(self, path_to_csv):
        self.csv_contents = pd.DataFrame()
        self.csv_dict = {}
        self.file_dir = Path(__file__).parent
        self.path_to_csv = path_to_csv
        self.balance_per_day = {}
        self.ten_highest_transactions = {}

    # Provide the path to the csv
    def read_csv(self):
        """Reads the csv and stores it in a pandas dataframe"""
        if self.path_to_csv == "" or self.path_to_csv is None:
            # If no path is provided, use the default path
            self.path_to_csv = os.path.join(self.file_dir, "credit_card_statement.csv")

        self.csv_contents = pd.read_csv(
            self.path_to_csv,
            header=0,
            names=[
                "card_number",
                "date",
                "amount",
                "reference_number",
                "country",
                "address",
                "discription",
            ],
        )
        return self.csv_contents

    def get_csv_dict(self):
        """Returns the csv dictionary"""
        self.read_csv()
        self.csv_dict = self.csv_contents.to_dict()
        return self.csv_dict

    def get_ten_highest_transactions(self):
        """Returns the ten highest transactions"""
        self.read_csv()
        # Sort the dataframe by date
        self.csv_contents = self.csv_contents.sort_values("date")

        # Get the top 10 transactions and sort
        top10_transactions = self.csv_contents.nlargest(10, "amount")[
            ["date", "amount"]
        ]
        # Sort the dataframe by date
        top10_transactions = top10_transactions.sort_values("date")
        # Convert the dataframe to a date list
        dates = top10_transactions["date"].tolist()
        # Convert the dataframe to a amount list
        amounts = top10_transactions["amount"].tolist()
        # Create a dictionary with the date and amount
        self.ten_highest_transactions = {"date": dates, "amount": amounts}

        # Return the dictionary
        return self.ten_highest_transactions

    def get_balance_per_day(self):
        """Returns the balance per day"""
        # Read the csv and group by date
        self.read_csv()
        # List to store the balance for each day
        balance = []
        # List to store the date of the month
        day_of_the_month = []
        # Attribute to hold the 2 lists which we will use
        self.balance_per_day = {}
        # Sort the dataframe by date
        self.csv_contents = self.csv_contents.sort_values("date")
        # Iterate through the unique dates
        for date in self.csv_contents["date"].unique():
            # Filter the dataframe by the date
            tempdf = self.csv_contents[self.csv_contents["date"] == date]

            # Sum the amount column and round to 2 decimal places
            # Append the balance to the list
            balance.append(round(tempdf["amount"].sum(), 2))
            # Append the date to the list
            day_of_the_month.append(date)

        # Create a dictionary with the date and balance
        self.balance_per_day = {"date": day_of_the_month, "balance": balance}
        # Return the dictionary
        return self.balance_per_day


csv_reader = CSVReader("")
print(csv_reader.get_balance_per_day())
