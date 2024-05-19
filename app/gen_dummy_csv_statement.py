#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Faker is used to generate random data. https://faker.readthedocs.io/en/master/
The script saves the generated data to a CSV file.
"""

import random

from numpy import int64
import pandas as pd

from faker import Faker

# Initialize Faker for generating random data
fake = Faker()

# Number of transactions
NUM_TRANSACTIONS = 1000

# Generate random data
data = {
    # Fake credit card number, transaction date, details, amount,
    # reference number, country, address, description
    "card_number": [int64(fake.credit_card_number())
                    for _ in range(NUM_TRANSACTIONS)],
    "date": [
        fake.date_between(start_date="-30d", end_date="today")
        for _ in range(NUM_TRANSACTIONS)
    ],
    "amount": [
        round(float(random.uniform(-1000, 10000)),
              2) for _ in range(NUM_TRANSACTIONS)
    ],
    "reference_number": [int64(fake.aba())
                         for _ in range(NUM_TRANSACTIONS)],
    "country": [fake.country().rstrip(',').strip()
                for _ in range(NUM_TRANSACTIONS)],
    "address": [fake.street_address().rstrip(',').strip()
                for _ in range(NUM_TRANSACTIONS)],
    "discription": [fake.bs().rstrip(',').strip()
                    for _ in range(NUM_TRANSACTIONS)],
}


# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("credit_card_statement.csv", index=False)
print("Dummy credit card statement saved to 'dummy_credit_card_statement.csv'")
