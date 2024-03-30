#Task- Add items to Python List
#Methods- similar to function, but associated with objects/classes

supplies = ["tent", "sleeping bags", "food"]

#Clear deletes entire list, prints empty one
#camping_list.clear()

'''remove only works on one item at a time
supplies.remove("tent")
supplies.remove("sleeping bags")'''

#You use 0 twice to remove the first two items, because when the first pop resolves the second item on the list becomes the first
print("Item deleted: " + supplies.pop(0)) #pop also allows you to print out which item it just deleted
supplies.pop(0)

print(supplies)