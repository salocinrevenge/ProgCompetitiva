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

def kmp_search(P, T):

    M = len(P)
    N = len(T)  

    lps = compute_lps_array(P)
    print(lps)

    i = 0 
    j = 0 


    all_cases = []
    while i < N:
        if P[j] == T[i]:
            j += 1
            i += 1

        if j == M:
            all_cases.append(i-j)
            
            j = lps[j - 1]
            
        elif i < N and P[j] != T[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return all_cases

def main():
    a = input()
    b = input()
    print(len(kmp_search(b,a)))

main()
