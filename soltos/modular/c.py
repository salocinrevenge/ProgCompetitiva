def main():
    a, b= map(int, input().split())
    prod = 1

    for i in range(a+1,b+1):
        if i % 10 == 0:
            prod = 0
            break
        prod *= (i%10)
    print(prod%10)



main()