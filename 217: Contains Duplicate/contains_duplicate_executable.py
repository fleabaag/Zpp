"""
Programa para resolver el problema #217
de LeetCode.
Author: @wallsified
Version: 1.0
"""

class ContainsDuplicate:
    """ 
    Clase que resuelve el problema #217
    de Leetcode
    """

    def contains_duplicate(self, nums: [int]) -> bool:
        nums.sort()
        for i in range (1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False

def main():
    """ 
    Main para ejecutar el programa en cuestión.
    """
    tests_dic = {
        "nums1": [1,2,3,1],
        "nums2": [1,2,3,4],
        "nums3": [1,1,1,3,3,4,3,2,4,2]
    }

    for index, value in tests_dic.items():
        output_string_one = f"Arreglo Ingresado: {value}, "
        resultado = ContainsDuplicate.contains_duplicate(value, value)
        output_string_two = f"Resultado: {resultado}"
        print(output_string_one, output_string_two)

if __name__ == "__main__":
    main()
