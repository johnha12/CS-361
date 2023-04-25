from CS361UI2 import get_user_choice


def main():
    print("Welcome to the Dessert Bar App!")
    input("Press enter to begin: ")
    """
    UI
    """
    choice = get_user_choice()
    print(f"This is main. You chose {choice}")


if __name__ == "__main__":
    main()
