def nth_prime(n):
    primes = [2]
    num = 3
    while len(primes) < n:
        if all(num % prime != 0 for prime in primes):
            primes.append(num)
        num += 2
    return primes[-1] 

n = 5
result = nth_prime(n)
print(f"{n}-ta liczba pierwsza: {result}")



def nth_prime_and_sum(n):
    primes, num = [], 2

    while len(primes) < n:
        if all(num % prime != 0 for prime in primes):
            primes.append(num)
        num += 1
    return primes[-1], sum(primes)


n = 5
nth_prime, prime_sum = nth_prime_and_sum(n)
print(prime_sum)