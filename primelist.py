import primenumbertest

def primes_below(n):
    l = []
    for i in range(2,n):
        if primenumbertest.is_prime(i):
            l.append(i)
    print(l)

primes_below(20)



