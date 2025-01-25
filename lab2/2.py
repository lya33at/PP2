#Most values are true
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))


#Some values are false
print(False)
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))


def myFunction():
    return True
print(myFunction())


def myFunction():
    return True
if myFunction():
    print("YES!")
else:
    print("NO!")


#check if an object is an integer or not
x = 200
print(isinstance(x, int))