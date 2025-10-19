
def solve_diff(n,k,pd):
    if n < k:
        pd[n] = 2**n
    if pd[n]:
        return pd[n]
    
    resp = 0
    for i in range(k):
        resp += solve_diff(n-1-i,k,pd)
    pd[n] = resp
    return resp



def main():
    while True:
        pd = [None]*101
        try:
            n, k = map(int, input().split())
            print(2**n-solve_diff(n,k,pd))
        except:
            break

main()


"""
4 1
4 2
4 3
4 4
6 2


"""