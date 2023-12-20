Hotels_in_Krakow = [
    {"name":"Sky","price":320.00},
    {"name":"Metropol","price":480.00},
    {"name":"New Port","price":420.00},
    {"name":"Aparthotel","price":390.00}
]
hotels_in_Sopot = [
    {"name":"Focus","price":510.00},
    {"name":"Aqua","price":345.00},
    {"name":"La Boutique","price":390.00},
    {"name":"Marina","price":410.00}
]
#a
def hotel_list(hotels):
    hotel_names = []

    for hotel in hotels:
        hotel_names.append(hotel["name"])
    return ",".join(hotel_names)

result = hotel_list(Hotels_in_Krakow)
print(result)

#b
def avg_price(hotels) :
    dlugosc = len(hotels)

    suma = 0
    for hotel in hotels:
        suma += (hotel["price"])

    avg = suma/dlugosc
    return suma

result = avg_price(Hotels_in_Krakow)
print(result)

#c
avg_Krakow = avg_price(Hotels_in_Krakow)
avg_Sopot = avg_price(hotels_in_Sopot)

result = avg_price(hotels_in_Sopot)
print(result)

if avg_Krakow > avg_Sopot:
    print("Cheaper hotels are in Sopot")
print("Cheaper hotels are in Krakow")