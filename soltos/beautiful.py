matriz = []
for i in range(5):
    matriz.append(input().split())
    if '1' in matriz[i]:
        cord = (i,matriz[i].index('1'))
print(abs(cord[0]-2)+abs(cord[1]-2))