def main():
    a, b = map(int, input().split())
    a_mods = [a//5,a//5,a//5,a//5,a//5]
    b_mods = [b//5,b//5,b//5,b//5,b//5]
    for i in range((a%5)):
        a_mods[i]+=1
    for i in range((b%5)):
        b_mods[i]+=1

    somas = a_mods[0]*b_mods[3]
    somas += a_mods[1]*b_mods[2]
    somas += a_mods[2]*b_mods[1]
    somas += a_mods[3]*b_mods[0]
    somas += a_mods[4]*b_mods[4]
    print(somas)


main()