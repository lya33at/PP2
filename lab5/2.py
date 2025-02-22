import re
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x) #['The', 'rain in Spain']


import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x) #The9rain9in9Spain


import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x) #The9rain9in Spain


import re
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)


import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span()) #(12, 17)


import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string) #The rain in Spain


import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group()) #Spain