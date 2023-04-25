while True:
    # Take user input
    user_input = input("Enter an Item ID, or 'h' to return Home: ")

    # Check for 'h'
    if user_input.lower() == 'h':
        print("Returning Home...")
        break

    # Convert input to integer
    try:
        user_int = int(user_input)
        print(f"You entered the Item ID: {user_int}")
        # Now have integer
        # Call your function here with user_int as argument
        break
    except ValueError:
        print("Invalid input. Please enter an integer or 'h'.")


# now have integer
def quick_add(user_int):
    if user_int == 0:
        print("return home")
    # if user_int is in menu, customize.
    else:
        print("customize? y/n/c")
