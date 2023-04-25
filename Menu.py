import json

# Open the JSON file
with open('Menu.json') as f:
    # Load the JSON data
    data = json.load(f)

# Loop through each item in the array
for item in data:
    # Print the id and name properties
    print(f"ID-{item['id']} | Name-{item['name']} | Price-${item['price']:.2f}")
    