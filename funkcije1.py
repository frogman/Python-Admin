#!!! When the function comes to a return it brakes and it is finished.


def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08 #bill = bill * 1.08
    print("With tax: %f" % bill)
    return bill


def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15 #1.15  #!!!!bill varijabla-objekat se ne nasledjuje kroz funkcije - one su privatne unutar funkcija
    print("With tip: %f" % bill)
    return bill
#http://www.saltycrane.com/blog/2008/01/python-variable-scope-notes/
#globalne i lokalne variable unutar funkcija


meal_cost = 100
meal_with_tax = tax( meal_cost )
meal_with_tip = tip( meal_with_tax )


def square(n):
    """Returns the square of a number."""
    squared = n ** 2
    print("%d squared is %d." % (n, squared))
    return squared


# Call the square function on line 9! Make sure to
# include the number 10 between the parentheses.
square( 10 )

#n is a parameter of square. A parameter acts as a variable name for a passed in argument.
#With the previous example, we called square with the argument 10. In this instance the function was called, n holds the value 10.
#A function can require as many parameters as you'd like, but when you call the function, you should generally pass in a matching
# number of arguments.

def power(base, exponent):  # Add your parameters here!
    result = base**exponent
    print("%d to the power of %d is %d." % (base, exponent, result))
#Function bodies can contain one or more return statement. They can be situated anywhere in the function body.
#A return statement ends the execution of the function call and "returns" the result, i.e. the value of the expression following the return keyword,
# to the caller. If the return statement is without an expression, the special value None is returned.
#If there is no return statement in the function code, the function ends, when the control flow reaches the end
#of the function body and the value "None" will be returned.
power(37,4)  # Add your arguments here!

#primjer poziva funkcije iz druge funkcije
def one_good_turn(n):
    return n + 1

def deserves_another(n):
    return one_good_turn( n ) + 2 #poziv prethhodne funkcije sa parametrom svojim n - koji je promenjen (n+1) kroz prvu funkciju


def cube(number):
    return number ** 3 #vraca broj na trecu - triput pomnozi(number*number*number)

def by_three(number):
    if number % 3 == 0: #ako je broj djeljiv sa 3 onda pozovi proceduru cube i promjeni argument kroz metodu procedure cube (triputa pomnozi)
        return cube( number )
    else:
        return False
print(by_three( 3 ))

#First, def a function, shut_down, that takes one argument s. Don't forget the parentheses or the colon!
#Then, if the shut_down function receives an s equal to "yes", it should return "Shutting down"
#Alternatively, elif s is equal to "no", then the function should return "Shutdown aborted".
#Finally, if shut_down gets anything other than those inputs, the function should return "Sorry"


def shut_down(s):
    if s == 'yes':
       return "Shutting down"
    elif s == "no":
       return "Shutdown Aborted"
    else:
       return "Sorry"

#If the type of the argument is either int or float, the function should return the absolute value of the function input.
def distance_from_zero(n):

    if type( n ) == int or type( n ) == float:
        print("The absolute value of the input is ", abs( n ))
        return abs( n )
    else:
        return "Nope"

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

#In the above example, we first give the player 10 tickets for every point that the player scored. Then, we check the value of score multiple times.
def finish_game(score):
    tickets = 10 * score
    if score >= 10:
        tickets += 50
    elif score >= 7:
        tickets += 20
    return tickets

print("Score of a player:")
print(finish_game(11))
