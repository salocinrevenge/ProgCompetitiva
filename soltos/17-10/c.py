
#Python traduzido dos slides

MAX_N = 1000010  # Constante para tamanho máximo

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

def lcp_construction(s: str, p: list[int]) -> list[int]:
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


def main():
    global T, n, SA
    # T = input()+"$"+input()
    a = input()
    b = input()
    T = a+'$'+b+'#'
    constructSA()
    sufix_array = SA[1:n]
    # print(sufix_array)
    lcp = lcp_construction(T[:-1],sufix_array)
    # print(lcp)

    best_tam = 0
    best_i = None
    for i in range(len(lcp)):
        tam = lcp[i]
        if tam <= best_tam: # tamanho n é melhor
            continue
        if sufix_array[i] < len(a) and sufix_array[i+1] < len(a):   # dois da primeira string
            continue
        if sufix_array[i] > len(a) and sufix_array[i+1] > len(a):   # dois da segunda string
            continue
        if sufix_array[i] == len(a) or sufix_array[i+1] == len(a):  # pegou o caracter de separacao
            continue
        best_i = i
        best_tam = tam
    
    if best_i == None:
        print(0,0,0,0)
        return 

    trocar = False
    inicio1 = sufix_array[best_i]
    if inicio1 > len(a):
        trocar = True
        inicio1 -= len(a)+1
    fim1 = inicio1 + best_tam

    inicio2 = sufix_array[best_i+1]
    if inicio2 > len(a):
        inicio2 -= len(a)+1
    fim2 = inicio2+best_tam

    if trocar:
        inicio1,inicio2,fim1,fim2 = inicio2,inicio1,fim2,fim1

    print(inicio1,fim1,inicio2,fim2)

main()