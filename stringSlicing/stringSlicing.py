#create a substring
#use indexing[] or slice()
#[start:stop:step]

name = "Dao Duy Thai"
firstName = name[0]
print(firstName)
firstName = name[0:3]
print(firstName)
firstName = name[:3]
print(firstName)
lastName = name[8:]
print(lastName)

funckyName = name[::2]
print(funckyName)

reversed_name = name[::-1]
print(reversed_name)

website1 = "www.daoduythai.com"
website2 = "www.wikipedia.com"
slice = slice(4, -4)
print(website1[slice])
print(website2[slice])



