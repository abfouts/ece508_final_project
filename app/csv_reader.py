#!python
# -*- coding: utf-8 -*-
"""
##############################################################################
# Class:        CSVReader
# Description:  Creates an object that uses a method that takes in a CSV and
#               parses the CSVs first row into unique column entry lists
#
# Date:         05/18/2024
# Author:       Abram Fouts, Nikolay
##############################################################################
"""
from pathlib import Path
import os
import pandas as pd


class CSVReader:
    """ The proper way to access the data is to use the dictionary
        mycsv = CSVReader()
        mycsv.read_csv('credit_card_statement.csv'
    """
    def __init__(self, path_to_csv):
        self.csv_contents = pd.DataFrame()
        self.csv_dict = {}
        self.file_dir = Path(__file__).parent
        self.path_to_csv = path_to_csv

    # Provide the path to the csv
    def read_csv(self):
        """ Reads the csv and stores it in a pandas dataframe"""
        if self.path_to_csv == "" or self.path_to_csv is None:
            # If no path is provided, use the default path
            self.path_to_csv = os.path.join(self.file_dir,
                                            'credit_card_statement.csv')

        self.csv_contents = pd.read_csv(self.path_to_csv,
                                        names=[
                                            'Card_Number',
                                            'Transaction_Date',
                                            'Amount',
                                            'Reference_Number',
                                            'Country',
                                            'Address',
                                            'Discription'
                                            ])
        return self.csv_contents

    def get_csv_dict(self):
        """ Returns the csv dictionary """
        self.read_csv()
        self.csv_dict = {
            'Card_Number': self.csv_contents['Card_Number'],
            'Transaction_Date': self.csv_contents['Transaction_Date'],
            'Amount': self.csv_contents['Amount'],
            'Reference_Number': self.csv_contents['Reference_Number'],
            'Country': self.csv_contents['Country'],
            'Address': self.csv_contents['Address'],
            'Discription': self.csv_contents['Discription']
        }
        return self.csv_dict


reader = CSVReader("")
data_dict = reader.get_csv_dict()
print(data_dict)
