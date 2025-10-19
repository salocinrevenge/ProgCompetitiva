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

def is_prime_on_this_list(primes, number):
    inicio = 0
    fim = len(primes) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        chute = primes[meio]
        if chute == number:
            return meio
        if chute > number:
            fim = meio - 1
        else:
            inicio = meio + 1
    return None

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

    
def totient_independente(n, primes, memo):
    if n in memo:
        return memo[n]
    divisores = decomposition_unique(n, primes) 
    ans = n
    for div in divisores:
        ans *= 1 - 1/div

    ans = int(ans)
    memo[n] = ans
    return ans

def calcular_quantos_primos_ja_foi(sweetness, primes):
    primos_ate_aqui = [0]
    atual = 0
    for i in range(len(sweetness)):
        # b_is_prime = is_prime_on_this_list(primes, sweetness[i]) # talvez usar set e in? ou calcular primo na moral?
        # if b_is_prime != None:
        if sweetness[i] in primes:
            atual += 1
        primos_ate_aqui.append(atual)
    return primos_ate_aqui


def main():
    MAX_N = 1000000001
    MAX_N = 10001
    primes = get_primes_until(ceil(MAX_N**0.5))
    primes_set = set(primes)    # solucao trocar por set
    n, q = map(int,input().split())
    pratos = list(map(int, input().split()))
    sweetness = []
    memo = dict()
    for prato in pratos:
        sweetness.append(totient_independente(prato, primes, memo))    # da pra usar um dicionario para guardar os ja calculados
    
    quantos_primos_ja_foi = calcular_quantos_primos_ja_foi(sweetness, primes_set) # primes set

    # print(quantos_primos_ja_foi)

    for _ in range(q):
        l, r = map(int,input().split())
        print(quantos_primos_ja_foi[r]-quantos_primos_ja_foi[l-1])





main()

"""
3 2
3 2 1
1 2
2 3


1
0

wtf isso passou??
"""