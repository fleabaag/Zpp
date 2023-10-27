#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    /**
     * Agrupa anagramas de una lista de palabras.
     *
     * Esta función toma un vector de palabras (strings) y devuelve un vector de
     * vectores que agrupa las palabras que son anagramas entre sí. Dos palabras
     * son anagramas si una se puede reorganizar para formar la otra.
     *
     * @param strs Vector de strings con las palabras a agrupar.
     * @return Un vector de vectores de strings, donde cada vector interno contiene
     *         palabras que son anagramas entre sí.
     */
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // Mapa para almacenar los grupos de anagramas. La clave es una palabra ordenada
        // alfabéticamente y el valor es un vector de palabras que son anagramas de esa clave.
        unordered_map<string, vector<string>> h;
        
        for (const string& word : strs) {
            string sortedWord = word;
            sort(sortedWord.begin(), sortedWord.end());
            
            // Agrupa la palabra original bajo la palabra ordenada en el mapa
            h[sortedWord].push_back(word);
        }
        
        vector<vector<string>> final;
        // Itera sobre los valores en el mapa y los añade al vector final
        for (const auto& pair : h) {
            final.push_back(pair.second);
        }
        
        return final;
    }
};

int main() {
    Solution sol;
    vector<string> strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
    vector<vector<string>> result = sol.groupAnagrams(strs);
    
    for (const auto& group : result) {
        for (const string& word : group) {
            cout << word << " ";
        }
        cout << endl;
    }
    
    return 0;
}
