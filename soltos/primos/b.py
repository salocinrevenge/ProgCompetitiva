from math import ceil

def is_t_prime(n):
    raiz_int = int(n**0.5)
    if raiz_int*raiz_int == n:
        if is_prime(raiz_int):
            return True
    return False


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n in (0,1):
        return False
    limite = ceil(n**0.5)+1
    for i in range(3,limite,2):
        if n % i == 0:
            return False
    return True

def main():
    _ = input()
    nums = list(map(int, input().split()))

    for n in nums:
        if is_t_prime(n):
            print("YES")
            continue
        print("NO")

main()