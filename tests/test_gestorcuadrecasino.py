import unittest
from datetime import datetime

from back.src.CuadreCasino.GestorCuadreCasino import GestorCuadreCasino
from back.src.Contador.Contador import Contador
from back.src.Casino.Casino import Casino


class TestGestorCuadreCasino(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorCuadreCasino()
        self.casino = Casino("Casino Test", "Dirección Falsa", 1)
        self.lista_contadores = [
            Contador(1, "2024-05-20", 1000.0, 500.0, 100.0, 200.0, None, self.casino),
            Contador(2, "2024-05-20", 1500.0, 700.0, 150.0, 250.0, None, self.casino),
            Contador(3, "2024-05-21", 3000.0, 1300.0, 300.0, 450.0, None, self.casino),
            Contador(4, "2024-05-21", 2000.0, 1000.0, 200.0, 300.0, None, self.casino)
        ]

    def test_sumar_contadores(self):
        suma = self.gestor.sumar_contadores(self.lista_contadores[:2])
        self.assertEqual(suma["in_"], 2500.0)
        self.assertEqual(suma["out"], 1200.0)
        self.assertEqual(suma["jackpot"], 250.0)
        self.assertEqual(suma["billetero"], 450.0)

    def test_total_contadores_por_casino_exito(self):
        total = self.gestor.total_contadores_por_casino("2024-05-20", "2024-05-21", 1, self.lista_contadores)
        self.assertEqual(total, (2500.0, 1100.0, 250.0, 300.0))

    def test_total_contadores_por_casino_fechas_invalidas(self):
        total = self.gestor.total_contadores_por_casino("2024-05-18", "2024-05-19", 1, self.lista_contadores)
        self.assertIsNone(total)

    def test_calculo_utilidad_por_casino_exito(self):
        utilidad = self.gestor.calculo_utilidad_por_casino("2024-05-20", "2024-05-21", 1, self.lista_contadores)
        self.assertEqual(utilidad, 1150.0)

    def test_calculo_utilidad_por_casino_fechas_invalidas(self):
        utilidad = self.gestor.calculo_utilidad_por_casino("2024-05-18", "2024-05-19", 1, self.lista_contadores)
        self.assertIsNone(utilidad)

    def test_guardar_resultados_exito(self):
        contadores = (2500.0, 1100.0, 250.0, 300.0)
        utilidad = 1150.0
        exito = self.gestor.guardar_resultados(contadores, utilidad, self.casino)
        self.assertTrue(exito)
        self.assertEqual(len(self.gestor.lista_cuadre_casino()), 1)

    def test_guardar_resultados_datos_invalidos(self):
        exito = self.gestor.guardar_resultados(None, None, self.casino)
        self.assertFalse(exito)

if __name__ == "__main__":
    unittest.main()
