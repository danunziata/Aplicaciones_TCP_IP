#!/bin/bash

# Obtener información del sistema
sistema_operativo=$(lsb_release -d | awk -F"\t" '{print $2}')
kernel=$(uname -r)
cpu=$(lscpu | grep "Model name" | awk -F ":" '{print $2}' | xargs)
memoria_total=$(free -h | awk '/Mem:/ {print $2}')
espacio_disco=$(df -h --total | awk 'END{print $2}')
version_bash=$(bash --version | grep "version" | awk '{print $4}' | head -n 1)
version_python=$(python3 --version 2>&1 | awk '{print $2}')

# Construir el objeto JSON
json="{\n\"sistema_operativo\": \"$sistema_operativo\", \
\n\"kernel\": \"$kernel\", \
\n\"cpu\": \"$cpu\", \
\n\"memoria_total\": \"$memoria_total\", \
\n\"espacio_disco\": \"$espacio_disco\", \
\n\"version_bash\": \"$version_bash\", \
\n\"version_python\": \"$version_python\"\n}"

# Imprimir el objeto JSON
echo -e $json

# Guardar la salida como JSON en un archivo
echo -e $json > sistema_info.json
