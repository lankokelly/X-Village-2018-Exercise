#Exercise 3
print ("\nExercise 3")
import random
answer = random.randint(1,100)
#print(answer)
guess = int(input("Enter a number : "))
while(1):
    while (answer != guess):
        if (guess < answer):
           print("Too small")
           guess = int(input("Enter a number : "))    
        else:
           print("Too big")
           guess = int(input("Enter a number : "))
    print("Correct !")
  
    break