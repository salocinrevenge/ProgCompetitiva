from copy import deepcopy

def contar_vizinhos_vivos(i,j,M):
    vizinhos = 0
    n_linhas, n_colunas = len(M), len(M[0])
    for di in range(-1,2):
        for dj in range(-1,2):
            if di == 0 and dj == 0:
                continue
            if M[(i+di)%n_linhas][(j+dj)%n_colunas] == "*":
                vizinhos+=1
    return vizinhos

def update(matriz):
    matriz_nova = deepcopy(matriz)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            vizinhos = contar_vizinhos_vivos(i,j,matriz)
            if vizinhos == 3:
                matriz_nova[i][j] = '*'
            elif vizinhos < 2 or vizinhos > 3:
                matriz_nova[i][j] = '-'
            
    return matriz_nova

def comp_hash(matriz):
    h = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == "*":
                h += i*25*25+j*25
    return h

def skip(hash_computados, visitados, hash_atual, c, n):
    # print("opa, vou spipar", visitados, hash_atual, c, n)
    precisa_rodar = c-n


    i = 0
    for vist in visitados:
        if vist[0] == hash_atual[0] and vist[1] == hash_atual[1]:
            inicio_ciclo = i
        i+=1
    tamanho_ciclo = len(visitados)-inicio_ciclo

    # print(f"vou pegar {precisa_rodar=} {tamanho_ciclo=} {(precisa_rodar)%tamanho_ciclo=} {visitados[inicio_ciclo+(precisa_rodar)%tamanho_ciclo]=}")
    alvo = visitados[inicio_ciclo+(precisa_rodar)%tamanho_ciclo]
    return hash_computados[alvo[0]][alvo[1]]

def simular(matriz, c):
    hashs_computados = dict()
    visitados = []
    for n in range(c):
        hash_atual = comp_hash(matriz)
        if hash_atual not in hashs_computados:
            hashs_computados[hash_atual] = [matriz]
        else:
            i =0
            for mats in hashs_computados[hash_atual]:
                if mats == matriz:
                    return skip(hashs_computados, visitados, [hash_atual,i], c,n)
                i+=1
            hashs_computados[hash_atual].append(matriz)
        visitados.append([hash_atual,len(hashs_computados[hash_atual])-1])
        matriz = update(matriz)
    return matriz

def mostrar_matriz(matriz):
    for linha in matriz:
        for char in linha:
            print(char,end="")
        print()

def main():
    n,m,c = map(int, input().split())

    matriz = []
    for i in range(n):
        matriz.append(list(input()))
    
    matriz = simular(matriz, c)
    mostrar_matriz(matriz)

main()



"""
4 6 3
------
------
------
-***--

4 6 1
------
------
------
-***--



"""