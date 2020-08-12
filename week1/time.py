import datetime as dt
import time as tm

# Time returns the current time in seconds since the Epoch. (Januray 1st, 1970)
curtime = tm.time()


# Convert the timestamp to datetime
dtnow = dt.datetime.fromtimestamp(curtime)

#Handy datatime attribute
print(dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second)

delta = dt.timedelta(days=100)
today = dt.date.today()
print(today - delta)
print(today > today - delta)