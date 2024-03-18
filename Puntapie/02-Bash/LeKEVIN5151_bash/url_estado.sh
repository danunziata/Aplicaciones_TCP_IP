#!/bin/bash

# Función para verificar el estado de un sitio web
check_website() {
    local url="$1"
    local status=$(curl -s -o /dev/null -w "%{http_code}" "$url")
    if [ "$status" == "200" ]; then
        echo "$(date +"%Y-%m-%d %H:%M:%S") - $url - $status - UP!"
    else
        echo "$(date +"%Y-%m-%d %H:%M:%S") - $url - $status - DOWN"
    fi
}

# Verificar el estado de un sitio web específico
if [ $# -eq 1 ]; then
    check_website "$1"
    exit 0
fi

# Verificar el estado de los sitios web en un archivo
if [ $# -eq 0 ]; then
    echo "No se proporcionó ninguna URL. Se utilizará una URL por defecto."
    default_url="https://www.example.com"
    check_website "$default_url"
    exit 0
fi

# Verificar el estado de los sitios web en un archivo
file="$1"
if [ ! -f "$file" ]; then
    echo "El archivo $file no existe o no es válido."
    exit 1
fi

while IFS= read -r line; do
    check_website "$line"
done < "$file"
