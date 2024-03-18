# Actividad 2: Verificación del Estado de Sitios Web

Como usuario, se solicita realizar un script de Bash que permita verificar el estado de un sitio web individual o realizar una verificación en masa de varios sitios web.

Para realizar la implementación, se ha pensado en tres secciones principales: Una correspondiente a una función que tome una URL y haga una solicitud HTTP a la misma, otra seccion para verificar el estado de un sitio web específico o si se usa una URL por defecto y otra para concer el estado de varias direcciones contenidas en un archivo.

## Utilización de una función

Para esta primera parte, se ha implementado un código como el que se muestra a continuación.

```bash
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
```

La función `check_website_status()` toma una URL como argumento. Luego, utiliza `curl`para hacer una solicitud HTTP a la URL especificada.

El parámetro `-s` hace que curl opere en modo silencioso, evitando que muestre información de progreso.

En cuanto al parámetro `-o /dev/null` hace que curl descargue la salida a `/dev/null`, lo que significa que no guarda el contenido de la respuesta en ningún archivo.

El parámetro `-w "%{http_code}"` le dice a `curl` que imprima solo el código de estado HTTP de la respuesta.

El código de estado se almacena en la variable `status_code`.

La fecha y la hora actual se obtienen usando el comando `date +"%Y-%m-%d %T"`.

Si el código de estado es igual a 200, se imprime un mensaje indicando que el sitio web está arriba junto con la fecha, hora y el código de estado. Por el contrario, si no es igual a 200, se imprime un mensaje indicando que el sitio web está abajo junto con la fecha, hora y el código de estado.

## Verificación del estado de un sitio web específico o uso de una URL por defecto

En esta sección el objetivo es controlar el estado de una página cuya dirección debe ser especificada. En caso de que no se establezca ninguna URL, se coloca una dirección por defecto, para la cual se decidió por el sitio web de la universidad.

```bash
if [ "$1" != "-f" ]; then
    if [ -z "$1" ]; then
        default_url="https://sisinfo.unrc.edu.ar/index.php?accion=salir"
        echo "No se proporcionó una URL específica. Utilizando la URL por defecto: $default_url"
        check_website_status "$default_url"
    else
        check_website_status "$1"
    fi
fi
```

Entonces, primero se verifica si se proporciona una URL específica como argumento al script.Si no se proporciona ningún argumento, se establece una URL por defecto (https://sisinfo.unrc.edu.ar/index.php?accion=salir).

Se llama a la función `check_website_status()` con la URL correspondiente.

Ambas salidas y entradas se muestran debajo.

```shell
> ./estado_URL.sh https://unrc.gitlab.io/labredes/
2024-03-14 15:21:14 - https://unrc.gitlab.io/labredes/ is UP! (Status code: 200)
```

```shell
> ./estado_URL.sh
No se proporcionó una URL específica. Utilizando la URL por defecto: https://sisinfo.unrc.edu.ar/index.php?accion=salir
2024-03-14 15:21:42 - https://sisinfo.unrc.edu.ar/index.php?accion=salir is UP! (Status code: 200)
```

## Verificación en masa utilizando un archivo de lista de sitios web

En esta última parte, se ha escrito un programa que trata de verificar el estado de varias URL que estan contenidas dentro de un archivo .txt.

```bash
if [ "$1" == "-f" ] && [ -n "$2" ] && [ -f "$2" ]; then
    echo "Realizando verificación en masa de sitios web listados en $2:"
    while IFS= read -r website || [ -n "$website" ]; do
        if [ -n "$website" ]; then
            check_website_status "$website"
        fi
    done < "$2"
fi
```

Esta sección verifica si se proporciona la opción `-f` seguida de un archivo válido como argumento al script.
Si se proporciona, el script lee cada línea del archivo y llama a la función `check_website_status()` con cada URL.

Se muestra un mensaje indicando que se está realizando una verificación en masa y se imprime el estado de cada sitio web en la lista, junto con la fecha, hora y el código de estado.

La correspondiente entrada y salida es como sigue:

```shell
> ./estado_URL.sh -f lista_URL.txt
Realizando verificación en masa de sitios web listados en lista_URL.txt:
2024-03-14 15:28:24 - https://cursos.ing.unrc.edu.ar/cursos/login/index.php is UP! (Status code: 200)
2024-03-14 15:28:26 - https://unrc.gitlab.io/labredes/ is UP! (Status code: 200)
2024-03-14 15:28:26 - https://unrc.gitlab.ioa/labredes/ is DOWN (Status code: 000)
2024-03-14 15:28:27 - https://mail.google.com/mail/u/0/inbox is DOWN (Status code: 302)
```

El script de bash correspondiente se encuentra haciendo click en el siguiente enlace [estado_URL.sh](https://github.com/danunziata/Aplicaciones_TCP_IP/tree/main/Puntapie/02-Bash/LeKEVIN5151_bash/url_estado.sh). Recordar que debemos dar permisos de ejecución a este archivo, mediante el comando `chmod +x estado_URL.sh`.

En relación al archivo que contiene algunas direcciones URL con las que se hicieron pruebas es [lista_URL.txt](https://github.com/danunziata/Aplicaciones_TCP_IP/tree/main/Puntapie/02-Bash/LeKEVIN5151_bash/lista_url.txt)
