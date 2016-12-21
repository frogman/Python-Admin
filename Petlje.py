#Running through all the items in a list is called traversing the list, or traversal.
#for each item in a list run the foor lpp
for f in ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
    invitation = "Hi " + f + ".  Please come to my party on Saturday!"
    print(invitation)

#Let us write a function now to sum up all the elements in a list of numbers.
def mysum(xs):
    "Sum all the numbers in the list xs, and return to total"
    running_total = 0
    for x in xs:
        running_total = running_total + x
    return running_total

print(mysum([1,2,3]))
print(mysum([1.25, 2.5, 1.75]) == 5.5) # suma brojeva u listi je jednaka == broju 5.5 zato je True
print(mysum([1, -2, 3]) == 2)
print(mysum([ ]) == 0)
print(mysum(range(11)) == 55)  # 11 is not included in the list.

#while statement
#You can almost read the while statement as if it were English. It means, while v is less than or equal to n,
#  continue executing the body of the loop. Within the body, each time, increment v. When v passes n, return your accumulated sum.
def sum_to(n):
    """Return the sum of 1+2+3 ... n"""
    ss = 0
    v = 1
    while v <= n: #dok je parametar n veci ili jednak od v evauliraj metode u petlji
        ss = ss + v
        v = v + 1
    return ss
print(sum_to(4) == 10)
print(sum_to(2))

#ista funkcija sa for petljom
#Notice the slightly tricky call to the range function —
#we had to add one range onto n, because range generates its list up to but excluding the value you give it.
#range generise listu do broja kojeg mu date ali iskljuci njega tip n = 4 , lista[1,2,3]
def sum_to_with_for(n):
    """ Return the sum of 1+2+3 ... n """
    ss  = 0
    for v in range(n+1): #za v u nizu od n=3 - [1,2]
        ss = ss + v
    return ss
print(sum_to_with_for(4)) #1+2+3+4 = 10 - rezultat

#The Collatz 3n + 1 sequence¶
#Let’s look at a simple sequence that has fascinated and foxed mathematicians for many years.
#They still cannot answer even quite simple questions about this.
#The “computational rule” for creating the sequence is to start from some given n, and to generate the next term of the sequence from n,
#either by halving n, (whenever n is even), or else by multiplying it by three and adding 1. The sequence terminates when n reaches 1.

def seq3np1(n):
    """ Print the 3n+1 sequence from n,
        terminating when it reaches 1.
    """
    while n != 1:
        print(n, end=", ")
        if n % 2 == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    print(n, end=".\n")


