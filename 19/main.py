from datetime import timedelta, date


start = date(1901,1,1)
count = 0

while start < date(2000, 12, 31):
    if start.weekday() == 6:
        count += 1

    if start.month == 12:
        start = start.replace(start.year+1,1,1)
    else:
        start = start.replace(start.year, start.month+1, 1)

print count
