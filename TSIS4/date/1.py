import datetime 
x = datetime.datetime.today() - datetime.timedelta(5)
print(x.strftime('%x'))