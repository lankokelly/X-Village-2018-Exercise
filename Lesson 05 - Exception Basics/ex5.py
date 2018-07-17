import random
item_in_shop = {"soybean_sauce": 0, "milk": 4, "salt": 10, "soybean_milk": 3}
items = [item for item in item_in_shop.keys()]
cnt = 5

def buy(item):
    if (item_in_shop[item]==0):
        raise Exception
    else:
        item_in_shop[item]-=1
    print("Mommy! I've bought {} for you!".format(item))

while cnt:
    cnt -= 1
    index = random.randint(0,3)
    item = items[index]
    try:
        buy(item)
    except Exception:
        print(item,"is not on sale right now")