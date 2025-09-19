def main():
    n = int(input())
    if n == 0:
        print(1)
        return
    finals = [8,4,2,6]
    print(finals[(n%4)-1])

main()