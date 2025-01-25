thisset = {"apple", "banana", "cherry"}
print(thisset) #cherry, banana, apple
#note: the set list is unordered, meaning: the items will appear in a random order.


thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) #apple, banana, cherry


#False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset) #False, True, banana, cherry, apple


myset = {"apple", "banana", "cherry"}
print(type(myset)) #<class 'set'>


thisset = set(("apple", "banana", "cherry")) #note the double round-brackets
print(thisset)