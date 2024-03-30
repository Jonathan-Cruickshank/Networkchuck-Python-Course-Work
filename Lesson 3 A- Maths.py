#'integer' just means whole number. I could never remember that in maths

name = "Jonathan" 
age = 24

#The 'type' function is useful for deducing what a part of the code does. Or solving an error that says "X thing can't be Y type of data".
print(type(name)) #<class 'str'>
print(type(age)) #<class 'int'>

#floating point number, or 'float'
actual_age = 24.3
print(type(actual_age)) #<class 'float'>

print(5 + 7) #Plus
print(5 - 7) #Minus
print(5 / 7) #Divide
print(5 * 7) #Times
print(5 ** 7) #Exponents (Five to the Seventh Power)

#Python follows Order of Operations
print(5 + 7 * 2)

#Equations can also be variables
maths = (5 + 7 * 2)
print(maths)

results = age + actual_age + maths
print(results)