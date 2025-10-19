# Contar divisores

def is_t_prime(n):
    n_divs = 0
    for i in range(1,n+1,1):
        if n % i == 0:
            n_divs +=1
            # print(f"HEY eu divido por {i} ")
    if n_divs == 3:
        return True
    return False

def main():
    _ = input()
    nums = list(map(int, input().split()))

    for n in nums:
        if is_t_prime(n):
            print("YES")
            continue
        print("NO")

main()