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