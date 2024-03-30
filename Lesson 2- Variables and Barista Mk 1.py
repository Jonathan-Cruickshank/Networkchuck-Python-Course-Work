#This lesson is about Variables, and how you can mix them together with print functions to make something pleasant for humans to read.

#Variables store data for future use
#This is a variable- name = ("Jonathan")

#Automated Barista Robot
print("Hello! Welcome to our coffee shop!")

name = input("What's your name?: ")

print("Hello " + name + ", thank you for coming in today.\n")

menu = ("Black coffee, Capachino, Latte- ")

'''
Challenge: Combine these two parts of the code-
print(name + ", what would you like from our menu todya? Here's what we're serving-\n" + menu)

order = input()
'''

order = input(name + ", what would you like from our menu todya? Here's what we're serving-\n" + menu)

print("\nThank you " + name + ", your " + order + " will be ready in just a minute.")