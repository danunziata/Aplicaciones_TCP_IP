#!/bin/bash

# Obtener información del sistema
sistema_operativo=$(lsb_release -d | awk -F'\t' '{print $2}')
kernel=$(uname -r)
cpu=$(lscpu | grep "Model name" | awk -F': ' '{print $2}')
memoria_total=$(free -h | grep "Mem:" | awk '{print $2}')
espacio_disco=$(df -h / | grep '/' | awk '{print $2}')
version_bash=$BASH_VERSION
version_python=$(python3 --version | awk '{print $2}')

# Crear objeto JSON
json=$(cat <<EOF
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

# Imprimir el objeto JSON en la salida estándar
echo "$json"

# Guardar el objeto JSON en un archivo
echo "$json" > system_info.json
