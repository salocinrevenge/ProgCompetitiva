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

def z_algorithm(s):
    n = len(s)
    z = [0] * n 
    l, r = 0, 0 

    for i in range(1, n):
        if i <= r:

            k = i - l
            z[i] = min(r - i + 1, z[k])

        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    return z



def main():
    a = input()
    print(*z_algorithm(a))

    print(*compute_lps_array(a))

main()
