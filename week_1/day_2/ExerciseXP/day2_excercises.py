#excercise 1
print("Hello world\n" * 5)

#excercise 2
print((99**3)*8)

#excercise 3
print(15 < 3) #false
print(3 == 3) #true
#print("3" > 3) #type error
print("Hello" == "hello") #false

#excercise 4
computer_brand = "mac"
print (f"I have a {computer_brand} computer")

#excercise 5
name = "Rachel"
age = 34
shoe_size = 7.5
info = (f"{name} loves dogs is {age} and went hiking last weekend wearing shoresh sandals, size {shoe_size}.")
print (info)

#excercise 6
a = 5
b = 2
if a > b:
    print ("Hello World")

#excercise 7
number = int(input("Enter a number:"))
if number % 2 == 1:
    print ("odd")
else:
    print ("even")

#excercise 8
name = input("What is your name: ")
if name == "Rachel":
    print ("We are twins")
else:
    print ("Rachel would be a better name")

#excercise 9
height = int(input("Write your height in cm: "))
if height >= 145:
    print("You can ride!")
else:
    print("Once you grow taller you can ride!")