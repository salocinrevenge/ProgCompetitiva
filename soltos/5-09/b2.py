def solve(n, k):
    if k > n:
        return 0
    
    if k == n:
        return 1
    
    result = 2**(n-k)
    print("resolvendo para ", n," e ",k, "deu ", pd[n][k])
    for i in range(k, n-2):
        result += 2**(i-k)

    return result + solve(n-1, k)
    



def main():
    while True:
        try:
            n, k = map(int, input().split())
        except:
            break

        print(solve(n,k))


    



main()