#!/bin/bash

# Función para verificar el estado de un sitio web
check_website() {
    local url="$1"
    local status_code=$(curl -s -o /dev/null -w "%{http_code}" "$url")
    local current_time=$(date +"%Y-%m-%d %H:%M:%S")

    if [ "$status_code" = "200" ]; then
        echo "$current_time - $url - $status_code - UP!"
    else
        echo "$current_time - $url - $status_code - DOWN"
    fi
}

# Verificar el estado de un sitio web individual
check_single_website() {
    local url="$1"
    if [ -z "$url" ]; then
        url="https://www.example.com"  # URL por defecto
    fi
    check_website "$url"
}

# Verificar el estado de múltiples sitios web desde un archivo
check_multiple_websites() {
    local file="$1"
    if [ ! -f "$file" ]; then
        echo "El archivo $file no existe o no es válido."
        exit 1
    fi

    while IFS= read -r line || [[ -n "$line" ]]; do
        check_website "$line"
    done < "$file"
}

# Manejar las opciones de línea de comandos
while getopts "f:" opt; do
    case $opt in
        f)
            file="$OPTARG"
            check_multiple_websites "$file"
            ;;
        \?)
            echo "Opción inválida: -$OPTARG" >&2
            exit 1
            ;;
    esac
done

# Si no se proporciona ninguna opción, verificar un sitio web individual
if [ "$OPTIND" -eq 1 ]; then
    check_single_website "$1"
fi
