x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x) #apple, kiwi, cherry


#add items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple) #apple, banana, cherry, orange


#2nd way
thistuple = ("apple", "banana", "cherry")
y = ("orange")
thistuple += y
print(thistuple)


#remove items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)


#2nd way
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists