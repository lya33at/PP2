#loop through a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)


thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])


thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]