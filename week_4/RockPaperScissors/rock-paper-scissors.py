
from game import Game

def get_user_menu_choice():
    print(" ")
    print("\n=== Main Menu ===")
    print("p - Play A New pGame")
    print("s - Show Scores")
    print("q - Quit")
    print(" ")
    choice = input("Please choose an option p, s, or q: ").strip().lower()

    while choice not in ['p', 's', 'q']:
        print("Invalid choice. Please select p, s, or q.")
        choice = input("Please choose an option p, s, or q: ").strip().lower()

    return choice

def print_results(results):
    print("\n=== Game Results ===")
    print(f"Wins: {results['win']}")
    print(f"Draws: {results['draw']}")
    print(f"Losses: {results['loss']}")

def main():
    results = {'win': 0, 'draw': 0, 'loss': 0}

    while True: 
        choice = get_user_menu_choice()

        if choice == 'p':
            game = Game()
            result = game.play()

            if result == "win":
                results['win'] += 1
            elif result == "draw":
                results['draw'] += 1
            else:
                results['loss'] += 1
        elif choice == 's':
            print_results(results)
        elif choice == 'q':
            print_results(results)
            print("Thank you for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()