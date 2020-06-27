k = int(input().rstrip())
l = int(input().rstrip())
m = int(input().rstrip())
n = int(input().rstrip())
d = int(input().rstrip())
dragons = [0 * i for i in range(d)]
trauma = 0

for pan in range(0, d, k):
    dragons[pan] += 1

for balcony in range(0, d, l):
    dragons[balcony] += 1

for heel in range(0, d, m):
    dragons[heel] += 1

for mom in range(0, d, n):
    dragons[mom] += 1

for i in dragons:
    if i > 0:
        trauma += 1

print(trauma)
