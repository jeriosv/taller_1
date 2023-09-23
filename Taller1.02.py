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
   