#keys
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",  
    "year" : 1964
}
x = thisdict.keys()
print(x) #dict_keys(['brand', 'model', 'year'])


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change


#values()
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change


#items()
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thidict dictionary")