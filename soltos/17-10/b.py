def counting_sort(k, n, SA, tempSA, RA):
    maxi = max(300, n)  # ASCII range ou n, o que for maior
    c = [0] * maxi

    for i in range(n):
        idx = RA[i + k] if i + k < n else 0
        c[idx] += 1

    sum = 0
    for i in range(maxi):
        t = c[i]
        c[i] = sum
        sum += t

    for i in range(n):
        idx = RA[SA[i] + k] if SA[i] + k < n else 0
        tempSA[c[idx]] = SA[i]
        c[idx] += 1

    for i in range(n):
        SA[i] = tempSA[i]

def constructSA(T):
    n = len(T)
    RA = [0] * n
    tempRA = [0] * n
    SA = [0] * n
    tempSA = [0] * n

    for i in range(n):
        RA[i] = ord(T[i])  # Inicializa RA com os códigos ASCII
        SA[i] = i          # Inicializa SA: [0, 1, 2, ..., n-1]

    k = 1
    while k < n:
        counting_sort(k, n, SA, tempSA, RA)     # Ordena pelos segundos k caracteres
        counting_sort(0, n, SA, tempSA, RA)     # Ordena pelos primeiros k caracteres

        r = 0
        tempRA[SA[0]] = r
        for i in range(1, n):
            same = (RA[SA[i]] == RA[SA[i - 1]] and
                    (RA[SA[i] + k] if SA[i] + k < n else -1) ==
                    (RA[SA[i - 1] + k] if SA[i - 1] + k < n else -1))

            tempRA[SA[i]] = r if same else r + 1
            if not same:
                r += 1

        for i in range(n):
            RA[i] = tempRA[i]

        if RA[SA[n - 1]] == n - 1:
            break
        k <<= 1

    return SA

def lcp_construction(s, p):
    n = len(s)
    rank = [0] * n
    for i in range(n):
        rank[p[i]] = i

    k = 0
    lcp = [0] * (n - 1)
    for i in range(n):
        if rank[i] == n - 1:
            k = 0
            continue
        j = p[rank[i] + 1]
        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k += 1
        lcp[rank[i]] = k
        if k > 0:
            k -= 1
    return lcp


def calcular(n_subs, k, sufix_array, lcp, i,a):
    falta = k-n_subs
    return a[sufix_array[i]:sufix_array[i]+falta+lcp[i]]

def main():
    a = input()
    k = int(input())
    T = a + '$'
    SA = constructSA(T)
    # Ignorar o índice do sufixo que começa com '$'
    sufix_array = SA[1:]  
    lcp = lcp_construction(T[:-1], sufix_array)  # Passa T sem '$'

    n_subs = 0
    lcp = [0] + lcp
    for i in range(len(sufix_array)):
        adicionar = len(a) - sufix_array[i] - lcp[i]
        if n_subs+adicionar>=k:
            print(calcular(n_subs, k, sufix_array, lcp, i,a))
            return
        else:
            n_subs += adicionar

main()
