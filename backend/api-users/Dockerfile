# Dockerfile del microservicio1
FROM python:3.9-slim

# Instalar las dependencias del sistema necesarias para PostgreSQL
RUN apt-get update && apt-get install -y libpq-dev

WORKDIR /backend/api-genres

# Copiar los archivos necesarios al contenedor
COPY requirements.txt .

# Instalar las dependencias del microservicio
RUN pip install -r requirements.txt

# Copiar los archivos necesarios al contenedor
COPY models.py .
COPY __init__.py .
COPY script.sh .


# Establecer el comando para ejecutar el microservicio
CMD [ "sh", "script.sh"]
