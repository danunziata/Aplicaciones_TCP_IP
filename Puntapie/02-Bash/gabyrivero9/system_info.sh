#!/bin/bash

# Obtener la información del sistema
sistema_operativo=$(lsb_release -d | awk -F"\t" '{print $2}')
kernel=$(uname -r)
cpu=$(lscpu | grep "Model name" | awk -F": " '{print $2}' | xargs)
memoria_total=$(free -h | awk '/^Mem/ {print $2}')
espacio_disco=$(df -h / | awk 'NR==2 {print $2}')
version_bash=$(bash --version | head -n1 | awk '{print $4}')
version_python=$(python3 --version | awk '{print $2}')

# Crear el objeto JSON
json_objeto=$(cat <<EOF
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
echo "$json_objeto"

# Guardar la salida como objeto JSON en un archivo llamado sistema_info.json
echo "$json_objeto" > system_info.json
