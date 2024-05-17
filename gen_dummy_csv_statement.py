#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Faker is used to generate random data. https://faker.readthedocs.io/en/master/
The script saves the generated data to a CSV file.
"""

import random
import pandas as pd

from faker import Faker

# Initialize Faker for generating random data
fake = Faker()

# Number of transactions
NUM_TRANSACTIONS = 1000

# Generate random data
data = {
    "Transaction Date": [
        fake.date_between(start_date="-30d", end_date="today")
        for _ in range(NUM_TRANSACTIONS)
    ],
    "Details": [fake.company() for _ in range(NUM_TRANSACTIONS)],
    "Amount in US dollars": [
        round(random.uniform(-10000, 10000), 2) for _ in range(NUM_TRANSACTIONS)
    ],
    "Reference Number": [fake.aba() for _ in range(NUM_TRANSACTIONS)],
    "Country": [fake.country() for _ in range(NUM_TRANSACTIONS)],
    "Address": [fake.street_address() for _ in range(NUM_TRANSACTIONS)],
    "Discription": [fake.bs() for _ in range(NUM_TRANSACTIONS)],
}


# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("dummy_credit_card_statement.csv", index=False)
print("Dummy credit card statement saved to 'dummy_credit_card_statement.csv'")
