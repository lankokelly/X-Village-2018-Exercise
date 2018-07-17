class Animal():
    def __init__(self,feet_number = 4):
        self.feet_number = feet_number
    def shoot(self):    
        print("Hello! I'm a animal.")
class Dog(Animal):
    pass

dog = Dog()
print(dog.feet_number)
dog.shoot()