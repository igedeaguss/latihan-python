import calendar
import datetime as dt
#menampilkan kalender
print (calendar.TextCalendar(firstweekday=6).formatyear(2023))

n1,n2,n3 = map(int,input().split())
waktu = dt.date(n3,n1,n2)
print(f"{waktu:%A}".upper())
print((calendar.day_name[calendar.weekday(n3,n1,n2)]).upper())