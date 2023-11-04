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

    def top_k_frequent(self, nums: [int], k: int) -> [int]:
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


def main():
    """ 
    Main para ejecutar el programa en cuestión.
    """
    arrays_dic = {
        "nums1": [1,1,1,2,3],
        "nums2": [1],
    }

    target_dic = {
        "target1": 2,
        "target2": 1,
    }

    # usamos zip() para iterar en dos diccionarios a la vez.
    for (num, array), (target, value) in zip(arrays_dic.items(), target_dic.items()):
        output_string_one = f"Arreglo Ingresado: {array}"
        output_string_two = f"Cantidad de Frecuentes: {value}"
        resultado = TopKFrequent.top_k_frequent(self = array, nums = array, k= value)
        output_string_three = f"Resultado: {resultado}"
        print(output_string_one, output_string_two, output_string_three, sep = ", ")

if __name__ == "__main__":
    main()
