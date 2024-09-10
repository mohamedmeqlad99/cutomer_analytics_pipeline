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

# Define the output file path
output_file = os.path.join(output_dir, 'customer_data.csv')

# Open the CSV file to write the data and ensure it's properly managed
try:
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)  # Write the header row

        # Generate fake data for each customer and write to the file
        for _ in range(num_records):
            customer_data = [
                fake.unique.uuid4(),      # customer_id
                fake.first_name(),        # first_name
                fake.last_name(),         # last_name
                fake.email(),             # email
                fake.phone_number(),      # phone_number
                fake.address(),           # address
                fake.date_of_birth(),     # date_of_birth
            ]
            writer.writerow(customer_data)  # Write the customer data
            # Optional: print for debugging
            # print(customer_data)

    print(f"File successfully written to: {output_file}")
except Exception as e:
    print(f"Error occurred: {e}")
