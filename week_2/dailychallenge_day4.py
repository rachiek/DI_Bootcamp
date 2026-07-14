
# Step 1: Get Input
# Use the input() function to get a string of words from the user.
# The words will be separated by commas.
# Step 2: Split the String
# Step 3: Sort the List
# Step 4: Join the Sorted List
# Step 5: Print the Result

# Print the resulting comma-separated string.

single_string = input("Enter a single string with words separated by commas: ") 
list_string = [word.strip() for word in single_string.split(",")]
list_string.sort()
result = ",".join(list_string)
print(result)


# Write a function that takes a sentence as input and returns the longest word in the sentence. If there are multiple longest words, return the first one encountered. Characters like apostrophes, commas, and periods should be considered part of the word.
# Step 1: Define the Function
# Define a function that takes a string (the sentence) as a parameter.
# Step 2: Split the Sentence into Words
# Step 3: Initialize Variables
# Step 4: Iterate Through the Words
# Step 5: Compare Word Lengths
# Step 6: Return the Longest Word

sentence = input("Enter a sentence: ")

def find_longest_word(sentence):
    words = sentence.split()
    longest_word = ""
    
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
            
    return longest_word
print(find_longest_word(sentence))