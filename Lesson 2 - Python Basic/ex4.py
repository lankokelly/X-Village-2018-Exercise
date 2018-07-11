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

#Exercise 5
print ("\nExercise 5")

for i in range(2,51):
    flag = 1
    for j in range ( 2,i ):
            if i % j == 0:
                flag = 0
                break
    if( flag ):
        print ( i )