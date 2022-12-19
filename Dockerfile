FROM python:3.8.10

WORKDIR /app
# Instalamos python dentro del contenedor de nuestra app
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

# Generamos las dependencias
# Va a instalar dentro del contenedor va a instalar todos los modulos que la app necesita

CMD ["python3","app.py"]