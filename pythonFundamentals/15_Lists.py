# list = used to store multiple items in a single variable

food = ["pizza", "hamburger", "chips", "spaghetti"]
# print(food)
# print(food[2])
food[2] = "sushi"
# print(food[2])

food.append("ice cream")
food.remove("sushi")
food.pop()
food.insert(0, "cake")
food.sort()
# food.clear()

for x in food:
    print(x)



