#Ex 1 print m*m table
def f(m):
       for i in range(1,m+1):
            for j in range(1,m+1):
                print(i, '*', j, '=', i*j, '\t', sep='',end='') #seperate
            print("")
f(9)