# Build a Farm class with:
# Method	What it does
# __init__(farm_name)	Stores name, creates empty animals dict
# add_animal(animal_type, count=1)	Adds/increments animal count in dict
# get_info()	Returns formatted string with farm name, all animals and counts, and "E-I-E-I-0!"
# Test it:

# macdonald = Farm("McDonald")
# macdonald.add_animal('cow', 5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())
# Expected output:

# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!
# Bonus — get_animal_types(): Returns a sorted list of all animal types.

# Bonus — get_short_info(): Returns: "McDonald's farm has cows, goats and sheeps." (adds "s" to animal names with count > 1)

# Bonus — **kwargs upgrade for add_animal: macdonald.add_animal(cow=5, sheep=2, goat=12) — all at once!

class Farm: 
   
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
          self.animals[animal_type] += count # already exists: increment
        else:
          self.animals[animal_type] = count  # new animal: create entry

    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
          info += f"{animal}  : {count} \n"
        info += "\n   E-I-E-I-O"

        return info
# Test
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())