# test/test_cuadre_maquina.py
import unittest
from datetime import date
from back.src.CuadreMaquina.CuadreMaquina import CuadreMaquina
from back.src.CuadreMaquina.GestorCuadreMaquina import GestorCuadreMaquina

class DummyMaquina:
    def __init__(self, id_maquina, nombre, asset=None, denominacion=1):
        self.id_maquina = id_maquina
        self.nombre = nombre
        self.asset = asset or f"Asset-{id_maquina}"
        self.denominacion = denominacion

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_maquina})"

class TestGestorCuadreMaquina(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorCuadreMaquina()
        self.maquina = DummyMaquina(1, "Tragamonedas 3000", asset="A001", denominacion=1)
        self.contadores = (1000.0, 800.0, 50.0, 100.0)  # in, out, jackpot, billetero
        self.utilidad = 50.0

    # --- Tests para guardar_resultados ---

    def test_guardar_resultados(self):
        self.gestor.guardar_resultados(self.contadores, self.utilidad, self.maquina)
        lista = self.gestor.lista_cuadre_quina()
        self.assertEqual(len(lista), 1)

        cuadre = lista[0]
        self.assertIsInstance(cuadre, CuadreMaquina)
        self.assertEqual(cuadre.in_, 1000.0)
        self.assertEqual(cuadre.out, 800.0)
        self.assertEqual(cuadre.jackpot, 50.0)
        self.assertEqual(cuadre.billetero, 100.0)
        self.assertEqual(cuadre.utilidad, 50.0)
        self.assertEqual(cuadre.maquina.nombre, "Tragamonedas 3000")

    def test_guardar_multiples_resultados(self):
        maquina2 = DummyMaquina(2, "Ruleta 5000", asset="A002", denominacion=5)
        contadores2 = (2000.0, 1500.0, 200.0, 100.0)
        utilidad2 = 200.0

        self.gestor.guardar_resultados(self.contadores, self.utilidad, self.maquina)
        self.gestor.guardar_resultados(contadores2, utilidad2, maquina2)

        lista = self.gestor.lista_cuadre_quina()
        self.assertEqual(len(lista), 2)
        self.assertEqual(lista[1].maquina.nombre, "Ruleta 5000")
        self.assertEqual(lista[1].utilidad, 200.0)

    def test_guardar_con_valores_limite(self):
        contadores_cero = (0.0, 0.0, 0.0, 0.0)
        utilidad_cero = 0.0

        self.gestor.guardar_resultados(contadores_cero, utilidad_cero, self.maquina)
        cuadre = self.gestor.lista_cuadre_quina()[0]

        self.assertEqual(cuadre.in_, 0.0)
        self.assertEqual(cuadre.out, 0.0)
        self.assertEqual(cuadre.jackpot, 0.0)
        self.assertEqual(cuadre.billetero, 0.0)
        self.assertEqual(cuadre.utilidad, 0.0)

    def test_guardar_con_valores_negativos(self):
        contadores_neg = (-100.0, -50.0, -10.0, -5.0)
        utilidad_neg = -20.0

        self.gestor.guardar_resultados(contadores_neg, utilidad_neg, self.maquina)
        cuadre = self.gestor.lista_cuadre_quina()[0]

        self.assertEqual(cuadre.in_, -100.0)
        self.assertEqual(cuadre.out, -50.0)
        self.assertEqual(cuadre.jackpot, -10.0)
        self.assertEqual(cuadre.billetero, -5.0)
        self.assertEqual(cuadre.utilidad, -20.0)

    def test_guardar_con_datos_invalidos(self):
        # Si guardar_resultados no valida tipos, este test fallará, 
        # es recomendable agregar validación en el método para que lance excepciones
        contadores_invalidos = ("mil", None, {}, [])
        utilidad_invalida = "cincuenta"

        with self.assertRaises((TypeError, ValueError, AttributeError)):
            self.gestor.guardar_resultados(contadores_invalidos, utilidad_invalida, self.maquina)

    # --- Tests para calculo_total_contadores ---

    def test_calculo_total_contadores_exitoso(self):
        # Creamos dos CuadreMaquina con fechas y mismos asset
        c1 = CuadreMaquina(10, 5, 1, 2, 0, self.maquina)
        c1.fecha = date(2025, 5, 1)
        c1.maquina.asset = "A001"
        c1.maquina.denominacion = 1

        c2 = CuadreMaquina(20, 10, 2, 4, 0, self.maquina)
        c2.fecha = date(2025, 5, 2)
        c2.maquina.asset = "A001"
        c2.maquina.denominacion = 1

        lista = [c1, c2]
        resultado = self.gestor.calculo_total_contadores(date(2025, 5, 1), date(2025, 5, 2), "A001", lista)
        # (20-10, 10-5, 2-1, 4-2) * denominacion 1
        self.assertEqual(resultado, (10, 5, 1, 2))

    def test_calculo_total_contadores_no_dos_contadores(self):
        c1 = CuadreMaquina(10, 5, 1, 2, 0, self.maquina)
        c1.fecha = date(2025, 5, 1)
        c1.maquina.asset = "A001"
        c1.maquina.denominacion = 1

        lista = [c1]  # Solo 1 contador
        resultado = self.gestor.calculo_total_contadores(date(2025, 5, 1), date(2025, 5, 2), "A001", lista)
        self.assertIsNone(resultado)

    def test_calculo_total_contadores_asset_diferente(self):
        c1 = CuadreMaquina(10, 5, 1, 2, 0, self.maquina)
        c1.fecha = date(2025, 5, 1)
        c1.maquina.asset = "A001"
        c1.maquina.denominacion = 1

        c2 = CuadreMaquina(20, 10, 2, 4, 0, self.maquina)
        c2.fecha = date(2025, 5, 2)
        c2.maquina.asset = "A002"  # Diferente asset
        c2.maquina.denominacion = 1

        lista = [c1, c2]
        resultado = self.gestor.calculo_total_contadores(date(2025, 5, 1), date(2025, 5, 2), "A001", lista)
        self.assertIsNone(resultado)

    # --- Tests para calculo_utilidad_maquina ---

    def test_calculo_utilidad_maquina_exitoso(self):
        c1 = CuadreMaquina(100, 80, 10, 20, 0, self.maquina)
        c1.fecha = date(2025, 5, 1)
        c1.maquina.asset = "A001"

        c2 = CuadreMaquina(150, 100, 20, 30, 0, self.maquina)
        c2.fecha = date(2025, 5, 2)
        c2.maquina.asset = "A001"

        lista = [c1, c2]
        resultado = self.gestor.calculo_utilidad_maquina(date(2025, 5, 1), date(2025, 5, 2), "A001", lista)
        # Utilidad = (150-100) - ((100-80) + (20-10)) = 50 - (20 + 10) = 20
        self.assertEqual(resultado, 20.0)

    def test_calculo_utilidad_maquina_no_dos_contadores(self):
        c1 = CuadreMaquina(100, 80, 10, 20, 0, self.maquina)
        c1.fecha = date(2025, 5, 1)
        c1.maquina.asset = "A001"

        lista = [c1]
        resultado = self.gestor.calculo_utilidad_maquina(date(2025, 5, 1), date(2025, 5, 2), "A001", lista)
        self.assertIsNone(resultado)

    def test_calculo_utilidad_maquina_asset_diferente(self):
        c1 = CuadreMaquina(100, 80, 10, 20, 0, self.maquina)
        c1.fecha = date(2025, 5, 1)
        c1.maquina.asset = "A001"

        c2 = CuadreMaquina(150, 100, 20, 30, 0, self.maquina)
        c2.fecha = date(2025, 5, 2)
        c2.maquina.asset = "A002"  # diferente

        lista = [c1, c2]
        resultado = self.gestor.calculo_utilidad_maquina(date(2025, 5, 1), date(2025, 5, 2), "A001", lista)
        self.assertIsNone(resultado)

if __name__ == "__main__":
    unittest.main()

