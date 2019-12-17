n = 2
i = int(input("Number to get primes\n"))

while i > 1:
    if i % n == 0:
        i = i / n
        print(n)
    else:
        n = n + 1
