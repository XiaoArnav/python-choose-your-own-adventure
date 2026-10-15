def get_choice(prompt, options):
    """Display numbered options and return a valid choice."""
    while True:
        print(f"\n{prompt}")
        for number, option in enumerate(options, start=1):
            print(f"{number}. {option}")

        choice = input("> ").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)

        print(f"Please enter a number from 1 to {len(options)}.")


def forest_path():
    print("\nYou enter the Whispering Forest. The trees lean toward you.")
    choice = get_choice(
        "What do you do?",
        [
            "Follow a trail of glowing mushrooms",
            "Climb a nearby oak tree",
            "Call out for help",
        ],
    )

    if choice == 1:
        print("\nThe mushrooms lead you to a hidden fairy village.")
        print("The fairies crown you Guardian of the Forest. You win!")
    elif choice == 2:
        print("\nFrom the treetop, you spot a castle beyond the forest.")
        print("You follow the view toward a new adventure. You survive!")
    else:
        print("\nA friendly fox answers your call and guides you home.")
        print("You made a new friend. You win!")


def cave_path():
    print("\nYou enter a dark cave. Water drips somewhere in the distance.")
    choice = get_choice(
        "What do you do?",
        [
            "Light a torch and explore",
            "Shout into the darkness",
            "Leave the cave",
        ],
    )

    if choice == 1:
        print("\nYour torch reveals a sleeping dragon guarding a treasure chest.")
        print("You quietly leave the treasure and escape safely. You survive!")
    elif choice == 2:
        print("\nYour shout wakes the dragon!")
        print("Luckily, the dragon is friendly and invites you to dinner. You win!")
    else:
        print("\nYou leave the cave and discover a village nearby.")
        print("The villagers welcome you as a hero. You win!")


def river_path():
    print("\nYou arrive at a fast-flowing river with no bridge in sight.")
    choice = get_choice(
        "How will you cross?",
        [
            "Build a raft from fallen branches",
            "Search for a bridge",
            "Swim across",
        ],
    )

    if choice == 1:
        print("\nYour raft holds together and carries you safely across.")
        print("On the other side, you find a bag of gold. You win!")
    elif choice == 2:
        print("\nYou find an ancient stone bridge covered in vines.")
        print("It leads you to a peaceful kingdom. You win!")
    else:
        print("\nThe current is too strong!")
        print("River sprites rescue you and teach you river magic. You survive!")


def play_game():
    print("\n" + "=" * 45)
    print("        THE LOST KINGDOM ADVENTURE")
    print("=" * 45)
    print("\nYou wake up at the edge of a mysterious kingdom.")
    print("Three paths lie ahead.")

    choice = get_choice(
        "Which path will you take?",
        [
            "The Whispering Forest",
            "The Dragon's Cave",
            "The Rushing River",
        ],
    )

    if choice == 1:
        forest_path()
    elif choice == 2:
        cave_path()
    else:
        river_path()


def main():
    print("Welcome, brave adventurer!")

    while True:
        play_game()
        again = input("\nWould you like to play again? (y/n): ").strip().lower()

        if again != "y":
            print("\nThanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
