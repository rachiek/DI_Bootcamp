# 🌟 Exercise 1 — Cats

from time import time


class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age  = cat_age

# Step 1: Create three cat objects
cat1 = Cat("Fluffy", 3)
cat2 = Cat("Whiskers", 7)
cat3 = Cat("Mittens", 1)

# Step 2: Write a function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    if (cat1.age >= cat2.age) and (cat1.age >= cat3.age):
      return cat1
    elif (cat2.age >= cat1.age) and (cat2.age >= cat3.age):
      return cat2
    else:
      return cat3

# Step 3: Print the result
oldest = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")


# 🌟 Exercise 2 — Dogs

# Step 1: Create the Dog class
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"print {self.name} jumps {self.height*2} cm high!")

# Step 2: Create dog objects
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Bella", 35)

# Step 3: Print details and call methods

davids_dog.bark()
sarahs_dog.bark()

davids_dog.jump()
sarahs_dog.jump()

# Step 4: Compare sizes
if davids_dog.height > sarahs_dog.height:
  print(f"{davids_dog.name} is bigger than {sarahs_dog.name}")
elif sarahs_dog.height > davids_dog.height:
  print(f"{sarahs_dog.name} is bigger than {davids_dog.name}")
else:
  print(f"They are the same size!")

# 🌟 Exercise 3 — Song

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
          print(line)

stairway = Song([
    "There's a lady who's sure",
    "all that glitters is gold",
    "and she's buying a stairway to heaven"
])


stairway.sing_me_a_song()

# 🌟 Exercise 4 — Zoo

class Zoo:
  def __init__(self, zoo_name):
    self.name = zoo_name
    self.animals = []     # <--- list attrubute, starts empty

  def add_animal(self, new_animal):
    if new_animal not in self.animals: # no duplicates
      self.animals.append(new_animal)

  def get_animals(self):
    print(self.animals)

  def sell_animal(self, animal_sold):
    if animal_sold in self.animals:
      self.animals.remove(animal_sold)

  def sort_animals(self):
      groups = {}

      for animal in sorted(self.animals): # sort first: Baboon, Bear, Cat...
        letter = animal[0]                # first letter: 'B', 'B', 'C'...
        if letter not in groups:
          groups[letter] = []             # new letter? create empty list
        groups[letter].append(animal)     # add animal to its letter's list

      return groups

  def get_groups(self):
      groups = self.sort_animals()
      for letter, animals in groups.items():
        print(f"{letter}: {animals}")

# Create a zoo and test it
brooklyn_safari = Zoo("Brooklyn Safari")
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.get_groups()

# Bonus: Modify the add_animal() method to get *args so you dont need to repeat 
# the method each time for a new animal, you can pass multiple animals names separated by a comma.
Zoo.add_animal = lambda self, *new_animals: [self.animals.append(animal) for animal in new_animals if animal not in self.animals]
   
brooklyn_safari = Zoo("Brooklyn Safari")
brooklyn_safari.add_animal("Giraffe", "Bear", "Baboon")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.get_groups()

