#loop through a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
    print(x) #brand, model, year


for x in thisdict.values():
    print(x)


for x in thisdict.keys():
    print(x)


#loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
    print(x, y)