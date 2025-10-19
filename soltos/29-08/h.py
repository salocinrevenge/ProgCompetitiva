def procurar_0mais_prox(i, cadeiras):
    dist = 0
    for _ in range(len(cadeiras)):
        dist += 1
        if i-dist>-1 and cadeiras[i-dist] == "0":
            return i-dist
        if i+dist < len(cadeiras) and cadeiras[i+dist] == "0":
            return i+dist
        
    raise Exception("erro")


def main():
    input()

    cadeiras = input().split()

    custo = 0

    for i in range(len(cadeiras)):
        if cadeiras[i] == "1":
            i_cadeira_prox = procurar_0mais_prox(i, cadeiras)
            cadeiras[i_cadeira_prox] = "2"
            custo += abs(i-i_cadeira_prox)

    

    print(custo)


main()


