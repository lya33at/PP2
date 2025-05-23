#Python Scope
def myfunc():
    x = 300
    print(x)
myfunc() #300


def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc() #300


x = 300
def myfunc():
    print(x)
myfunc()
print(x) #300


x = 300
def myfunc():
    x = 200
    print(x)
myfunc()
print(x)


def myfunc():
    global x
    x = 300
myfunc()
print(x) #300


x = 300
def myfunc():
    global x
    x = 200
myfunc()
print(x)


def myfunc1():
    x = "Jane"
    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return x 
print(myfunc1())