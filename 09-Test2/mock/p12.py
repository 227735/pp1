def f(time_24h):
    hours, minutes = [int(part) for part in time_24h.split(':')]
    hours = hours % 12 if hours % 12 != 0 else 12

    time_12h = "{:02d}:{:02d}{}".format(hours, minutes, "pm")
    return time_12h

time_24h = "23:05"
result = f(time_24h)
print(result)