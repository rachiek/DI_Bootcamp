#Excercise 1: 

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

# oal: Create a PetDog class that inherits from Dog and adds training and tricks.



# Key Python Topics:

# Inheritance
# super() function
# *args
# Random module


# Instructions:

# Step 1: Import the Dog Class

# In a new Python file, import the Dog class from the previous exercise.


# Step 2: Create the PetDog Class

# Create a class called PetDog that inherits from the Dog class.
# Add a trained attribute to the __init__ method, with a default value of False.
# trained means that the dog is trained to do some tricks.
# Implement a train() method that prints the output of bark() and sets trained to True.
# Implement a play(*args) method that prints “<dog_names> all play together”.
# *args on this method is a list of dog instances.
# Implement a do_a_trick() method that prints a random trick if trained is True.
# Use this list for the ramdom tricks:
# tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
# Choose a random index from it each time the method is called.


# Step 3: Test PetDog Methods

# Create instances of the PetDog class and test the train(), play(*args), and do_a_trick() metho