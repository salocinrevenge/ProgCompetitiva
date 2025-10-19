from math import ceil

def get_primes_until_and_pure_power(n):
    numeros = [i for i in range(2,n+1)]
    primaridade = [0]*(n-1)

    real_primes_and_powers = []

    for i in range(len(numeros)):
        if primaridade[i] < 2:
            real_primes_and_powers.append(numeros[i])
            if primaridade[i] == 0:
                for j in range(i+numeros[i], len(numeros), numeros[i]):
                    primaridade[j] += 1

    return real_primes_and_powers



def main():
    n = int(input())

    primes = get_primes_until_and_pure_power(n)
    print(len(primes))
    print(*primes)

main()