#Python Strings 
print("Hello")
print('Hello') #same


print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')



a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


a = "Hello, World!"
print(a[1]) #e


for x in "banana":
    print(x)


a = "Hello, World!"
print(len(a))


txt = "The best things in life are free!"
print("free" in txt) #True


txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")


txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")