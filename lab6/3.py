#remove the file "demofile.txt":
import os
os.remove("demofile.txt")


#check if file exists, then delete it:
import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")


#remove the folder "myfolder":
import os
os.rmdir("myfolder")
#NOTE: you can remove only empty folders