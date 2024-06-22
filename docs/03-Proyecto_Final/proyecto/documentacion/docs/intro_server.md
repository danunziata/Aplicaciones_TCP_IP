# Introducción al Servidor IoT con Contenedores Docker
Este proyecto configura un servidor IoT utilizando Docker Compose para gestionar múltiples servicios esenciales para la captura, almacenamiento, procesamiento y visualización de datos IoT. Los servicios implementados incluyen EMQX para la mensajería MQTT, InfluxDB para la base de datos de series temporales, Telegraf para la recolección y el envío de métricas, MySQL para la autenticación y Grafana para la visualización de datos. A continuación, se detallan los componentes y su configuración.

## Componentes del Servidor
1. Telegraf:
    - Descripción: Telegraf es un agente para la recolección de métricas y datos, y su envío a diversos destinos, como InfluxDB.
    - Configuración:
        - Imagen: Usa la imagen `telegraf:1.22.4`.
        - Volúmenes:
            - `./telegraf/data/telegraf.conf`: Contiene la configuración de Telegraf.
        - Modo de red: bridge
        - Política de Reinicio: Reinicio en caso de fallo con un retraso de 10 segundos, hasta un máximo de 20 intentos.

2. EMQX (EMQ X Broker):
    - Descripción: EMQX es un broker MQTT de alto rendimiento utilizado para manejar la mensajería entre dispositivos IoT.
    - Configuración:
        - Puertos:
            - 18083: Proporciona acceso al dashboard de EMQX.
            - 1883: Puerto estándar para las conexiones MQTT.
            - 8883: Puerto SSL
        - Volúmenes:
            - `./emqx/data/data`: Almacena los datos de EMQX.
            - `./emqx/data/log`: Almacena los logs de EMQX.

3. MySQL:
    - Descripción: MySQL se utiliza como base de datos relacional para gestionar la autenticación de usuarios de EMQX.
    - Configuración:
        - Puertos:
            - 3306: Puerto estándar para conexiones MySQL.
        - Volúmenes:
            - `./mysql/data`: Almacena los datos de MySQL.
            - `./init.sql`: Script SQL de inicialización para configurar la base de datos.

4. InfluxDB:
    - Descripción: InfluxDB es una base de datos de series temporales ideal para almacenar datos de sensores IoT.
    - Configuración:
        - Puertos:
            - 8086: Puerto para acceder a la API HTTP de InfluxDB.
        - Volúmenes:
            - `./influxdb/data/data`: Almacena los datos de InfluxDB.
            - `./influxdb/data/config`: Contiene archivos de configuración de InfluxDB.

5. Grafana:
    - Descripción: Grafana es una plataforma de análisis y visualización de datos que se utiliza para crear dashboards interactivos a partir de los datos almacenados en InfluxDB.
    - Configuración:
        - Puertos:
            - 3000: Proporciona acceso al dashboard de Grafana.
        - Volúmenes:
            - `./grafana/data`: Almacena los datos de Grafana.
        - Secrets:
            - `grafana_admin_password`: Almacena la contraseña del administrador de Grafana.

Red Bridge: Esta configuración permite la comunicación entre los contenedores dentro de la misma red de Docker.

## Configuración de Docker Compose
El archivo docker-compose.yaml define cómo se orquestan estos servicios, especificando las imágenes de Docker, los volúmenes montados, los puertos expuestos y las redes a las que están conectados. A continuación se muestra la estructura del archivo docker-compose.yaml:
```yaml
version: "3.9"
services:
  emqx:
    user: root
    build: ./emqx
    ports:
      - "18083:18083"
      - "1883:1883"
      - "8883:8883"
    volumes:
      - ./emqx/data/data:/opt/emqx/data
      - ./emqx/data/log:/opt/emqx/log
      #- ./emqx/config/emqx_auth_mysql.conf:/opt/emqx/etc/plugins/emqx_auth_mysql.conf
    network_mode: "bridge"

  influxdb:
    build: ./influxdb
    ports: 
      - "8086:8086"
    volumes:
      - ./influxdb/data/data:/var/lib/influxdb2
      - ./influxdb/data/config:/etc/influxdb2
    network_mode: "bridge"
  
  telegraf:
    build: ./telegraf
    deploy:
      restart_policy:
        condition: on-failure
        delay: 10s
        max_attempts: 20
    volumes:
      - ./telegraf/data/telegraf.conf:/etc/telegraf/telegraf.conf
    network_mode: "bridge"

  mysql:
    build: ./mysql
    ports:
      - "3306:3306"
    volumes:
      - ./mysql/data:/var/lib/mysql
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
    network_mode: "bridge"

  grafana:
    user: root
    build: ./grafana
    ports:
      - "3000:3000"
    volumes:
      - ./grafana/data:/var/lib/grafana
    secrets:
      - source: grafana_admin_password
        target: /run/secrets/admin_password
    network_mode: "bridge"
    
secrets:
  grafana_admin_password:
    file: ./grafana/secrets/grafana_admin_password
```

Este archivo se encuentra en: [docker-compose.yaml](https://github.com/danunziata/Aplicaciones_TCP_IP/blob/develop/docs/03-Proyecto_Final/proyecto/server/docker-compose.yaml).

Este entorno IoT completo permite la captura, procesamiento, almacenamiento y visualización de datos en tiempo real, facilitando la monitorización y análisis de diversos parámetros de sensores conectados.