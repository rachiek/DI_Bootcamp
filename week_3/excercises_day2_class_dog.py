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