import datetime
x = datetime.datetime.now()
x = x.replace(microsecond=0)
print(x)