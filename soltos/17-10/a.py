
#Python traduzido dos slides

MAX_N = 500010  # Constante para tamanho máximo

# Arrays principais
T = ""                  # A string de entrada
n = 0                   # Comprimento da string
RA = [0] * MAX_N        # Rank array
tempRA = [0] * MAX_N    # Rank temporário
SA = [0] * MAX_N        # Suffix array
tempSA = [0] * MAX_N    # Suffix temporário
c = [0] * MAX_N         # Para o counting sort

def counting_sort(k):
    global n, SA, tempSA, RA, c
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

def constructSA():
    global T, n, RA, tempRA, SA
    n = len(T)

    for i in range(n):
        RA[i] = ord(T[i])  # Inicializa RA com os códigos ASCII
        SA[i] = i          # Inicializa SA: [0, 1, 2, ..., n-1]

    k = 1
    while k < n:
        counting_sort(k)     # Ordena pelos segundos k caracteres
        counting_sort(0)     # Ordena pelos primeiros k caracteres

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

def main():
    global T, n, SA
    T = input()+"$"
    constructSA()
    print(*SA[1:n])
main()