#Calculate the cost of renting the car:
#Every day you rent the car costs $40
#If you rent the car for 7 or more days, you get $50 off your total.
#Alternatively (elif), if you rent the car for 3 or more days, you get $20 off your total.
#You cannot get both of the above discounts.
#Return that cost.

#nije radila
#def rental_car_cost(days):
#    car_cost = 40 * days
#    if days >= 7:
#       car_cost -= 50
#    elif days >= 3:
#       car_cost -= 20
#       return car_cost

def rental_car_cost(days):
    carcost = 40 * days
    if days >= 7:
       carcost -= 50
    elif days >= 3:
         carcost -= 20
    return carcost #!!!! PRETHODNA funkcija nije radila jer je return bio uvucen i ident se odnosio samo na poslednju petlju (elif)
                   #a ne na cjelu proceduru - return mora biti u ravni sa if i elif!!!!!!!

b = 7
print((rental_car_cost(b)))
