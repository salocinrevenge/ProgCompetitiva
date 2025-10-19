def main():
    n,x = map(int, input().split())
    ts = list(map(int, input().split()))

    somas = dict()
    for num in ts:
        novo = dict()
        novo[num] = 1
        for key in somas.keys():
            if key+num > x:
                continue
            if key+num not in novo:
                novo[key+num] = 0
            novo[key+num] += somas[key]
        
        for key in novo:
            if key not in somas:
                somas[key] = 0
            somas[key] += novo[key]

    if x not in somas:
        print("0")
    else:
        print(somas[x])



main()


# n passou :(