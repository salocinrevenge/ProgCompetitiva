import sys
sys.setrecursionlimit(10000000)

def solve(a, b):
    if a == 1:
        return b
    if b == 1:
        return a
    if a == b:
        return 1
    if a > b:
        q = int(a/b)
        return q+solve(a-q*b, b)
    # a < b
    return solve(b,a)


def main():
    a,b = map(int,input().split())
    print(solve(a,b))

main()

"""
muitas recursoes!
"""