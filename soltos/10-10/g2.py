def solve(pd, inicio, fim, ruas):
    if inicio == fim:
        pd[inicio][fim] = ""
        return ""
    if pd[inicio][fim]:
        return pd[inicio][fim]
    caracter = ruas[inicio][fim]
    for j in range(inicio+1,fim):
        caminho = ruas[inicio][j]
        assert caminho != '*'
        for k in range(j, fim):
            caminho2 = ruas[fim][k]
            if j>k:
                break
            if caminho2 != caminho:
                continue
            char = solve(pd, j, k, ruas)
            char = caminho+char+caminho
            if len(char) > len(caracter) or (len(char) == len(caracter) and char < caracter):
                caracter = char
            
    pd[inicio][fim] = caracter
    return pd[inicio][fim]




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
        print(res)

main()