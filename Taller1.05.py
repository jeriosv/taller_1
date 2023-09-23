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
