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


