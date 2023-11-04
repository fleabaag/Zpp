class Solution:
    """
    Solución al problema ArrayProductExceptSelf en LeetCode
    """

    def product_except_self(self, nums: List[int]) -> List[int]:
        """
        Funcion para devolver una lista tal que respuesta[i] sea igual 
        al producto de todos los elementos de numeros excepto lista[i].
        """

        tamanio = len(nums)
        resultado = []

        # Creamos dos arreglos del mismo tamanio para recorrer el arreglo dado
        prod_izq = [0]*tamanio
        prod_der = [0]*tamanio

        # Casos Especiales de los arreglos
        prod_izq[0] = 1
        prod_der[tamanio-1] = 1

        # Vamos anadiendo valores a los arreglos izquierdo y derecho.
        # Consideramos i-1 para no pasarnos del indice.
        # En el caso del derecho, consideramos tamanio-i-1 y tamanio-i para ir en reversa.
        for i in range(1,tamanio):

            prod_izq[i] = prod_izq[i-1] * nums[i-1]
            prod_der[tamanio-i-1] = prod_der[tamanio-i] * nums[tamanio-i]

        # Multiplicamos cada entrada de cada arreglo y lo anadimos al arreglo vacio.
        for i in range(tamanio):
            resultado.append(prod_izq[i] * prod_der[i])

        return resultado
