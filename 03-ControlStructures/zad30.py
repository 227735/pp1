time_24_hour = input("Enter time (24-hour format):")

hours, minutes = map(int, time_24_hour.split(':'))

period = "am" if hours < 12 else "pm"

if hours == 0:
    hours_12_hour = 12
elif hours <= 12:
    hours_12_hour = hours
else:
    hours_12_hour = hours - 12

print(f"Time in 12-hour format: {hours_12_hour}:{minutes:02d}{period}")