"""
- csv - package that needs to be imported used to access the reader and writer operation functions for csv
- read operations
    - csv.reader - to get the csv reader object which is an iterable cursor, each iteration returining a row
    - next(<csv_reader_obj>) - skip the line (used to skip the header)

- write operations
    - csv.writer -  to get a csv object
    - two data structures can be used to write data into csv
        - list
        - dictionary
"""

import csv

#Reading a CSV file
with open("output.csv", "r") as file:
    csv_reader = csv.reader(file)

    next(csv_reader) # next skips the iteration in an iterator - in this case, we skip the header
    for row in csv_reader:
        print(row)

# Writing to a CSV file from a list of lists
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"],
]

with open("output.csv", mode="w", newline="") as file:

    csv_writer = csv.writer(file)

    # Write header
    csv_writer.writerow(data[0])

    # Write the rest of the rows
    csv_writer.writerows(data[1:])


# Writing to a CSV file from a dictionary:
data2 = [{"Name": "Matt", "Age": 46, "City": "Las Vegas"}]
with open("output.csv", mode="w", newline="") as file:

    fieldNames = ["Name", "Age", "City"]
    csv_writer = csv.DictWriter(file, fieldnames=fieldNames)

    csv_writer.writeheader()  # writes the field names
    csv_writer.writerows(data2) # writes rows from dictionary
