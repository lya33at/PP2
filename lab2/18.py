#loop through a tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)


#loop through the index numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])


#using a while loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i+1 