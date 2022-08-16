# tuple = collection which is ordered and unchangeable used to group together related data

student = ("Duy Thai", 21, "male")
print(student.count(21))
print(student.index("male"))

for i in student:
    print(i)

if "Duy Thai" in student:
    print("Duy Thai is here")

