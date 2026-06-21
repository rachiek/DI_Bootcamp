# Exercise 1: Favorite Numbers
# Key Python Topics:

# Sets
# Adding/removing items in a set
# Set concatenation (using union)


# Instructions:

# Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
# Note: Sets are unordered collections, so ensure no duplicate numbers are added.

# my_fav_numbers = {11,91,115}
# my_fav_numbers.add(25)
# my_fav_numbers.add(55)
# my_fav_numbers.remove(55)
# friend_fav_numbers = {2,16,87}
# our_fav_numbers = my_fav_numbers | friend_fav_numbers
# print(our_fav_numbers)

# 🌟 Exercise 2: Tuple
# Key Python Topics:

# Tuples (immutability)


# Instructions:

# Given a tuple of integers, try to add more integers to the tuple.
# # Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.
# tuple1 = (1,3,5,7)
# tuple1.append(3)


# 🌟 Exercise 3: List Manipulation
# Key Python Topics:

# Lists
# List methods: append, remove, insert, count, clear


# Instructions:

# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("Kiwi")
# basket.insert(0,"Apples")
# print(basket.count("Apples"))
# basket.clear()
# print(basket)

# 🌟 Exercise 4: Floats
# Key Python Topics:

# Lists
# Floats and integers
# Range generation


# Instructions:

# Recap: What is a float? What’s the difference between a float and an integer?
# Create a list containing the following sequence of mixed types: floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?

# mixed_list = []
# current_num = 1.5
    
# while current_num <= 5:
#     if current_num.is_integer():
#         mixed_list.append(int(current_num))
#     else:
#         mixed_list.append(current_num)
#     current_num += 0.5
# print(mixed_list)

# 🌟 Exercise 5: For Loop
# Key Python Topics:

# Loops (for)
# Range and indexing


# Instructions:

# Write a for loop to print all numbers from 1 to 20, inclusive.

# list = []
# for x in range (1, 20+1):
#     list.append(x)

# print(list)

# Write another for loop that prints every number from 1 to 20 where the index is even.

# list2 = []
# for y in range (2, 20+1, 2):
#     list2.append(y)

# print (list2)


# 🌟 Exercise 6: While Loop
# Key Python Topics:

# Loops (while)
# Conditionals


# Instructions:

# Use an input to ask the user to enter their name.
# Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
# # hint: check for the method isdigit()
# while True:
#     name = input ('Enter your name: ')
#     if name.isdigit():
#         print ('Name may not contain digits')
#     elif len(name) < 3 :
#         print ('Name must be longer than 3 letters!')
#     else: 
#         print ('Thank you')
#         break

# if the input is incorrect, keep asking for the correct input until it is correct
# if the input is correct print “thank you” and break the loop
# Example:

# Alt text



# 🌟 Exercise 7: Favorite Fruits
# Key Python Topics:

# Input/output
# Strings and lists
# Conditionals


# Instructions:

# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"

# fruit_list = input ('Enter your favorite fruits separated by spaces: ')
# favorite_fruits = fruit_list.split()
# chosen_fruit = input("Enter the name of any fruit: ")
# if chosen_fruit in favorite_fruits:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy it!")

# 🌟 Exercise 8: Pizza Toppings
# Key Python Topics:

# Loops
# Lists
# String formatting


# Instructions:

# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.



# 🌟 Exercise 9: Cinemax Tickets
# Key Python Topics:

# Conditionals
# Lists
# Loops


# Instructions:

# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.



print("Enter the age of each family member. Type 'done' when you are finished.")

while True:
    user_input = input("Enter age (or 'done'): ")
    if user_input == 'done':
        break
    age = int(user_input)
    if age < 3:
        ticket_price = 0
        print(" -> Under 3: Free!")
    elif age <= 12:
        ticket_price = 10
        print(" -> Age 3 to 12: $10")
    else:
        ticket_price = 15
        print(" -> Over 12: $15")
    total_cost = 0
    total_cost += ticket_price
print(f"Total ticket cost for the family: ${total_cost}")


# Bonus:

# Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
# Write a program to:
# Ask for each person’s age.
# Remove anyone who isn’t allowed to watch.
# Print the final list of attendees.