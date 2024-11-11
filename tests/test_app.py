import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        # Se crea el cliente de prueba
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        # Hacemos una solicitud GET a la ruta '/'
        response = self.app.get('/')
        # Verificamos que el código de estado sea 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Opcional: Verificar contenido
        self.assertIn(b'index', response.data)

    def test_about(self):
        # Hacemos una solicitud GET a la ruta '/about'
        response = self.app.get('/about')
        # Verificamos que el código de estado sea 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Opcional: Verificar contenido
        self.assertIn(b'about', response.data)

if __name__ == '__main__':
    unittest.main()

