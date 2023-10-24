#include <unordered_map>
#include <string>
using namespace std;
class Solution {
public:

    /**
     * @brief Verifica si dos cadenas son anagramas.
     * 
     * Este método compara las frecuencias
     * de los caracteres en las cadenas dadas para determinar si son anagramas.
     *
     * @param s Primera cadena.
     * @param t Segunda cadena.
     * @return true si las cadenas son anagramas, false en caso contrario.
     */
    bool isAnagram(string s, string t) {
        // Si las longitudes son diferentes, no pueden ser anagramas.
        if (s.length() != t.length()) {
            return false;
        }

        // Diccionarios para almacenar las frecuencias de los caracteres.
        unordered_map<char, int> countS, countT;

        // Contabiliza las frecuencias de los caracteres en las cadenas s y t.
        for (size_t i = 0; i < s.length(); ++i) {
            ++countS[s[i]];
            ++countT[t[i]];
        }

        // Compara las frecuencias de los caracteres en las cadenas s y t.
        for (auto const& pair : countS) {
            char c = pair.first;
            if (countS[c] != countT[c]) {
                return false;
            }
        }
        
        return true;  // Retorna true si todas las frecuencias coinciden.
    }
};