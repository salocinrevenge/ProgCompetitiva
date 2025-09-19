def extendedEuclid( a , b ):
    global x0, y0, d
    if b == 0:
        x0 = 1
        y0 = 0
        d = a
        return
    extendedEuclid(b,a%b)
    x1 = y0
    y1 = x0 - ( a // b ) * y0
    x0 = x1
    y0 = y1



def main():
    global x0, y0, d
    t = int(input())
    for _ in range(t):
        n,s,k = map(int, input().split())
        extendedEuclid(k,n)

        b = (-s)%n

        if b%d == 0:
            
            x0 = ((b//d) * x0)%(n//d)
            print(x0)
        else:
            print(-1)



main()