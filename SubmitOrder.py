import json

# Open the JSON file
with open('Menu.json') as f:
    # Load the JSON data
    data = json.load(f)


while True:
    # Take user input
    print("Your total is : $17.99")
    # Loop through each item in the array
    for item in data:
        # Print the id and name properties
        print(f"ID-{item['id']} | Name-{item['name']} | Price-${item['price']:.2f}")
    user_input = input("Would you like to submit your order? y/n: ")

    # Check for 'h'
    if user_input.lower() == 'y':
        print("You said yes!")
        break
    if user_input.lower() == 'n':
        print("You said no.")
        break

    # Convert input to integer
    try:
        user_string = int(user_input)
        print(f"You entered the Item ID: {user_string}")
        # Now have integer
        # Call your function here with user_int as argument
        break
    except ValueError:
        print("Invalid input. Please enter y/n.")


# now have integer
def confirm(user_string):
    if user_string == 0:
        print("return home")
    # if user_int is in menu, customize.
    else:
        print("customize? y/n/c")
