#You can access an individual item on the list by its index.
# An index is like an address that identifies the item's place in the list.
numbers = [5, 6, 7, 8]

print("Adding the numbers at indices 0 and 2...")
print(numbers[0] + numbers[2])
print("Adding the numbers at indices 1 and 3...")

#List indices begin with 0, not 1! You access the first item in a list like this: list_name[0].
#INDICES -INDEXI
print(numbers[1] + numbers[3])

letters = ['a','b','c']
letters.append('d')
print(len(letters))
print(letters)

suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]
first  = suitcase[0:2]  # The first and second items (index zero and one)
middle = suitcase[2:4]  # Third and fourth items (index two and three)
last   = suitcase[4:6]  # The last two items (index four and five)

print(first)
print(middle)
print(last)
#List slicing - we start counting indices from 0 and that we stopped before index 3.
#myList = [0,1,2,3,4], the ending index of your slice will be one beyond the actual last index of the list. Check it out:
#myList[3:5]
#Returns [3, 4]

#!!! List indexing nije isto sto i slicing - kod indeksiranja biramo poziciju pocevsi od nule kao prvi karakter
#kod slicing - rezanja mi brojimo od 0 ukljucenjo prvo desno do zadnjeg iskljcueno npr 5

word = "Python"
#indexing
print(word[3]) # stampa indeksira poziciju 3 - dobijamo h
#slicing
print(word[0:2]) #ukljucuje poziciju prvu i stampa 0 i 1 i ukljucuje 2 ali ne stampa broj 2 - dobijamo Py

