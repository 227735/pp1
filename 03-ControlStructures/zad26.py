car_speed = int(input("Enter vehicle speed: "))

speed_limit_min = 40
speed_limit_max = 140

if car_speed >= speed_limit_min and car_speed  <= speed_limit_max:
    print("Speed is valid")
else:
    print("Invalid car speed!!")