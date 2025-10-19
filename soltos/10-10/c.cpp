#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <limits>

using namespace std;

int needleman_wunsch(const string& a, const string& b, const string& mode = "global", const vector<int>& pontuacao = {0, -1, -2}) {
    vector<vector<int>> matriz;
    // inicialização da primeira linha
    vector<int> linha;
    linha.push_back(0); // posição 0,0

    for (size_t i = 0; i < a.size(); ++i) {
        if (mode == "semi") {
            linha.push_back(0);
        }
        if (mode == "global") {
            linha.push_back((int(i) + 1) * pontuacao[2]);
        }
    }
    matriz.push_back(linha);

    // inicialização da primeira coluna
    for (size_t i = 0; i < b.size(); ++i) {
        if (mode == "semi") {
            matriz.push_back({0});
        }
        if (mode == "global") {
            matriz.push_back({(int(i) + 1) * pontuacao[2]});
        }
    }

    // preencher matriz geral
    for (size_t i = 1; i <= b.size(); ++i) {
        for (size_t j = 1; j <= a.size(); ++j) {
            int m;
            if (a[j - 1] == b[i - 1]) {
                m = matriz[i - 1][j - 1] + pontuacao[0];
            } else {
                m = matriz[i - 1][j - 1] + pontuacao[1];
            }
            int g1 = matriz[i - 1][j] + pontuacao[2];
            int g2 = matriz[i][j - 1] + pontuacao[2];
            matriz[i].push_back(max({m, g1, g2}));
        }
    }

    if (mode == "global") {
        return matriz.back().back();
    }
    if (mode == "semi") {
        int maximo = matriz.back().back();
        for (size_t j = 0; j < matriz[0].size(); ++j) {
            if (matriz.back()[j] > maximo) {
                maximo = matriz.back()[j];
            }
        }
        return maximo;
    }

    return 0; // fallback
}

int main() {
    string temp;
    getline(cin, temp); // ler linha vazia ou >query
    string query;
    getline(cin, query);

    vector<pair<string, int>> best;
    int maior = numeric_limits<int>::min();

    while (true) {
        string ignore1, ignore2, seq;
        if (!getline(cin, ignore1)) break;
        if (!getline(cin, ignore2)) break;
        if (!getline(cin, seq)) break;

        int pontuacao = needleman_wunsch(query, seq, "global", {5, -4, -7});
        if (pontuacao >= maior) {
            if (pontuacao > maior) {
                best.clear();
            }
            maior = pontuacao;
            best.emplace_back(seq, pontuacao);
        }
    }

    cout << "The query sequence is:\n" << query << "\n\n";
    cout << "The most similar sequences are:\n";
    for (auto& pair : best) {
        cout << "\n" << pair.first << "\n";
        cout << "The similarity score is: " << pair.second << "\n";
    }

    return 0;
}
