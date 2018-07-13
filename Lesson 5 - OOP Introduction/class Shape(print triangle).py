class Shape: 
    edge = 'default_edge'
    
    def set_edge(self, edge_arg):
        self.edge = edge_arg
        
    def display(self):
        #self.edge = 5
        ctr1 = 1
        while(self.edge > 0):
            while (ctr1 < 6):
                print( "*" * ctr1 )
                ctr1 += 1
                self.edge -= 1
            break


x = Shape()
x.set_edge(5)
x.display()