n1 : float 
n2 : float
n3 : float
n4 : float
n5 : float

n1 = float(input("Ingrese el primer número real : "))
n2 = float(input("Ingrese el segundo número real: "))
n3 = float(input("Ingrese el tercer número real : "))
n4 = float(input("Ingrese el cuarto número real : "))
n5 = float(input("Ingrese el quinto número real : "))

promedio : float = (n1+n2+n3+n4+n5) / 5
mediana : float
promedioMultiplicativo : float = (n1*n2*n3*n4*n5) ** (1/5)


print( " El promedio aritmético de los cinco números es: ", (promedio))
print( " El promedio multiplicativo de los cinco números es: ", (promedioMultiplicativo))

