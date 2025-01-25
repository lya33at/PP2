#append items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) #apple, banana, cherry, orange


#insert items
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) #apple, orange, banana, cherry


#extend list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) #apple, banana, cherry, mango, pineaplle, papaya


#add any iterable
thislist = ["apple", "banana", "cherry"]
tropical = ("kiwi", "orange")
thislist.extend(tropical)
print(thislist) #apple, banana, cherry, kiwi, orange