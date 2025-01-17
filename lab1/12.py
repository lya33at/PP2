#Python Numbers
x = 1 #int
y = 2.8 #float
z = 1j #complex
print(type(x))
print(type(y))
print(type(z))


#int
x = 1
y = 173472635723
z = -87634
print(type(x))
print(type(y))
print(type(z))



#float
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))


#complex
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))


#convert from one type to another
x = 1 #int
y = 2.8 #float
z = 1j #complex
a = float(x) #convert from int to float
b = int(y) #convert from float to int
c = complex(x) #convert from int to complex
print(type(a))
print(type(b))
print(type(c))


#random num
import random
print(random.randrange(1, 10))