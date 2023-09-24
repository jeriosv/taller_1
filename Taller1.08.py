frecuencia : float 

frecuencia = float(input("Ingrese la frecuencia de una onda en hertz [Hz]: \n Tip: Para ingresar en notación científica, escribir e (base 10): ejemplo 15.6e14 :  "))

if (30.0e18<frecuencia):
   print("La onda se ubica en Rayos Gamma.")
elif (30.0e15<=frecuencia) and (frecuencia<30.0e18):
   print("La onda se ubica en Rayos X.")
elif (1.5e15<=frecuencia) and (frecuencia<30.0e15):
   print("La onda se ubica en Ultravioleta extremo.")
elif (7.89e14<=frecuencia) and (frecuencia<1.5e15):
   print("La onda se ubica en Ultravioleta cercano.")
elif (384e12<=frecuencia) and (frecuencia<7.89e14):
   print("La onda se ubica en Espectro Visible.")
elif (120e12<=frecuencia) and (frecuencia<384e12):
   print("La onda se ubica en Infrarrojo cercano.")
elif (6.00e12<=frecuencia) and (frecuencia<120e12):
   print("La onda se ubica en Infrarrojo medio.")
elif (300e9<=frecuencia) and (frecuencia<6.00e12):
   print("La onda se ubica en Infrarrojo lejano / submilimétrico.")
elif (3e8<=frecuencia) and (frecuencia<300e9):
   print("La onda se ubica en Microondas.")
elif (300e6<=frecuencia) and (frecuencia<3e8):
   print("La onda se ubica en Ultra Alta Frecuencia - Radio.")
elif (30e6<=frecuencia) and (frecuencia<300e6):
   print("La onda se ubica en Muy Alta Frecuencia - Radio.")
elif (1.7e6<=frecuencia) and (frecuencia<30e6):
   print("La onda se ubica en Onda Corta - Radio.")
elif (650e3<=frecuencia) and (frecuencia<1.7e6):
   print("La onda se ubica en Onda Media - Radio.")
elif (30e3<=frecuencia) and (frecuencia<650e3):
   print("La onda se ubica en Onda Larga - Radio.")
elif (frecuencia<30e3):
   print("La onda se ubica en Muy Baja Frecuencia - Radio.")
elif (frecuencia<0):
   print("Error: El valor de frecuencia ingresada es un número negativo.")
   