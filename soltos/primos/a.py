from math import floor


def solve(n, divisores):
    ans = 0
    for div in divisores:
        # print("testando ", div)
        outro = n/div
        if (outro + 1 - div)%2 == 0:
            ans+=1
            # print("ta certo")
    return ans

def get_divisores(n):
    divisores = []
    raiz = floor(n**0.5)
    for div in range(1, raiz+1):
        if n % div ==0:
            divisores.append(int(div))
            divisores.append(int(n/div))
    return divisores

def main():
    n = int(input())
    dobro = 2*n
    divisores = get_divisores(dobro)
    print(solve(dobro,divisores))







main()