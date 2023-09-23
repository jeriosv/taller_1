distancia : float 

distancia = float(input("Ingrese el valor de una distancia [en metros] : "))

velocidadLuz : float = 299792.458      # Velocidad de la Luz [m/s]
velocidadSonido : float = 343.2       # Velocidad del sonido (en el aire) [m/s]
velocidadComercial : float = 141.263889  # Velocidad del vehículo comercial más veloz [m/s]. SSC Tuatara, velocidad máxima reconocida oficialmente de 508,55 km/h
velocidadBolt : float = 10.4384133612 # Velocidad alcanzada por Usain Bolt en los 100 metros en 9,58s [m/s]

print( "El tiempo que le tomaría a la luz recorrer la distancia: ", distancia/velocidadLuz, " s")
print( "El tiempo que le tomaría al sonido en el aire recorrer la distancia: ", distancia/velocidadSonido, " s")
print( "El tiempo que le tomaría al vehículo comercial más veloz en recorrer la distancia: ", distancia/velocidadComercial, " s")
print( "El tiempo que le tomaría a Usain Bolt recorrer la distancia: ", distancia/velocidadBolt, " s")
