# Utilizar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo de requisitos al contenedor
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente al contenedor
COPY . .

# Ejecutar las migraciones
RUN python manage.py makemigrations
RUN python manage.py migrate

# Exponer el puerto en el que Django se ejecutará
EXPOSE 8000

# Establecer el comando de inicio para el servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]