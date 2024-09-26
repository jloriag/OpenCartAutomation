# 1. Usar una imagen base de Python
FROM python:3.9-slim

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Añadir la carpeta /app al PYTHONPATH
ENV PYTHONPATH=/app

# 3. Copiar el archivo de requerimientos al contenedor
COPY requirements.txt .

# 4. Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar el código del proyecto al directorio de trabajo del contenedor
COPY . .

# 6. Exponer el puerto (si es necesario, por ejemplo, si tienes una app web)
#EXPOSE 5000

# 7. Definir el comando que se ejecutará cuando el contenedor inicie
CMD ["python", "tests/test_database_operations.py"]