number_of_groups = input("number of groups: ")
groups = input("groups: ")
sep_groups = groups.split(" ")
sep_groups.sort()

taxis = 0
in_taxi = 0


for i in sep_groups:
    in_taxi = int(i)
    for j in range(1, len(sep_groups)):
        in_taxi += int(sep_groups[j])
        if in_taxi == 4:
            index = sep_groups.index(j)
            sep_groups.pop(index)
            taxis += 1
        elif in_taxi <= 4:
            continue
        elif in_taxi >= 4:
            break
    taxis += 1

print(taxis)