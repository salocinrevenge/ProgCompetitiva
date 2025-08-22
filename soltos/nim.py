def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        nums = map(int, input().split())

        xor = 0
        for num in nums:
            xor = xor ^ num
        if xor == 0:
            print("second")
        else:
            print("first")



main()