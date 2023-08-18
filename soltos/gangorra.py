valores = list(map(int, input().split()))
if valores[0]*valores[1]<valores[2]*valores[3]:
    print(1)
elif valores[0]*valores[1]>valores[2]*valores[3]:
    print(-1)
else: print(0)