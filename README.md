# Notas

## Python 3 en ubuntu

Para correr comandos de python asegurandose que son en python 3 con
```python3 -m ```

### Crear entorno virtual

"venv" puede ser cualquier nombre , normalmente es venv

```python3 -m virtualenv venv```

```virtualenv --python=python3 venv```


### Correr entorno virtual 

```source venv/bin/activate```



## Pip install requirements

```pip install -r requirements.txt```

## Variables

```python
a = 2
b = 3
```

### suma

```python
a + b
```

### resta

```python
a - b
```

### division real

```python
a / b
```

### division entera

```python
a // b
```

### modulo

```python
a % b
```

### multiplicacion

```python
a * b
```

### potencia

```python
a ** b
```

### retorna el tipo de valor que posee esa variable

```python
type(a)
```

### concatenar

```python
print('a' + 'b')
```

### concatenar mismo string n veces

```python
print('a ' * 5)
```

### reasignacion y suma

```python
a += b
```

### Scope de las variables

```python
hel = 'HELL' # variable publica
_he = 'I am private' #variable privada
YO = ' constante' #variable constante , no se reasigna 
__que = 'variable' #convencion de que la variables es final no debe ser modificada por ningun motivo
```
### Operadores logicos

igual
```==```

distinto
```!=```

mayor que
```>```

menor que
```<```

mayor igual
```>=```

menor igual
```<=```

AND
```and```

OR
```or```

NOT
```not```

## String

Metodos de los string Algunos son:

- upper
- lower
- find
- startswith
- endswith
- capitalize
- replace('string_in','string_to_replace_with')

```python
luis = 'luis'
luis.upper() #sera igual a LUIS
```

Operadores de pertenencia

- in
- not in

## Operaciones con listas

### index en listas

en ciertas listas si pasa el mismo elemento a la funcion index te retorna el index

```python
n = ['0','2','bana','1','f']
b = n[0]
n.index(b) #0

```

### Suma

```python
a = [1, 2]
b = [2, 3]
a + b # [1, 2, 2, 3]
```

### Multiplicación

```python
a = [1, 2]
a * 2 # [1, 2, 1, 2]
```

### append

```python
a = [1]
a.append(2) # [1, 2]
```

### pop

borra el ultimo elementos de la lista o el indice del elemento y lo retorna

```python
a = [1, 2]
b = a.pop()
print(a) # [1]
print(b) # 2
```

### sort

```python
a = [3, 8, 1]
a.sort() # [1, 3, 8]
```

### del

```python
a = [1, 2, 3]
del a[-1] #borra el ultimo elemento
```

### remove

```python
a = ['hola','adios', 'que tal']
a.remove('adios')
```

### ordendar lista de forma descendente

```python
sorted(list, reverse=True)
list.sort(reverse=True)
```

## Tipos de listas

### arrays

[]

### diccionarios

{'h': 'hello'}

### Tuplas

son listas inmutables ,no pueden ser modificadas

```python
f = ('h','d','d')
```

## Sets o conjuntos

listas que no pueden tener elementos duplicados

```python
normal_set = {} #se puede inicializar así
normal_set = set(["a", "b","c"]) # o con el keyword
normal_set.add('d')
normal_set.remove('a')
```

## Curiosidades

### Dir
  
  ```python
    a = 'hola'
    dir(a) #imprime todos los metodos que posee ese objeto

    d = None #valor nulo de python
  ```

### Id

  ```python
    a = 'hola'
    id(a)#imprime la direccion de memoria de a
  
    d = None #valor nulo de python
  ```

### Interpolar

```python
cadena = "Hi, I am {name} and I am {age} years old"
cadena.format(age=26, name="John")
#Hi, I am John and I am 26 years old
```

### Aplicaciones de linea de comandos

para en un entorno virtual instalar la app
```pip install --editable .```

## Errores

aventar errores en python con el keyword ```raise```

try except else finally

```python
try:
    # trata de ejecutar el codigo
    # se recomienda una unica linea dentro de try
    pass
except expression as identifier: # se especifico del tipo de error que se desea atrapar
    #hubo errore ejecuta este codigo
    pass
else:
    #no hubo errores ejecuta este codgio
    pass
finally:
    # siempre ejecuta este codigo
    pass
```

Links utiles:

[Errores newbies en pythons](https://www.dropbox.com/s/cqsxfws52gulkyx/drawing.pdf)
[python 3 exceptions](http://docs.python.org.ar/tutorial/3/errors.html)
[python 2 exceptions](http://docs.python.org.ar/tutorial/3/errors.html)

### Context Managers

```python
with open(‘some_file.txt’) as f:
    lines = f.readlines()
```

```python
class CustomOpen(object):
    def __init__(self, filename):
        self.file = open(filename)

    def __enter__(self):
        return self.file

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        self.file.close()

with CustomOpen('file') as f:
    contents = f.read()
```

```python
from contextlib import contextmanager

@contextmanager
def custom_open(filename):
    f = open(filename)
    try:
        yield f
    finally:
        f.close()

with custom_open('file') as f:
    contents = f.read()
```

### Iterators and generators

```python
for i in range(10):
    print(i)
```

```python
def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b
```

```python
  fib1 = fibonacci(20)
  fib_nums = [num for num in fib1]
  #...
  double_fib_nums = [num * 2 for num in fib1] # no va a funcionar
  double_fib_nums = [num * 2 for num in fibonacci(30)] # sí funciona
```

## Debes seguir PEPs

- PEP 8: Estilo de escritura de python ( muy importante)
- PEP257 python docstring
- PEP20 import this: el Zen de python

## Zen of python

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
