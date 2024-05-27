# ECE 508 Final Project - Spending Spreadsheet Tracker

ECE508 - Python & Scripting Wksp
Final Project - Budget Spreadsheet Tracker
Spring 2024 Jean Paul Mugisha
Abram Fouts, Niko Nikolov
This project is written in Python and uses the pandas library for data manipulation and the Tkinter library for the
graphical user interface.

## Used Packages
tkinter
matplotlib
pandas
path
os


## File Structure

The project consists of the following Python files:

- `gen_dummy_csv_statement.py`
- `csv_reader.py`
- `gui.py`

### `gen_dummy_csv_statement.py`

This file is responsible for generating a dummy credit card statement in CSV format. The generated CSV file is saved
as `credit_card_statement.csv`.

### `csv_reader.py`

This file contains the `CSVReader` class which is responsible for reading and parsing the CSV file generated
by `gen_dummy_csv_statement.py`. The class provides several methods for extracting specific information from the CSV
file, such as:

- `read_csv()`: Reads the CSV file and stores it in a pandas DataFrame.
- `get_csv_dict()`: Returns a dictionary representation of the CSV file.
- `get_ten_highest_transactions()`: Returns the ten highest transactions.
- `get_balance_per_day()`: Returns the balance per day.
- `get_category_sum()`: Returns the total amount spent per category.
- `get_category_count()`: Returns the number of transactions per category.

### `gui.py`

This file contains the graphical user interface for the application. It uses the Tkinter library to create the
interface. The file contains several classes:

- `Backend`: This class is responsible for handling the backend operations of the application, such as uploading the CSV
  file, resetting the application, and generating the report.
- `PlotTop` and `PlotBottom`: These classes are responsible for creating the plots that are displayed in the
  application.
- `Buttons`: This class is responsible for creating the buttons in the application.
- `MyCanvas`: This class is responsible for creating the canvas in the application.
- `Application`: This is the main application class. It initializes and runs the application.

The application allows the user to upload a CSV file, generate a report based on the data in the CSV file, and reset the
application. The report includes plots of the balance per day, the ten highest transactions, the total amount spent per
category, and the number of transactions per category.
