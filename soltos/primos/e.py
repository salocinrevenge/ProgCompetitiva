from math import ceil

def get_primes_until(n):
    numeros = [i for i in range(2,n+1)]
    primo = [True]*(n-1)

    real_primes = []

    for i in range(len(numeros)):
        if primo[i]:
            real_primes.append(numeros[i])
            for j in range(i+numeros[i], len(numeros), numeros[i]):
                primo[j] = False

    return real_primes

def find(n, primes):
    i = 0
    prod = 1
    while prod <= n:
        prod *= primes[i]
        i+=1
    return i


def main():
    MAX_N = 10000
    primes = get_primes_until(ceil(MAX_N**0.5))
    # print(primes)

    q = int(input())

    for _ in range(q):
        n = int(input())
        print(max(find(n, primes)-1,0))






main()