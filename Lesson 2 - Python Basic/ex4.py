#Exercise 4 - nested while loop
print ("\nExercise 4")  
base = 5
ctr1 = 1
while(base > 0):
    while (ctr1 < 6):
       print( "*" * base )
       ctr1 += 1
       base -= 1

    break
