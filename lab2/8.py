#remove specified item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) #apple, cherry


thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist) #apple, cherry, banana, kiwi


#remove specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) #apple, cherry


thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) #banana, cherry


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) #[]