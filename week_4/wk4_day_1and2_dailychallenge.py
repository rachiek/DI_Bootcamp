# Part 1: Quiz
# Object-Oriented Programming (OOP) Concepts
# What is a class?
# A class is a blueprint or a template for creating objects. It defines a set of attributes (data) and methods (functions) that the created objects will have. It acts as a user-defined data type.
# What is an instance?
# An instance is a specific, unique object created from a class. While a class provides the structure, an instance is the concrete realization of that structure in memory, holding its own specific data values.
# What is encapsulation?
# Encapsulation is the bundling of data and the methods that operate on that data into a single unit (a class). It often involves restricting direct access to some of an object's components, which is a way of preventing unintended interference and misuse of the internal state of an object.
# What is abstraction?
# Abstraction is the concept of hiding complex implementation details and showing only the necessary features of an object. It allows a user to interact with an object through a simplified interface without needing to understand the underlying logic.
# What is inheritance?
# Inheritance is a mechanism where a new class (subclass or child) derives attributes and behaviors from an existing class (superclass or parent). This promotes code reusability and establishes a hierarchy.
# What is multiple inheritance?
# Multiple inheritance is a feature of object-oriented programming where a subclass can inherit attributes and methods from more than one parent class.
# What is polymorphism?
# Polymorphism allows objects of different classes to be treated as objects of a common superclass. It most commonly manifests as the ability of different classes to respond to the same method call in their own specific way (e.g., method overriding).
# What is method resolution order or MRO?
# Method Resolution Order (MRO) is the set of rules that defines the order in which a programming language searches for a method in the hierarchy of classes. This is particularly important in languages that support multiple inheritance to resolve potential conflicts when multiple parent classes provide methods with the same name.

# Part 2: Create a Deck of Cards
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()


if __name__ == "__main__":
    deck = Deck()

    # 1. Check deck size
    print("Initial deck size:", len(deck.cards))

    # 2. Check uniqueness
    unique_cards = set(str(card) for card in deck.cards)
    print("Unique card count:", len(unique_cards))

    # 3. Show the first card before shuffle
    print("First card before shuffle:", deck.cards[0])

    # 4. Shuffle the deck
    deck.shuffle()
    print("First card after shuffle:", deck.cards[0])

    # 5. Deal one card
    dealt_card = deck.deal()
    print("Dealt card:", dealt_card)
    print("Deck size after deal:", len(deck.cards))