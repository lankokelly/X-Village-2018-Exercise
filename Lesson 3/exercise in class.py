# immutable objects  # int, float, bool, str, etc.
# mutable objects    # list, set, dict, etc.
# exercise 1.1
a = "Hello"
b = a
b = "World"
print(a) #Hello

# exercise 1.2
a = ["Hello"]
b = a
b[0] = "World"
print(a) #['World']

#------------------------#

# example 2
def g(n):
    tmp = 1
    for i in range(1, n+1 ,1):
        tmp = tmp * i
    return tmp

x = g(5) # function call, 1*2*3*4*5
print(x)

# example 3  Computes total cost, including 3% tax
# on number items at a cost of price each
def totalcost(number, price):
    tax_rate = 0.03 # 3% tax
    cost = number * price
    total = cost + (cost*tax_rate)
    return total

n = 5
p = 30
bill = totalcost(n, p)
print('Bill: ',bill)
