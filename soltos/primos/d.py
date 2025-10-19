def fatorial(n):
    a = 1
    for i in range(2,n+1):
        a*= i
    return a

def main():
    a,b = map(int, input().split())

    print(fatorial(min(a,b)))

main()