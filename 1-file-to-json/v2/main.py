import json

# Set the divider string
divider = ','

# Open the input file
with open('input.txt', 'r') as f:
  lines = f.readlines()

# Create an empty dictionary to store the key-value pairs
data = {}

# Iterate through the lines in the file
for line in lines:
  # Split the line on the divider string
  key, value = line.strip().split(divider)

  # Add the key-value pair to the dictionary
  data[key] = value

# Open the output file
with open('output.json', 'w') as f:
  # Write the dictionary to the output file as JSON
  json.dump(data, f)