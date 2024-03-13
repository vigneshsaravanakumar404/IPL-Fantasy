# Imports
import json
import os
import json

# Variables
DATA = "ipl_male_json"

# Functions
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Remove Old Files
print("Removing old files...")
for filename in os.listdir(DATA):
    if filename.endswith(".json"):
        file_path = os.path.join(DATA, filename)
        with open(file_path, "r") as file:
            data = json.load(file)
        file_date = data.get("info", {}).get("dates", [])[0]
        
        if file_date and file_date >= "2023-01-01":
            print(f"Processing file: {filename}")
        else:
            os.remove(file_path)
            print(f"File removed: {filename}")
clear()
print("There are " + str(len(os.listdir(DATA))) + " files left.")
