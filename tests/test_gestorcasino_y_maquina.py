import unittest
from unittest.mock import patch
from back.src.Casino.GestorCasino import GestorCasino
from back.src.Maquina.GestorMaquina import GestorMaquina

class TestGestorCasinoYMaquina(unittest.TestCase):

    def setUp(self):
        # Mock para evitar escritura en disco
        self.patcher_write = patch('back.src.Casino.GestorCasino.GestorArchivos.escribir_csv', return_value=True)
        self.patcher_modify = patch('back.src.Casino.GestorCasino.GestorArchivos.modificar', return_value=True)
        self.mock_write = self.patcher_write.start()
        self.mock_modify = self.patcher_modify.start()

        # Instancias de gestores
        self.gestor_casino = GestorCasino()
        self.gestor_casino.agregar_casino("Casino Prueba", "Calle Falsa 123", 1)
        self.gestor_maquina = GestorMaquina(self.gestor_casino)

    def tearDown(self):
        self.patcher_write.stop()
        self.patcher_modify.stop()

    def test_agregar_maquina_en_casino_existente(self):
        resultado = self.gestor_maquina.agregar_maquina("MarcaX", "ModeloY", "SN123", 101, 1, 0.25)
        self.assertTrue(resultado)
        maquina = self.gestor_maquina.buscar_maquina(101)
        self.assertIsNotNone(maquina)
        self.assertEqual(maquina.casino.codigo, 1)

    def test_modificar_maquina_cambio_de_marca(self):
        self.gestor_maquina.agregar_maquina("MarcaA", "ModeloB", "SN001", 102, 1, 0.5)
        resultado = self.gestor_maquina.modificar_maquina(102, "marca", "MarcaNueva")
        self.assertTrue(resultado)
        self.assertEqual(self.gestor_maquina.buscar_maquina(102).marca, "MarcaNueva")

    def test_desactivar_y_activar_maquina(self):
        self.gestor_maquina.agregar_maquina("MarcaC", "ModeloD", "SN002", 103, 1, 1.0)
        self.assertTrue(self.gestor_maquina.desactivar_maquina(103))
        self.assertEqual(self.gestor_maquina.buscar_maquina(103).estado, "Inactiva")
        self.assertTrue(self.gestor_maquina.activar_maquina(103))
        self.assertEqual(self.gestor_maquina.buscar_maquina(103).estado, "Activa")

if __name__ == '__main__':
    unittest.main()
