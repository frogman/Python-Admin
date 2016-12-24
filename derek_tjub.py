import random
import sys
import os

quote = "\"Using single quote"
multiquote = ''' like any other qu
ote on the other side'''

print("%s %s %s" % ('I like quote', quote, multiquote))

print('\n' * 5)
print("Bez nove linije", end="")
print("-nastavljamo stampanje")

grocery_list = ["Sok", "Paradajz", "Banane", "Krompir"]
grocery_list[0] = "Zeleni sok"
print('First list item:', grocery_list[0])
print(grocery_list[1:3]) #indeksi 1 i 2 ne ukljucujuci 3
other_events = ['Operi Auto', 'Pokupi klince', 'Provjeri Kintu']
todo_lista = [other_events, grocery_list]
print(todo_lista)







