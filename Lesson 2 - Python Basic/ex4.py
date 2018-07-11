# Exercise 1
a = 1
b = 2
c = -63
root = b^2 - 4*a*c
x  = (-b + root**0.5)/ 2 / a
x_ = (-b - root**0.5)/ 2 / a
print ( round(x) )
print ( round(x_))

#Exercise 2
print ("\nExercise 2")
A = [-1, -10]
B = [5, -5]
C = [1, 1]
D = [-2, 3]      
Point = [A,B,C,D]
index = 0
while(index < 4):
  if ( Point[index][0]  > 0) :
      if Point[index][1]  > 0:
          print (Point[index],(" : I"))
      else:
          print (Point[index],(" : IV"))
  else:
      if Point[index][1] > 0:
          print (Point[index],(" : II"))
      else:
          print (Point[index],(" : III"))   
  index += 1

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






#while(2,100)
#while range(2,i)
#if (i%j!=0) :print(i)
 



