import json
import curses

# Open the JSON file
with open('About.json') as f:
    # Load the JSON data
    data = json.load(f)
    paragraph = data["paragraph"]
    

def main(stdscr):
    # Turn on arrow key recognition
    stdscr.keypad(True)

    # Define the list of choices
    choices = ["Home"]

    # Start at position (0,0)
    y, x = 0, 0

    while True:
        # Clear the screen
        stdscr.clear()

        # Print the paragraph from the JSON file
        stdscr.addstr(f"{paragraph}\n\n")

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
                break
            else:
                # Do something with the selected choice
                if choices[y] == "Home":
                    # Go back to the home screen
                    main(stdscr)

        # Keep the cursor within the range of choices
        y = max(0, min(len(choices) - 1, y))

    # Turn off arrow key recognition
    stdscr.keypad(False)


if __name__ == "__main__":
    curses.wrapper(main)
