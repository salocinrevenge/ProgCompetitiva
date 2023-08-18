def main():
    n = int(input())
    extremos = []
    for i in range(n):
        entrada = input().split()
        extremos.append((int(entrada[0]), -1, i))
        extremos.append((int(entrada[1]), 1, i))

    # print(extremos)
    # ordena com base no primeiro elemento de forma crescente
    extremos.sort()
    # print(extremos)

    maximo = 0
    cortando = 0

    cortados = set()
    resposta = None
    for i in range(len(extremos)):
        cortando+=extremos[i][1]*-1
        if extremos[i][1] == -1:
            cortados.add(extremos[i][2]+1)
        else:
            cortados.remove(extremos[i][2]+1)
        if cortando > maximo:
            maximo = cortando
            resposta = set()
            for elemento in cortados:
                resposta.add(elemento)

    # imprime os elementos de resposta separados por espaco
    print(maximo)
    print(*resposta)



main()