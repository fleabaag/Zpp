# Notas Z++

### Glosario de Estructuras y Conceptos Básicos en C++

#### 1. Arreglos
```cpp
int arr[10]; // Arreglo de enteros de tamaño 10
```

#### 2. Vectores
```cpp
#include <vector>
using namespace std;
vector<int> v; // Vector de enteros
```

#### 3. Pares
```cpp
#include <utility>
using namespace std;
pair<int, int> p = {1, 2}; // Par de enteros
```

#### 4. Listas Enlazadas
```cpp
#include <list>
using namespace std;
list<int> l; // Lista enlazada de enteros
```

#### 5. Pilas
```cpp
#include <stack>
using namespace std;
stack<int> s; // Pila de enteros
```

#### 6. Colas
```cpp
#include <queue>
using namespace std;
queue<int> q; // Cola de enteros
```

#### 7. Conjuntos
```cpp
#include <set>
using namespace std;
set<int> s; // Conjunto de enteros
```

#### 8. Mapas
```cpp
#include <map>
using namespace std;
map<int, int> m; // Mapa que mapea enteros a enteros
```

#### 9. Mapas Desordenados
```cpp
#include <unordered_map>
using namespace std;
unordered_map<char, int> count; // Mapa desordenado que mapea caracteres a enteros
```

#### 10. Espacios de Nombres y `using namespace std`
```cpp
#include <iostream>
using namespace std;
int main() {
    cout << "Hello, World!" << endl;
    return 0;
}
```

#### 11. Directivas `#include`
```cpp
#include <iostream> // Incluye la biblioteca estándar de entrada/salida
```

#### 12. Plantillas (Templates) y Operador `<>`
```cpp
#include <unordered_map>
#include <vector>
#include <string>
using namespace std;

int main() {
    unordered_map<string, vector<string>> h; // Mapa desordenado que mapea strings a vectores de strings
    unordered_map<char, int> countS, countT; // Mapas desordenados que mapean caracteres a enteros
    return 0;
}
```

#### 13. Iteradores
```cpp
#include <vector>
using namespace std;

int main() {
    vector<int> v = {1, 2, 3};
    vector<int>::iterator it = v.begin(); // Iterador para un vector de enteros
    return 0;
}
```

### Hacks y Trucos en C++

#### 1. Uso de `auto`
```cpp
auto x = 5; // x es automáticamente de tipo int
```

#### 2. Rango `for` Loop
```cpp
#include <vector>
using namespace std;

int main() {
    vector<int> v = {1, 2, 3};
    for (auto& elem : v) {
        // Código
    }
    return 0;
}
```

#### 3. Funciones Lambda
```cpp
auto sum = [](int a, int b) { return a + b; };
```

Este glosario y los trucos proporcionados deberían ayudarte a tener una referencia rápida mientras estudias o resuelves problemas competitivos en C++. ¡Buena suerte!