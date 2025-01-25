#add items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset) #orange, apple, cherry, banana


#add sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) #cherry, apple, pineapple, mango, banana, papaya


#add any iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset) #{kiwi, apple, cherry, banana, orange}