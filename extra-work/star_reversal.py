rows = 4 # Initialize the number of rows
for i in range(rows, 0, -1):  # Loop from the number of rows down to 1
    for j in range(i):
        # This code prints a right-angled triangle pattern of stars in reverse order
        print("*", end="")
    print()  # Move to the next line after each row
