"""
Programa para resolver el problema #242
de LeetCode, alternativamente
Author: @wallsified
Version: 1.0

Nota: La versión de Leetcode es 
únicamente la función dentro de la clase. 
El resto se añade para hacerlo ejecutable.

"""

class ValidAnagram:
    """ 
    Clase que resuelve el problema #217
    de Leetcode
    """

    @staticmethod
    def valid_anagram(string: str, compare: str) -> bool:
        """
        Se contruyen objetos "Counter" que crean un diccionario
        donde cada entrada es "caractér: incidencias" (ie. 'a' : 5). 
        Posteriormente se verifica si se trata del mismo diccionario
        (mismas llaves, mismos valores.)
        
        Regresa
        -------
            bool: Si los diccionarios son iguales o no.

        """
        return sorted(string) == sorted(compare) #otra solución de una linea

def main():
    """ 
    Main para ejecutar el programa en cuestión.
    """

    test_list = ["anagram", "nagaram", "rat", "car", "asdfghjkl", "lkjhgfdsa"]

    for i in range(0, len(test_list), 2):
        output_string_one = f"Cadena Ingresada: '{test_list[i]}'."
        output_string_two = f"Comparada Con: '{test_list[i + 1]}'."
        result = ValidAnagram.valid_anagram(string=test_list[i], compare=test_list[i+1])
        output_string_three = f"¿Es un anagrama válido?: {result}"
        print(output_string_one, output_string_two, output_string_three, sep=" ")

if __name__ == "__main__":
    main()
