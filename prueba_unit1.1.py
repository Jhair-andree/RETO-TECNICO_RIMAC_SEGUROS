import unittest
mapeo_ingles_espanol = {
    "name": "nombre",
    "height": "altura",
    "mass": "masa",
    # Agrega más atributos según sea necesario
}

def transformar_a_espanol(datos_en_ingles):
    datos_en_espanol = {}
    for clave, valor in datos_en_ingles.items():
        if clave in mapeo_ingles_espanol:
            clave_espanol = mapeo_ingles_espanol[clave]
            datos_en_espanol[clave_espanol] = valor
        else:
            datos_en_espanol[clave] = valor
    return datos_en_espanol

datos_en_ingles = {"name": "Luke", "height": "172", "mass": "77"}
datos_en_espanol = transformar_a_espanol(datos_en_ingles)

print(datos_en_espanol)

class TestTransformacionAPI(unittest.TestCase):
    def setUp(self):
        self.datos_en_ingles_base = {"name": "Luke", "height": "172", "mass": "77"}
        self.datos_esperados_base = {"nombre": "Luke", "altura": "172", "mas


class TestTransformacionAPI(unittest.TestCase):
    def setUp(self):
        self.datos_en_ingles_base = {"name": "Luke", "height": "172", "mass": "77"}
        self.datos_esperados_base = {"nombre": "Luke", "altura": "172", "mas}
