def carbon_foot(rate):
    def way(km): 
        return rate * km 
    if type == 'car': return 0.24

f = carbon_foot('car')
print(f(100)) 

#rate * km
#rate(kg/km): 公車:0.03, 汽車:0.24, 機車:0.06

#way = carbon_foot('car')
#way(100): 0.24 * 100 = 24.0 (kg/km)