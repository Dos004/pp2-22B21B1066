import datetime

x = datetime.datetime.now()
y = datetime.datetime.now() - datetime.timedelta(1)
difference = (x - y).total_seconds()
print(difference)