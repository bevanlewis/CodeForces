n = int(input(""))
holder = []

for i in range(1, n + 1):
    holder.append(i)

if len(holder) == 1:
    print(-1)
else:
    for j in range(0, len(holder) - 1, 2):
        a = holder[j]
        b = holder[j+1]
        holder[j+1] = a
        holder[j] = b

    for k in holder:
        print(k, end=" ")