# Taller 1

1. Realice el quiz Python Beginner Quiz (20 preguntas) y adjunte pantallazo con el resultado (mínimo 90% bien).


2. Realice un programa que lea tres números reales y determine cuál es el mayor.


```python

numero1 : float 
numero2 : float
numero3 : float

numero1 = float(input("Ingrese el primer número real : "))
numero2 = float(input("Ingrese el segundo número real: "))
numero3 = float(input("Ingrese el tercer número real : "))

if (numero1>numero2) and (numero1>numero3):
   print( " El primer número es el mayor de todos: ", (numero1))
elif (numero2>numero1) and (numero2>numero3):
   print( " El segundo número es el mayor de todos: ", (numero2))
elif (numero3>numero1) and (numero3>numero2):
   print( " El tercer número es el mayor de todos: ", (numero3))

```


3. Realice un programa que lea un número enteros y determine si es par o impar.


```python

numero : float 

numero = float(input("Ingrese un número entero : "))

if (numero % 2) == 0:
   print( "El número es par.")
else:
   print( "El número es impar.")

```


4. Realice un programa que lea dos números reales y determine si el primero es múltiplo del segundo.

```python

numero1 : float 
numero2 : float 

numero1 = float(input("Ingrese el primer número real: "))
numero2 = float(input("Ingrese el segundo número real: "))

if (numero2 % numero1) == 0:
   print( "El primer número sí es múltiplo del segundo número.")
else:
   print( "El primer número no es múltiplo del segundo número.")

```


5. Realice un programa que lea tres números reales y determine si la suma de los dos primeros es mayor, menor o igual que el tercer número.

```python

numero1 : float 
numero2 : float
numero3 : float

numero1 = float(input("Ingrese el primer número real : "))
numero2 = float(input("Ingrese el segundo número real: "))
numero3 = float(input("Ingrese el tercer número real : "))

if (numero1+numero2) == numero3:
   print( " La suma de los dos primeros números es igual al tercer número.")
   print((numero1), " + ", (numero2), " = ", (numero3))
elif (numero1+numero2) > numero3:
   print( " La suma de los dos primeros números es mayor al tercer número.")
   print((numero1), " + ", (numero2), " > ", (numero3))
elif (numero1+numero2) < numero3:
   print( " La suma de los dos primeros números es menor al tercer número.")
   print((numero1), " + ", (numero2), " < ", (numero3))

```


6. Escriba un programa que solicite al usuario una letra y determine si es una vocal o una consonante.

```python

   ```


7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones:

    -El promedio
    -La mediana
    -El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
    -Ordenar los números de forma ascendente
    -Ordenar los números de forma descendente
    -La potencia del mayor número elevado al menor número
    -La raíz cúbica del menor número

```python

   ```


8. Escriba un programa al que se le ingrese la frecuencia de una onda en hz y como salida arroje en que parte del espectro electromagnético se encuentra.

```python

   ```


9. Escriba un programa que reciba el nombre en minúsculas de un país de America y retorne la ciudad capital, si el país no pertenece al continente debe arrojar país no identificado.

```python

   ```


10. Escriba un programa que dada una distancia calcule:

    -El tiempo que le tomaría a la luz recorrer la distancia.
    -El tiempo que le tomaría al sonido (en el aire) recorrer la distancia.
    -El tiempo que le tomaría al vehiculo comercial más veloz recorrer la distancia.
    -El tiempo que le tomaría a Bolt recorrer la distancia.


```python

   ```


