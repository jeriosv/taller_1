import math

# Pedir 5 números reales
numeros = []
for i in range(5):
    numero = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

# Calcular el promedio
promedio = sum(numeros) / len(numeros)

# Calcular la mediana
numeros_ordenados = sorted(numeros)
if len(numeros) % 2 == 0:
    mediana = (numeros_ordenados[len(numeros) // 2 - 1] + numeros_ordenados[len(numeros) // 2]) / 2
else:
    mediana = numeros_ordenados[len(numeros) // 2]

# Calcular el promedio multiplicativo
producto = 1
for numero in numeros:
    producto *= numero
promedio_multiplicativo = math.pow(producto, 1 / len(numeros))

# Ordenar los números de forma ascendente y descendente
ascendente = sorted(numeros)
descendente = sorted(numeros, reverse=True)

# Calcular la potencia del mayor número elevado al menor número
mayor = max(numeros)
menor = min(numeros)
potencia = math.pow(mayor, menor)

# Calcular la raíz cúbica del menor número
raiz_cubica = math.pow(menor, 1/3)

# Mostrar resultados
print(f"Promedio: {promedio}")
print(f"Mediana: {mediana}")
print(f"Promedio Multiplicativo: {promedio_multiplicativo}")
print(f"Números Ordenados Ascendentemente: {ascendente}")
print(f"Números Ordenados Descendentemente: {descendente}")
print(f"Potencia del Mayor al Menor: {potencia}")
print(f"Raíz Cúbica del Menor: {raiz_cubica}")
