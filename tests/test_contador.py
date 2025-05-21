import unittest
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from back.src.GestorPrincipal import GestorPrincipal

class TestContador(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorPrincipal()
        self.gestor.agregar_casino("CasinoTest", "Calle Falsa 123", 1)
        self.gestor.agregar_maquina("MarcaX", "ModeloY", "1234", 10, 1, 100.0)

    def test_agregar_contador(self):
        maquina = self.gestor.gestor_maquina.buscar_maquina(10)
        casino = self.gestor.gestor_casino.buscar_casino(1)
        resultado = self.gestor.gestor_contador.agregar_registro_contador(
            1, "2024-05-20", maquina, casino, 1000.0, 800.0, 50.0, 150.0
        )
        self.assertTrue(resultado)
        contador = self.gestor.gestor_contador.buscar_contador(1)
        self.assertIsNotNone(contador)
        self.assertEqual(contador.in_, 1000.0)

    def test_modificar_contador(self):
        maquina = self.gestor.gestor_maquina.buscar_maquina(10)
        casino = self.gestor.gestor_casino.buscar_casino(1)
        self.gestor.gestor_contador.agregar_registro_contador(
            2, "2024-05-20", maquina, casino, 500.0, 400.0, 20.0, 80.0
        )
        self.gestor.gestor_contador.modificar_contador(2, "in", 999.0)
        contador = self.gestor.gestor_contador.buscar_contador(2)
        self.assertEqual(contador.in_, 999.0)

    def test_mostrar_contadores_por_rango(self):
        maquina = self.gestor.gestor_maquina.buscar_maquina(10)
        casino = self.gestor.gestor_casino.buscar_casino(1)
        self.gestor.gestor_contador.agregar_registro_contador(
            3, "2024-05-20", maquina, casino, 600.0, 300.0, 10.0, 90.0
        )
        resultado = self.gestor.gestor_contador.mostrar_contadores_por_rango("2024-05-19", "2024-05-21")
        self.assertTrue(len(resultado) >= 1)

    def test_buscar_contador_inexistente(self):
        contador = self.gestor.gestor_contador.buscar_contador(999)
        self.assertIsNone(contador)

if __name__ == '__main__':
    unittest.main()
