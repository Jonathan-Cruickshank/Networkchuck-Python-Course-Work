#Booleans = the data type for True and False
me = "Jon"
me
#Result = 'Jon'

me == "Jon"
#Result = True

me == "Bob"
#Return = False

not me == "Bob"
#Return = True

me != "Bob"
#Return = Ture (Using a comparison operator rather than a logical operator)

print(type(me == "Jon"))
#Result = <class 'bool'>

#The double = makes Python check if a statement is True or False, and since I defined "me = Jon" it returns "me == "Jon"" as True


#'not' statement. Even the tutorial says these are just weird.

print("Hello, welcome to our coffee shop")

name = input("What's your name?: ")

if not name == "Ben":
    print("Get out of here")
else:
    print("Come on in!")

#Result- any name other than Ben triggers the 'else' statement because it's "not Ben"