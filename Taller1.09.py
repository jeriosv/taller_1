# Definir un diccionario con los países y sus capitales en América
paises_y_capitales = {
    "argentina": "Buenos Aires",
    "brasil": "Brasilia",
    "canada": "Ottawa",
    "chile": "Santiago",
    "colombia": "Bogota",
    "estados unidos": "Washington d.c.",
    "mexico": "Ciudad de Mexico",
    "peru": "Lima",
    "belice": "Belmopan",
    "guatemala": "Ciudad de Guatemala",
    "el salvador": "San Salvador",
    "honduras": "Tegucigalpa",
    "nicaragua": "Managua",
    "costa rica": "San Jose",
    "panama": "Ciudad de Panamá",
    "cuba": "La Habana",
    "jamaica": "Kingston",
    "haiti": "Puerto Principe",
    "republica dominicana": "Santo Domingo",
    "bahamas": "Nassau",
    "puerto rico": "San Juan",
    "antigua y barbuda": "Saint John",
    "dominica": "Roseau",
    "san cristobal y nieves": "Basseterre",
    "santa lucia": "Castries",
    "san vicente y las granadinas": "Kingstown",
    "trinidad y tobago": "Puerto España",
    "granada": "Saint George",
    "barbados": "Bridgetown",
    "venezuela": "Caracas",
    "guyana": "Georgetown",
    "surinam": "Paramaribo",
    "bolivia": "Sucre",
    "ecuador": "Quito",
    "paraguay": "Asuncion",
    "uruguay": "Montevideo"
}         

# Función para obtener la capital de un país en minúsculas
def obtener_capital(pais):
    # Convertir el país a minúsculas
    pais = pais.lower()
    
    # Verificar si el país está en el diccionario
    if pais in paises_y_capitales:
        return paises_y_capitales[pais]
    else:
        return "País no identificado."

# Pedir al usuario que ingrese un país y mostrar la capital
pais_ingresado = input("Ingresa el nombre de un país de América: ")
capital = obtener_capital(pais_ingresado)
print(f"La capital de {pais_ingresado.capitalize()} es {capital.capitalize()}.")