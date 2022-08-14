#logical operator (and, or, not) = used to check if two or more statements are true?

temp = int(input("What is the temperature outside?: "))


if not(temp >= 0 and temp <= 30):
    print("The temperature is good today!")
    print("Go outside!")
elif not(temp < 0 or temp > 30):
    print("The temperature is not good today!")
    print("Stay inside!")








