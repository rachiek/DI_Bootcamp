# Exercise 1: Random Sentence Generator (~20 minutes)
# Build a program that reads words from a file and generates random sentences.

# Functions to implement:

# Function	Details
# get_words_from_file(file_path)	Opens the file, reads content, splits into words, returns the list
# get_random_sentence(length)	Takes a number, picks that many random words, joins with spaces, returns lowercase string
# main()	Asks for sentence length (2-20), validates input with try/except, calls the other functions
# Rules:

# main() should ask the user for a number between 2 and 20 (inclusive)
# If the user types something that isn't a number → catch ValueError, print error message
# If the number is outside 2-20 → print an error message (not an exception — just a check)
# Use random.choice() to pick random words
# The sentence should be all lowercase
# Example output:

# Enter sentence length (2-20): 5
# Generated sentence: gentle river apple swift code

# Enter sentence length (2-20): hello
# Invalid input! Please enter a number.

# Enter sentence length (2-20): 25
# Please enter a number between 2 and 20.

# # 🌟 Exercise 1 — Random Sentence Generator
# import random

# def get_words_from_file(file_path):
#   # read file, split into words, return list
#   with open(file_path, "r") as f:
#     content = f.read()

#   return content.split() # returns a list of words

# def get_random_sentence(length):
#     # pick random words, join, return lowercase
#     words = get_words_from_file("week_3/words.txt")
#     chosen = [random.choice(words) for _ in range(length)]
#     return " ".join(chosen)

# def main():
#     # get input, validate, generate sentence
#     try:
#       length = int(input("Enter sentence length (2-20): "))
#     except ValueError:
#       print("Invalid input! Please enter a number.")
#       return

#     if length < 2 or length > 20:
#       print("Please enter a number between 2 and 20")
#       return

#     sentence = get_random_sentence(length)
#     print(f"Generated sentence: {sentence}")

# main()

# 🌟 Exercise 2: Working with JSON (~15 minutes)
# Given this JSON string:

# sampleJson = """{
#    "company":{
#       "employee":{
#          "name":"emma",
#          "payable":{
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""
# Steps:

# Parse the JSON string using json.loads()
# Access and print the employee's salary
# Add a "birth_date" key to the employee with value "1990-05-15"
# Save the modified data to a file called employee.json using json.dump() with indent=2
# Read the file back and print it to verify
# Expected output:

# Salary: 7000
# Modified data saved to employee.json
# Verified — birth_date: 1990-05-15

# 🌟 Exercise 2 — Working with JSON
import json

sampleJson = """{
   "company":{
      "employee":{
         "name":"emma",
         "payable":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Step 1: Parse the JSON string
data = json.loads(sampleJson)
# Step 2: Access and print the salary
salary = data["company"]["employee"]["payable"]["salary"]
print(f"Salary: {salary}")

# Step 3: Add birth_date to the employee
data["company"]["employee"]["birth_date"] = "1990-05-15"

# Step 4: Save to employee.json
with open("employee.json", "w") as f:
    json.dump(data, f, indent=2)

# Step 5: Read back and verify
with open ("employee.json", "r") as f:
    verified_data = json.load(f)
    
print(f"Verified data: {verified_data}")
print(f"Name: {verified_data['company']['employee']['name']}")
print(f"Birth Date: {verified_data['company']['employee']['birth_date']}")