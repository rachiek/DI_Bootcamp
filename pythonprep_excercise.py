my_string = "Hello Class"
my_number = 18

print(f"{len(my_string)} chars in {my_string}")
# Exercise 19 (*)
print(ord(my_string[3]))
# Exercise 20 (*)
result = ""
for c in my_string:
    if 96 < ord(c) < 123:
        result += c
print(result)