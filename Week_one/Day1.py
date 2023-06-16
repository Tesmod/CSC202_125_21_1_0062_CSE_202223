#Day One
#Printing, Commenting, Debugging, String Manipulation and Variables

print("Hello World!")

print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

#String Manipulation
print("Hello World!\nHello World!\nHello World!")
print("Hello" + "Angela")
print("Hello" + " " + "Angela")

#Fix the code below
print("Day - 1 String Manipulation")
print("String concatenation is done with the '+' sign")
print('e.g print("Hello " + "World!")')
print("New lines can be created with a backslash and n")

#Using the input function
print("Hello " + input("What is your name?") + "!")

#Finding the number of characters in a given name
print(len(input("What is your name?")))

#Learning Variables
name = input("What is your name?")
print(name)
name = input("What is your name?")
length = len(name)
print(length)
#Swapping assigned variables
a = input("a:")
OB
b = input("b:")
c = a
a = b
b = c
print("a = " + a)
print("b = " + b)
#Exercise
print("Hello! Welcome to the Band Name Generator.")
city_name = input("What city did you grow up in? \n")
pet_name = input("What is the name of your pet? \n")
band_name = print("The name of your band could be: " + city_name + " " + pet_name)
