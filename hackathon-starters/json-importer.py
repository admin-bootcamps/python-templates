import json  # Import the built-in JSON module to work with JSON files

# Function to load a JSON file and return the parsed Python object
def json_to_python_object(file_path):
    # Open the file in read mode with UTF-8 encoding
    with open(file_path, 'r', encoding="UTF-8") as file:
        data = json.load(file)  # Load and parse the JSON content into a Python object (usually a list or dict)
    return data  # Return the loaded data


# Define the path to the JSON file (update this path as needed)
file_path = 'datasets/fake_news_data.json'  # Replace with your JSON file path

# Call the function and store the resulting data in 'data_list'
data_list = json_to_python_object(file_path)

# Calculate the number of items (rows) in the list
rows = len(data_list)

# Format the entire JSON data into a pretty-printed string for display
formatted_data = json.dumps(data_list, indent=4)

# Print the formatted JSON and the number of data items
print(f"\n-------\nImported JSON:\n-------\nExample (first list item): {formatted_data}\n-------\nData points (number of items): {rows}\n-------\nEnd")
