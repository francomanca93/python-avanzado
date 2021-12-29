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
  - [Programando closures](#programando-closures)
  - [Decoradores](#decoradores)
  - [Programando decoradores](#programando-decoradores)
- [Estructuras de datos avanzadas](#estructuras-de-datos-avanzadas)
  - [Iteradores](#iteradores)
  - [La sucesión de Fibonacci](#la-sucesión-de-fibonacci)
  - [Generadores](#generadores)
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

## Closures

## Programando closures

## Decoradores

## Programando decoradores

# Estructuras de datos avanzadas

## Iteradores

## La sucesión de Fibonacci

## Generadores

## Mejorando nuestra sucesión de Fibonacci

## Sets

## Operaciones con sets

## Eliminando los repetidos de una lista

# Bonus

Manejo de fechas
Time zones

# Conclusión

