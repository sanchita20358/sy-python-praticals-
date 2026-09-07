food = 0
travel = 0
shopping = 0

n = int(input("Enter number of expenses: "))

for i in range(n):
    category = input("Enter category: ").lower()
    amount = float(input("Enter amount: "))

    if category == "food":
        food = food + amount
    elif category == "travel":
        travel = travel + amount
    elif category == "shopping":
        shopping = shopping + amount
    else:
        print("Invalid category")

print("\n----- MONTHLY EXPENSE SUMMARY -----")
print("Food     =", food)
print("Travel   =", travel)
print("Shopping =", shopping)
print("Total    =", food + travel + shopping)
