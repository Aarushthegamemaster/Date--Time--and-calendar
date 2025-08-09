import datetime

months = [datetime.date(2025, i, 1).strftime('%B') for i in range(1, 13)]

for month in months:
    print(month)

