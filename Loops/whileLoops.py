#while loops = a statements that will execute it's block of code
#               as long as it's condition remains true

name = None
# while len(name) == 0:
#     name = input("Enter your name: ")

while not(name):
    name = input("Enter your name: ")


print("Hello " + name)

