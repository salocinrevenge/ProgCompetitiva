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

def decomposition_unique(n, primes):
    primos_decompostos = []
    raiz_n = int(n**0.5)
    for primo in primes:
        if primo > raiz_n:
            break
        if n % primo == 0:
            primos_decompostos.append(primo)
            while n % primo == 0:
                n /= primo
    n = int(n)
    if n != 1:
        primos_decompostos.append(n)
    return primos_decompostos

    
def totient(n, dividores):
    ans = n
    for div in dividores:
        ans *= 1 - 1/div

    return int(ans)


def main():
    MAX_N = 1000001
    t = int(input())
    primes = get_primes_until(ceil(MAX_N**0.5))
    for _ in range(t):
        n = int(input())
        dec_primos = decomposition_unique(n,primes)
        print(totient(n, dec_primos))



main()

"""
5
10
100
1000
10000
100000



5
1
2
3
4
5




"""