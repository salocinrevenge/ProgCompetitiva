from itertools import chain, combinations

def powerset(s):
    """Gera o powerset de um iterável."""
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

def main():
    n,x = map(int, input().split())
    ts = list(map(int, input().split()))
    ps1 = powerset(ts[len(ts)//2:])
    ps2 = powerset(ts[:len(ts)//2])

    somas = dict()

    resp = 0

    for conjunto in ps1:
        soma = 0
        for num in conjunto:
            soma += num
        if soma not in somas:
            somas[soma] = 1
        else:
            somas[soma] +=1


    for conjunto in ps2:
        soma = 0
        for num in conjunto:
            soma += num
        if x - soma in somas:
            resp += somas[x-soma]

    print(resp)





main()

# passou com pipy