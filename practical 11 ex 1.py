

seats = [
    ['O', 'O', 'O'],
    ['O', 'O', 'O'],
    ['O', 'O', 'O']
]


print("===== MOVIE THEATRE SEATING =====")

for row in seats:
    print(" ".join(row))


row = int(input("\nEnter row number (1-3): "))
column = int(input("Enter column number (1-3): "))


row_index = row - 1
column_index = column - 1


if seats[row_index][column_index] == 'O':
    seats[row_index][column_index] = 'X'
    print("Seat reserved successfully!")
else:
    print("Sorry! Seat is already reserved.")


print("\n===== UPDATED SEATING =====")

for row in seats:
    print(" ".join(row))
