def main():
    x,k,d = map(int, input().split())
    x = abs(x)
    menor_pos = x % d
    menor_neg = abs(menor_pos - d)

    distancia_total = abs(x-menor_pos)

    n_passos = distancia_total//d

    if n_passos>=k:
        print(x-k*d)
        return
    if n_passos%2 == k%2:
        print(menor_pos)
        return
    print(menor_neg)
    return
    
    



main()