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





#while(2,100)
#while range(2,i)
#if (i%j!=0) :print(i)
 



