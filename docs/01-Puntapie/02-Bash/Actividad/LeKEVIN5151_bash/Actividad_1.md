# Actividad 1

## Obtener información del sistema en formato JSON utilizando un script Bash

Esta actividad, lo que solicita es que como usuario de Ubuntu, ejecutar un script Bash que permita obtener información del sistema en formato JSON. Esto brindará los detalles del sistema, como el sistema operativo, el kernel, la CPU, la memoria total, el espacio en disco, la versión de Bash y la versión de Python.

El script utilizado es el siguiente, el cual lo explicaremos en 4 partes:

## Parte 1 (Obtención de la información)

#### Obtener Información del Sistema Operativo

El siguiente comando se utiliza para obtener información sobre el sistema operativo:

```bash
sistema_operativo=$(lsb_release -d | awk -F"\t" '{print $2}')
```

Este comando utiliza el comando `lsb_release -d` para obtener una descripción detallada del sistema operativo, y luego utiliza `awk` para extraer la segunda columna de la salida, que contiene la descripción del sistema operativo.

#### Obtener Información del Kernel

El siguiente comando se utiliza para obtener la versión del kernel:

```bash
kernel=$(uname -r)
```

Este comando utiliza el comando `uname -r` para obtener la versión del kernel actual del sistema.

#### Obtener Información de la CPU

El siguiente comando se utiliza para obtener información sobre la CPU:

```bash
cpu=$(lscpu | grep "Model Name" | awk -F ":" '{print $2}' | xargs)
```

Este comando utiliza el comando `lscpu` para obtener información detallada sobre la CPU, luego filtra la línea que contiene "Model Name" con `grep`, utiliza `awk` para extraer el modelo de la CPU de la salida, y finalmente `xargs` para eliminar los espacios adicionales alrededor del modelo.

#### Obtener Información de la Memoria

El siguiente comando se utiliza para obtener la cantidad total de memoria del sistema:

```bash
memoria_total=$(free -h | awk '/Mem:/ {print $2}')
```

Este comando utiliza el comando `free -h` para mostrar la memoria física y swap del sistema en un formato legible para humanos, y luego utiliza `awk` para encontrar la línea que contiene "Mem:" y extraer el valor de la segunda columna, que es la memoria total.

#### Obtener Información del Espacio en Disco

El siguiente comando se utiliza para obtener el espacio total en disco:

```bash
espacio_disco=$(df -h --total | awk 'END{print $2}')
```

Este comando utiliza el comando `df -h --total` para mostrar el espacio en disco disponible en un formato legible para humanos, y luego utiliza `awk` para encontrar la última línea de la salida (que contiene el total) y extraer el valor de la segunda columna, que es el espacio total en disco.

#### Obtener Versiones de Bash y Python

Los siguientes comandos se utilizan para obtener las versiones de Bash y Python:

```bash
version_bash=$(bash --version | grep "version" | awk '{print $4}' | head -n 1)
version_python=$(python3 --version 2>&1 | awk '{print $2}')
```

- El comando para obtener la versión de Bash utiliza `bash --version` para mostrar la versión de Bash instalada, luego `grep` para filtrar la línea que contiene "version", `awk` para extraer el número de versión y `head -n 1` para obtener solo la primera línea de salida.
- El comando para obtener la versión de Python utiliza `python3 --version` para mostrar la versión de Python 3 instalada y `awk` para extraer el número de versión.

## Parte 2 (Construir el objeto JSON)

En esta sección se describe cómo se construye un objeto JSON utilizando la información obtenida en la primera parte del script.

El objeto JSON se compone de los siguientes campos:

1. **sistema_operativo**: Describe el sistema operativo del sistema.
2. **kernel**: Indica la versión del kernel del sistema.
3. **cpu**: Especifica el modelo de la CPU del sistema.
4. **memoria_total**: Muestra la cantidad total de memoria del sistema.
5. **espacio_disco**: Indica el espacio total en disco del sistema.
6. **version_bash**: Muestra la versión de Bash instalada en el sistema.
7. **version_python**: Indica la versión de Python instalada en el sistema.

A continuación se muestra el código utilizado para construir el objeto JSON:

```bash
json="\"sistema_operativo\": \"$sistema_operativo\", \
\n\"kernel\": \"$kernel\", \
\n\"cpu\": \"$cpu\", \
\n\"memoria_total\": \"$memoria_total\", \
\n\"espacio_disco\": \"$espacio_disco\", \
\n\"version_bash\": \"$version_bash\", \
\n\"version_python\": \"$version_python\""
```

Este código asigna los valores de las variables obtenidas anteriormente a las correspondientes claves del objeto JSON, asegurándose de que estén correctamente formateados para su uso en un archivo JSON.

## Parte 3 (Imprimir y guardar el objeto JSON)

En esta sección del script, se imprime el objeto JSON que ha sido construido previamente utilizando la información obtenida del sistema operativo, hardware y software.

El siguiente comando se utiliza para imprimir el objeto JSON en la salida estándar:

```bash
echo -e $json
```

Luego, enviamos esta información a un archivo llamado "sistema_info.json"

```bash
echo -e $json > sistema_info.json
```
