"""
Programa para resolver el 
problema #347 de LeetCode
Author: @wallsified
Version: 1.0
"""

from collections import Counter

class TopKFrequent:
    """
    Clase que devuelve un arreglo de los k elementos más
    repetidos en una lista
    """

    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        """
        Método para identificar los valores con mas 
        incidencias usando Counter.

        Regresa
        ------
        Lista con los k elementos más repetidos
        
        """

        dic = Counter(nums) #Creamos un diccionario con los contadores por incidencias
        frequency_sorted = dic.most_common(k) # Most common justo nos da las k-tuplas más comunes
        results = []
        for tupla in frequency_sorted:
            # desenpacamos los valores de la tupla, en este caso nos importa solo el primer valor
            (value, repetitions) = tupla
            results.append(value)
        return results
