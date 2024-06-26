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

