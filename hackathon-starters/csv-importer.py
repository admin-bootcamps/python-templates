import csv  # Import CSV module to read CSV files
import json  # Import JSON module to format output for readability

headers = []  # Initialize an empty list to store CSV headers (field names)

# Define a function to read a CSV file and return its contents and headers
def csv_to_python_object(file_path):
    """
    Reads a CSV file and returns a list of dictionaries.
    Each dictionary represents a row with column headers as keys.
    """
    data = []  # Initialize an empty list to store rows as dictionaries
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)  # Create a DictReader to parse rows into dictionaries
        headers = reader.fieldnames  # Extract the column headers from the first row
        for row in reader:
            data.append(row)  # Append each row dictionary to the data list
    return data, headers  # Return both the data list and the headers list

# Specify the path to the CSV file (update as needed)
file_path = 'datasets/csv-animals-dataset/zoo2.csv'  # Replace with your CSV file path

# Call the function to load CSV data and headers
data_list, headers = csv_to_python_object(file_path)

# Format headers as a pretty-printed JSON string for readable output
formatted_headers = json.dumps(headers, indent=4)

# Format the first row of data as a pretty-printed JSON string for example output
formatted_data = json.dumps(data_list[0], indent=4)

# Count the number of rows in the dataset
rows = len(data_list)

# Print the formatted headers, example row, and row count
print(f"\n-------\nImported CSV\n-------\nCategories: {formatted_headers}\n-------\nExample (first list item): {formatted_data}\n-------\nData points (number of rows): {rows}\n-------\nEnd")
