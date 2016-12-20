#Calculate the cost of renting the car:
#Every day you rent the car costs $40
#If you rent the car for 7 or more days, you get $50 off your total.
#Alternatively (elif), if you rent the car for 3 or more days, you get $20 off your total.
#You cannot get both of the above discounts.
#Return that cost.

def rentalcarcost(days):
    cost = 40 * days
    if days >= 7:
       cost -= 50
    elif days >= 3:
       cost -= 20
       return cost
input(rentalcarcost(days))
print("The cost of days with discount is: %s" % (rentalcarcost()))
