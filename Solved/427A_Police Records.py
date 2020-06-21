number_of_events = int(input('Enter number of events: '))
events = input('Events: ')
sep_events = events.split(" ")

crime = 0
officer = 0
untreated = 0

print(sep_events)

for i in sep_events:
    if int(i) < 0 and officer == 0:
        crime += 1
    elif int(i) > 0:
        officer += int(i)
    elif int(i) < 0 and officer >= 0:
        officer -= 1

print(crime)
