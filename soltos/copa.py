times = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
for i in range(3,-1,-1):
    perderam = []
    for j in range(2**(i)):
        resultado = list(map(int, input().split()))
        if resultado[0]<resultado[1]:
            perderam.append(times[j*2])
        else:
            perderam.append(times[j*2+1])
    for perdedor in perderam:
        times.remove(perdedor)
print(times[0])