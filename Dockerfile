FROM ubuntu:20.04

RUN apt-get update && apt-get install -y 
RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:ondrej/php
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install php8.3 libapache2-mod-php -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install apache2 -y
RUN apt-get install mysql-server -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get -y install nano
RUN apt-get install php-gd -y
RUN apt-get install php-curl -y
RUN apt-get install php-zip -y
RUN apt-get install php-mysql -y

#RUN a2enmod php
RUN a2enmod rewrite

RUN chown -R www-data:www-data /var/www/html

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

# Configurar MySQL
RUN service mysql start 
#mysql -e "CREATE DATABASE opencart;" && \
#mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%' WITH GRANT OPTION;"  && \
#mysql -e "GRANT USAGE ON *.* TO 'user'@'localhost';"  && \
#mysql -e "GRANT CREATE, SELECT, INSERT, UPDATE, DELETE, INDEX, ALTER ON *.* TO 'user'@'localhost';"  && \
#mysql -e "FLUSH PRIVILEGES;" 
#mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'user'@'localhost' IDENTIFIED BY 'userpassword';" 
#RUN mysql -e "FLUSH PRIVILEGES;" 
#mysql -e "GRANT ALL PRIVILEGES ON opencart.* TO 'user'@'localhost';" 
#RUN mysql -e "FLUSH PRIVILEGES;"

RUN python3 tests/test_unzip.py

RUN mv /var/www/html/files/opencart-4.0.2.3/upload/admin/config-dist.php /var/www/html/files/opencart-4.0.2.3/upload/admin/config.php

RUN chmod -R 777 /var/www/html/files/opencart-4.0.2.3/upload/

RUN chown -R www-data:www-data /var/www/html/files/opencart-4.0.2.3/upload/

#RUN python3 tests/test_rename_file.py




# Exponer el puerto 80 para Apache
EXPOSE 80

# Comando para iniciar tanto MySQL como Apache al arrancar el contenedor
#CMD service mysql start
#CMD python3 tests/test_unzip.py && chmod 755 files/opencart-4.0.2.3/upload/system/storage/cache/ && chmod 755 files/opencart-4.0.2.3/upload/system/storage/logs/ && chmod 755 files/opencart-4.0.2.3/upload/system/storage/download/ && chmod 755 files/opencart-4.0.2.3/upload/system/storage/upload/ && chmod 755 files/opencart-4.0.2.3/upload/image/ && chmod 755 files/opencart-4.0.2.3/upload/image/cache/ && chmod 755 files/opencart-4.0.2.3/upload/image/catalog/ && chmod 755 files/opencart-4.0.2.3/upload/config-dist.php && chmod 755 files/opencart-4.0.2.3/upload/admin/config-dist.php && chmod 755 files/opencart-4.0.2.3/upload/system/framework.php && chmod 755 files/opencart-4.0.2.3/upload/system/vendor.php && apachectl -D FOREGROUND && tail -f /dev/null
CMD apachectl -D FOREGROUND && tail -f /dev/null
#CMD apachectl -D FOREGROUND
