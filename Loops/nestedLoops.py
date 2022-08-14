#nested loops = the inner loop will finish all of it's iterations before
#                finishing one iteration of the outer loops

rows = int(input("Rows: "))
columns = int(input("Columns: "))
symbol = input("Enter symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end ="")
    print()
