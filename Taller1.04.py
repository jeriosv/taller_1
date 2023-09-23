numero1 : float 
numero2 : float 

numero1 = float(input("Ingrese el primer número real: "))
numero2 = float(input("Ingrese el segundo número real: "))

if (numero2 % numero1) == 0:
   print( "El primer número sí es múltiplo del segundo número.")
else:
   print( "El primer número no es múltiplo del segundo número.")
