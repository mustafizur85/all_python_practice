import datetime as dt

currentLocaldateTime= dt.datetime.now()
print(currentLocaldateTime)

currentLocaldate = dt.date.today()
print(currentLocaldate)

print("current year:",currentLocaldate.year)
print("current month:", currentLocaldate.month)
print("current day", currentLocaldate.day)

print("current Hour",currentLocaldateTime.hour)
print("current minut", currentLocaldateTime.minute)
print("current second",currentLocaldateTime.second)
print("current microsecond",currentLocaldateTime.microsecond)

#format time
now = dt.datetime.now()
timeNow =now.strftime("%H-%M-%S")
print(timeNow)

