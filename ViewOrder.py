import curses
import json


def main(stdscr):
    # Turn on arrow key recognition
    stdscr.keypad(True)

    # Open the JSON file
    with open('A5ViewOrder.json') as f:
        # Load the JSON data
        data = json.load(f)

    # Define a list of choices
    choices = ["Home"] + [f"ID-{item['id']} | Name-{item['name']} | Price-${item['price']:.2f}" for item in data]

    # Start at position (0,0)
    y, x = 2, 0

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
            if y == 0:
                # Do something for the "Home" choice
                stdscr.addstr("You chose Home\n")
                stdscr.getch()
            else:
                # Do something with the selected choice
                selected_item = data[y-1]
                stdscr.addstr(f"You chose {selected_item['name']} for ${selected_item['price']:.2f}\n")
                stdscr.getch()

        # Keep the cursor within the range of choices
        y = max(0, min(len(choices) - 1, y))

    # Turn off arrow key recognition
    stdscr.keypad(False)


if __name__ == "__main__":
    curses.wrapper(main)
