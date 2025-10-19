fatoriais = dict()

def fatorial(n):
    if n in fatoriais:
        return fatoriais[n]


    if n <=1:
        return 1
    fatoriais[n] = n*fatorial(n-1)
    return fatoriais[n]

def calcular(jogadas, prob):
    chance = 0
    for n in range(jogadas, 2*jogadas):
        temp = fatorial(2*jogadas-1)/(fatorial(n)*fatorial(2*jogadas-1-n))
        chance += temp * (prob**n) * ((1-prob)**(2*jogadas-1-n))
    return chance

def main():
    n = int(input())


    for _ in range(n):
        jogadas = int(input())
        prob = float(input())
        print(f'{calcular(jogadas, prob):.2f}')


main()

"""
5
25
0.5
25
0.4
25
0.6
15
0.8
10
0.95

"""