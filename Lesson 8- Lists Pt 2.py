#Task- Add items to Python List
#Methods- similar to function, but associated with objects/classes

camping_list = ["tent", "sleeping bags", "food"]
print(type(camping_list))

camp_site = ["Crystal Lake", 404, 95.5, True]

me = camping_list[2]
print(me)

me = camping_list[-1]
print(me)

#camping_list.append("toilet paper", "bidet") doesn't work, it can only take one argument
camping_list.append("toilet paper")
camping_list.append("bidet")

#extend lets you add a list to a list
camping_list.extend(["toilet paper", "bidet"])

camping_list = camping_list + ["toilet paper", "bidet"]

#index number dictates where the data is placed
camping_list.insert(0, "toilet paper")

#using negavive inded for second to last
camping_list.insert(-1, "peanuts")

print(camping_list)