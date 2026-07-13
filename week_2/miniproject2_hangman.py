# Use python to create a Hangman game.



# Instructions
# The computer choose a random word and mark stars for each letter of each word.
# Then the player will guess a letter.
# If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
# If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
# The player will continue guessing letters until they can either solve the word(s) (or phrase) or all six body parts are on the gallows.
# The player can’t guess the same letter twice.


# Starter code
# Here is a piece of code that will give you a random word.


import random

wordslist = [
    'correction', 'childish', 'beach', 'python', 'assertive', 
    'interference', 'complete', 'share', 'credit card', 'rush', 'south'
]
word = random.choice(wordslist) 

### YOUR CODE STARTS FROM HERE ###

# Visual states for the gallows (0 wrong guesses up to 6 wrong guesses)
HANGMAN_STAGES = [
    """
       --------
       |      |
       |      
       |    
       |      
       |     
    - - - - -
    """,
    """
       --------
       |      |
       |      O
       |    
       |      
       |     
    - - - - -
    """,
    """
       --------
       |      |
       |      O
       |      |
       |      |
       |     
    - - - - -
    """,
    """
       --------
       |      |
       |      O
       |     /|
       |      |
       |     
    - - - - -
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |      |
       |     
    - - - - -
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |      |
       |     / 
    - - - - -
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |      |
       |     / \\
    - - - - -
    """
]

# Track guessed letters
guessed_letters = set()
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman!")

# Game loop
while wrong_guesses < max_wrong:
    # Print the current state of the gallows
    print(HANGMAN_STAGES[wrong_guesses])
    
    # Build the hidden word display (stars for letters, spaces stay as spaces)
    display_word = ""
    for letter in word:
        if letter == " ":
            display_word += " "
        elif letter in guessed_letters:
            display_word += letter
        else:
            display_word += "*"
            
    print(f"Word: {display_word}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    
    # Check if the player won
    if "*" not in display_word:
        print("\n🎉 Congratulations! You guessed the word correctly!")
        break
        
    # Get player input
    guess = input("Guess a letter: ").lower().strip()
    
    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single valid letter.")
        continue
    if guess in guessed_letters:
        print(f"❌ You already guessed '{guess}'. Try a different letter.")
        continue
        
    # Add to guessed list
    guessed_letters.add(guess)
    
    # Check if guess is in the word
    if guess in word:
        print(f"✨ Good job! '{guess}' is in the word.")
    else:
        print(f"💀 Oops! '{guess}' is not in the word.")
        wrong_guesses += 1

# If the player runs out of guesses
if wrong_guesses == max_wrong:
    print(HANGMAN_STAGES[wrong_guesses])
    print("💥 Game Over! The gallows are full.")
    print(f"The word was: '{word}'")

