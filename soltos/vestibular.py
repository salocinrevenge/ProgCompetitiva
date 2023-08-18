n = input()
A = input()
B = input()
c = 0
for i in range(int(n)):
    if A[i] == B[i]:
        c+=1
print(c)
