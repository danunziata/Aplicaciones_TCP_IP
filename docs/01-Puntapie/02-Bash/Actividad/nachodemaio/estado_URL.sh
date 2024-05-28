#!/bin/bash

DEFAULT_URL="https://www.example.com"

# Función para verificar el estado de un sitio web
check_website() {
    local url=$1
    local status_code=$(curl -o /dev/null -s -w "%{http_code}" "$url")

    if [ "$status_code" -eq 200 ]; then
        echo "$url - $status_code - UP!"
    else
        echo "$url - $status_code - DOWN"
    fi
}

# Verificación de argumentos
if [ "$#" -eq 0 ]; then
    echo "No se proporcionó URL. Usando la URL por defecto: $DEFAULT_URL"
    check_website "$DEFAULT_URL"
elif [ "$1" == "-f" ]; then
    if [ -z "$2" ]; then
        echo "Debe proporcionar un archivo después de la opción -f."
        exit 1
    elif [ ! -f "$2" ]; then
        echo "El archivo $2 no existe."
        exit 1
    else
        while IFS= read -r url; do
            check_website "$url"
        done < "$2"
    fi
else
    check_website "$1"
fi
