# Path to the existing class map file
input_file = 'class_map_clean.txt'
# Path to the output file where the new formatted map will be saved
output_file = 'class_map_with_quotes.txt'

# List to store the formatted lines
formatted_lines = []

# Read the class map from the input file
with open(input_file, 'r') as f:
    for line in f:
        # Strip any extra spaces/newlines
        line = line.strip()

        # Split the line by colon to get label and bird species name
        label, bird_name = line.split(': ')

        # Add single quotes around bird name, and add a comma at the end
        formatted_line = f"{label}: '{bird_name}',"
        formatted_lines.append(formatted_line)

# Save the new formatted class map to a new file
with open(output_file, 'w') as f_out:
    for formatted_line in formatted_lines:
        f_out.write(f"{formatted_line}\n")

print(f"Class map with quotes and commas has been saved to {output_file}")
