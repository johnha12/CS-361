while True:
    # Take user input
    user_input = input("Are you sure? y/n: ")

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
