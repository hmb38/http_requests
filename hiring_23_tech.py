import json

from pprint import pprint


# Open the JSON file
with open("hiring.json", encoding = "utf8") as file:
    # Load the JSON data from the file
    hiring_data = json.load(file)

pprint(hiring_data)