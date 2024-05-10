# Sistema de Monitoreo de IoT con MQTT, Node-RED, InfluxDB, Grafana y Home Assistant.

## Resumen
El proyecto tiene como objetivo desarrollar un sistema completo de monitoreo de IoT que capture y almacene los datos de temperatura y uso de CPU de servidores, y proporcione visualizaciones en tiempo real y automatización a través de diferentes componentes. Se utilizarán tecnologías como MQTT, Node-RED del lado del servidor y python y bash del lado de los clientes.

Objetivo general: Implementar un sistema integral de monitoreo de IoT que permita capturar, almacenar y visualizar los datos de temperatura y uso de CPU de servidores,



## Milestone 1: Despliegue de Node-RED y EMQX como servicios

1. Configurar el entorno de Docker y Docker Compose.
2. Crear un archivo `docker-compose.yml` para definir los servicios de Node-RED y EMQX.
3. Configurar el servicio de Node-RED en Docker Compose, especificando los volúmenes, puertos y dependencias necesarios.
4. Configurar el servicio de EMQX en Docker Compose, especificando los volúmenes, puertos y configuraciones necesarias.
5. Ejecutar `docker-compose up` para desplegar los contenedores de Node-RED y EMQX.

## Milestone 2: Aprovisionamiento de configuraciones

1. Configurar las credenciales y configuraciones específicas de Node-RED, como la configuración de conexión a EMQX y otros nodos necesarios.
2. Aprovisionar los archivos de configuración necesarios para EMQX, como los archivos de configuración general, autenticación y tópicos MQTT.
3. Reiniciar los contenedores de Node-RED y EMQX para aplicar las nuevas configuraciones.

## Milestone 3: Creación del cliente Bash

1. Crear un archivo Bash que utilice el comando `lm-sensors` para obtener la información de temperatura y uso de CPU.
2. Configurar el cliente Bash para publicar los datos obtenidos en un tópico MQTT específico en el broker EMQX.

## Milestone 4: Creación del cliente Python

1. Crear un script en Python que utilice la librería Paho para conectarse al broker EMQX.
2. Implementar la lógica necesaria para obtener la información de temperatura y uso de CPU utilizando `lm-sensors`.
3. Configurar el cliente Python para publicar los datos obtenidos en un tópico MQTT específico en el broker EMQX.

Cada milestone representa un hito importante en el proceso de despliegue y configuración. Al completar estos milestones, habrás desplegado Node-RED y EMQX como servicios, aprovisionado sus configuraciones y creado los clientes Bash y Python para enviar la información de lm-sensors al broker MQTT.
