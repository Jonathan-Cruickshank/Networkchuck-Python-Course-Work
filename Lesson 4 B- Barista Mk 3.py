#Task- If the customer is named "Ben" don't let them continue
#Control the flow of the program

print("Hello! Welcome to our coffee shop!")

name = input("What's your name?: ")

#The tutorial recommends running an 'exit' function under the 'if', since indenting everything in 'else' could take time. That's how I tried to solve the challenge at first. Since this is still a short script I'll leave it like that here as an example and change it in the next version.
 
if name == "Ben":
    print("ACCESS DENIED!!!")
    exit()

else:
    print("Hello " + name + ", thank you for coming in today.\n")

    menu = ("Black coffee, Capachino, Latte- ")

    order = input(name + ", what would you like from our menu today? Here's what we're serving-\n" + menu)
    price = 3

    quantity = input("Ok, how many " + order + "'s would you like?: ")

    total = price * int(quantity)

    print("\nThank you " + name + ", your " + quantity + " " + order + "'s will be ready in just a minute. The cost comes to £" + str(total))