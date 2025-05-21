import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from back.src.GestorPrincipal import GestorPrincipal

class TestCasinoMaquina(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorPrincipal()

    def test_agregar_casino(self):
        self.gestor.agregar_casino("juan", "calle 23", 1)
        casino = self.gestor.gestor_casino.buscar_casino(1)
        self.assertIsNotNone(casino)
        self.assertEqual(casino.nombre, "juan")

    def test_agregar_maquina(self):
        self.gestor.agregar_casino("juan", "calle 23", 1)
        self.gestor.agregar_maquina("macvc", "hdfd", "2113", 1, 3, 230.3)
        maquina = self.gestor.gestor_maquina.buscar_maquina(3)
        self.assertIsNotNone(maquina)
        self.assertEqual(maquina.marca, "macvc")

    def test_modificar_maquina(self):
        self.gestor.agregar_casino("juan", "calle 23", 1)
        self.gestor.agregar_casino("samuel", "calle 13", 2)
        self.gestor.agregar_maquina("macvc", "hdfd", "2113", 1, 3, 230.3)
        self.gestor.modificar_maquina(3, "casino", 2)
        maquina = self.gestor.gestor_maquina.buscar_maquina(3)
        self.assertEqual(maquina.casino.codigo, 2)

    def test_activar_desactivar_maquina(self):
        self.gestor.agregar_casino("juan", "calle 23", 1)
        self.gestor.agregar_maquina("macvc", "hdfd", "2113", 1, 3, 230.3)

        self.gestor.desactivar_maquina(3)
        maquina = self.gestor.gestor_maquina.buscar_maquina(3)
        self.assertEqual(maquina.estado, "Inactiva")

        self.gestor.activar_maquina(3)
        maquina = self.gestor.gestor_maquina.buscar_maquina(3)
        self.assertEqual(maquina.estado, "Activa")

    def test_desactivar_maquina_inexistente(self):
        resultado = self.gestor.desactivar_maquina(999)
        self.assertFalse(resultado)

if __name__ == '__main__':
    unittest.main()
