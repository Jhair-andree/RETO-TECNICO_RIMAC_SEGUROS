# Ejemplo de diccionario de mapeo
mapeo_ingles_espanol = {
    "name": "nombre",
    "height": "altura",
    "mass": "masa",
    # Agrega más atributos según sea necesario
}

# Función para transformar un diccionario de atributos
def transformar_a_espanol(datos_en_ingles):
    datos_en_espanol = {}
    for clave, valor in datos_en_ingles.items():
        if clave in mapeo_ingles_espanol:
            clave_espanol = mapeo_ingles_espanol[clave]
            datos_en_espanol[clave_espanol] = valor
        else:
            datos_en_espanol[clave] = valor
    return datos_en_espanol

# Ejemplo de uso
datos_en_ingles = {"name": "Luke", "height": "172", "mass": "77"}
datos_en_espanol = transformar_a_espanol(datos_en_ingles)

print(datos_en_espanol)
