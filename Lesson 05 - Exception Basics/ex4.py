class RelationException(Exception):
    def __init__(self, error_msg):
        self.message = error_msg
    def __str__(self):
        return self.message  

relation = {'Jason':'Mary', 'Mary':'Jason', 'Jennifer':'Ken', 'Ken':'Jennifer', 'Tina':'Kim', 'Kim':'Tina'}
def check(pa, pb):
    if((pa not in relation) == False):
        if relation[pa] != pb:
            print("Are you sure that",pa,"and",pb,end="")
            raise RelationException(" are in love with each other?")
    else :
        print("No relation found")
        print("Are you sure that",pa,"and",pb,end="")
        raise RelationException(" are in love with each other?")
    
try:
    p1 = input("Please enter the first person: ")
    p2 = input("Please enter the second person: ")
    check(p1, p2)
    print("{} and {} are in love with each other!".format(p1, p2))
    
except RelationException as e:
    print(e)