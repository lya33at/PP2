class MyClass:
    x = 5
print(MyClass) #<class '__main__.MyClass'>


p1 = MyClass()
print(p1.x) #5


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age) #John 36


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 36)
print(p1)


p1.age = 40


del p1.age


del p1


class Person:
    pass