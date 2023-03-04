import json

# Open the input file and read the contents
with open("input.txt", "r") as f:
    contents = f.read()

# Split the contents into lines and extract the key-value pairs
lines = contents.split("\n")
data = {}
for line in lines:
    key, value = line.split(",")
    data[key] = int(value)

# Write the dictionary to a JSON file
with open("output.json", "w") as f:
    json.dump(data, f)
