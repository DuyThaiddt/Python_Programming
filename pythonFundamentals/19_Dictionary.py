# dictionary =  a changeable, unordered collection of unique key: value pairs
#               Fast because they use hashing, allow us to access a value quickly

capitals = {"Vietnam":"Ha Noi",
            "India":"New Dehli",
            "Russia":"Moscow",
            "China":"Beijing",
            "Germany":""}

# print(capitals["Vietnam"])
# print(capitals.get("Germany"))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
for key, value in capitals.items():
    print(key, value)

capitals.update({"German":"Berlin"})

