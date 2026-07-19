# # Excercise 1: 
# nstructions:

# Use the provided Pets and Cat classes to create a Siamese breed, instantiate cat objects, and use the Pets class to manage them.
# See the example below, before diving in.

# Step 1: Create the Siamese Class
# Create a class called Siamese that inherits from the Cat class.
# You can add any specific attributes or methods for the Siamese breed, or leave it as is if there are no unique behaviors.
# Step 2: Create a List of Cat Instances
# Create a list called all_cats that contains instances of Bengal, Chartreux, and Siamese cats.
# Example: all_cats = [bengal_obj, chartreux_obj, siamese_obj]
# Give each cat a name and age.
# Step 3: Create a Pets Instance
# Create an instance of the Pets class called sara_pets, passing the all_cats list as an argument.git 
# Step 4: Take Cats for a Walk

# Call the walk() method on the sara_pets instance.
# This should print the result of calling the walk() method on each cat in the list.

class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is just walking around"


class Siamese(Cat):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def walk(self):
        return f"{self.name} the Siamese is just walking around"


all_cats = [
    Cat("Bengal", 3),
    Cat("Chartreux", 5),
    Siamese("Luna", 2, "Cream")
]

sara_pets = Pets(all_cats)

sara_pets.walk()

#Excercise 2:
# Step 1: Create the Dog Class
# Create a class called Dog with name, age, and weight attributes.
# Implement a bark() method that returns “<dog_name> is barking”.
# Implement a run_speed() method that returns weight / age * 10.
# Implement a fight(other_dog) method that returns a string indicating which dog won the fight, based on run_speed * weight.
# Step 2: Create Dog Instances
# Create three instances of the Dog class with different names, ages, and weights.
# Step 3: Test Dog Methods

# Call the bark(), run_speed(), and fight() methods on the dog instances to test their functionality.
class Dog:
    def __init__(self, name, age, weight, breed):
        self.name = name
        self.age = age
        self.weight = weight
        self.breed = breed

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        my_speed = self.run_speed() * self.weight
        their_speed = other_dog.run_speed() * other_dog.weight

        if my_speed > their_speed:
            return f"{self.name} wins!"
        elif their_speed > my_speed:
            return f"{other_dog.name} wins!"
        else:
            return "It's a draw!"


d1 = Dog("Rex", 4, 20.0, "German Shepherd")
d2 = Dog("Bella", 2, 12.0, "Poodle")
d3 = Dog("Max", 6, 30.0, "Saint Bernard")

print(d1.bark())
print(d2.bark())
print(d3.bark())
print(d1.run_speed())
print(d2.run_speed())
print(d3.run_speed())
print(d1.fight(d2))
print(d1.fight(d3))
print(d2.fight(d3))

#Excercise 3

# # Instructions:

# # Step 1: Import the Dog Class

# # In a new Python file, import the Dog class from the previous exercise.


# # Step 2: Create the PetDog Class

# # Create a class called PetDog that inherits from the Dog class.
# # Add a trained attribute to the __init__ method, with a default value of False.
# # trained means that the dog is trained to do some tricks.
# # Implement a train() method that prints the output of bark() and sets trained to True.
# # Implement a play(*args) method that prints “<dog_names> all play together”.
# # *args on this method is a list of dog instances.
# # Implement a do_a_trick() method that prints a random trick if trained is True.
# # Use this list for the ramdom tricks:
# # tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
# # Choose a random index from it each time the method is called.


# # Step 3: Test PetDog Methods

# # Create instances of the PetDog class and test the train(), play(*args), and do_a_trick() metho
import random

class PetDog(Dog):
    def __init__(self, name, age, weight, breed, trained=False):
     super().__init__(name, age, weight, breed)
     self.trained = trained
     
    def train(self):
        print(self.bark())
        self.trained = True
    
    def play(self, *doginstances): 
        dog_names = [dog.name for dog in doginstances]
        print(f"{', '.join(dog_names)} all play together")  
    
    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            random_trick = random.choice(tricks)
            print(f"{self.name} {random_trick}")
        else:
            print(f"{self.name} is not trained yet.")

d1 = PetDog("Rex", 4, 20.0, "German Shepherd")
d2 = PetDog("Bella", 2, 12.0, "Poodle")
d3 = PetDog("Max", 6, 30.0, "Saint Bernard")

d1.train()
d1.play(d2, d3)
d1.do_a_trick() 

#Excercise 4
# Instructions:

# Step 1: Create the Person Class
# Define a Person class with the following attributes:
# first_name
# age
# last_name (string, should be initialized as an empty string)
# Add a method called is_18():
# It should return True if the person is 18 or older, otherwise False.

# Step 2: Create the Family Class
# Define a Family class with:
# A last_name attribute
# A members list that will store Person objects (should be initialized as an empty list)
# Add a method called born(first_name, age):
# It should create a new Person object with the given first name and age.
# It should assign the family’s last name to the person.
# It should add this new person to the members list.

# Add a method called check_majority(first_name):
# It should search the members list for a person with that first_name.
# If the person exists, call their is_18() method.
# If the person is over 18, print:
# "You are over 18, your parents Jane and John accept that you will go out with your friends"
# Otherwise, print:
# "Sorry, you are not allowed to go out with your friends."


# Add a method called family_presentation():
# It should print the family’s last name.
# Then, it should print each family member’s first name and age.


# Expected Behavior:

# Once implemented, your program should allow you to:

# Create a family with a last name.
# Add members to the family using the born() method.
# Use check_majority() to see if someone is allowed to go out.
# Display family information with family_presentation().
# Don’t forget to test your classes by creating an instance of Family, adding members, and calling each method to see the expected output.



class Person:
    def __init__(self, first_name, age,):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name): 
        self.last_name = last_name
        self.members = []
    
    def born(self, first_name, age):
        new_member = Person(first_name, age)
        new_member.last_name = self.last_name
        self.members.append(new_member)
    
    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(f"You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print(f"Sorry, you are not allowed to go out with your friends.")
                return
        print(f"No member found with the first name {first_name}.")

    def family_presentation(self):
        print(f"Family Last Name: {self.last_name}")
        for member in self.members:
            print(f"First Name: {member.first_name}, Age: {member.age}")

family1 = Family("Smith")
family1.born("Alice", 20)
family1.born("Bob", 16)
family1.born("Jane", 50)
family1.born("John", 52)
family1.check_majority("Alice")
family1.check_majority("Bob")
family1.family_presentation()