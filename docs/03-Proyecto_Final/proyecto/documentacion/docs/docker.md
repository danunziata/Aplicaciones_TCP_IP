# Docker Compose

<div align="center">
   <img src="/images/dockerlogo.png" alt="Logo" width="300" height="300">
</div>
<br />

Docker Compose es una herramienta para definir y ejecutar aplicaciones Docker multi-contenedor. Con Docker Compose, se usar un archivo YAML para configurar los servicios de la aplicación, como EMQX, Telegraf, InfluxDB, etc. Luego, con un solo comando (docker-compose up), se puede crear e iniciar todos los contenedores definidos en el archivo y con ciertas configuraciones.

**Ventajas de Docker Compose respecto a Dockerfile:**

- Gestión Multi-Contenedor:
    - Dockerfile: Define cómo construir una imagen de Docker para un solo contenedor.
    - Docker Compose: Permite definir y ejecutar múltiples contenedores que interactúan entre sí. Ideal para aplicaciones complejas que requieren múltiples servicios.

- Simplificación del Proceso de Desarrollo:
    - Dockerfile: Se necesita ejecutar manualmente los comandos para construir y ejecutar cada contenedor.
    - Docker Compose: Con un solo comando (docker-compose up), se puede levantar toda la aplicación, incluidos todos los servicios necesarios.
- Redes y Volúmenes Automatizados:
    - Dockerfile: Se necesita configurar manualmente las redes y volúmenes.
    - Docker Compose: Facilita la configuración y gestión de redes y volúmenes, permitiendo la comunicación automática entre contenedores y la persistencia de datos.
- Entorno Reproducible:
    - Dockerfile: Puede ser parte de un flujo de trabajo más amplio pero requiere scripts adicionales para manejar múltiples contenedores.
    - Docker Compose: Proporciona un entorno de desarrollo completo y reproducible con la misma configuración para todos los desarrolladores, facilitando la colaboración.
- Escalabilidad:
    - Dockerfile: Puedes construir y ejecutar contenedores individuales.
    - Docker Compose: Permite escalar servicios especificando el número de instancias que deseas ejecutar (docker-compose up --scale).

En este proyecto, se combinan Dockerfiles con Docker Compose para permitir definir y orquestar múltiples servicios en un entorno consistente. Cada servicio tiene su propio Dockerfile que define cómo se construye su imagen de contenedor, y docker-compose.yml especifica cómo se deben construir e interactuar estos contenedores.

<div align="center">
   <img src="/images/dockercompose.png" alt="Logo" width="500" height="500">
</div>
<br />

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

  influxdb:
    build: ./influxdb
    ports: 
      - "8086:8086"
    volumes:
      - ./influxdb/data/data:/var/lib/influxdb2
      - ./influxdb/data/config:/etc/influxdb2
  
  telegraf:
    build: ./telegraf
    deploy:
      restart_policy:
        condition: on-failure
        delay: 10s
        max_attempts: 20
    volumes:
      - ./telegraf/data/telegraf.conf:/etc/telegraf/telegraf.conf
      - ./seguridad/certs/:/etc/telegraf/certs/

  mysql:
    build: ./mysql
    ports:
      - "3306:3306"
    volumes:
      - ./mysql/data:/var/lib/mysql
      - ./mysql/init.sql:/docker-entrypoint-initdb.d/init.sql

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

  streamlit:
    build: ./streamlitapp
    ports:
      - "8501:8501"
    environment:
      - INFLUXDB_URL=http://influxdb:8086
      - INFLUXDB_TOKEN=labtcpip-iotdata-auth-token
      - INFLUXDB_ORG=labiot2024
      - INFLUXDB_BUCKET=iotdata
secrets:
  grafana_admin_password:
    file: ./grafana/secrets/grafana_admin_password
```

Este archivo se encuentra en: [docker-compose.yaml](https://github.com/danunziata/Aplicaciones_TCP_IP/blob/develop/docs/03-Proyecto_Final/proyecto/server/docker-compose.yaml).

Este entorno IoT completo permite la captura, procesamiento, almacenamiento y visualización de datos en tiempo real, facilitando la monitorización y análisis de diversos parámetros de sensores conectados.