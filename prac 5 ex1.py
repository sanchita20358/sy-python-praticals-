total = 0
count = 0

while True:
    expense = float(input("Enter expense (0 to stop): "))

    if expense == 0:
        break

    total = total + expense
    count = count + 1

print("\n----- MONTHLY EXPENSE -----")
print("Total Expenditure =", total)
print("Number of Expenses =", count)
