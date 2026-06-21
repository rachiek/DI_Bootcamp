# 1. Ask the user for two inputs:

# A number (integer).
# A length (integer).

# number = int(input('number: '))
# length = int (input('length: '))
# print(number)
# print (length)

# # 2. Create a program that generates a list of multiples of the given number.
# # 3. The list should stop when it reaches the length specified by the user.

# multiples_list = []
# for item in range (1, length + 1):
#     multiples_list.append (item * number)
# print (multiples_list)


# Instructions:
# 1. Ask the user for a string.
string = input('Enter a word with duplicate letters: ')
print(string)

print(set(string))

# 2. Write a program that processes the string to remove consecutive duplicate letters.

# The new string should only contain unique consecutive letters.
# For example, “ppoeemm” should become “poem” (removes consecutive duplicates like ‘pp’, ‘ee’, and ‘mm’).
# 3. The program should print the modified string.



# Example 1:

# Input:
# user’s word: "ppoeemm"
# Output:
# "poem"


# Example 2:

# Input:
# user’s word: "wiiiinnnnd"
# Output:
# "wind"


# Example 3:

# Input:
# user’s word: "ttiiitllleeee"
# Output:
# "title"


# Example 4:

# Input:
# user’s word: "cccccaaarrrbbonnnnn"
# Output:
# "carbon"


# Notes:
# The final string will not include any consecutive duplicates, but non-consecutive duplicates are allowed.
# Example: In "recursive", the two ‘r’s and two ‘e’s are allowed because they are not consecutive.
