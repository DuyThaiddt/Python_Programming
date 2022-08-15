#slicing = create a substring by extracting elements from another string
#   indexing[] or slice()
#   [start:stop:step]

name = "DUY THAI"
firstName = name[:3]
lastName = name[4:]
funckyName = name[::2]
reversedName = name[::-1]
print(firstName)
print(lastName)
print(funckyName)
print(reversedName)

website = "https://google.com"
website1 = "https://wikipedia.com"
slice = slice(8,-4)
print(website[slice])
print(website1[slice])









