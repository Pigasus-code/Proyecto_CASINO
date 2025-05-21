import unittest
from back.src.Maquina.GestorMaquina import GestorMaquina
from back.src.Casino.GestorCasino import GestorCasino

class DummyCasino:
    def __init__(self, nombre, direccion, codigo):
        self.nombre = nombre
        self.direccion = direccion
        self.codigo = codigo
        self.estado = "Activo"

    def activar(self):
        self.estado = "Activo"
        return True

    def desactivar(self):
        self.estado = "Inactivo"
        return True

class TestGestorMaquina(unittest.TestCase):

    def setUp(self):
        self.gestor_casino = GestorCasino()
        self.casino = DummyCasino("Casino Prueba", "Calle Falsa 123", 1)
        self.gestor_casino._GestorCasino__casinos.append(self.casino)  # Bypass para pruebas
        self.gestor_maquina = GestorMaquina(self.gestor_casino)

    def test_agregar_maquina_exito(self):
        resultado = self.gestor_maquina.agregar_maquina("MarcaX", "ModeloY", "S123", 10, self.casino, 0.25)
        self.assertTrue(resultado)
        self.assertIsNotNone(self.gestor_maquina.buscar_maquina(10))

    def test_agregar_maquina_duplicada(self):
        self.gestor_maquina.agregar_maquina("MarcaX", "ModeloY", "S123", 10, self.casino, 0.25)
        resultado = self.gestor_maquina.agregar_maquina("MarcaZ", "ModeloZ", "S999", 10, self.casino, 0.50)
        self.assertFalse(resultado)

    def test_modificar_maquina_marca(self):
        self.gestor_maquina.agregar_maquina("MarcaA", "ModeloB", "S111", 11, self.casino, 0.10)
        resultado = self.gestor_maquina.modificar_maquina(11, "marca", "MarcaMod")
        self.assertTrue(resultado)
        self.assertEqual(self.gestor_maquina.buscar_maquina(11).marca, "MarcaMod")

    def test_modificar_maquina_a_casino_existente(self):
        nuevo_casino = DummyCasino("Nuevo Casino", "Nueva Dir", 2)
        self.gestor_casino._GestorCasino__casinos.append(nuevo_casino)
        self.gestor_maquina.agregar_maquina("MarcaA", "ModeloB", "S111", 12, self.casino, 0.10)
        resultado = self.gestor_maquina.modificar_maquina(12, "casino", 2)
        self.assertTrue(resultado)
        self.assertEqual(self.gestor_maquina.buscar_maquina(12).casino.codigo, 2)

    def test_modificar_maquina_con_dato_invalido(self):
        self.gestor_maquina.agregar_maquina("MarcaA", "ModeloB", "S111", 13, self.casino, 0.10)
        resultado = self.gestor_maquina.modificar_maquina(13, "invalido", "dato")
        self.assertFalse(resultado)

    def test_desactivar_maquina(self):
        self.gestor_maquina.agregar_maquina("MarcaX", "ModeloY", "S123", 14, self.casino, 0.25)
        resultado = self.gestor_maquina.desactivar_maquina(14)
        self.assertTrue(resultado)
        self.assertEqual(self.gestor_maquina.buscar_maquina(14).estado, "Inactiva")

    def test_activar_maquina(self):
        self.gestor_maquina.agregar_maquina("MarcaX", "ModeloY", "S123", 15, self.casino, 0.25)
        self.gestor_maquina.desactivar_maquina(15)
        resultado = self.gestor_maquina.activar_maquina(15)
        self.assertTrue(resultado)
        self.assertEqual(self.gestor_maquina.buscar_maquina(15).estado, "Activa")

    def test_lista_maquinas(self):
        self.gestor_maquina.agregar_maquina("MarcaX", "ModeloY", "S123", 16, self.casino, 0.25)
        maquinas = self.gestor_maquina.lista_maquinas()
        self.assertEqual(len(maquinas), 1)
        self.assertEqual(maquinas[0].asset, 16)

if __name__ == '__main__':
    unittest.main()
