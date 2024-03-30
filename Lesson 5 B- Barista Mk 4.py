#Task One- If the customer is named "Ben" AND they answer "Yes" to "Are you evil?" don't let them continue
#Task Two- If the cucstomer is named Ben and they answer "no" give them a special message
#Task Three- Use "if" statement to give one item a different price to the others
#Task Four- Let customers choose extras that change the price

#Nested "if" statements are handy to establish if multiple things are true

print("Hello! Welcome to our coffee shop!")

name = input("What's your name?: ")
 
if name == "Ben":
    evil_status = input("Are you evil? (Y/N): ")
    if evil_status == "Y":
        print("You can't come in!")
        exit()
    else:
        print("Congratulations, non-evil Ben! Please take a look at our menu")

#This is the solution I used to task two and it worked, I'm filling in the one the tutorial used. Should have figured the solution would be a nested statement
#if name == "Ben" and evil_status == "N":
#    print("Congratulations, non-evil Ben! Please take a look at our menu")

else:
    print("Hello " + name + ", thank you for coming in today.\n")

menu = ("Black coffee, Capachino, Latte- ")

order = input("So " + name + ", what would you like from our menu today? Here's what we're serving-\n" + menu)

if order == "Black coffee":
    price = 1
elif order == "Capachino":
    price = 2
elif order == "Latte":
    price = 3
    whip = input("Would you like whipped cream? (Y/N): ")
    if whip == "Y":
        print("Adding whipped cream!")
    price = 5
    if whip == "N":
        print("Ok, no whip.")
else:
    print("Sorry, we don't have that here.")
    price = 0
    exit()

quantity = input("Ok, how many " + order + "'s would you like?: ")

'''Doing this with ifs to show how messy it is
if order == "Black coffee":
    price = 1
if order == "Capachino":
    price = 2
if order == "Latte":
    price = 3'''

total = price * int(quantity)

print("\nThank you " + name + ", your " + quantity + " " + order + "'s will be ready in just a minute. The cost comes to £" + str(total))