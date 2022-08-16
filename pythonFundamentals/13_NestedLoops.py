# nested loop = The "inner loop" will finish all of its iterations before finishing one iteration of the "outer loop"
rows = int(input("Enter rows: "))
columns = int(input("Enter columns: "))
symbol = input("Enter symbol: ")
for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()

