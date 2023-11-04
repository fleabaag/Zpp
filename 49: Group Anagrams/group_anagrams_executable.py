"""
Programa para resolver el problema #49
de LeetCode.
Author: @wallsified
Version: 1.0
"""

class GroupAnagrams:
    """
    Clase que resuelve el problema #49
    de Leetcode
    """
    def group_anagrams(self, strs: [str]) -> [[str]]:
        """_summary_

        Parametros
        ----------
            - strs[str]: Lista con palabras a validar

        Regresa
        -------
            -[[str]]: Lista de listas con los anagramas organizados
        """

        wording = {}
        for word in strs:
            temp = ''.join(sorted(word))
            if temp not in wording:
                wording[temp] = [word]
            else:
                wording[temp].append(word)
        results = []
        for value in wording.values():
            results.append(value) #esto es solo estilización
        return results


def main():
    """
    Main para ejecutar el programa en cuestión.
    """
    tests_dic = {
        "words1": ["eat","tea","tan","ate","nat","bat"],
        "words2": [""],
        "words": ["a"]
    }

    for index, value in tests_dic.items():
        output_string_one = f"Arreglo Ingresado: {value}, "
        resultado = GroupAnagrams.group_anagrams(value, value)
        output_string_two = f"Acomodo de Duplicados: {resultado}"
        print(output_string_one, output_string_two)

if __name__ == "__main__":
    main()
