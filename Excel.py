import warnings
import pandas as pd
import time
import os
import math
import random

data_path = input('Enter The File Path of The database: ')
sub_heading = input(
    "Enter the name of the sub-heading for your data (Enter 'Name' as it is the subheading it will use): ")
emailAddress = input("Enter the email address: ")

start_time = time.time()

warnings.filterwarnings("ignore")

data = pd.read_excel(data_path)
print(f'\nYour Database:\n\n{data}\n')


def find_space(data, sub_heading, a):

    first_names, middle_names, last_names = [], [], []

    for i in range(len(data[sub_heading])):

        full_name = data[sub_heading][i+a]

        first_name, middle_name, last_name = full_name.split("//")

        middle_names.append(middle_name.lower())
        first_names.append(first_name.lower())
        last_names.append(last_name.lower())

    return first_names, middle_names, last_names


name_first, name_middle, name_last = find_space(data, sub_heading, 0)


for i in range(len(data[sub_heading])):
    n1, n2, n3 = data[sub_heading][i].split("//")
    data[sub_heading][i] = f"{n1} {n2} {n3}"


def generateEmails(first_names, middle_names, last_names, email_address):
    generatedEmails = []
    randomInt = math.floor(random.randint(1, 2))

    for i in range(len(first_names)):
        if randomInt == 1:
            generatedEmails.append(
                f"{first_names[i]}.{middle_names[i][0]}@{email_address}")
        else:
            generatedEmails.append(
                f"{first_names[i]}.{last_names[i][0]}@{email_address}")

    return generatedEmails


the_generated_emailIds = generateEmails(
    name_first, name_middle, name_last, emailAddress)

print(
    f"Generated Emails:\n{the_generated_emailIds[0:15]}...\n")

data2 = data.copy()

data2['Emails'] = the_generated_emailIds
print(f"New Data:\n{data2}\n")

file_path = os.path.abspath(__file__)
nameofpath = []
nameofpath.extend(file_path.split("\\"))
filePath = ""

for j in range(len(nameofpath) - 1):
    filePath += nameofpath[j]
    filePath += "/"

data2.to_excel(f"{filePath[0:-1]}/New Data.xlsx", index_label=None)
print(filePath[0:-1])

end_time = time.time()

print(f"Time taken to execute code: {end_time-start_time}")
