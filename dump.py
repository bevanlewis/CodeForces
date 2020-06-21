def top(clicks, row, column, changes):
    changes[row][column] += clicks[row][column]
    changes[row + 1][column] += clicks[row][column] # middle

def middle(clicks, row, column, changes):
    changes[row][column] += clicks[row][column]
    changes[row + 1][column] += clicks[row][column]  # bottom
    changes[row - 1][column] += clicks[row][column]  # top

def bottom(clicks, row, column, changes):
    changes[row][column] += clicks[row][column]
    changes[row - 1][column] += clicks[row][column]  # top

changes = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
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

for row in range(3):
    for column in range(3):
        if row == 1:
            top(clicks, row, column, changes)
        elif row == 2:
            middle(clicks, row, column, changes)
        elif row == 3:
            bottom(clicks, row, column, changes)








