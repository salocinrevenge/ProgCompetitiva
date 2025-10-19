def visit(vertices, visitado, diametro_noh, i):
    if visitado[i]:
        return diametro_noh[i]
    visitado[i] = True
    diametro_max = diametro_noh[i]
    for j in range(len(vertices[i])):
        a = visit(vertices, visitado, diametro_noh, vertices[i][j])
        if a> diametro_max:
            diametro_max = a
    diametro_noh[i] = diametro_max+1
    return diametro_max+1

def main():
    n = int(input())
    vertices = []
    for _ in range(n):
        vertices.append([])
    visitado = [False] *n
    diametro_noh = [0]*n
    for i in range(n-1):
        a,b = map(int, input().split())
        vertices[a-1].append(b-1)

    diametro_max = 1
    for i in range(n):
        a = visit(vertices, visitado, diametro_noh, i)
        if a> diametro_max:
            diametro_max = a

    print(diametro_max)
    


main()


"""
5
5 4
4 3
3 2
2 1


5
4 3
3 2
5 4
3 1


"""