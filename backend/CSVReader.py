##############################################################################
# Class:        CSVReader
# Description:  Creates an object that uses a method that takes in a CSV and 
#               parses the CSVs first row into unique column entry lists
#               
# Date:         05/18/2024
# Author:       Abram Fouts, Nikolay 
##############################################################################

import pandas as pd

class CSVReader:
  def __init__(self):
    #self.csv = csv
    self.csv_contents = None
    self.csv_dict = {}

  # Provide the path to the csv
  def read_csv(self, csv):
    self.csv_contents = pd.read_csv(csv, error_bad_lines=False, warn_bad_lines=True)

  def extract_data(self):
    header = self.csv_contents.columns.tolist()
    data = self.csv_contents.values.tolist()
    self.csv_dict = {"header": header, "data": data}

'''
The proper way to access the data is to use the dictionary

mycsv = CSVReader()
mycsv.read_csv('../dummy_credit_card_statement.csv')
mycsv.extract_data()

print(mycsv.csv_dict['header']) # Prints the header, add a [0] for column 0
print(mycsv.csv_dict['data'][0]) # Prints the first row of data, add another [0] for the first element
'''


