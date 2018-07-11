def carbon_foot(rate):
        def way(km): # Generate and return way 
            return rate * km # action retains N from enclosing scope return action
        if ('car'):
            way=0.24
        return way

f = carbon_foot('car')
print(f(100)) #24.0

#rate * km
#rate(kg/km): 公車:0.03, 汽車:0.24, 機車:0.06

#way = carbon_foot('car')
#way(100): 0.24 * 100 = 24.0 (kg/km)