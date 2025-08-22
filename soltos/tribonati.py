def prod(A, B):
    C = []
    for i in range(len(A)):
        c_i = []
        for j in range(len(B[0])):
            sum = 0
            for k in range(len(A[i])):
                sum = (sum + (A[i][k] * B[k][j])%1000000009) %1000000009
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


def tribonati(n):
    A = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
    base = [[2],[1],[0]]

    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2

    return prod(pot(A, n-3), base)[0][0]



def main():
    while True:
        n = int(input())

        if n == 0:
            break

        print(tribonati(n))


main()