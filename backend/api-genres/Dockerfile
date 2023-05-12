# Dockerfile del microservicio1
FROM python:3.9-slim

WORKDIR /app

# Copiar los archivos necesarios al contenedor
COPY ../requirements.txt .

# Instalar las dependencias del microservicio
RUN pip install -r requirements.txt

# Copiar los archivos necesarios al contenedor
COPY ../models.py .
COPY __init__.py .

# Exponer el puerto en el que se ejecutará el microservicio (puede ser diferente según tus necesidades)
EXPOSE 5000

# Establecer el comando para ejecutar el microservicio
CMD [ "python", "microservice1.py" ]
