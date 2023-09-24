import pandas as pd
import numpy as np
from faker import Faker
import random

# Set display options to ensure all columns are printed
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

# Initialize Faker library for generating random names
fake = Faker()

# Define the number of rows you want to generate
num_rows = 4000

# Generate random data
data = {
    'IGA': [str(random.randint(10000, 99999)) for _ in range(num_rows)],
    'CREWBASE': [random.choice(['BOM', 'DEL', 'COK','MAA','CCU','HYD','PNQ','LKO','IXC','BLR']) for _ in range(num_rows)],
    'CREWNAME': [fake.name() for _ in range(num_rows)],
    'RANK': [random.choice(['CP', 'FO', 'LD', 'CA']) for _ in range(num_rows)],
    'LAYOVERCOUNT': [f"{random.randint(1, 10)} LAYOVER + {random.randint(1, 24)} Hours" for _ in range(num_rows)],
    'AIRCRAFTTYPE': [random.choice(['321', '320', 'ATR']) for _ in range(num_rows)],
}

# Create DataFrame
df = pd.DataFrame(data)

# Define a function to calculate the total amount paid based on rank and layover count
def calculate_total_amount_paid(rank, layover_count):
    layover, hours = layover_count.split(' LAYOVER + ')
    layover = int(layover)
    hours = int(hours.split(' ')[0])

    if rank in ['CP', 'FO']:
        amount = layover * (2000 if rank == 'CP' else 1000) + hours * 100
    else:  # rank in ['LD', 'CA']
        amount = layover * 750 + hours * 30
    return amount

# Calculate the total amount paid for each row and add it to the DataFrame
df['TOTAl Amount Paid'] = df.apply(lambda row: calculate_total_amount_paid(row['RANK'], row['LAYOVERCOUNT']), axis=1)

# print(df)
# Save DataFrame to Excel file
df.to_excel(r"../Output/DomesticLayoverAllowance.xlsx", index=False)
