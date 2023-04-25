import curses


def get_user_choice():
    # Clear the screen
    stdscr = curses.initscr()
    stdscr.clear()

    # Turn on arrow key recognition
    stdscr.keypad(True)

    # Define a list of choices
    choices = ["View Menu", "View Order", "Submit Order", "Quick Add to Order", "About", "Exit/Restart"]

    # Start at position (0,0)
    y, x = 0, 0

    while True:
        # Clear the screen
        stdscr.clear()

        # Print the choices
        for i, choice in enumerate(choices):
            if i == y:
                stdscr.addstr(f"> {choice}\n")
            else:
                stdscr.addstr(f"  {choice}\n")

        # Wait for user input
        key = stdscr.getch()

        # Handle arrow key input
        if key == curses.KEY_UP:
            y -= 1
        elif key == curses.KEY_DOWN:
            y += 1

        # Handle Enter key input
        elif key == 10:
            if y == len(choices) - 1:
                return choice
            else:
                # Do something with the selected choice
                print(f"You chose {choices[y]}")
                stdscr.getch()

        # Keep the cursor within the range of choices
        y = max(0, min(len(choices) - 1, y))

    # Turn off arrow key recognition
    stdscr.keypad(False)
    curses.endwin()
