#!/bin/bash

# Función para verificar el estado de un sitio web específico
check_single_website() {
    local url="${1:-http://example.com}"  # URL predeterminada si no se proporciona una específica
    local timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    local status_code=$(curl -s -o /dev/null -w "%{http_code}" "$url") #Curl trae todo el contenido html que un servidor tiene. Luego con lo otro filtramos.
    
    if [ "$status_code" -eq 200 ]; then
        echo "$timestamp - $url - $status_code - UP!"
    else
        echo "$timestamp - $url - $status_code - DOWN"
    fi
}

# Función para realizar una verificación en masa utilizando un archivo de lista de sitios web
check_multiple_websites() {
    local file="$1"
    while IFS= read -r url; do
        check_single_website "$url"
    done < "$file"
}

# Comprobar si se proporciona una opción -f seguida de un archivo válido
if [[ "$1" == "-f" && -f "$2" ]]; then
    check_multiple_websites "$2"
else
    check_single_website "$1"
fi
