#change item value 
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) #apple, blackcurrant, cherry


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"] 
print(thislist) #apple, blackcurrant, watermelon, orange, kiwi, melon, mango


#insert items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) #apple, banana, watermelon, cherry