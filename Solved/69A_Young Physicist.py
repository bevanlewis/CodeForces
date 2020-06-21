no_of_forces = int(input())  # "Enter no of forces: "
x, y, z = 0, 0, 0

for i in range(no_of_forces):
    forces = input().split()  # "Enter coordinates: "
    x += int(forces[0])
    y += int(forces[1])
    z += int(forces[2])

if x == 0 and y == 0 and z == 0:
    print("YES")
else:
    print("NO")