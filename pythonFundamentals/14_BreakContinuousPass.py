# Loop control statements = change a loop execution from its normal sequence
# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, act as a place holder

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break

# phoneNumber = "123-456-789"
# for i in phoneNumber:
#     if i == "-":
#         continue
#     print(i, end = "")

for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)