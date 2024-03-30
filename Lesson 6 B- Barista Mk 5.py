#Task One- Add multiple names to blacklist
#Task Two- If a name on the blacklist had done x good deeds today, let them in

print("Hello! Welcome to our coffee shop!")

name = input("What's your name?: ")

'''
Better to wrap an 'int' aroudn the input than a 'str' around the minimum
    good_deeds = int(input("How many good deeds have you done today?: "))
    if evil_status == "Y" and good_deeds <= str(3):
'''
if name == "Ben" or name == "Patricia" or name == "Loki":
    evil_status = input("Are you evil? (Y/N): ")
    good_deeds = int(input("How many good deeds have you done today?: "))
    if evil_status == "Y" and good_deeds <= 3:
        print("You can't come in " + name + "! Be gone!")
        exit()
    else:
        print("Congratulations, non-evil " + name + "! Please take a look at our menu")

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

total = price * int(quantity)

print("\nThank you " + name + ", your " + quantity + " " + order + "'s will be ready in just a minute. The cost comes to £" + str(total))