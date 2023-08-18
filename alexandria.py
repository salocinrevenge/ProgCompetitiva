def buscaBinaria(lista, item):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            fim = meio - 1
        else:
            inicio = meio + 1
    return None

def buscaBinariaRecursiva(lista, item):
    if len(lista) == 0:
        return None
    
    meio = len(lista) // 2
    chute = lista[meio]
    if chute == item:
        return meio
    if chute > item:
        return buscaBinariaRecursiva(lista[:meio], item)
    else:
        return buscaBinariaRecursiva(lista[meio + 1:], item)
    
def dentroMapa(mapa, pos):
    if pos[0] < 0 or pos[0] >= len(mapa):
        return False
    if pos[1] < 0 or pos[1] >= len(mapa[0]):
        return False
    return True

def mostrarLabirinto(labirinto):
    for i in range(len(labirinto)):
        for j in range(len(labirinto[0])):
            print(labirinto[i][j][0] if labirinto[i][j][2] is None else labirinto[i][j][2], end = "")
        print()

def mazeSolver(maze, inicio = None, fim = None):
    # maze é uma matriz de tuplas de caracteres (char, distancia ao inicio, caminho ate inicio)
    # maze deve começar com (caracter, 0, None) em todas as posições
    # start e end são listas de tuplas (linha, coluna)
    # retorna uma lista de caracteres representando o caminho do inicio ao fim mais proximo
    # ou None se não houver caminho
    # altera o labirinto para resolve-lo

    if fim == None or inicio == None:
    # obtem os pontos de inicio e fim se eles n forem passados
        inicio = []
        fim = []
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j][0] == "I":
                    inicio.append((i, j))
                if maze[i][j][0] == "F":
                    fim.append((i, j))
    else:
        for pos in inicio:
            maze[pos[0]][pos[1]] = (caracteres["inicio"], 0, None)
        for pos in fim:
            maze[pos[0]][pos[1]] = (caracteres["fim"], 0, None)

    caracteres = {"caminho": ".", "parede": "#", "inicio": "I", "fim": "F"}
    direcoesIda = {"direita": (0, 1, "<"), "esquerda": (0, -1, ">"), "cima": (-1, 0, "V"), "baixo": (1, 0, "A")} # (linha, coluna, caracter indicando de onde vim)
    # seta os inicios e fins

    atuais = fim.copy()
    resolvido = False
    inicioAtingido = None   # para saber qual inicio esta mais proximo do fim
    while len(atuais) > 0:
        proximos = []
        for pos in atuais:
            for direcao in direcoesIda.values():
                novaPos = (pos[0] + direcao[0], pos[1] + direcao[1])
                if dentroMapa(maze, novaPos):
                    if maze[novaPos[0]][novaPos[1]][2] is None: # se ainda não foi visitado
                        if maze[novaPos[0]][novaPos[1]][0] == caracteres["inicio"]:    # chegou no fim
                            maze[novaPos[0]][novaPos[1]] = (caracteres["inicio"], maze[pos[0]][pos[1]][1] + 1, direcao[2])
                            inicioAtingido = novaPos
                            resolvido = True
                            break
                        if maze[novaPos[0]][novaPos[1]][0] == caracteres["caminho"]:    # Se eh caminho
                            maze[novaPos[0]][novaPos[1]] = (caracteres["caminho"], maze[pos[0]][pos[1]][1] + 1, direcao[2])
                            proximos.append(novaPos)
            if resolvido:
                break
        if resolvido:
            break
        atuais = proximos.copy()
    # se não foi resolvido
    if not resolvido:
        return None
    
    # monta o caminho
    caminho = []
    pos = inicioAtingido

    decidirDir = {"<": (0,-1), ">": (0,1), "V": (1,0), "A": (-1,0)}

    caminho.append(maze[pos[0]][pos[1]][2])
    while maze[pos[0] + decidirDir[maze[pos[0]][pos[1]][2]][0]][pos[1] + decidirDir[maze[pos[0]][pos[1]][2]][1]][0] != caracteres["fim"]: # enquanto não chegar no fim
        pos = (pos[0] + decidirDir[maze[pos[0]][pos[1]][2]][0], pos[1] + decidirDir[maze[pos[0]][pos[1]][2]][1])
        caminho.append(maze[pos[0]][pos[1]][2])
    return caminho

def getRelevante(labirinto):
    # retorna uma lista com as posicoes do inicio e do fim
    inicio = []
    fim = []
    for i in range(len(labirinto)):
        for j in range(len(labirinto[0])):
            if labirinto[i][j] == "I":
                inicio.append((i, j))
            if labirinto[i][j] == "F":
                fim.append((i, j))
    return inicio, fim


def main():
    # ler labirinto
    nLinhas, nColunas = map(int, input().split())
    labirinto = []
    for i in range(nLinhas):
        linhaLida = list(input())
        linhaLabirinto = []
        for j in range(len(linhaLida)):
            linhaLabirinto.append((linhaLida[j], 0, None))
        labirinto.append(linhaLabirinto)

    print("Resposta:")
    print(mazeSolver(labirinto))
    mostrarLabirinto(labirinto)

main()


"""
4 4
..I.
.#..
#F..
....

10 10
..........
.......F..
..F.#.....
....#.....
.######...
......#...
...I..#...
..........
......I...
..........
"""