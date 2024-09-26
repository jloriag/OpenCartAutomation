import unittest
from utils.database_utils import DatabaseUtils

class TestDatabaseOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        DatabaseUtils.create_mysql_database('db', 'user', 'userpassword', 'opencart')

    def test_example(self):
        # Aquí puedes escribir tus pruebas que utilizan la base de datos
        self.assertTrue(True)

    @classmethod
    def tearDownClass(cls):
        # Limpiar la base de datos si es necesario
        pass

if __name__ == '__main__':
    unittest.main()