#python dictionaries
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",  
    "year" : 1964
}
print(thisdict) #{'brand' : 'Ford',  'model' : 'Mustang', 'year' : 1964}


thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",  
    "year" : 1964
}
print(thisdict["brand"]) #Ford


thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",  
    "year" : 1964, 
    "year" : 2020
}
print(thisdict) #{'brand' : 'Ford',  'model' : 'Mustang', 'year' : 2020}


thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",  
    "year" : 1964
}
print(len(thisdict)) #3


#type is <class 'dict'>


#it is also possible to use the dict() constructor to make a dictionary.
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)