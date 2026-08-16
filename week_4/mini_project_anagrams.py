from anagram_checker import AnagramChecker
import os


def main():
    file_path = os.path.join(os.path.dirname(__file__), "sowpods.txt")
    checker = AnagramChecker(file_path)

    while True:
        print("\n=== Anagram Menu ===")
        print("1. Enter a word")
        print("2. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            word = input("Enter a word: ").strip()

            if len(word.split()) != 1:
                print("Error: Please enter only one word.")
                continue

            if not word.isalpha():
                print("Error: Only alphabetic characters are allowed.")
                continue

            normalized_word = word.lower()
            anagrams = checker.get_anagrams(normalized_word)

            if anagrams:
                print(f"\nAnagrams for '{word}':")
                print(", ".join(sorted(anagrams)))
            else:
                print(f"No anagrams found for '{word}'.")

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()
