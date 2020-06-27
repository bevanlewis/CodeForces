cupboard = []
time = 0
no_of_cupboards = int(input())
for i in range(no_of_cupboards):
    left_right = list(map(int, input().split()))
    cupboard.append(left_right)

left_open, right_open = 0, 0
for i in range(no_of_cupboards):
    if cupboard[i][0] == 1:  # left open
        left_open += 1  # total count of all the open doors
    if cupboard[i][1] == 1:  # right open
        right_open += 1

if left_open > right_open:  # left side has more open doors
    time += (no_of_cupboards - left_open)  # as number of closed door is lower and we will need to open them
    time += right_open  # time taken to close the open doors which are lower in number
else:
    time += (no_of_cupboards - right_open)
    time += left_open

print(time)
