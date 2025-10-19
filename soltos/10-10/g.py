def solve(pd, inicio, fim, ruas):
    if inicio == fim:
        pd[inicio][fim] = (0,0, 0, "", "")
    if pd[inicio][fim]:
        return pd[inicio][fim]
    melhor_inicio, melhor_fim, melhor_comprimento, caracter,base = fim,fim,1,ruas[inicio][fim], ruas[inicio][fim]
    for j in range(inicio+1,fim):
        caminho = ruas[inicio][j]
        for k in range(j, fim):
            caminho2 = ruas[fim][k]
            if j>k:
                break
            if caminho2 != caminho:
                continue
            cur_ini,cur_fim, compr, char, base2 = solve(pd, j, k, ruas)
            compr +=2
            if (compr == melhor_comprimento and caracter > caminho)  or (compr == melhor_comprimento and caracter == caminho and base2 < base) or compr > melhor_comprimento:
                melhor_inicio, melhor_fim, melhor_comprimento, caracter, base = j,k, compr, caminho, base2
            
    pd[inicio][fim] = (melhor_inicio,melhor_fim, melhor_comprimento, caracter, base)
    return pd[inicio][fim]

def reconstruct(pd, inicio,fim):
    if inicio == fim:
        return ""
    else:
        melhor_inicio, melhor_fim, melhor_comprimento, caracter, base =pd[inicio][fim]
        if melhor_comprimento == 1:
            return caracter
        string_retorno = reconstruct(pd, melhor_inicio, melhor_fim)
        return caracter+string_retorno+caracter





def main():
    n_testes = int(input())

    for _ in range(n_testes):

        n = int(input())

        ruas = []
        for rua in range(n):
            ruas.append(list(input()))
        pd = []
        for rua in range(n):
            pd.append([None]*n)
        res = solve(pd, 0,n-1, ruas)
        print(reconstruct(pd, 0, n-1))

main()