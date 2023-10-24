"""
Programa para resolver el problema #1
de LeetCode de forma lineal.
Author: @wallsified
Version: 1.0
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # esta la vi en las soluciones pero vale la pena entenderla
        nums_indexed = {} # iterar sobre el diccionario es O(n)
        for index, number in enumerate(nums):
            complement = target - number #la idea es ¿en la posición index, cuanto falta para alcanzar el objetivo tomando en cuenta el valor en index?
            if complement in nums_indexed: # buscamos si el complemento en está en el diccionario
                return [index, nums_indexed[complement]] #entonces los valores que queremos están en index y en valor de la llave del complemento
                #digamos, si nuestro complemento es 2, y se encuentra en la posición 10, nums_indexed[complement] nos regresa el valor de la posción del complemento.
            nums_indexed[number] = index # caso contrario, añadimos al diccionario donde se añade de forma "numero : posición"