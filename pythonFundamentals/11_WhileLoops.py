# while loop = a statement that will execute its block of code as long as its condition remains true
#
# name = ""
#
# while len(name) == 0:
#     name = input("Enter your name: ")
# print("Hello " + name)

name = None
while not name:
    name = input("Enter your name: ")
print("Hello " + name)

# while 1 == 1:
#     print("Hello, I'm stuck in a loop")


