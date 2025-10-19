def needleman_wunsh(a,b,mode = "global", pontuacao = (0,-1,-2)): # (match gap mismatch)
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
                m = matriz[i-1][j-1] + pontuacao[2] 
            g1 = matriz[i-1][j] + pontuacao[1]
            g2 = matriz[i][j-1] + pontuacao[1]
            matriz[i].append(max(g1,g2,m))
    
    # print(matriz)
    if mode == "global":
        return matriz[-1][-1]
    if mode == "semi":
        maximo = matriz[-1][-1]
        for j in range(len(matriz[0])):
            maximo = max(maximo, matriz[-1][j])
        return maximo
    

def main():
    while True:
        try:
            a = input()
            b = input()
            print(needleman_wunsh(a,b,"global",(1,0,0)))
        except:
            return


main()