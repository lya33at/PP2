import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
    print("YES! We have a match!")
else:
    print("No match")


import re
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x) #['ai', 'ai']


import re
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x) #[]


import re
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position: ", x.start())


import re
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x) #none


import re
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x) #['The', 'rain', 'in', 'Spain']