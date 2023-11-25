import unittest

mapeo_ingles_espanol = {
    "name": "nombre",
    "height": "altura",
    "mass": "masa",
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
    def test_transformar_a_espanol(self):
        datos_en_ingles = {"name": "Luke", "height": "172", "mass": "77"}
        datos_esperados = {"nombre": "Luke", "altura": "172", "masa": "77"}

        datos_transformados = transformar_a_espanol(datos_en_ingles)

        self.assertEqual(datos_transformados, datos_esperados)

    def test_transformar_a_espanol_con_atributos_faltantes(self):
        datos_en_ingles = {"name": "Leia", "gender": "female"}
        datos_esperados = {"nombre": "Leia", "gender": "female"}

        datos_transformados = transformar_a_espanol(datos_en_ingles)

        self.assertEqual(datos_transformados, datos_esperados)

if __name__ == '__main__':
    unittest.main()
