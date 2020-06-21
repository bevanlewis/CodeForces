number = int(input("Enter the number: "))

if number%2 == 0:  # even
    max_no_of_primes = number//2
    print(max_no_of_primes)
    for i in range(max_no_of_primes):
        print(2, end=" ")

else:  # odd
    number += 1
    max_no_of_primes = number//2
    print(max_no_of_primes - 1)
    for i in range(max_no_of_primes - 2):
        print(2, end=" ")
    print(3)
