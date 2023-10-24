"""
Programa para resolver el problema #1
de LeetCode usando fuerza bruta (O(n^2)).
Author: @wallsified
Version: 1.0

"""

class TwoSumBrute:
    """
    Clase que resuelve por fuerza bruta el problema.
    "Dada una matriz de números enteros y un objetivo entero, 
    devuelva los índices de los dos números que sumen el objetivo."
    """

    def two_sum_brute(self, nums: [int], target: int) -> [int]:
        """
        Método para resolver por fuerza bruta el problema

        Regresa
        -------
        Lista con los indices de los valores que sumados dan el objetivo

        """
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)): # i+1 evita usar el mismo indice en cada vuelta.
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []

def main():
    """ 
    Main para ejecutar el programa en cuestión.
    """
    arrays_dic = {
        "nums1": [2,7,11,15],
        "nums2": [3,2,4],
        "nums3": [3,3]
    }

    target_dic = {
        "target1": 9,
        "target2": 6,
        "target3":6
    }

    # usamos zip() para iterar en dos diccionarios a la vez.
    for (num, array), (target, value) in zip(arrays_dic.items(), target_dic.items()):
        output_string_one = f"Arreglo Ingresado: {array}"
        output_string_two = f"Objetivo a Sumar: {value}"
        resultado = TwoSumBrute.two_sum_brute(self = array, nums = array, target= value)
        output_string_three = f"Los indices a sumar son: {resultado}"
        print(output_string_one, output_string_two, output_string_three, sep = ", ")


if __name__ == "__main__":
    main()
