number = int(input())
percentage = list(map(int, input().rstrip().split()))
add = sum(percentage)
ans = add/number
print(ans)
