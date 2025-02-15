#Python Modules
def greeting(name):
    print("Hello, " + name)


import mymodule
mymodule.greeting("Jonathan") #Hello, Jonathan


person1 = {
    "name": "John", 
    "age": 36,
    "country": "Norway"
}


import mymodule
a = mymodule.person1["age"]
print(a) #36


import mymodule as mx
a = mx.person1["age"]
print(a) #36


import platform
x = platform.system()
print(x) #Windows


"""
import platform
x = dir(platform)
print(x)
"""

def greeting(name):
    print("Hello, " + name)
person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}


from mymodule import person1
print(person1["age"]) #36