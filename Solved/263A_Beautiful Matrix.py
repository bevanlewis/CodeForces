row_1 = input().split()
row_2 = input().split()
row_3 = input().split()
row_4 = input().split()
row_5 = input().split()

matrix = [row_1, row_2, row_3, row_4, row_5]
steps = 0
row_with_1 = 0
column_with_1 = 0

for row in range(0, 5):
    for column in range(0, 5):
        if int(matrix[row][column]) == 1:
            row_with_1 = row + 1
            column_with_1 = column + 1
            break


steps += abs(row_with_1 - 3)
steps += abs(column_with_1 - 3)

print(steps)
