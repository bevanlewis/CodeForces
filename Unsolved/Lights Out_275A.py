changes = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

switch_board = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

row_1 = input("Enter: ").split()
row_2 = input("Enter: ").split()
row_3 = input("Enter: ").split()

clicks = [row_1, row_2, row_3] # has the input

for row in range(1, 4):
    for column in range(1, 4):
        if int(clicks[row][column])%2 = 0:




            changes[row][column - 1] = int(clicks[row - 1][column - 1])  # Left
            changes[row][column + 1 ] = int(clicks[row - 1][column - 1]) # Right
            changes[row][column] = int(clicks[row - 1][column - 1])
            changes[row - 1][column] = int(clicks[row - 1][column - 1])  # Down
            changes[row + 1][column] = int(clicks[row - 1][column - 1])  # Up

print(changes)








