def compute_lps_array(P):
    M = len(P)
    lps = [0] * M
    length = 0
    i = 1
    while i < M:
        if P[i] == P[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def main():
    lps = compute_lps_array(input())
    # print(lps)
    ans = []
    atual = lps[-1]
    while atual > 0 :
        ans.append(atual)
        # print(atual)
        atual = lps[atual - 1]
    print(*ans[::-1])
    
            

main()