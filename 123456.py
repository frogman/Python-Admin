i = 0;
while (i <= 20):
    if (i % 2 == 0):
        print( i )
    elif (i == 9):
        # Forces the loop to end all together
        break
    else:
        # Shorthand for i = i + 1
        i += 1
        print("Sledeca")
        # Skips to the next iteration of the loop
        continue

    i += 1