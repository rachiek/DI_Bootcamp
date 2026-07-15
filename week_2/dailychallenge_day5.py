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
    
    def get_animal_types(self):
        return sorted(self.animals.keys())
    
    def get_short_info(self):
        animal_list = []
        for animal, count in self.animals.items():
            if count > 1:
                animal_list.append(animal + 's')  # pluralize
            else:
                animal_list.append(animal)
        animals_str = ', '.join(animal_list)
        return f"{self.name}'s farm has {animals_str}."
    

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())

Farm.add_animal = lambda self, **kwargs: [self.add_animal(animal, count) for animal, count in kwargs.items()]