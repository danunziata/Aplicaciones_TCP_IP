FROM ubuntu:22.04

# Actualizar la lista de paquetes e instalar herramientas necesarias
RUN apt update && apt upgrade -y && apt install -y python3-pip unzip curl

# Crear directorio /REFLEX y copiar archivos game_snake.py y requirements.txt
RUN mkdir -p /REFLEX/REFLEX
COPY game_snake.py /REFLEX/
COPY requirements.txt /REFLEX/

# Instalar las dependencias desde el archivo requirements.txt
WORKDIR /REFLEX
RUN pip install -r requirements.txt

# Crear script de inicialización de reflex
RUN echo '#!/bin/bash' > init_reflex.sh \
    && echo 'echo "blank" | reflex init' >> init_reflex.sh \
    && echo 'cp /REFLEX/game_snake.py /REFLEX/REFLEX/REFLEX.py' >> init_reflex.sh \
    && chmod +x init_reflex.sh

# Ejecutar script de inicialización de reflex y luego reflex run
CMD ["bash", "-c", "./init_reflex.sh && reflex run"]
