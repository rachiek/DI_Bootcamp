
#Excercise 1
#You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result_dict = dict(zip(keys, values))

print(result_dict)

#Excercise 2

# Write a program that calculates the total cost of movie tickets for a family based on their ages.

# Family members’ ages are stored in a dictionary.
# The ticket pricing rules are as follows:
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $15

# Loop through the family dictionary to calculate the total cost.
# Print the ticket price for each family member.
# Print the total cost at the end.

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0

for name, age in family.items ():
    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15
    
    total_cost += ticket_price
    print (f"{name} (Age {age}): ${ticket_price}")

print (f'The total cost is: ${total_cost}')

# Excercise 3
# create and manipulate a dictionary that contains information about the Zara brand.
# create a dictionary called brand with the provided data.
# Modify and access the dictionary as follows:
# Change the value of number_stores to 2.
# Print a sentence describing Zara’s clients using the type_of_clothes key.
# Add a new key country_creation with the value Spain.
# Check if international_competitors exists and, if so, add “Desigual” to the list.
# Delete the creation_date key.
# Print the last item in international_competitors.
# Print the major colors in the US.
# Print the number of keys in the dictionary.
# Print all keys of the dictionary.

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

brand["number_stores"] = 2
print(f'Zara services a number of clients including{brand['type_of_clothes']}')
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
  brand["international_competitors"].append("Desigual")
brand.pop('country_creation')
print(brand["international_competitors"][-1])
print(brand["major_color"]['US'])
print(len(brand))
print(print(list(brand.keys())))

#bonus
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 7000
}

merged_zara = brand | more_on_zara
print (merged_zara)

#Excercise 4
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
char_index = {}

for x in range(len(users)):
    character = users [x]
    char_index [character] = x

print (char_index)

char_index_rev = {}

for y in range(len(users)):
    character = users [y]
    char_index_rev [y] = character

print (char_index_rev)

sorted_dict = {character:index for index, character in enumerate(sorted(users))}
print (sorted_dict)
