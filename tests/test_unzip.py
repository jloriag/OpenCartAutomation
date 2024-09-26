import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.zip_page import ZipPage


class TestUnZip(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.file_name="opencart-4.0.2.3"
        cls.zip_file_path="files/opencart-4.0.2.3.zip"
        cls.extract_to_path="/var/www/html/files/"

    # Crea el directorio de extracción si no existe
        if not os.path.exists(cls.extract_to_path):
            os.makedirs(cls.extract_to_path)

    def test_unzip_file(self):
        # Crear una instancia de la clase ZipPage
        zip_page = ZipPage(self.zip_file_path, self.extract_to_path)

        # Llamar al método que descomprime el archivo
        zip_page.unzip_file()

        # Verificar si los archivos fueron descomprimidos
        extracted_files = os.listdir(self.extract_to_path)
        self.assertTrue(len(extracted_files) > 0, "La carpeta de destino está vacía.")

if __name__ == "__main__":
    unittest.main()