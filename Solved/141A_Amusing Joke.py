run = True
while run:
    guest_name = input("").upper()
    host_name = input("").upper()
    name_mash = guest_name + host_name

    joke_mash = input("").upper()

    if len(guest_name) > 100 or len(host_name) > 100 or len(name_mash) > 100:
        run = False

    for i in joke_mash:
        if joke_mash.count(i) != name_mash.count(i):
            print("NO")
            run = False
            break
    else:
        print("YES")
        run = False
