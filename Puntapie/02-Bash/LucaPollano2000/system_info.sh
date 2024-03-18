#!/bin/bash

# Recopilación de información del sistema
sistema_operativo=$(lsb_release -d | awk -F"\t" '{print $2}')
kernel=$(uname -r)
cpu=$(lscpu | grep "Nombre del modelo" | awk -F":" '{print $2}' | xargs)
memoria_total=$(free -h | awk '/Mem/{print $2}')
espacio_disco=$(df -h / | awk 'NR==2{print $2}')
version_bash=$(bash --version | awk 'NR==1{print $4}')
version_python=$(python3 --version | awk '{print $2}')

# Creación del objeto JSON
json_data=$(cat <<EOF
{
    "sistema_operativo": "$sistema_operativo",
    "kernel": "$kernel",
    "cpu": "$cpu",
    "memoria_total": "$memoria_total",
    "espacio_disco": "$espacio_disco",
    "version_bash": "$version_bash",
    "version_python": "$version_python"
}
EOF
)

# Imprimir JSON en la salida estándar
echo "$json_data"

# Guardar JSON en un archivo
echo "$json_data" > sistema_info.json
