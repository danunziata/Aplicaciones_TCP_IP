FROM ubuntu:latest

# Establecer directorio de trabajo
WORKDIR /app

# Actualizar lista de paquetes e instalar herramientas
RUN apt-get update && \
    apt-get install -y \
        python3-pip \
        unzip \
        curl \
        pkg-config \
        libcairo2-dev  

# Copiar el archivo requirements.txt
COPY requirements.txt /app/

# Instalar paquetes Python desde el archivo requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copiar el archivo home.py y reemplazar el existente
COPY app.py /app/

# Copiar el script start.sh al contenedor
COPY start.sh /app/start.sh

# Dar permisos de ejecución al script
RUN chmod +x /app/start.sh

# Especificar el comando predeterminado al iniciar el contenedor
CMD ["/app/start.sh"]
