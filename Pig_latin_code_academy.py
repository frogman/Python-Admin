print('Welcome to the Pig Latin Translator!')

pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print(original)
else:
    print('empty')
word = original.lower()
first = word[0]
new_word = word + first + pyg
new_word = new_word[1:len(new_word)] #slicing of string from 1 until end of complete string
