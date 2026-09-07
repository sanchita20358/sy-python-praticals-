name1 = input("Enter item 1 name: ")
qty1 = int(input("Enter quantity: "))
price1 = float(input("Enter price: "))

name2 = input("Enter item 2 name: ")
qty2 = int(input("Enter quantity: "))
price2 = float(input("Enter price: "))

name3 = input("Enter item 3 name: ")
qty3 = int(input("Enter quantity: "))
price3 = float(input("Enter price: "))

total = (qty1 * price1) + (qty2 * price2) + (qty3 * price3)

print("\n----- GROCERY BILL -----")
print(name1, qty1, price1, qty1 * price1)
print(name2, qty2, price2, qty2 * price2)
print(name3, qty3, price3, qty3 * price3)
print("------------------------")
print("Total Bill =", total)
