#Tuples are very similar to lists, except they use round brackets and are geenrally faster. Also lists are "mutable" (changable) while tuples are "imutable" (not changable)
#Because Lists are stored in two blocks of memory to allow for new points to be added, while tuples are only stored in one

#Tuples are good for "read once" data

import timeit

#List speed test
print(timeit.timeit(stmt='["red", "blue", "green", 5, 7, 12, 18, "dude"]', number=10000000))

#Tuple speed test
print(timeit.timeit(stmt='("red", "blue", "green", 5, 7, 12, 18, "dude")', number=10000000))

'''
Same code run 3 times
List-  2.8925835719855970, 2.7057576520019210, 2.8191651070083026
Tuple- 0.7222144489933271, 0.6604027439898346, 0.6611850640038028
'''

#Lets you pack seperate variables
networkchuck = ("Chuck", 33, "coffee")
(name, age, drink) = networkchuck
print(name)
print(age)
print(drink)

#Tuples only need commas
tuple = 1,