# POO: Conceptos Clave

## Índice
1. [Objetos Hasheables en Python](#objetos-hasheables-en-python)
2. [Objetos Mutables e Inmutables en Python](#objetos-mutables-e-inmutables-en-python)
3. [Keywords en Python](#keywords-en-python)
4. [*args y **kwargs en Python](#args-y-kwargs-en-python)
5. [Decoradores en Python](#decoradores-en-python)
6. [Iteradores en Python](#iteradores-en-python)

## Objetos Hasheables en Python

En Python, un **objeto hasheable** es aquel que puede ser utilizado como clave en un diccionario o como elemento en un conjunto. Para que un objeto sea hasheable, debe cumplir con dos condiciones principales:

1. **Implementar el método `__hash__()`:**  
   Este método debe devolver un valor entero que represente el hash del objeto. Este valor se utiliza internamente en estructuras como diccionarios y conjuntos para organizar y acceder a los elementos de manera eficiente.

2. **Implementar el método `__eq__()`:**  
   Este método se utiliza para comparar si dos objetos son iguales. Si dos objetos son iguales (`a == b`), deben tener el mismo valor de hash (`hash(a) == hash(b)`).

---

### **Características de un Objeto Hasheable**
- **Inmutabilidad:**  
  El valor de hash no debe cambiar durante la vida del objeto. Por esta razón, los objetos mutables (como listas o diccionarios) no son hasheables, mientras que los objetos inmutables (como tuplas, cadenas o números) sí lo son.
  
- **Consistencia:**  
  Si dos objetos son iguales según `__eq__()`, deben tener el mismo hash. Esto garantiza que los objetos puedan ser comparados y almacenados correctamente en estructuras de datos basadas en hash.

---

### **Ejemplos de Objetos Hasheables**
- **Enteros:**  
  ```python
  hash(42)  # Devuelve un valor de hash
- **Cadenas:**  
  ```python
  hash("hola")  # Devuelve un valor de hash
- **Tuplas Inmutables:**  
  ```python
  hash((1, 2, 3))  # Devuelve un valor de hash

### **Ejemplos de Objetos No Hasheables**
- **Enteros:**  
  ```python
  hash([1, 2, 3])  # Genera un TypeError
- **Cadenas:**  
  ```python
  hash({"a": 1})  # Genera un TypeError

---

### **Cómo Hacer un Objeto Personalizado Hasheable**

  Para que un objeto personalizado sea hasheable, debes implementar los métodos `__hash__()` y `__eq__()`. Aquí tienes un ejemplo: 
  ```python
  class Persona:
      def __init__(self, nombre, edad):
          self.nombre = nombre
          self.edad = edad

      def __hash__(self):
          return hash((self.nombre, self.edad))  # Hash basado en nombre y edad

      def __eq__(self, otro):
          return self.nombre == otro.nombre and self.edad == otro.edad

  # Uso
  p1 = Persona("Juan", 30)
  p2 = Persona("Juan", 30)

  print(hash(p1))  # Devuelve un valor de hash
  print(p1 == p2)  # True, porque son iguales según __eq__

  ```
  En este ejemplo, la clase Persona es hasheable porque implementa `__hash__()` y `__eq__()`, y sus atributos (nombre y edad) son inmutables.

### **Nota Importante**

  Si un objeto es mutable y cambia su estado, su hash también podría cambiar, lo que rompería la consistencia en estructuras como diccionarios o conjuntos. Por eso, es importante garantizar que los objetos hasheables sean inmutables o que su hash no dependa de atributos mutables 


## Objetos Mutables e Inmutables en Python

En Python, los objetos se clasifican en **mutables** e **inmutables** según si su estado (es decir, su valor o contenido) puede cambiar después de su creación. Esta distinción es fundamental para entender cómo funcionan las estructuras de datos, la asignación de variables y el manejo de la memoria en Python.

---

### **Objetos Inmutables**
Un objeto **inmutable** es aquel cuyo estado no puede modificarse después de su creación. Si intentas "modificar" un objeto inmutable, en realidad se crea un nuevo objeto con el nuevo valor.

#### **Ejemplos de Objetos Inmutables:**
- **Enteros:** `42`
- **Flotantes:** `3.14`
- **Cadenas:** `"hola"`
- **Tuplas:** `(1, 2, 3)`
- **Frozensets:** `frozenset({1, 2, 3})`

#### **Características:**
1. **Seguridad en hilos:** Al no poder cambiar su estado, son seguros para usar en programación concurrente.
2. **Claves en diccionarios:** Solo los objetos inmutables pueden ser claves en diccionarios o elementos en conjuntos.
3. **Eficiencia:** Al ser inmutables, Python puede optimizar su almacenamiento en memoria.

#### **Ejemplo:**
```python
a = "hola"
b = a  # 'b' apunta al mismo objeto que 'a'
a = a + " mundo"  # Se crea un nuevo objeto para 'a'

print(a)  # "hola mundo"
print(b)  # "hola" (no cambia)
```
### **Objetos Inmutables**
Un objeto **inmutable** es aquel cuyo estado no puede modificarse después de su creación. Si intentas "modificar" un objeto inmutable, en realidad se crea un nuevo objeto con el nuevo valor.

#### **Ejemplos de Objetos Inmutables:**
- **Enteros:** `42`
- **Flotantes:** `3.14`
- **Cadenas:** `"hola"`
- **Tuplas:** `(1, 2, 3)`
- **Frozensets:** `frozenset({1, 2, 3})`

#### **Características:**
1. **Flexibilidad:** Permiten modificar su contenido sin necesidad de crear nuevos objetos.
2. **Uso en estructuras dinámicas:** Ideales para estructuras de datos que cambian frecuentemente, como listas o diccionarios.
3. **Cuidado con las referencias:** Al modificar un objeto mutable, todas las referencias a ese objeto verán los cambios.
#### **Ejemplo:**
```python
lista1 = [1, 2, 3]
lista2 = lista1  # 'lista2' apunta al mismo objeto que 'lista1'
lista1.append(4)  # Modifica el objeto original

print(lista1)  # [1, 2, 3, 4]
print(lista2)  # [1, 2, 3, 4] (ambas listas reflejan el cambio)
```
### **¿Cuándo Usar Objetos Mutables o Inmutables?**
#### **Usar Objetos Inmutables Cuando:**
- Necesitas garantizar que el valor no cambie (por ejemplo, claves en diccionarios).
- Trabajas en entornos concurrentes o multihilo.
- Quieres evitar efectos secundarios no deseados al pasar datos entre funciones.
#### **Usar Objetos Mutables Cuando:**
- Necesitas modificar el contenido de un objeto frecuentemente.
- Trabajas con estructuras de datos dinámicas, como listas o diccionarios.
- Quieres evitar la sobrecarga de crear nuevos objetos constantemente.

## Keywords en Python

En Python, las **keywords** (o palabras clave) son términos reservados que tienen un significado especial en el lenguaje. Estas palabras no pueden ser utilizadas como identificadores (nombres de variables, funciones, clases, etc.), ya que están destinadas a fines específicos dentro de la sintaxis del lenguaje.

---

### **Lista de Keywords en Python**
A continuación se muestra la lista completa de keywords en Python (hasta Python 3.11):

| Keyword      | Descripción                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `and`        | Operador lógico "Y".                                                        |
| `as`         | Utilizado para crear alias en importaciones o con `with`.                   |
| `assert`     | Verifica que una condición es verdadera; de lo contrario, lanza un error.   |
| `async`      | Define una función o bloque asíncrono.                                      |
| `await`      | Espera a que una corrutina (función asíncrona) termine.                     |
| `break`      | Sale de un bucle (`for` o `while`).                                         |
| `class`      | Define una clase.                                                          |
| `continue`   | Salta a la siguiente iteración de un bucle.                                 |
| `def`        | Define una función.                                                        |
| `del`        | Elimina una variable o un elemento de una lista/diccionario.               |
| `elif`       | Condicional "else if".                                                     |
| `else`       | Bloque que se ejecuta si una condición no se cumple.                       |
| `except`     | Captura excepciones en bloques `try`.                                       |
| `False`      | Valor booleano "falso".                                                    |
| `finally`    | Bloque que siempre se ejecuta, independientemente de excepciones.          |
| `for`        | Bucle que itera sobre una secuencia.                                       |
| `from`       | Importa partes específicas de un módulo.                                   |
| `global`     | Declara una variable global dentro de una función.                         |
| `if`         | Condicional que ejecuta un bloque si se cumple una condición.              |
| `import`     | Importa un módulo o librería.                                              |
| `in`         | Verifica si un valor está presente en una secuencia.                       |
| `is`         | Compara si dos objetos son el mismo (misma identidad).                     |
| `lambda`     | Define una función anónima (sin nombre).                                   |
| `None`       | Representa la ausencia de valor.                                           |
| `nonlocal`   | Declara una variable no local en una función anidada.                      |
| `not`        | Operador lógico "NO".                                                      |
| `or`         | Operador lógico "O".                                                       |
| `pass`       | Instrucción nula (no hace nada).                                           |
| `raise`      | Lanza una excepción manualmente.                                           |
| `return`     | Devuelve un valor desde una función.                                       |
| `True`       | Valor booleano "verdadero".                                                |
| `try`        | Bloque que captura excepciones.                                            |
| `while`      | Bucle que se ejecuta mientras una condición sea verdadera.                 |
| `with`       | Simplifica el manejo de recursos (como archivos).                          |
| `yield`      | Devuelve un valor desde una función generadora.                            |

---

### **Uso de Keywords**
Las keywords se utilizan para definir la estructura y el flujo de un programa en Python. Aquí hay algunos ejemplos comunes:

#### **1. Condicionales (`if`, `elif`, `else`):**
```python
if edad >= 18:
    print("Eres mayor de edad.")
elif edad > 0:
    print("Eres menor de edad.")
else:
    print("Edad no válida.")
```   
#### **2. Bucles (`for`, `while`):**
```python
for i in range(5):
    print(i)  # Imprime números del 0 al 4

contador = 0
while contador < 5:
    print(contador)
    contador += 1
```
#### **3. Funciones (`def`, `return`):**
```python
def suma(a, b):
    return a + b

resultado = suma(3, 5)  # Devuelve 8
```
#### **4. Manejo de excepciones (`try`, `except`, `finally`):**
```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero.")
finally:
    print("Este bloque siempre se ejecuta.")
```
#### **2. Contextos ( `whit`):**
```python
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
```
### **Consejos sobre Keywords**


#### **1. No uses keywords como nombres de variables:**
Si intentas usar una keyword como nombre de variable, obtendrás un error de sintaxis. Por ejemplo:
```python
if = 10  # Error: 'if' es una keyword.
```   

## *args y **kwargs en Python

En Python, `*args` y `**kwargs` son convenciones utilizadas para manejar un número variable de argumentos en funciones. Estas herramientas son especialmente útiles cuando no sabes de antemano cuántos argumentos se pasarán a una función o cuando quieres que tu función sea flexible y reutilizable.

---

### **¿Qué es `*args`?**
`*args` permite pasar un número variable de argumentos **posicionales** a una función. Los argumentos se reciben como una tupla.

#### **Sintaxis:**
```python
def funcion(*args):
    # args es una tupla que contiene todos los argumentos posicionales
    pass
```
#### **Ejemplo:**
```python
def suma(*args):
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado

print(suma(1, 2, 3))  # Devuelve 6
print(suma(4, 5, 6, 7))  # Devuelve 22
```
#### **Características:**
- `*args` recoge todos los argumentos posicionales en una tupla.
- Puedes usar cualquier nombre después del `*`, pero `args` es la convención.
- Útil cuando no sabes cuántos argumentos se pasarán.

### **¿Qué es `**kwargs`?**
`**kwargs` permite pasar un número variable de argumentos con nombre (o keyword arguments) a una función. Los argumentos se reciben como un diccionario.

#### **Sintaxis:**
```python
def funcion(**kwargs):
    # kwargs es un diccionario que contiene todos los argumentos con nombre
    pass
```
#### **Ejemplo:**
```python
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Juan", edad=30, ciudad="Madrid")
# Salida:
# nombre: Juan
# edad: 30
# ciudad: Madrid
```
#### **Características:**
- `*kwargs` recoge todos los argumentos con nombre en un diccionario.
- Puedes usar cualquier nombre después del `**`, pero `kwargs` es la convención.
- Útil cuando quieres manejar argumentos opcionales o configurables.

### **Combinando `*args` y `**kwargs`**
Puedes combinar `*args` y `**kwargs` en una misma función para manejar tanto argumentos posicionales como con nombre.
#### **Ejemplo:**
```python
def funcion_combinada(*args, **kwargs):
    print("Argumentos posicionales:", args)
    print("Argumentos con nombre:", kwargs)

funcion_combinada(1, 2, 3, nombre="Juan", edad=30)
# Salida:
# Argumentos posicionales: (1, 2, 3)
# Argumentos con nombre: {'nombre': 'Juan', 'edad': 30}
```
#### **Reglas:**
- `*args` debe ir antes que `**kwargs` en la definición de la función.
- Los argumentos posicionales se asignan a `*args`.
- Los argumentos con nombre se asignan a `**kwargs`.
#### **Casos de Uso Comunes:**
1. **Funciones flexibles:** Crear funciones que acepten cualquier número de argumentos, como la función `print()`.
2. **Decoradores:** En la creación de decoradores, `*args` y `**kwargs` permiten manejar cualquier función decorada, independientemente de sus argumentos.
3. **Herencia y polimorfismo:** En clases, puedes usar `*args` y `**kwargs` para pasar argumentos a métodos de la clase base.
#### **Ejemplo con Herencia:**
```python
class Animal:
    def __init__(self, nombre, **kwargs):
        self.nombre = nombre
        for clave, valor in kwargs.items():
            setattr(self, clave, valor)

class Perro(Animal):
    def __init__(self, raza, **kwargs):
        super().__init__(**kwargs)
        self.raza = raza

mi_perro = Perro(nombre="Rex", raza="Labrador", edad=5)
print(mi_perro.nombre)  # Rex
print(mi_perro.raza)    # Labrador
print(mi_perro.edad)    # 5
```

---

## Decoradores en Python

Los **decoradores** en Python son una herramienta poderosa que permite modificar o extender el comportamiento de una función o método sin cambiar su código original. Son ampliamente utilizados para añadir funcionalidades como logging, validación, caching, y más, de manera limpia y reusable.

---

### **¿Qué es un Decorador?**
Un decorador es una función que toma otra función como argumento, le añade alguna funcionalidad y devuelve una nueva función. En esencia, "decora" la función original.

---

### **Sintaxis Básica**
Para aplicar un decorador, se usa el símbolo `@` seguido del nombre del decorador, justo antes de la definición de la función que se desea decorar.

```python
@decorador
def funcion():
    pass
```
Esto es equivalente a:
```python
def funcion():
    pass
funcion = decorador(funcion)
```
### **Crear un Decorador**
Un decorador es simplemente una función que recibe una función como argumento y devuelve otra función.
#### **Ejemplo Básico:**
```python
def mi_decorador(func):
    def wrapper():
        print("Algo sucede antes de llamar a la función.")
        func()
        print("Algo sucede después de llamar a la función.")
    return wrapper

@mi_decorador
def decir_hola():
    print("¡Hola!")

decir_hola()
# Salida:
# Algo sucede antes de llamar a la función.
# ¡Hola!
# Algo sucede después de llamar a la función.
```
### **Decoradores con Argumentos**
Si la función decorada recibe argumentos, el decorador debe manejar estos argumentos en su función interna `(wrapper)`.
#### **Ejemplo:**
```python
def decorador_con_argumentos(func):
    def wrapper(*args, **kwargs):
        print("Antes de llamar a la función.")
        resultado = func(*args, **kwargs)
        print("Después de llamar a la función.")
        return resultado
    return wrapper

@decorador_con_argumentos
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Juan")
# Salida:
# Antes de llamar a la función.
# Hola, Juan!
# Después de llamar a la función.
```
### **Decoradores Anidados**
Puedes aplicar múltiples decoradores a una función. El orden en que se aplican es de abajo hacia arriba.
#### **Ejemplo:**
```python
def decorador_uno(func):
    def wrapper():
        print("Decorador Uno: Antes")
        func()
        print("Decorador Uno: Después")
    return wrapper

def decorador_dos(func):
    def wrapper():
        print("Decorador Dos: Antes")
        func()
        print("Decorador Dos: Después")
    return wrapper

@decorador_uno
@decorador_dos
def decir_hola():
    print("¡Hola!")

decir_hola()
# Salida:
# Decorador Uno: Antes
# Decorador Dos: Antes
# ¡Hola!
# Decorador Dos: Después
# Decorador Uno: Después
```
### **Decoradores con Parámetros**
Los decoradores también pueden recibir parámetros. Para esto, necesitas crear una función que devuelva un decorador.
#### **Ejemplo:**
```python
def decorador_con_parametros(mensaje):
    def decorador(func):
        def wrapper(*args, **kwargs):
            print(mensaje)
            return func(*args, **kwargs)
        return wrapper
    return decorador

@decorador_con_parametros("Este es un mensaje personalizado.")
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Ana")
# Salida:
# Este es un mensaje personalizado.
# Hola, Ana!
```
### **Decoradores Built-in en Python**
Python incluye algunos decoradores incorporados que son muy útiles:

1. `@staticmethod`:

    Define un método estático que no recibe una referencia implícita (`self` o `cls`).
    ```python
    class MiClase:
        @staticmethod
        def metodo_estatico():
            print("Este es un método estático.")
    ```
2. `@classmethod`:

    Define un método de clase que recibe la clase (`cls`) como primer argumento.
    ```python
    class MiClase:
        @classmethod
        def metodo_de_clase(cls):
            print(f"Este es un método de clase de {cls.__name__}.")
    ```

3. `@property`:

    Define un método como una propiedad, permitiendo acceso controlado a atributos.
    ```python
    class MiClase:
        def __init__(self, valor):
            self._valor = valor

        @property
        def valor(self):
            return self._valor

        @valor.setter
        def valor(self, nuevo_valor):
            self._valor = nuevo_valor
    ```

## Iteradores en Python

En Python, un **iterador** es un objeto que permite recorrer (iterar) una colección de elementos, como una lista, tupla, diccionario o cualquier objeto iterable. Los iteradores son la base de los bucles `for` y otras estructuras que requieren recorrer elementos.

---

### **¿Qué es un Iterador?**
Un iterador es un objeto que implementa dos métodos:
1. **`__iter__()`:** Devuelve el propio objeto iterador.
2. **`__next__()`:** Devuelve el siguiente elemento de la secuencia. Si no hay más elementos, lanza la excepción `StopIteration`.

---

### **Crear un Iterador**
Para crear un iterador, debes definir una clase que implemente los métodos `__iter__()` y `__next__()`.

#### **Ejemplo Básico:**
```python
class MiIterador:
    def __init__(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin

    def __iter__(self):
        return self

    def __next__(self):
        if self.inicio < self.fin:
            valor = self.inicio
            self.inicio += 1
            return valor
        else:
            raise StopIteration

# Uso del iterador
mi_iterador = MiIterador(1, 5)
for numero in mi_iterador:
    print(numero)
# Salida:
# 1
# 2
# 3
# 4
```
### **Iteradores vs Iterables**
- **Iterable:** Es un objeto que puede devolver un iterador. Ejemplos: listas, tuplas, cadenas, diccionarios.

- **Iterador:** Es el objeto que realiza la iteración sobre el iterable.

#### **Ejemplo Básico:**
```python
# Un iterable (lista)
mi_lista = [1, 2, 3]

# Obtener un iterador
mi_iterador = iter(mi_lista)

# Recorrer el iterador
print(next(mi_iterador))  # 1
print(next(mi_iterador))  # 2
print(next(mi_iterador))  # 3
# print(next(mi_iterador))  # Lanza StopIteration
```
### **Iteradores Infinitos**
Un iterador puede ser infinito si no se define un límite en el método `__next__()`.
```python
class IteradorInfinito:
    def __init__(self):
        self.numero = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.numero += 1
        return self.numero

# Uso (¡Cuidado! Este bucle no termina)
# for numero in IteradorInfinito():
#     print(numero)
```