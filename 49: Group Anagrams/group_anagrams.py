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
    def group_anagrams(self, strs: List[str]) -> List[[str]]:
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
