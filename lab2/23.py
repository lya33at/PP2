#remove item, if the item to remove does not exist, remove() will raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)


#2nd way
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
#if the item to remove does not exist, discard() will NOT raise an error.


thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset) #apple, banana


thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) #set()


thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) #error