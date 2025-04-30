### Write a python program to generate dummy data for a healthcare file uploading web application that parses the data for compliance checking. 
### Create a .txt file with customer dummy data that allows for user input for the number of records to be generated.
### All the fields can be randomly generated using the Faker library and the random library.
### All the fields will be separated by a pipe character. 
### The .txt file should contain the following fields: 
        # Project ID, Customer ID, First Name, Last Name, Sex, Birthday, Street Address, City, State
### Add a compliance checking field called pregnant with the following values: 1=Yes, 2=No, NULL
### If the Sex is F, then pregnant should be randomly generated with the following values: 1=Yes, 2=No
### If the Sex is M, then pregnant should be NULL
### Include two additional fields for compliance checking: in_care and care_type
        # The in_care field should be randomly generated with the following values: 1=Yes, 2=No, 3=Unknown
        # The care_type field should be randomly generated with the following values: A=cancer, B=heart, C=diabetes, D=mental health, E=other
        # IF in_care is 1, then care_type should be randomly generated with the following values: A=cancer, B=heart, C=diabetes, D=mental health, E=other
        # IF in_care is 2 or 3, then care_type should be N/A  
### The .txt should contain a header and trailer for the data. 
### The header should contain the following fields:
##      # Header: H (for header) Project ID, Record Count, Date Created
### The trailer should contain the following fields:
        # Trailer: T (for trailer) Record Count, Date Created
### The naming convetion for the file should be as follows:
        # Project ID_Record Count_Date Created.txt
### The file should be saved in the same directory as the python script.

import os
import random
from faker import Faker
from datetime import datetime

# Initialize Faker
fake = Faker()

# User input for Project ID and Record Count to be generated and declared as global variables
project_id = input("Enter Project ID: ")
record_count = int(input("Enter number of records to be generated: "))

# Get current date to use in Header and Trailer
date_created = datetime.now().strftime("%Y%m%d") 

# Generate header of the file with Project ID, Record Count, Date Created
def generate_header(project_id, record_count):
    header = f"H|{project_id}|{date_created}|{record_count}\n"
    return header
# Generate trailer of the file with Record Count, Date Created
def generate_trailer(project_id, record_count):
    trailer = f"T|{project_id}|{date_created}|{record_count}\n"
    return trailer
# Generate dummy data for the file
def generate_dummy_data(record_count):
    data = [] # List to hold the generated data for the file
    for i in range(record_count): # Loop to generate the specified number of records
        customer_id = fake.bothify(text='P#####') # An extra loop could be considered here (or a while True loop) to ensure unique customer IDs because there might be some overlap at some point. Check your database frequently via querying to ensure uniqueness.
        first_name = fake.first_name()
        last_name = fake.last_name()
        sex = random.choice(['M', 'F'])
        if sex == 'M':
            pregnant = ''
        elif sex == 'F':
            pregnant = random.choice(['1', '2'])
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=65)
        street_address = fake.street_address()
        city = fake.city()
        state = fake.state()
        in_care = random.choice(['1', '2', '3']) # Randomly generated in_care value for compliance checking 1=Yes, 2=No, 3=Unknown
        if in_care == '1':
            care_type = random.choice(['A', 'B', 'C', 'D', 'E']) # Randomly generated care type for compliance checking A=cancer, B=heart, C=diabetes, D=mental health, E=other
        elif in_care == '2' or '3':
            care_type = 'N/A' # Not applicable if in_care is No or Unknown
        data.append(f"{project_id}|{customer_id}|{first_name}|{last_name}|{sex}|{birthday}|{street_address}|{city}|{state}|{pregnant}|{in_care}|{care_type}\n")
    return data
# Main function to generate and compile the file 
def generate_file(project_id, record_count):
    header = generate_header(project_id, record_count)
    data = generate_dummy_data(record_count)
    trailer = generate_trailer(project_id, record_count)
    file = header + "".join(data) + trailer
    return file
# User input for Project ID and Record Count

def main():
    # Generate the file content
    file_content = generate_file(project_id, record_count)
    
    # Define the folder and file name
    folder_name = "testFiles"
    os.makedirs(folder_name, exist_ok=True)  # Ensure the folder exists
    file_name = f"{project_id}_{date_created}_{record_count}.txt"
    file_path = os.path.join(folder_name, file_name)  # Combine folder and file name
    
    # Write the file to the specified folder
    with open(file_path, "w") as file:
        file.write(file_content)
    
    print(f"File {file_name} generated successfully.")

if __name__ == "__main__":
    main()
# The code generates a file with dummy data for a file uploading web application that parses the data for compliance checking.







