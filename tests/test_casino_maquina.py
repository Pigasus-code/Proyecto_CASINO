import unittest
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
        maquina = self.gestor.gestor_maquina.buscar_maquina(1)
        self.assertIsNotNone(maquina)
        self.assertEqual(maquina.nombre, "macvc")

    def test_modificar_maquina(self):
        self.gestor.agregar_casino("juan", "calle 23", 1)
        self.gestor.agregar_casino("samuel", "calle 13", 2)
        self.gestor.agregar_maquina("macvc", "hdfd", "2113", 1, 3, 230.3)
        self.gestor.modificar_maquina(1, "casino", 2)
        maquina = self.gestor.gestor_maquina.buscar_maquina(1)
        self.assertEqual(maquina.id_casino, 2)

    def test_activar_desactivar_maquina(self):
        self.gestor.agregar_casino("juan", "calle 23", 1)
        self.gestor.agregar_maquina("macvc", "hdfd", "2113", 1, 3, 230.3)

        self.gestor.desactivar_maquina(1)
        maquina = self.gestor.gestor_maquina.buscar_maquina(1)
        self.assertFalse(maquina.activa)

        self.gestor.activar_maquina(1)
        maquina = self.gestor.gestor_maquina.buscar_maquina(1)
        self.assertTrue(maquina.activa)

    def test_desactivar_maquina_inexistente(self):
        with self.assertRaises(Exception):  # ajusta si tu método no lanza excepción
            self.gestor.desactivar_maquina(999)

if __name__ == '__main__':
    unittest.main()

