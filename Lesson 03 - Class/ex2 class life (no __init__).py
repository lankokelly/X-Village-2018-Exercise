class Life:
    def set_map(self,m):
        init_map = [['*']*m]
        k=m
        for m in range(1,m):
            init_map.append(['*']*k)
        #print(m,k)
        for i in range(0,k):
            for j in range (0,k):
                print (init_map[i][j],end=" ")
            print("")
        print("")
        self.map = init_map
        self.k = k

    def set_pattern (self,p=1):
        if (p==1):
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

map_1 = Life()
map_1.set_map(5)
map_1.set_pattern(1)
map_1.display()

map_2 = Life()
map_2.set_map(7)
map_2.set_pattern(1)
map_2.display()