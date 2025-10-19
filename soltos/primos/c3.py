def main():
    a,b = map(int,input().split())
    soma = 0
    while a != 0 and b != 0:
        if a > b:
            soma += a // b
            a %= b
        else:
            soma += b // a
            b %= a
    
    print(soma)

main()