"""
Programa para resolver el problema #1
de LeetCode de forma lineal.
Author: @wallsified
Version: 1.0
"""

class TwoSumLineal:
    """
    Clase que resuelve por fuerza bruta el problema.
    "Dada una matriz de números enteros y un objetivo entero,
    devuelva los índices de los dos números que sumen el objetivo."
    """

    def two_sum_lineal(self, nums: [int], target: int) -> [int]:
        """
        Método para resolver por fuerza bruta el problema

        Regresa
        -------
        Lista con los indices de los valores que sumados dan el objetivo

        """
        # esta la vi en las soluciones pero vale la pena entenderla
        nums_indexed = {} # iterar sobre el diccionario es O(n)
        for index, number in enumerate(nums):
            complement = target - number #la idea es ¿en la posición index, cuanto falta para
                #alcanzar el objetivo tomando en cuenta el valor en index?
            if complement in nums_indexed: # buscamos si el complemento en está en el diccionario
                return [nums_indexed[complement], index] #entonces los valores que queremos
                    # están en index y en valor de la llave del complemento, digamos, si nuestro
                    # complemento es 2, y se encuentra en la posición 10, nums_indexed[complement]
                    # nos regresa el valor de la posción del complemento.
            nums_indexed[number] = index # caso contrario, añadimos al diccionario donde se añade
                    #de forma "numero : posición"

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
        resultado = TwoSumLineal.two_sum_lineal(self = array, nums = array, target= value)
        output_string_three = f"Los indices a sumar son: {resultado}"
        print(output_string_one, output_string_two, output_string_three, sep = ", ")


if __name__ == "__main__":
    main()
