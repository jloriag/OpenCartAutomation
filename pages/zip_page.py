import zipfile
import os

class ZipPage:
    def __init__(self,zip_file_path,extract_to_path):
        self.zip_file_path=zip_file_path #Ruta del archivo Zip
        self.extract_to_path=extract_to_path# Carpeta donde se va a extraer

    def unzip_file(self):
        if not os.path.exists(self.zip_file_path):
            raise FileNotFoundError(f"El archivo {self.zip_file_path} no fue encontrado.")
        
        if not zipfile.is_zipfile(self.zip_file_path):
            raise zipfile.BadZipFile(f"El archivo {self.zip_file_path} no es un archivo ZIP valido")
        
        with zipfile.ZipFile(self.zip_file_path, "r") as zip_ref:
            zip_ref.extractall(self.extract_to_path)
        print(f"Archivo descomprimido en {self.extract_to_path}")