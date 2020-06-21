no_of_student_and_time = input("Enter ").split()
n, t = no_of_student_and_time
output = ''
while 1 <= int(n) and int(t) <= 50:
    queue = input('Enter: ')
    queue_list = []
    for i in queue:
        queue_list.append(i)

    for j in range(int(t)):
        for i in range(0, len(queue_list) - 1, 2):
            if queue_list[i] == 'B' and queue_list[i + 1] == 'G':
                queue_list[i + 1] = 'B'
                queue_list[i] = 'G'
        break

    for k in queue_list:
        output += k

    print(output)
    break



