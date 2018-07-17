def func(m):
    pet=["dog","cat"]
    for i in range(0,m):
        if(i<2):
            print(pet[i])
        else:
            raise IndexError
try:
    func(3)
except IndexError :
    print("index out of range, it must be 0 or 1 ! We just have 2 pets now")
else:
    print(pet)
