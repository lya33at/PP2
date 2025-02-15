#Python Dates
import datetime
x = datetime.datetime.now()
print(x)


import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A")) #2025 #Saturday


import datetime
x = datetime.datetime(2020, 5, 17)
print(x)


import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B")) #June