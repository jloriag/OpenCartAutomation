from utils.database_utils import DatabaseUtils

class TestSetup:
    @staticmethod
    def setup_database():
        # Crear base de datos SQLite
        DatabaseUtils.create_mysql_database('localhost', 'root', 'root', 'opencart')

    @staticmethod
    def teardown_database():
        # Aquí puedes agregar código para limpiar la base de datos después de las pruebas, si es necesario
        pass