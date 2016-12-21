#Running through all the items in a list is called traversing the list, or traversal.
#for each item in a list run the foor lpp
#for f in ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
#    invitation = "Hi " + f + ".  Please come to my party on Saturday!"
#    print(invitation)

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
