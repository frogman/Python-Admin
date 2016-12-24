import random
import sys
import os

quote = "\"Using single quote"
multiquote = ''' like any other qu
ote on the other side'''

print("%s %s %s" % ('I like quote', quote, multiquote))

#print('\n' * 5) #5 novih linija puta 5
print("Bez nove linije", end="")
print("-nastavljamo stampanje")

grocery_list = ["Sok", "Paradajz", "Banane", "Krompir"]
grocery_list[0] = "Zeleni sok"
print('First list item:', grocery_list[0])
print(grocery_list[1:3]) #indeksi 1 i 2 ne ukljucujuci 3
other_events = ["Operi Auto", "Pokupi klince", "Provjeri Kintu"]
todo_lista = [other_events, grocery_list]
print((todo_lista[1][2])) # druga lista (indeks 1 ima lista) i treci element ima indeks 2
grocery_list.append("Luk") # dodajemo na kraj liste
grocery_list.insert(2, "Beli Luk") #insert na poziciju
grocery_list.remove("Zeleni sok")
grocery_list.sort()
grocery_list.reverse()
del grocery_list[4]
print(todo_lista)
todo_lista2 = grocery_list + todo_lista
print(len(todo_lista2))

#TUPLES - nemogu se menjati nakon kreiranja ali manje memorije koriste

pi_tuple = (3,1,3,4,5,2,4) # tuples su definisani-okruzeni sa ()

# Convert tuple into a list
new_tuple = list(pi_tuple)
# Conver a list into a tuple
new_list = tuple(new_tuple)
print(len(new_list))
print(min(pi_tuple))
print(new_list)
# tuples also have len(tuple), min(tuple) and max(tuple)

# DICTIONARY or MAP -------------
# Made up of values with a unique key for each value
# Similar to lists, but you can't join dicts with a +
super_villains = {'Fidler' :  'Isaac Bowin',
                  'Captain Cold' : 'Leondard Snart',
                  'Crni Guja' : 'Nikola Kojo',
                  'Supermen' : 'Clark Kirk'}

print(super_villains)
















