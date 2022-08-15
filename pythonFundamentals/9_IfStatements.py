# if statement = a block of code that will execute if its condition is true

age = int(input("How old are you: "))
if age < 0:
    print("You haven't been born yet!")
elif age == 100:
    print("You are an century old!")
elif age < 18:
    print("You are a child!")
elif age >= 18:
    print("You are an adult!")