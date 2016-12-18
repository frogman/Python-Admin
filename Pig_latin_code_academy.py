print('Welcome to the Pig Latin Translator!')

# Start coding here!
original = input("Enter a word:")
if len(original) and original.isalpha() > 0:
    print(original)
else:
    print("Empty")