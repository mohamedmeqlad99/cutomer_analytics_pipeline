import os
from faker import Faker
import csv

# Initialize Faker
fake = Faker()

# Define the number of records you want to generate
num_records = 1000

# Define the output directory and ensure it exists
output_dir = '../data'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the columns for customer data
columns = ['customer_id', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'date_of_birth']

# Open the CSV file to write the data
output_file = os.path.join(output_dir, 'customer_data.csv')
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(columns)  # Write the header row

    # Generate fake data for each customer
    for _ in range(num_records):
        writer.writerow([
            fake.unique.uuid4(),      # customer_id
            fake.first_name(),        # first_name
            fake.last_name(),         # last_name
            fake.email(),             # email
            fake.phone_number(),      # phone_number
            fake.address(),           # address
            fake.date_of_birth(),     # date_of_birth
        ])
