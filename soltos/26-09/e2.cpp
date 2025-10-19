#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <algorithm> // Para std::max, embora não seja usado no solve

using namespace std;

// A função solve retorna uma string ("YES" ou "NO")
// 'palavras': A lista de palavras a serem consideradas.
// 'not_letter': O conjunto de caracteres que não podem ser usados.
string solve(const vector<string>& palavras, const unordered_set<char>& not_letter) {
    // Equivalente a 'if len(palavras) < 2: return "YES"'
    if (palavras.size() < 2) {
        return "YES";
    }

    // A palavra em 'palavras[0]' deve existir, pois size >= 2
    int tamanho_palavra = palavras[0].length();

    // Equivalente a 'ja_vi_como_candidatas = set()'
    unordered_set<char> ja_vi_como_candidatas;

    // Itera sobre as posições (índices) das letras nas palavras
    // Equivalente a 'for j in range(len(palavras[0])):'
    for (int j = 0; j < tamanho_palavra; ++j) {
        // Equivalente a 'candidatas = []'
        vector<char> candidatas; 

        // Coleta as letras candidatas nesta posição 'j' que ainda não foram vistas em 'ja_vi_como_candidatas'
        // Equivalente a:
        // for pal in palavras:
        //     if pal[j] in ja_vi_como_candidatas:
        //         continue
        //     candidatas.append(pal[j])
        //     ja_vi_como_candidatas.add(pal[j])
        for (const string& pal : palavras) {
            char letra_atual = pal[j];
            if (ja_vi_como_candidatas.count(letra_atual) == 0) { // count() retorna 1 se estiver presente, 0 se não
                candidatas.push_back(letra_atual);
                ja_vi_como_candidatas.insert(letra_atual); // add do python é insert em C++ set/unordered_set
            }
        }
        
        // Equivalente a 'letras_pos = dict()'
        // Mapeamento: letra -> (posição -> lista de palavras com essa letra nessa posição)
        // char -> (int -> vector<string>)
        unordered_map<char, unordered_map<int, vector<string>>> letras_pos;

        // Itera sobre as letras candidatas coletadas
        // Equivalente a 'for letra in candidatas:'
        for (char letra : candidatas) {
            // Equivalente a:
            // if letra in not_letter:
            //     continue
            if (not_letter.count(letra) > 0) {
                continue;
            }

            // A próxima verificação 'if letra in letras_pos.keys(): continue' é redundante
            // na tradução para C++, porque 'candidatas' vem de 'ja_vi_como_candidatas',
            // e 'letras_pos' é criada vazia em cada iteração de 'j'. No entanto,
            // podemos manter o fluxo lógico (embora letras_pos.keys() estaria vazio aqui).

            bool flag_continue_letra = false; // Equivalente a 'flag_continue' no Python

            // Verifica se a letra está presente em TODAS as palavras
            // e preenche o dicionário 'letras_pos'
            // Equivalente a:
            // for pal in palavras:
            //     n_tenho_essa_letra = True
            //     ...
            //     if n_tenho_essa_letra:
            //         flag_continue = True
            //         break
            for (const string& pal : palavras) {
                bool n_tenho_essa_letra = true;
                // Itera sobre as letras de 'pal'
                for (int i = 0; i < pal.length(); ++i) {
                    if (pal[i] == letra) {
                        n_tenho_essa_letra = false;
                        
                        // Garante que as estruturas aninhadas existam antes de acessar
                        // letras_pos[letra] e letras_pos[letra][i]
                        // O C++ unordered_map com [] insere se a chave não existe, usando o construtor default
                        letras_pos[letra][i].push_back(pal); 
                        
                        // O 'if' para verificar a existência de 'letra' em 'letras_pos' e 'i' em 'letras_pos[letra]'
                        // não é estritamente necessário em C++ com '[]', mas o push_back é o que importa.
                        // O código Python era um pouco mais defensivo com a criação dos dicts.
                    }
                }
                
                if (n_tenho_essa_letra) {
                    flag_continue_letra = true;
                    break;
                }
            }

            // Equivalente a 'if flag_continue: continue'
            if (flag_continue_letra) {
                continue;
            }

            // Se chegamos até aqui, a 'letra' está em todas as 'palavras'.
            
            // Tenta a chamada recursiva para cada posição 'pos' onde a 'letra' aparece
            // Equivalente a 'for pos in letras_pos[letra].keys():'
            bool all_recursive_calls_succeeded = true;
            
            for (const auto& par_pos_palavras : letras_pos.at(letra)) {
                // 'pos' é par_pos_palavras.first
                // 'sub_palavras' é par_pos_palavras.second
                
                // Cria o novo conjunto 'not_letter' para a chamada recursiva: not_letter.union({letra})
                unordered_set<char> new_not_letter = not_letter;
                new_not_letter.insert(letra); // Union com {letra}
                
                // Chamada recursiva
                string teste_letra = solve(par_pos_palavras.second, new_not_letter);

                // Equivalente a 'if teste_letra == "NO": break'
                if (teste_letra == "NO") {
                    all_recursive_calls_succeeded = false;
                    break;
                }
            }

            // Equivalente a 'else: return "YES"'
            // Se o loop acima completou sem um 'break' (all_recursive_calls_succeeded é true),
            // significa que para ESTA letra, TODAS as sub-recursões retornaram "YES".
            if (all_recursive_calls_succeeded) {
                return "YES";
            }
        }
    }
    
    // Equivalente a 'return "NO"'
    return "NO";
}

// Função principal para entrada/saída
void main_c_plus_plus() {
    int l, n;
    
    // Leitura da primeira linha: l, n
    if (!(cin >> l >> n)) return; // Adiciona um pequeno controle de erro de leitura

    vector<string> palavras;
    // Leitura das 'n' palavras
    for (int i = 0; i < n; ++i) {
        string palavra;
        cin >> palavra;
        palavras.push_back(palavra);
    }
    
    // Chama a função solve e imprime o resultado
    // O set inicial é vazio: unordered_set<char>()
    cout << solve(palavras, unordered_set<char>()) << endl;
}

// Ponto de entrada do programa C++
int main() {
    // Otimizações de I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    main_c_plus_plus();
    
    return 0;
}