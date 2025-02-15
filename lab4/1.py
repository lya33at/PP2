mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit)) #apple
print(next(myit)) #banana
print(next(myit)) #cherry


mystr = "banana"
myit = iter(mystr)
print(next(myit)) #b
print(next(myit)) #a
print(next(myit)) #n
print(next(myit)) #a
print(next(myit)) #n
print(next(myit)) #a


mytuple = ("apple", "banana", "cherry")
for x in mytuple:
    print(x) #apple #banana #cherry


mystr = "banana"
for x in mystr:
    print(x) #b #a #n #a #n #a


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter)) #b #a #n #a #n #a #1 #2 #3 #4 #5


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
    print(x)