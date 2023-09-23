a : str
b : int

a = input("Ingrese un caracter: ")
b = ord(a)

if (b >= 65 and b <= 90) or (b >= 97 and b <= 122):
   if (b==65 or b==69 or b==73 or b==79 or b==85 or b==97 or b==101 or b==105 or b==111 or b==117):
      print("El caracter ", (a), " es una vocal.")
   else:
      print("El caracter ", (a), " es una consonante.")
else: 
   print("El caracter ", (a), " no es una vocal, ni una consonante.")
