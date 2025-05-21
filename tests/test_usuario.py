import unittest
from back.src.Usuario.Administrador import Administrador
from back.src.Usuario.Operador import Operador
from back.src.Usuario.Soporte import Soporte
from back.src.Usuario.GestorUsuario import GestorUsuario

# Mock para GestorArchivos, para no tocar archivos reales en pruebas
class MockGestorArchivos:
    @staticmethod
    def escribir_csv(path, datos):
        # Simula siempre que se pudo escribir sin errores
        return True

    @staticmethod
    def modificar(path, clave, valor_clave, atributo, nuevo_valor):
        # Simula modificación exitosa
        return True

# Patching (parchear) GestorArchivos en GestorUsuario para tests
import back.src.Usuario.GestorUsuario as gestor_module
gestor_module.GestorArchivos = MockGestorArchivos


class TestGestorUsuario(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorUsuario()

    def test_crear_usuario_administrador(self):
        exito = self.gestor.crear_usuario("admin1", "pass123", "Admin Uno", "123456789", "Administrador")
        self.assertTrue(exito)
        usuario = self.gestor.buscar_usuario("admin1")
        self.assertIsNotNone(usuario)
        self.assertIsInstance(usuario, Administrador)
        self.assertEqual(usuario.nombre, "Admin Uno")

    def test_crear_usuario_operador(self):
        self.gestor.crear_usuario("oper1", "pass456", "Operador Uno", "987654321", "Operador")
        usuario = self.gestor.buscar_usuario("oper1")
        self.assertIsInstance(usuario, Operador)

    def test_crear_usuario_soporte(self):
        self.gestor.crear_usuario("soporte1", "pass789", "Soporte Uno", "111222333", "Soporte")
        usuario = self.gestor.buscar_usuario("soporte1")
        self.assertIsInstance(usuario, Soporte)

    def test_crear_usuario_duplicado(self):
        self.gestor.crear_usuario("user1", "pass", "User Uno", "000111222", "Administrador")
        exito = self.gestor.crear_usuario("user1", "pass2", "User Dos", "333444555", "Operador")
        self.assertFalse(exito)

    def test_buscar_usuario_no_existe(self):
        usuario = self.gestor.buscar_usuario("noexiste")
        self.assertIsNone(usuario)

    def test_modificar_usuario_nombre(self):
        self.gestor.crear_usuario("user2", "pass", "Nombre Original", "000111222", "Administrador")
        exito = self.gestor.modificar_usuario("user2", "nombre", "Nombre Modificado")
        self.assertTrue(exito)
        usuario = self.gestor.buscar_usuario("user2")
        self.assertEqual(usuario.nombre, "Nombre Modificado")

    def test_modificar_usuario_usuario_repetido(self):
        self.gestor.crear_usuario("user3", "pass", "Nombre", "000111222", "Administrador")
        self.gestor.crear_usuario("user4", "pass", "Nombre", "000111222", "Administrador")
        # Intentar cambiar user3 a user4 (repetido)
        exito = self.gestor.modificar_usuario("user3", "usuario", "user4")
        self.assertFalse(exito)

    def test_modificar_usuario_atributo_invalido(self):
        self.gestor.crear_usuario("user5", "pass", "Nombre", "000111222", "Administrador")
        exito = self.gestor.modificar_usuario("user5", "atributo_no_valido", "valor")
        self.assertFalse(exito)

    def test_activar_desactivar_usuario(self):
        self.gestor.crear_usuario("user6", "pass", "Nombre", "000111222", "Administrador")
        # Por defecto está activo, intentar activar devuelve False (ya activo)
        self.assertFalse(self.gestor.activar_usuario("user6"))
        # Desactivar
        self.assertTrue(self.gestor.desactivar_usuario("user6"))
        usuario = self.gestor.buscar_usuario("user6")
        self.assertEqual(usuario.estado, "Inactivo")
        # Ahora activar sí debe devolver True
        self.assertTrue(self.gestor.activar_usuario("user6"))
        self.assertEqual(usuario.estado, "Activo")

    def test_activar_desactivar_usuario_no_existente(self):
        self.assertFalse(self.gestor.activar_usuario("noexiste"))
        self.assertFalse(self.gestor.desactivar_usuario("noexiste"))


if __name__ == "__main__":
    unittest.main()
