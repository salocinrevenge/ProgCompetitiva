n = int(input())
limite = int(n**0.5)
divisores = []
for i in range(1,limite+1):
    if n%i == 0:
        divisores.append(i)
        divisores.append(n//i)
for i in sorted(divisores):
    print(i,end=" ")
print()