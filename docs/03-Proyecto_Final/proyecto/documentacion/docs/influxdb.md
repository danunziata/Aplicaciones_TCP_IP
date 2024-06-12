# InfluxDB
## Descripción
InfluxDB es una base de datos de series temporales de alto rendimiento desarrollada por InfluxData. Está diseñada para manejar grandes volúmenes de datos de eventos en tiempo real y se utiliza comúnmente para el monitoreo, análisis y almacenamiento de datos provenientes de sensores, registros de aplicaciones, y métricas de sistemas.

En este proyecto, InfluxDB se utiliza para almacenar los datos recolectados de varios sensores (Sonoff, DHT11 y Raspy) mediante Telegraf. Los datos almacenados en InfluxDB pueden ser posteriormente visualizados y analizados en Grafana.

## Dockerfile
El siguiente `Dockerfile` se utiliza para construir la imagen de InfluxDB, configurando los parámetros iniciales necesarios para la base de datos:

```dockerfile
# influxdb/Dockerfile
FROM influxdb:2.2.0-alpine

ENV DOCKER_INFLUXDB_INIT_MODE=setup
ENV DOCKER_INFLUXDB_INIT_USERNAME=labiot
ENV DOCKER_INFLUXDB_INIT_PASSWORD=labiot2024
ENV DOCKER_INFLUXDB_INIT_ORG=labiot2024
ENV DOCKER_INFLUXDB_INIT_BUCKET=iotdata
ENV DOCKER_INFLUXDB_INIT_RETENTION=1w
ENV DOCKER_INFLUXDB_INIT_ADMIN_TOKEN=labtcpip-iotdata-auth-token
```

Este archivo se encuentra en: [Dockerfile](https://github.com/danunziata/Aplicaciones_TCP_IP/blob/develop/docs/03-Proyecto_Final/proyecto/server/influxdb/Dockerfile)
## docker-compose.yaml
La configuración de `docker-compose.yaml` para el servicio de InfluxDB se detalla a continuación. Este servicio se construye a partir del Dockerfile y utiliza volúmenes para persistir los datos y la configuración.

```yaml
influxdb:
  build: ./influxdb
  ports: 
    - "8086:8086"
  volumes:
    - ./influxdb/data/data:/var/lib/influxdb2
    - ./influxdb/data/config:/etc/influxdb2
```
Este archivo se encuentra en: [docker-compose.yaml](https://github.com/danunziata/Aplicaciones_TCP_IP/blob/develop/docs/03-Proyecto_Final/proyecto/server/docker-compose.yaml)

### Explicación de la Configuración
- build: Especifica la ruta al directorio que contiene el Dockerfile de InfluxDB.
- ports: Expone el puerto 8086 del contenedor para que InfluxDB sea accesible desde el host.
- volumes: Monta los volúmenes necesarios para persistir los datos y la configuración de InfluxDB.

## Integración con Telegraf
Telegraf está configurado para enviar los datos recolectados a InfluxDB. A continuación, se muestra la configuración relevante en telegraf.conf:

```toml
[[outputs.influxdb_v2]]
  urls = ["http://influxdb:8086"]
  token = "labtcpip-iotdata-auth-token"
  organization = "labiot2024"
  bucket = "iotdata"
```

### Explicación de la Configuración
- urls: La URL del servicio de InfluxDB.
- token: El token de autenticación para InfluxDB.
- organization: La organización en InfluxDB a la que se enviarán los datos.
- bucket: El bucket en InfluxDB donde se almacenarán los datos.

## Dashboard
En primer lugar, para acceder a la interfaz de InfluxDB es encesario autenticarse con usuario y contraseña que se haya declarado en las varaibles de entorno del Dockerfile.

<div align="center">
   <img src="/images/influxdb_auth.png" alt="Logo" width="500" height="500">
</div>
<br />

Debido a que Telegraf envia los datos a InfluxDB no es necesario cargar una nueva fuente de datos. Las fuentes de las que recibe son los tres sensores.

Luego de iniciar sesión, en la parte izquierda de la interfaz web, se debe acceder a "Explore" si se desean ver las graficas, donde se puede filtrar con "_measurement" las medidas de cada sensor y luego algun campo en específico. Por ejemplo:

<div align="center">
   <img src="/images/influxdb_cap1.png" alt="Logo" width="500" height="500">
</div>
<br />

Es de gran importancia mencionar que se debe seleccionar el bucket que haya sido descrito en las variables de entorno, el cual, en este caso, es "iotdata"

## Resumen
Esta configuración asegura que InfluxDB esté correctamente preparado para recibir y almacenar datos de sensores enviados a través de Telegraf. La combinación de Docker y Docker Compose permite desplegar fácilmente el entorno completo, facilitando la gestión y escalabilidad del sistema. Con los datos almacenados en InfluxDB, se pueden crear dashboards detallados en Grafana para la visualización y análisis de las métricas en tiempo real.