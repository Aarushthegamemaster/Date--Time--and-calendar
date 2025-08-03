from datetime import date, time, datetime

today = date.today()
now = datetime.now()
print("Today's date is", today)
print("\nThe exact time is", now)
print("\nDate Components:", today.year, today.month, today.day)