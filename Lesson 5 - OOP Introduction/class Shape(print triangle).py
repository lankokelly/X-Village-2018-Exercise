class Shape: 
    edge = 'default_edge'
    
    def set_edge(self, edge_arg):
        self.edge = edge_arg
        
    def display(self):
        for i in range(1,self.edge +1):
            print( "*" * i )


x = Shape()
x.set_edge(5)
x.display()
