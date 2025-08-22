def prod(A, B, m):
    C = []
    for i in range(len(A)):
        c_i = []
        for j in range(len(B[0])):
            sum = 0
            for k in range(len(A[i])):
                sum = (sum + (A[i][k] * B[k][j])%m) %m
            c_i.append(sum)
        C.append(c_i)
    return C


def pot(A, k, m):
    if k == 1:
        return A
    if k % 2 == 1:
        sub = pot(A, k//2, m)
        return prod(prod(A,sub, m),sub, m)
    sub = pot(A,k//2, m)
    return prod(sub,sub, m)


def tribonati(n, m):
    A = [[1, 1, 1], [1, 0, 0], [0, 0, 1]]
    base = [[1],[1],[1]]

    if n == 0:
        return 1
    if n == 1:
        return 1

    return prod(pot(A, n-1, m), base, m)[0][0]



def main():
    i = 0
    while True:
        n, m = map(int, input().split())

        if n == 0 and m ==0:
            break
        i+=1
        print(f"Case {i}: {n} {m} ",end = "")
        print(tribonati(n, m))


main()