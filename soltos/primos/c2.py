from math import floor

def main():
    a,b = map(int,input().split())
    soma = 0
    while True:
        if a == 0:
            break
        if a == 1:
            soma +=b
            break
        if b == 1 or b ==0:
            soma +=a
            break
        if a == b:
            soma +=1
            break
        if a > b:
            q = floor(a/b)
            soma += q
            a = a-q*b
            continue
        if a < b:
            a,b = b,a
    print(soma)

main()