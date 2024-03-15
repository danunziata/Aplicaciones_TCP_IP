#!/bin/bash

default_url="https://www.example.com"
file_flag=false

# Función para verificar el estado de un sitio web
check_website() {
    url=$1
    status_code=$(curl -s -o /dev/null -w "%{http_code}" "$url")

    if [[ $status_code -eq 200 ]]; then
        echo "$url is UP!"
    else
        echo "$url is DOWN"
    fi
}

# Procesar opciones de línea de comandos
while getopts ":f:" option; do
    case $option in
        f)
            file_flag=true
            file_path=$OPTARG
            ;;
        \?)
            echo "Opción inválida: -$OPTARG" >&2
            exit 1
            ;;
        :)
            echo "La opción -$OPTARG requiere un argumento." >&2
            exit 1
            ;;
    esac
done

# Si se proporciona un archivo de lista de sitios web
if [ "$file_flag" = true ]; then
    if [ -f "$file_path" ]; then
        while IFS= read -r website; do
            check_website "$website"
        done < "$file_path"
    else
        echo "El archivo $file_path no existe."
        exit 1
    fi
# Si no se proporciona una URL específica, se utiliza la URL por defecto
elif [ $# -eq 0 ]; then
    check_website "$default_url"
# Si se proporciona una URL específica
else
    check_website "$1"
fi
