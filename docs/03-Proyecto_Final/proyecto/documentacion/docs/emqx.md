# EMQX
EMQX (EMQ X Broker) es un broker de mensajes MQTT de código abierto y altamente escalable, diseñado para admitir millones de conexiones simultáneas. Es compatible con el protocolo MQTT (Message Queuing Telemetry Transport), que es un protocolo de mensajería ligero y eficiente, ideal para aplicaciones de Internet de las Cosas (IoT), sistemas de automatización, monitoreo remoto y más. EMQX ofrece características avanzadas como la persistencia de mensajes, QoS (Quality of Service) y soporte para múltiples protocolos de autenticación y autorización.

En este proyecto, EMQX se utiliza como el broker MQTT para gestionar la comunicación entre los sensores IoT y los servicios que procesan y almacenan los datos. Los sensores publican datos en tópicos MQTT, y EMQX distribuye estos mensajes a los suscriptores interesados, como Telegraf, que luego los envía a InfluxDB para su almacenamiento y análisis.

## Configuración del Docker Compose para EMQX
En el archivo `docker-compose.yaml`, se define un servicio para EMQX con la siguiente configuración:

```yaml
version: "3.9"
services:
  emqx:
    user: root
    build: ./emqx
    ports:
      - "18083:18083" #interfaz web de administración
      - "1883:1883" #conexiones MQTT sin cifrar
      - "8883:8883" #conexiones MQTT cifradas (SSL/TLS)
    volumes:
      - ./emqx/data/data:/opt/emqx/data
      - ./emqx/data/log:/opt/emqx/log
```
Este archivo se encuentra en: [docker-compose.yaml](https://github.com/danunziata/Aplicaciones_TCP_IP/blob/develop/docs/03-Proyecto_Final/proyecto/server/docker-compose.yaml)
## Configuración del Dockerfile para EMQX
El archivo Dockerfile para EMQX se encuentra en el directorio `./emqx` y se ve así:

```Dockerfile
# Utiliza la imagen base de EMQX
FROM emqx:latest

# Copia el archivo de configuración personalizado (si es necesario)
# COPY config/emqx_auth_mysql.conf /opt/emqx/etc/plugins/emqx_auth_mysql.conf

# Configura las credenciales del dashboard
ENV EMQX_DASHBOARD__DEFAULT_USERNAME=labiot
ENV EMQX_DASHBOARD__DEFAULT_PASSWORD=labiot
ENV EMQX_ALLOW_ANONYMOUS=false

# Configura la autenticación MySQL
ENV EMQX_AUTH__MYSQL__SERVER=127.0.0.1:3306
ENV EMQX_AUTH__MYSQL__USERNAME=labiot
ENV EMQX_AUTH__MYSQL__PASSWORD=labiot2024
ENV EMQX_AUTH__MYSQL__DATABASE=emqx_auth
```
Este archivo se encuentra en: [Dockerfile](https://github.com/danunziata/Aplicaciones_TCP_IP/blob/develop/docs/03-Proyecto_Final/proyecto/server/emqx/Dockerfile)
## Resumen
En este proyecto, EMQX actúa como el broker MQTT, facilitando la comunicación entre los sensores IoT y los servicios que procesan y almacenan los datos. La configuración en docker-compose.yaml y el Dockerfile asegura que EMQX esté correctamente configurado y listo para recibir y distribuir mensajes MQTT, haciendo que la arquitectura del proyecto sea escalable y fácil de gestionar. La configuración de la autenticación MySQL y las credenciales del dashboard aseguran que solo los usuarios autorizados puedan acceder y publicar mensajes en el broker.