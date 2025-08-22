def prod(A, B):
    C = []
    for i in range(len(A)):
        c_i = []
        for j in range(len(B[0])):
            sum = 0
            for k in range(len(A[i])):
                sum = (sum + (A[i][k] * B[k][j])%1000000007) %1000000007
            c_i.append(sum)
        C.append(c_i)
    return C


def pot(A, k):
    if k == 1:
        return A
    if k % 2 == 1:
        sub = pot(A, k//2)
        return prod(prod(A,sub),sub)
    sub = pot(A,k//2)
    return prod(sub,sub)



def main():
    n,m,k = map(int, input().split())
    A = []

    for _ in range(n):
        A.append([0]*n)

    for _ in range(m):
        a,b = map(int,input().split())
        A[a-1][b-1] += 1

    B = pot(A,k)
    print(B[0][n-1]%1000000007)


main()

"""
3 4 8
1 2
2 3
3 1
3 2



"""