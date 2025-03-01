f = open("demofile.txt", "w")
f.write("""Hello! Welcome to demofile.txt. 
        This file is for testing purposes.
         Good Luck!""")
f.close()
f = open("demofile.txt", "r")
print(f.read())


f = open("demofile.txt", "r")
print(f.read(5))


f = open("demofile.txt", "r")
print(f.readline())



#By calling readline() two times, you can read the two first lines:
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())


f = open("demofile.txt", "r")
for x in f:
    print(x)


#close file
f = open("demofile.txt", "r")
print(f.readline())
f.close()