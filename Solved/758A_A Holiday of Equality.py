no_of_citizens = int(input("Enter no. of citizens: "))
welfare_of_each = input("Enter Welfare: ")
sep_welfare = welfare_of_each.split(" ")

max_money = int(max(sep_welfare))

burles = 0
for i in sep_welfare:
    burles += (max_money - int(i))

print(burles)