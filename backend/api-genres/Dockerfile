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

# Establecer las variables de entorno para la conexión con PostgreSQL
ENV POSTGRES_HOST=44.209.15.122
ENV POSTGRES_PORT=5432
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=utec
ENV POSTGRES_DB=tienda

# Establecer el comando para ejecutar el microservicio
CMD [ "sh", "script.sh"]
