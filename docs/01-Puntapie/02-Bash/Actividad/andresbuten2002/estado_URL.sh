#!/bin/bash

# Función para verificar el estado de un sitio web
check_website_status() {
    local url="$1"
    local status_code=$(curl -s -o /dev/null -w "%{http_code}" "$url" 2>/dev/null)
    local timestamp=$(date +"%Y-%m-%d %T")

    if [ "$status_code" -eq 200 ]; then
        echo "$timestamp - $url is UP! (Status code: $status_code)"
    else
        echo "$timestamp - $url is DOWN (Status code: $status_code)"
    fi
}

# Verificar el estado de un sitio web específico o utilizar una URL por defecto
if [ "$1" != "-f" ]; then
    if [ -z "$1" ]; then
        default_url="https://sisinfo.unrc.edu.ar/index.php?accion=salir"
        echo "No se proporcionó una URL específica. Utilizando la URL por defecto: $default_url"
        check_website_status "$default_url"
    else
        check_website_status "$1"
    fi
fi

# Realizar verificación en masa utilizando un archivo de lista de sitios web
if [ "$1" == "-f" ] && [ -n "$2" ] && [ -f "$2" ]; then
    echo "Realizando verificación en masa de sitios web listados en $2:"
    while IFS= read -r website || [ -n "$website" ]; do
        if [ -n "$website" ]; then
            check_website_status "$website"
        fi
    done < "$2"
fi
