f = open("demofile2.txt", "w")
f.write("Now the file has more content!")
f.close()
#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())


f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())


#Create a file called "myfile.txt":
f = open("myfile.txt", "x")


#Create a new file if it does not exist:
f = open("myfile.txt", "w")