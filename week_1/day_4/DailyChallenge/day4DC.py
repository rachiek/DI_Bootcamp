# 1. Ask the user for two inputs:

# A number (integer).
# A length (integer).

# # 2. Create a program that generates a list of multiples of the given number.
# # 3. The list should stop when it reaches the length specified by the user.

number = int(input('number: '))
length = int (input('length: '))
print(number)
print (length)


multiples_list = []
for item in range (1, length + 1):
    multiples_list.append (item * number)
print (multiples_list)


# Instructions:
# 1. Ask the user for a string.
# 2. Write a program that processes the string to remove consecutive duplicate letters.
# The new string should only contain unique consecutive letters.
# For example, “ppoeemm” should become “poem” (removes consecutive duplicates like ‘pp’, ‘ee’, and ‘mm’).
# 3. The program should print the modified string.
 

user_string = input("Enter a string with duplicate letters: ")


modified_string = ""
for char in user_string:
    if len(modified_string) == 0 or char != modified_string[-1]:
        modified_string += char
print(f"Modified string: {modified_string}")

