def solve(palavras, not_letter):
    if len(palavras) < 2:
        return "YES"


    ja_vi_como_candidatas = set()
    for j in range(len(palavras[0])):
        candidatas = []
        for pal in palavras:
            if pal[j] in ja_vi_como_candidatas:
                continue
            candidatas.append(pal[j])
            ja_vi_como_candidatas.add(pal[j])

        
        letras_pos = dict()
        for letra in candidatas:
            if letra in not_letter:
                continue
            if letra in letras_pos.keys():
                continue
            flag_continue = False
            for pal in palavras:
                n_tenho_essa_letra = True
                for i in range(len(pal)):
                    if pal[i] == letra:
                        n_tenho_essa_letra = False
                        if letra not in letras_pos:
                            letras_pos[letra] = dict()
                        if i not in letras_pos[letra]:
                            letras_pos[letra][i] = []
                        letras_pos[letra][i].append(pal)
                if n_tenho_essa_letra:
                    flag_continue = True
                    break
            if flag_continue:
                continue
            for pos in letras_pos[letra].keys():
                teste_letra = solve(palavras= letras_pos[letra][pos], not_letter= not_letter.union({letra}))
                if teste_letra == "NO":
                    break
            else:
                return "YES"
    return "NO"
        

                

def main():
    l,n = map(int, input().split())
    palavras = []
    for _ in range(n):
        palavras.append(input())
    
    print(solve(palavras, set()))

main()

