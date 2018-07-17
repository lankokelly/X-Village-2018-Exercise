class Life:
    def __init__(self,n,p=1):
        self.n = n
        self.p = p
    
    def set_map(self):
        init_map = [['*']*self.n]
        k=self.n
        for self.n in range(1,self.n):
            init_map.append(['*']*k)

        self.map = init_map
        self.k = k

        self.map[int((self.k-1)/2-1)][int((self.k-1)/2-1)]='0'
        self.map[int((self.k-1)/2-1)][int((self.k-1)/2)]='0'
        self.map[int((self.k-1)/2-1)][int((self.k-1)/2+1)]='0'
        self.map[int((self.k-1)/2)][int((self.k-1)/2-1)]='0'
        self.map[int((self.k-1)/2+1)][int((self.k-1)/2)]='0'
    
    def display(self):
        for i in range(0,self.k):
            for j in range (0,self.k):
                print (self.map[i][j],end=" ")
            print("")
        print("")

map_1 = Life(5,1)
map_1.set_map()
map_1.display()
