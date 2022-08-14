#set = collection which is unordered, unindexed, not allow any duplicated value

utensils = {"fork", "spoon", "knife"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()

dishes = {"bowl", "plate", "cup", "knife"}
# utensils.update(dishes)

dinnerTable = utensils.union(dishes)

# print(utensils.difference(dishes))
# print(dishes.difference(utensils))
# for i in dinnerTable:
#     print(i)

print(utensils.intersection(dishes))


