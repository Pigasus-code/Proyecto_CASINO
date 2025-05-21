import unittest
from unittest.mock import patch
from back.src.Casino.GestorCasino import GestorCasino

class TestGestorCasino(unittest.TestCase):

    def setUp(self):
      
        self.patcher_write = patch('back.src.Casino.GestorCasino.GestorArchivos.escribir_csv', return_value=True)
        self.patcher_modify = patch('back.src.Casino.GestorCasino.GestorArchivos.modificar', return_value=True)
        self.mock_write = self.patcher_write.start()
        self.mock_modify = self.patcher_modify.start()

        self.gestor = GestorCasino()

    def tearDown(self):
        self.patcher_write.stop()
        self.patcher_modify.stop()

    def test_agregar_casino_exitoso(self):
        resultado = self.gestor.agregar_casino("Casino Uno", "Calle 1", 100)
        self.assertTrue(resultado)
        self.assertIsNotNone(self.gestor.buscar_casino(100))

    def test_agregar_casino_duplicado(self):
        self.gestor.agregar_casino("Casino Uno", "Calle 1", 100)
        resultado = self.gestor.agregar_casino("Casino Repetido", "Calle 2", 100)
        self.assertFalse(resultado)

    def test_buscar_casino_existente(self):
        self.gestor.agregar_casino("Casino Test", "Calle Test", 101)
        casino = self.gestor.buscar_casino(101)
        self.assertIsNotNone(casino)
        self.assertEqual(casino.nombre, "Casino Test")

    def test_buscar_casino_inexistente(self):
        casino = self.gestor.buscar_casino(999)
        self.assertIsNone(casino)

    def test_modificar_nombre(self):
        self.gestor.agregar_casino("Casino A", "Dir A", 1)
        resultado = self.gestor.modificar_casino(1, "nombre", "Nuevo Nombre")
        self.assertTrue(resultado)
        self.assertEqual(self.gestor.buscar_casino(1).nombre, "Nuevo Nombre")

    def test_modificar_con_atributo_invalido(self):
        self.gestor.agregar_casino("Casino A", "Dir A", 1)
        resultado = self.gestor.modificar_casino(1, "invalido", "dato")
        self.assertFalse(resultado)

    def test_modificar_codigo_existente(self):
        self.gestor.agregar_casino("Casino A", "Dir A", 1)
        self.gestor.agregar_casino("Casino B", "Dir B", 2)
        resultado = self.gestor.modificar_casino(1, "codigo", 2)  
        self.assertFalse(resultado)

    def test_activar_casino_existente(self):
        self.gestor.agregar_casino("Casino Act", "Dir", 10)
        self.gestor.desactivar_casino(10)
        resultado = self.gestor.activar_casino(10)
        self.assertTrue(resultado)
        self.assertEqual(self.gestor.buscar_casino(10).estado, "Activo")

    def test_desactivar_casino_inexistente(self):
        resultado = self.gestor.desactivar_casino(999)
        self.assertFalse(resultado)

    def test_filtro_por_activos(self):
        self.gestor.agregar_casino("Casino A", "Dir A", 1)
        self.gestor.agregar_casino("Casino B", "Dir B", 2)
        self.gestor.desactivar_casino(2)
        activos = self.gestor.filtro_por_activos()
        self.assertEqual(len(activos), 1)
        self.assertEqual(activos[0].codigo, 1)

    def test_filtro_por_inactivos(self):
        self.gestor.agregar_casino("Casino A", "Dir A", 1)
        self.gestor.desactivar_casino(1)
        inactivos = self.gestor.filtro_por_inactivos()
        self.assertEqual(len(inactivos), 1)
        self.assertEqual(inactivos[0].estado, "Inactivo")

if __name__ == '__main__':
    unittest.main()
