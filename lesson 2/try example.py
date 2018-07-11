#break
n = 1000
while n > 0:
    n -= 1
    print (n)
    if (n % 11 == 0):
        print("correct", n)
        break
#continue
n = 10
while n > 0:
    if n == 5:
        n -= 1
        continue
    print(n, end=' ')
    n -= 1
print("End")

#m*m
n = 7
i = 1
j = 1
while i <= n:
    while j <= n:
        print(i, '*', j, '=', i* j, sep='', end='\t')
        j += 1
    print("")
    j = 1
    i += 1

#find max value in list
a = [10, 2, 8, 15, 21, 1]
max = 0 #need to assign a value to max because it will be compared in for loop
for i in a:
    if max < i:
        max = i
print(max)
    
#list of list
A = [-1, -10]
B = [5, -5]
C = [1, 1]
D = [-2, 3]
dots = [  ['A', A], ['B', B], ['C', C], ['D', D]  ]

for i in dots:
    print(i[0], "is in", end=' ')
    if i[1][0] > 0 and i[1][1] > 0:
        print("I")
    elif i[1][0] < 0 and i[1][1] > 0:
        print("II")
    elif i[1][0] < 0 and i[1][1] < 0:
        print("III")
    elif i[1][0] > 0 and i[1][1] < 0:
        print("IV")

#

