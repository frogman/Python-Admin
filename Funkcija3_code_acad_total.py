#Vacation Plan of costs - sum of 3 functions
def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    carcost = 40 * days
    if days >= 7:
        carcost -= 50
    elif days >= 3:
        carcost -= 20
    return carcost

def trip_cost(city, days):
    return hotel_cost( days ) + rental_car_cost( days ) + plane_ride_cost( city )

print(trip_cost("Tampa",4))
