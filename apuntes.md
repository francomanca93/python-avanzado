<div align="center">
    <h1>Curso Profesional de Python</h1>
    <img src="https://imgur.com/ZFkZ0uX.png" width="">
</div>

## Tabla de contenidos

- [Introducción](#introducción)
  - [¿Cómo funciona Python?](#cómo-funciona-python)
    - [Lenguajes: Compilados vs Interpretados](#lenguajes-compilados-vs-interpretados)
    - [Garbage collector](#garbage-collector)
    - [Carpeta _ _pycache_ _](#carpeta-_-pycache-_)
  - [Cómo organizar las carpetas de tus proyectos](#cómo-organizar-las-carpetas-de-tus-proyectos)
- [Static Typing](#static-typing)
  - [¿Qué son los tipados?](#qué-son-los-tipados)
    - [Clasificacion](#clasificacion)
    - [Ejemplos de tipado](#ejemplos-de-tipado)
  - [Tipado estático en Python](#tipado-estático-en-python)
    - [Modulo mypy](#modulo-mypy)
  - [Practicando el tipado estático](#practicando-el-tipado-estático)
- [Conceptos avanzados de funciones](#conceptos-avanzados-de-funciones)
  - [Scope: alcance de las variables](#scope-alcance-de-las-variables)
  - [Closures](#closures)
    - [Reglas para encontrar un closure](#reglas-para-encontrar-un-closure)
  - [Programando closures](#programando-closures)
  - [Decoradores](#decoradores)
  - [Programando decoradores](#programando-decoradores)
    - [Entendiendo *args y **kwargs](#entendiendo-args-y-kwargs)
- [Estructuras de datos avanzadas](#estructuras-de-datos-avanzadas)
  - [Iteradores](#iteradores)
    - [Clase con metodos iter y next - Creando un iterador](#clase-con-metodos-iter-y-next---creando-un-iterador)
  - [La sucesión de Fibonacci](#la-sucesión-de-fibonacci)
  - [Generadores](#generadores)
    - [Generator Expression](#generator-expression)
  - [Mejorando nuestra sucesión de Fibonacci](#mejorando-nuestra-sucesión-de-fibonacci)
  - [Sets](#sets)
  - [Operaciones con sets](#operaciones-con-sets)
  - [Eliminando los repetidos de una lista](#eliminando-los-repetidos-de-una-lista)
- [Bonus](#bonus)
- [Conclusión](#conclusión)

# Introducción

## ¿Cómo funciona Python?

### Lenguajes: Compilados vs Interpretados

- Los **lenguajes compilados** convierten el código a binario que es el que lee la computadora.
- Los **lenguajes interpretados** requieren de un programa que lee las instrucciones en tiempo real y las ejecuta, por lo que el programa interpreta el código escrito y lo traduce en lenguaje de máquina en tiempo real. Esto explicaría porque en los notebook escritos en collab o jupyter podemos ejecutar nuestro código de python por partes.

![compilador-vs-interpretado](https://imgur.com/YbfsCWU.png)

### Garbage collector

Es una sección especial de python que se encarga de tomar los objetos y las variables que no están en uso y eliminarlas.

### Carpeta _ _pycache_ _

En la carpeta __ pycache __ tenemos el bytecode que es el código intermedio que crea python al ser un lenguaje interpretado para que pueda ser leido por la máquina virtual. La ventaja es que funciona como una especie de recuperacion del código que ya hemos trabajado, para que la proxima vez que se ejecute el programa sea más rápido, ya que no tiene que convertirse a bytecode de nuevo.

## Cómo organizar las carpetas de tus proyectos

📁 **Módulo: es cualquier archivo de Python**. Generalmente, contiene código que puedes reutilizar.

🗄 **Paquete: es un conjunto de módulos**. Siempre posee el archivo __init__.py.

![paquete-modulo1](https://imgur.com/xfPx20u.png)

![paquete-modlo2](https://imgur.com/C9MiqBG.png)

Un ejemplo de organizar los archivos de 🐍Python es de la siguiente manera:

![ejemplo-organizar](https://imgur.com/MSRRiBm.png)

🐍 __init __.py
Cuando un nuevo objeto es contruido, este es inicializado por la llamada del moetodo init en el objeto. __ init __ es pronunciado **“dunder init”:** dunder es la abreviacion en ingles de **“double-underscore”**.

🌳 **Comando tree**: En una terminal Unix, se puede instalar con `sudo apt-get install tree` para ver un árbol de las carpetas.
Luego puedo ingresar a la carpeta de un proyecto y ejecutar el comando `tree`.

Con `tree -I venv` se puede ignorar la carpeta `venv` que tiene todos los paquetes que se han instalado en el entorno virtual.

> NOTA: Cada proyecto es diferente y a medida que vayas avanzando como ingeniero de software veremos diferentes formas de organizarlas, por ejemplo frameworks como Django, Flask o FastAPI tienen recomendacion de como ordenar las carpetas, entre otros. Pero los conceptos básicos es lo que se nombre aqui.

# Static Typing

## ¿Qué son los tipados?

El tipado del lenguaje depende de cómo trata a los tipos de datos o datos primitivos.

Para saber que son los tipados, tenemos que recordar que son los tipos:

![tipos-primitivos](https://imgur.com/8BgNgmt.png)

Los datos pueden ser **arreglos** (listas de valores), **numeros** (int o float), **strings** (cadenas de char), **booleanos** (true o false). Estos datos son llamada tipos de **datos primitivos**.

### Clasificacion

Entendiendo lo anterior tenemos la siguiente clasificación:

- **Estático o Static**: Son los que levantan los errores de tipo en tiempo de compilación. Esto es, si al estar programando tenemos un error de tipo, entonces el lenguaje nos avisa antes de que se ejecute (mientras compila).

![static](https://imgur.com/jbsa15f.png)

- **Dinámico o Dynamic**: Opuesto al estático, levantan los errores de tipo en el tiempo de ejecución, es decir, el error sale mientras el programa se ejecuta en esa línea donde está el error.

![dynamic](https://imgur.com/ePe21lv.png)

- **Fuerte o strong**: Son los que tratan con mas severidad a los datos de diferentes tipos, por ejemplo, impide combinar un número entero con una cadena de caracteres.
- **Débil o weak**: Los lenguajes de tipado débil tratan con menos severidad a los datos de diferentes tipos por ejemplo cambia (castea) un tipo de dato para poder operar con el, por ejemplo al sumar un número con un carácter nos entregaría una cadena que concatena ambos valores.

### Ejemplos de tipado

![ejemplos-tipado](https://imgur.com/hRcIpMS.png)

- **Strong & Dynamic** 💪💫 : Python, Ruby, Erlang

```python
# python
str = "Hello"
str = 5 # No hay problema :)
```

- **Strong & Static** 💪🗻: Java, C#, Scala

```java
// java
String str = "hello";
str = 5; // Error
```

- **Weak & Dynamic** 😫💫 : JavaScript, PHP, Perl

```js
// javascript
const x = 1
const y = "2"
const z = x + y // "12" - JS es raro 😅
```

```php
<?php
$str = 5 + "5"; //10 - PHP es raro 😅 (hace lo contrario a JS)
?>
```

- **Weak & Static** 😫🗻 : C, C++
Discucion en stackoverflow sobre este tipo de lenguajes: [Is there a statically weak typed language?](https://stackoverflow.com/questions/14046246/is-there-a-statically-weak-typed-language)

> Nota: **El tipado dinámico es peligroso**.

## Tipado estático en Python

Para hacer que Python sea de tipado estático es necesario agregar algo de sintaxis adicional a lo aprendido, además, esta característica **solo se puede aplicar a partir de la versión 3.6**.

```py
# De esta manera se declara una variable, se colocan los dos puntos (:), el tipo de dato y para finalizar se usa el signo igual para asignar el valor a la variable.

<variable> : <tipo_de_dato> = <valor_asignado>

a: int = 5
print(a)

b: str = "Hola"
print(b)

c: bool = True
print(c)
```

Del mismo modo se puede usar esta metodología de tipado en Python a funciones adicionando el signo menos a continuación del signo mayor que para determinar el tipo de dato. Ejemplo:

```py
def <nombre_func> ( <parametro1> : <tipo_de_dato>, <parametro2> : <tipo_de_dato> ) ->  <tipo_de_dato> :
	pass

# ejemplo:
def suma(a: int, b: int) -> int :
	return a + b

print(suma(1,2))

# 3
```

Existe una librería de fabrica que viene preinstalada con Python que se llama `typing`, que es de gran utilidad para trabajar con tipado con estructuras de datos **entre la versión 3.6 y 3.9**, entonces:

```py
from typing import Dict, List

positives: List [int] = [1,2,3,4,5]

users: Dict [str, int] = {
	"argentina": 1.
	"mexico": 34,
	"colombia": 45,
}

countries: List[Dict[str, str]] = [
	{
		"name" : "Argentina",
		"people" : "45000",
	},
	{
		"name" : "México",
		"people" : "9000000",
	},
	{
		"name" : "Colombia",
		"people" : "99999999999",
	}
]
```

```py
from typing import Tuple, Dict, List

CoordinatesType = List[Dict[str, Tuple[int, int]]]

coordinates: CoordinatesType = [
	{
		"coord1": (1,2),
		"coord2": (3,5)
	},
	{
		"coord1": (0,1),
		"coord2": (2,5)
	}
]
```

### Modulo mypy

El modulo `mypy` se complementa con el modulo typing ya que permitirá mostrar los errores de tipado debil en Python.

## Practicando el tipado estático

Practicando el tipado estático en el archivo [palidrome.py](palindrome.py)


El modulo mypy se complementa con el modulo typing ya que permitirá mostrar los errores de tipado débil en Python. Para revisar si algún archivo contiene errores de tipado ejecutamos en la línea de comandos lo siguiente:

```shell
mypy archivo.py --check-untyped-defs
```

Como resultado nos mostrará si existe algún error de compatibilidad de tipos.

![mypy-check](https://imgur.com/CixlJKB.png)

Una herramienta útil para validar código antes de subirlo a un repositorio git es [pre-commit](https://pre-commit.com/). En el siguiente enlace podemos ver mas acerca de [mypy](https://sinclert.github.io/python-types/) y en este otro enlace podemos ver como [desarrollar código limpio de Python](https://www.seraph.to/python-clean-python-code.html#python-clean-python-code)

Dejo un artículo con varias reglas de pre-commit para python enlace

# Conceptos avanzados de funciones

## Scope: alcance de las variables

El **scope** es el alcance que tienen las variables. Depende de donde declares o inicialices una variable para saber si tienes acceso. **Regla de oro**:

> una variable solo esta disponible dentro de la region donde fue creada

- **Local Scope**: Es la región que corresponde el ámbito de una función, donde podremos tener una o mas variables, las variables van a ser accesibles únicamente en esta region y no serán visibles para otras regiones

```py
# Local Scope

def my_func():
  y = 5 #La variable solo está disponible en esta función
  print(y)

my_func() # 5
```

- **Global Scope**: Al escribir una o mas variables en esta region, estas podrán ser accesibles desde cualquier parte del código.

```py
# Global Scope
y = 5

def my_func():
  print(y)

def my_other_func():
  print(y)

my_func() # 5
my_other_func() # 5
```

Mezclando global y local scopes, donde hay que tener en cuenta que podemos tener dos variables que se llaman igual, pero dado a que una es global y otra es local, son objetos diferentes. En la función, se le da prioridad a la variable más local.

- Ejemplo 1:

```py
# global y local scopes

z = 5 # global

def my_func():
  z = 3 # z local
  print(z)

my_func() # 3 - local

print(z) # 5 - global
```

- Ejemplo 2:

```py
z = 5

def my_func():
  z = 3

  def my_other_func():
    z = 2
    print(z)

  my_other_func() # 2

  print(z) # 3

my_func()

print(z) # 5

# Salida:
# > 2
# > 3
# > 5
```

## Closures

Antes de ver que es un closure tenemos que saber que es una nested function.

- **Nested functions**: Las funciones anidadas son simplemente funciones creadas dentro de otra función.

```py
def main():
	a = 1
	def nested():
		print(a)
	return nested

my_func = main()
my_func()
# 1
```

- Closure: Es hacer return de una función creada dentro de otra función y luego guardar esas funciones en variables que podemos utilizar. Dicho de otra forma es es cuando una variable de un scope superior es recordada por una función de scope inferior (aunque luego se elimine la de scope superior).

```py
def main():
	a = 1
	def nested():
		print(a)
	return nested

my_func = main()
my_func()
# 1
del(main)
my_func()
# 1
```

### Reglas para encontrar un closure

- Debemos tener una nested function.
- La nested function debe referenciar un valor de un scope superior.
- La función que envuelve a la nested function debe retornarla también.

Ejemplo de closures para crear funciones:

```py
def make_multiplier(x):
	def multiplier(n):
		return x*n
	return multiplier

times10 = make_multiplier(10)
times4 = make_multiplier(4)

print(times10(3)) # 30
print(times4(5)) #20
print(times10(times4(2))) # 80
```

Los closure aparecen en dos casos particulares:

- Cuando tenemos una clase corta (con un solo método), los usamos para que sean elegantes.
- Cuando usamos decoradores.

## Programando closures

Practicando el concepto de closures en [closures.py](closures.py)

## Decoradores

Un decorador es una función que recibe como parámetro otra función, le añade cosas y retorna una función diferente. Tienen la misma estructura que los Closures pero en vez de variables lo que se envía es una función. Ejemplo:

```py
def decorador(func):
    def envoltura():
        print("Esto se añade a mi función original.")
        func()
    return envoltura

def saludo():
    print("¡Hola!")

saludo()
# Salida:
# ¡Hola!

saludo = decorador(saludo) # Se guarda la función decorada en la variable saludo
saludo()                   # La función saludo está ahora decorada
# Salida:
# Esto se añade a mi función original.
# ¡Hola!
```

Se puede hacer de manera mas sencilla, con **azúcar sintáctica (sugar syntax)**: Cuando tenemos un código que está embellecido para que nosotros lo veamos de una manera más estética, ayudando a entender de manera mas sencilla el código. De esta manera, tenemos el código anterior:

Sin usar **sugar sintax**:

```py
def decorador(func):
    def envoltura():
        print("Esto se añade a mi función original.")
        func()
    return envoltura

def saludo():
    print("¡Hola!")
saludo = decorador(saludo) # Se guarda la función decorada en la variable saludo (se decora)

saludo() # La función saludo está ahora decorada
```

Usando **sugar sintax**:

```py
def decorador(func):
    def envoltura():
        print("Esto se añade a mi función original.")
        func()
    return envoltura

# De esta manera se decora la función saludo (equivale a saludo = decorador(saludo) de la última línea, quedando ahora en la línea inmediata superior ):
@decorador
def saludo():
    print("¡Hola!")

saludo()                   # La función saludo está ahora decorada 
```

Esto permite ahorrar código al implementar características (decoradores) comunes a diferentes funciones:

```py
def decorator_upper(func):                  # Función decoradora
    def wrapper(text):                      # Función anidada
        return func(text).upper()           # Operación que realiza el decorado a la función (func), inserta el texto a la función original. Convierte todo a mayúsculas.
    return wrapper                          # Devuelve wapper como indica la regla de los Clousures

@decorator_upper                            # Decora la función message
def message(name):
    return f'{name}, recibiste un mensaje'  # Esto es lo que realiza la función message, previo a ser decorada.

@decorator_upper                            # Decora la función warning
def warning(name):
    return f'Usa solo mayúsculas {name}'  # Esto es lo que realiza la función warning, previo a ser decorada.

print(message("Cesar")) # Output: CESAR, RECIBISTE UN MENSAJE
print(warning("Cesar")) # Output: USA SOLO MAYÚSCULAS CESAR
```

## Programando decoradores

En el siguiente ejercicio creamos un decorador para saber cuando tarda una funcion en ejecutarse, [decorators.py](decorators.py) y en ello vimos ***args** y ****kwargs**

### Entendiendo *args y **kwargs

Cuando tengas que pasar argumentos a una función y no sepas cuantos, usa *args luego recorre la variable args para usarlos. **Son argumentos posicionales.**

```py
def sum(*args):
    value = 0
    for n in args:
        value += n
    return value
```

El parámetro *args recibe los argumentos como una **tupla**.

Si no sabes cuantos argumentos vas a necesitar y quieres darles nombre a esas variables usarás **kwargs. **Son argumentos con nombre.**

```py
def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))


name_1="Alex",
name_2="Gray",
name_3="Harper",
name_4="Phoenix",
name_5="Remy",
name_6="Val"
```

El parámetro **kwargs recibe los argumentos como un **diccionario**.

# Estructuras de datos avanzadas

## Iteradores

Un iterator es una estructura de datos para guardar datos infinitos pero antes de entender qué son los **iteradores**, primero debemos entender a los **iterables**.

Los **iterables** son aquellas estructuras de datos divisibles en elementos únicos que se pueden recorrer en un ciclo, por ejemplo: listas, strings, etc.

Todos los iterables pueden convertirse en **iteradores** para poder ser recorridos en un ciclo.

Ejemplo:

```py
# Creando un iterador

my_list = [1,2,3,4,5]
my_iter = iter(my_list)

# Iterando un iterador

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# Cuando no quedan datos, genera un error donde la excepción StopIteration es elevada.

# Salida

# > 1
# > 2
# > 3
# > 4
# > 5
# > Traceback (most recent call last):
# >   File "UBICATION_FILE/iterators.py", line 13, in <module>
# >     print(next(my_iter))
# > StopIteration
```

Para solucionar lo anterior iteramos un iterador en un ciclo while:

```py
# Creando un iterador

my_list = [1,2,3,4,5]
my_iter = iter(my_list)

# Iterando un iterador

while True: # ciclo infinito
  try:
    element = next(my_iter)
    print(element)
  except StopIteration: # Salimos del ciclo cuando aparece la exception StopIteration
    break

# Salida

# > 1
# > 2
# > 3
# > 4
# > 5
```

> **Momento impactante**: El ciclo “for” dentro de Python, no existe. Es un while con StopIteration, o sea el ciclo anterior. 🤯🤯🤯
> El ciclo for es un **sugar sintax** del ciclo while True con las condiciones necesarias para que se comporte como el for que conocemos.

```py
my_list = [1,2,3,4,5]

for element in my_list:
  print(element)

# Salida

# > 1
# > 2
# > 3
# > 4
# > 5

```

### Clase con metodos iter y next - Creando un iterador

```py
class EvenNumbers:
  """Clase que implementa un iterador de todos los números pares,
  o los números pares hasta un máximo
  """

  #* Constructor de la clase
  def __init__(self, max = None): #self hace referencia al objeto futuro que voy a crear con esta clase
    self.max = max


  # "El método __iter__() devuelve el objeto iterador en sí. Si es necesario, se puede realizar alguna inicialización."
  def __iter__(self):
    self.num = 0 #Primer número par
    #* Convertir un iterable en un iterador
    return self

  # "El  método __next__() debe devolver el siguiente elemento de la secuencia.Al llegar al final, y  debe subir el error StopIteration."
  def __next__(self):
    if not self.max or self.num <= self.max:
      result = self.num
      self.num += 2
      return result
    else:
      raise StopIteration
```

Un iterador es una expresión que explica con obtener el resultado de un iterable, esto nos trae algunas ventajas:

- Nos ahorra recursos.
- Ocupan poca memoria.

## La sucesión de Fibonacci

En el siguiente archivo [iterators.py](iterators.py) se guarda la [sucesión de fibonacci](https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci) en un **iterador**. La sucesión es infinita y los recursos computacionales que tenemos son finitos (ram: 8GB, 16GB, 32GB...), por lo tanto no podemos guarda a esta sucesion en un iterable, como una lista. Por lo tanto creamos un iterador.

El iterador es una clase que con tiene el metodo **iter** (creación del iterador) y el método **next** (metodo acceder a cada uno de los valores) y en el constructor **init** seteamos el numero máximo de valores que queremos extraer del iterador. Para extraerlo necesitamos un bucle, en este caso usamos el for.

```py
import time

class FiboIter():
    def __init__(self, max):
      self.max = max

    def __iter__(self):
      self.n1 = 0
      self.n2 = 1
      self.counter = 0
      return self

    def __next__(self):
      if self.counter < self.max:
        if self.counter == 0:
          self.counter += 1
          return self.n1
        elif self.counter == 1:
          self.counter += 1
          return self.n2
        else:
          self.aux = self.n1 + self.n2
          self.n1, self.n2 = self.n2, self.aux
          self.counter += 1
          return self.aux
      else:
        print('Fin de la iteracion')
        raise StopIteration


if __name__ == '__main__':
    fibonacci = FiboIter(1)
    for element in fibonacci:
        print(element)
        time.sleep(1) # wait a second
```

## Generadores

**Los Generadores son iteradores con Sugar Syntax.**

Ejemplo:

```py
def my_gen():

  """un ejemplo de generadores"""

  print('Hello world!')
  n = 0
  yield n

  print('Hello heaven!')
  n = 1
  yield n

  print('Hello hell!')
  n = 2
  yield n


a = my_gen()
print(next(a)) # Hello world!
print(next(a)) # Hello heaven!
print(next(a)) # Hello hell!
print(next(a)) StopIteration
```

**Yield** es lo mismo que **return**, es una palabra clave que se usa para retornar un valor de una función **pero** sin destruir los estados de las variables locales y cuando se llama a la función, la ejecución comienza desde el último yield declarado. **Toda función que contenga la palabra clave yield es denominada como un generador.**

### Generator Expression

Un “list comprehension” es una manera sencilla de implementar un ciclo el cual nos permite crear una nueva lista con elementos basados en los valores de una lista existente. Dicha lista creada almacena cada uno de estos nuevos valores.

A diferencia de un List comprehension que puede ocupar mucha memoria pues cada valor es almacenado en la variable, un **Generator expression** solo los recorre, sin guardarlos en una lista nueva. Permite traer un elemento a la vez cuando se recorra usando un ciclo for.

```py
# Generator expression

my_list = [0, 1, 4, 7, 9, 10]

my_second_list = [x*2 for x in my_list] # List comprehension
my_second_gen = (x*2 for x in my_list)  # Generator expression
```

Como se puede ver en el ejemplo, la diferencia en la sintaxis únicamente es en **el uso de paréntesis** en lugar del uso de corchetes.

Ventajas de los Generadores:

- Es mas fácil de escribir que un iterador
- Ahorra Tiempo y Memoria
- Permite guardar secuencias infinitas

## Mejorando nuestra sucesión de Fibonacci

En el siguiente código esta la sucesión de fibonacci utilizando generadores, sin un valor maximo como parámetro.

```py
def fibo_gen():
    n1 = 0
    n2 = 1
    counter = 0

    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux


if __name__ == '__main__':
    fibonacci = fibo_gen()
    for element in fibonacci:
        print(element)
        time.sleep(1)
```

En el archivo [generators.py](generators.py) tenemos la versión mejorada del código anterior con ingreso de un parámetro máximo para el generador.

## Sets

Los sets son una estructura de datos muy similares a las listas en cuanto a su forma, pero presentan ciertas características particulares:

- Los sets son **inmutables**.
- Cada elemento del set es único, esto es que no se admiten duplicados, aun si durante la definición del set se agregan elementos repetidos pyhton solo guarda un elemento.
- Los sets guardan los elementos en desorden

Para declararlos se utilizan los **{}** parecido a los diccionarios solo que carece de la composición de conjunto {a:b, c:d}

```py
# set de enteros
my_set = {1, 3, 5}
print(my_set)

# set de diferentes tipos de datos
my_set = {1.0, "Hi", (1, 4, 7)}
print(my_set)
```

Los sets no pueden ser leídos como las listas o recorridos a través de slices, esto debido a que no tienen un criterio de orden. Sin embargo si podemos agregar o eliminar items de los sets utilizando métodos:

- `add()`: nos permite agregar elementos al set, si se intenta agregar un elemento existente simplemente python los ignorara.
- `update()`: nos permite agregar múltiples elementos al set.
- `remove()`: permite eliminar un elemento del set, en el caso en que no se encuentre presente dicho elemento, Python elevará un error.
- `discard()`: permite eliminar un elemento del set, en el caso en que no se encuentre presente dicho elemento, Python dejará el set intacto, sin elevar ningún error.
- `pop()`: permite eliminar un elemento del set, pero lo hará de forma aleatoria.
- `clear()`: Limpia completamente el set, dejándolo vació.

```py
#ejemplo de operaciones sobre sets 
my_set = {1, 2, 3} 
print(my_set) #Output {1, 2, 3} 

#añadiendo un elemento al set 
my_set.add(4) 
print(my_set) #Output {1, 2, 3, 4}

#añadiendo varios elementos al set, python ignorará elementos repetidos 
my_set.update([1, 5, 6]) 
print(my_set) #Output {1, 2, 3, 4, 5, 6}

# eliminado elementos del set 
my_set.discard(1) 
print(my_set) #Output {2, 3, 4, 5, 6}

# borrando un elemento aleatorio 
my_set.pop()
print(my_set) #Output el set menos un elemento aleatorio 

#limpiar el set 
my_set.clear()
print(my_set) # Output set() 
```

Podemos utilizar estructuras de datos existentes para transformarlas a sets utilizando el método set:

```py
#usando listas para crear sets
my_list = [1, 2, 3, 3, 4, 5]
my_set = set(my_list)
print(my_set)  #output {1, 2, 3, 4, 5}

#usando tuplas para crear sets 
my_tuple: ('hola', 'hola', 1, 2)
my_set2: set(my_tuple)
print(my_set2) #Output {'hola', 1}
```

## Operaciones con sets

## Eliminando los repetidos de una lista

# Bonus

Manejo de fechas
Time zones

# Conclusión

