def f(d):
    in_park = []
    result = []

    for car, action in d:
        if action == "in" and car not in in_park:
            in_park.append(car)
        elif action == "out" and car in in_park:
            in_park.remove(car)

    result = sorted(in_park)
    return result

cars = [["KR234", "in"], ["BA123", "in"], ["GX444", "in"], ["KR234", "out"], ["BA111", "in"], ["BA123", "out"], ["KR234", "in"]]
print(f(cars))

cars1 = [["KR234", "in"], ["KR234", "out"]]
print(f(cars1))