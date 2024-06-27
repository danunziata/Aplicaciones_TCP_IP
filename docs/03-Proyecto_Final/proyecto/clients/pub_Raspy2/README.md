# Monitoreo de temperatura y uso de CPU dentro de Raspberry Pi 2

Para poder compilar y ejecutar el siguiente codigo, es necesario contar con una Raspberry Pi 2 que utilize un sistema operativo Raspberry PI OS.

---

## Requisitos previos

- Instalar python3 utilizando el siguiente comando dentro de la terminal:

`sudo apt install python3`

- Instalar la libreria de python **psutil** utilizando el siguiente comando dentro de la terminal:

`sudo apt install python3-psutil`

- Instalar la libreria de python **paho-MQTT** utilizando el siguiente comando dentro de la terminal:

`sudo apt install python3-paho-mqtt`

- Instalar la libreria de python **JSON** utilizando el siguiente comando dentro de la terminal:

`sudo apt install python3-json`

---

## Implementacion y ejecucion

Modificar los valores de las variables `broker`, `port`, `topic`, `client_id`, `username` y `password` dentro del archivo python `raspymain.py` o `cputemp.py`, segun corresponda, con los valores correspondientes.
Dentro de un terminal, situarse en la misma direccion en la que se encuentra el archivo antes mencionado. Luego, ejecutar el script utilizando el siguiente comando:

`python3 raspymain.py`