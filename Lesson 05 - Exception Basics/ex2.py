def div(dividend, divisor):
    if(int(divisor)==0):
        print("when dividend=",dividend," divisor=",divisor,end="")
        print(", warning : divisor can not equal to zero")
    else:
        print("The answer is {}".format(dividend/divisor))

for i in range(5, -1, -1):
    for j in range(5, -1, -1):
        div(i, j)