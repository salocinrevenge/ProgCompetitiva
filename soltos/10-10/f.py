def obter_sequencia(a,b,matriz, pontuacao, pos = None, mode = "global"):
    if not pos:
        pos = (len(matriz)-1, len(matriz[-1],-1))

    sequencia_final = []
    while pos != (0,0):
        #gap 1
        if pos[1]>0:
            if matriz[pos[0]+0][pos[1]-1] + pontuacao[2] == matriz[pos[0]][pos[1]]:
                pos = (pos[0]+0,pos[1]-1)
                # print("gap, pos: ", pos)
                continue

        if pos[0]>0 and pos[1]>0:
            #match
            if matriz[pos[0]-1][pos[1]-1] + pontuacao[0] == matriz[pos[0]][pos[1]] and a[pos[1]-1] == b[pos[0]-1]:
                pos = (pos[0]-1,pos[1]-1)
                sequencia_final.append(a[pos[1]])
                # print("match, pos: ", pos, "a: ", a[pos[0]])
                continue

            #mismatch
            if matriz[pos[0]-1][pos[1]-1] + pontuacao[1] == matriz[pos[0]][pos[1]]:
                pos = (pos[0]-1,pos[1]-1)
                # print("mis, pos: ", pos)
                continue

        if pos[0]>0:
            #gap 2
            if matriz[pos[0]-1][pos[1]-0] + pontuacao[2] == matriz[pos[0]][pos[1]]:
                pos = (pos[0]-1,pos[1]-0)
                # print("gap, pos: ", pos)
                continue
        
    return sequencia_final[::-1]



def needleman_wunsh(a,b,mode = "global", pontuacao = (0,-1,-2), obter_seq = False): # (match mismatch gap)
    matriz = []
    # inicialização da primeira linha
    linha = [0] # 0,0
    for i in range(len(a)):
        if mode == "semi":
            linha.append(0)
        if mode == "global":
            linha.append((i+1)*pontuacao[2])
    matriz.append(linha)

    # inicialização da primeira coluna
    for i in range(len(b)):
        if mode == "semi":
            matriz.append([0])
        if mode == "global":
            matriz.append([(i+1)*pontuacao[2]])
    
    # print(matriz)
    # preencher matriz geral
    for i in range(1,len(b)+1):
        for j in range(1,len(a)+1):
            if a[j-1] == b[i-1]:
                m = matriz[i-1][j-1] + pontuacao[0] 
            else:   
                m = matriz[i-1][j-1] + pontuacao[1] 
            g1 = matriz[i-1][j] + pontuacao[2]
            g2 = matriz[i][j-1] + pontuacao[2]
            matriz[i].append(max(g1,g2,m))
    
    # print("matriz: ###################")
    # mostrar_matriz(matriz)
    # print("################")

    melhor_pontuacao = None
    if mode == "global":
        melhor_pontuacao = matriz[-1][-1]
    if mode == "semi":
        maximo = matriz[-1][-1]
        for j in range(len(matriz[0])):
            maximo = max(maximo, matriz[-1][j])
        melhor_pontuacao = maximo
    if not obter_seq:
        return melhor_pontuacao
    else:
        return melhor_pontuacao, obter_sequencia(a,b,matriz, pontuacao, (len(matriz)-1, len(matriz[-1])-1), mode)
    

def mostrar_matriz(matriz):
    for linha in matriz:
        for num in linha:
            print(num, end=" ")
        print()


def main():
    n_test_cases = int(input())
    for _ in range(n_test_cases):
        n_strings = int(input())
        s1 = input()
        for n_string in range(n_strings-1):
            s2 = input()
            pont, s1 = needleman_wunsh(s1,s2,"global", (1,0,0), obter_seq=True)
            # print("Hey, olha o s1: ",s1)

        print(pont)
        print(''.join(s1))
        
    


main()

"""


"""