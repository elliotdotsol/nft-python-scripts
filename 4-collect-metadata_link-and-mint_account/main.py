import json

# Define the names of the input and output files
cache_file_name = "cache.json"
cmid_file_name = "cmid.json"
output_file_name = "output.json"

# Open the first JSON file and load the data
try:
    with open(cache_file_name, "r") as cache_file:
        cache_data = json.load(cache_file)
except FileNotFoundError:
    print(cache_file_name + " not found.")
    cache_data = {}

# Extract the necessary information from the first JSON file
try:
    metadata_links = [item["metadata_link"] for item in cache_data["items"].values() if "metadata_link" in item and "collection" not in item["metadata_link"]]
except KeyError:
    print("metadata_link not found in cache.json")
    metadata_links = []

# Initialize the mint_accounts variable
mint_accounts = []

# Extract the necessary information from the second JSON file
try:
    with open(cmid_file_name, "r") as cmid:
        cmid_data = json.load(cmid)
        mint_accounts = [item["mint_account"] for item in cmid_data if "mint_account" in item]
except FileNotFoundError:
    print(cmid_file_name + " not found.")
except KeyError:
    print("mint_account not found in " + cmid_file_name)

# Write the combined data to a new JSON file
if metadata_links and mint_accounts:
    # Use the zip function to combine the metadata_links and mint_accounts lists
    combined_data = zip(metadata_links, mint_accounts)
    # Create a list of dictionaries where each dictionary contains a "mint_account" key and a "new_uri" key
    output_data = [{"mint_account": mint_account, "new_uri": new_uri} for new_uri, mint_account in combined_data]
    with open(output_file_name, "w") as output_file:
        json.dump(output_data, output_file)
    print("Data written successfully to " + output_file_name)
else:
    print("Not enough data to write to " + output_file_name)
