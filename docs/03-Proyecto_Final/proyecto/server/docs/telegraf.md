# Telegraf
Telegraf es un agente de recolección de datos y métricas escrito en Go. Es parte de la suite de productos TICK (Telegraf, InfluxDB, Chronograf, y Kapacitor) desarrollada por InfluxData. Telegraf es altamente configurable, soporta una amplia gama de plugins de entrada, salida, procesadores y agregadores, permitiendo la recolección, el procesamiento y la transmisión de métricas de diversas fuentes a múltiples destinos.

En este proyecto, Telegraf se utiliza para recolectar datos de varios sensores (Sonoff, DHT11, y Raspy) a través del protocolo MQTT y enviar estos datos a InfluxDB para su almacenamiento y análisis.

## Dockerfile
El siguiente `Dockerfile` se utiliza para construir la imagen de Telegraf, copiando el archivo de configuración necesario dentro del contenedor:

```dockerfile
# Utiliza la imagen base de Telegraf
FROM telegraf:1.22.4

# Copia el archivo de configuración de Telegraf en el contenedor
COPY ./data/telegraf.conf /etc/telegraf/telegraf.conf

# Comando para iniciar Telegraf
CMD ["telegraf"]
```
Este archivo esta en [Dockerfile](https://github.com/danunziata/Aplicaciones_TCP_IP/blob/develop/docs/03-Proyecto_Final/proyecto/server/telegraf/Dockerfile)

## docker-compose.yaml
La configuración de `docker-compose.yaml` para el servicio de Telegraf se detalla a continuación. Este servicio se construye a partir del Dockerfile y utiliza un archivo de configuración específico. Además, se establece una política de reinicio en caso de fallos.
```yaml
telegraf:
  build: ./telegraf
  deploy:
    restart_policy:
      condition: on-failure
      delay: 10s
      max_attempts: 20
  volumes:
    - ./telegraf/data/telegraf.conf:/etc/telegraf/telegraf.conf
```
## telegraf.conf
El archivo de configuración de Telegraf define cómo y qué datos se recolectan de los sensores, así como a dónde se envían estos datos. Aquí está el contenido del archivo telegraf.conf utilizado en este proyecto:
```toml
[global_tags]
  project = "tcpipfinalproject"

[agent]
  interval = "10s"
  round_interval = true
  metric_batch_size = 1000
  metric_buffer_limit = 10000
  collection_jitter = "0s"
  flush_interval = "10s"
  flush_jitter = "0s"
  precision = "0s"
  hostname = "telegrafoutput"
  omit_hostname = false

# Input plugin for Sonoff sensor data
[[inputs.mqtt_consumer]]
  servers = ["tcp://emqx:1883"]
  topics = ["sensor/sonoff/#"]
  qos = 2
  username = "sonoff"
  password = "tcpip2024"
  data_format = "json"
  
  name_override = "sonoff_measurement"
  tag_keys = ["ENERGY"]

# Input plugin for DHT11 sensor data
[[inputs.mqtt_consumer]]
  servers = ["tcp://emqx:1883"]
  topics = ["sensor/dht11/#"]
  qos = 2
  username = "dht11"
  password = "sebacrack"
  data_format = "json"

  name_override = "dht11_measurement"
  tag_keys = ["DHT11"]

# Input plugin for Raspy sensor data
[[inputs.mqtt_consumer]]
  servers = ["tcp://emqx:1883"]
  topics = ["sensor/raspy/#"]
  qos = 2
  username = "raspy"
  password = "tcpip2024"
  data_format = "json"
  
  name_override = "raspy_measurement"
  tag_keys = ["RASPY"]

[[outputs.influxdb_v2]]
  urls = ["http://influxdb:8086"]
  token = "labtcpip-iotdata-auth-token"
  organization = "labiot2024"
  bucket = "iotdata"
```
### Explicación de la Configuración
- global_tags: Define etiquetas globales que se añadirán a todas las métricas recolectadas.
- agent: Configura el comportamiento del agente de Telegraf, incluyendo intervalos de recolección y parámetros de buffering.
- inputs.mqtt_consumer: Configura la entrada de datos desde diferentes sensores a través de MQTT. Se especifican diferentes usuarios y tópicos para cada tipo de sensor.
    - servers: La dirección del servidor MQTT (EMQX).
    - topics: Los tópicos de MQTT desde los cuales se recibirán los datos.
    - qos: El nivel de Quality of Service para la suscripción MQTT.
    - username y password: Credenciales de autenticación para el servidor MQTT.
    - data_format: El formato de los datos recibidos (en este caso, JSON).
    - name_override: Nombre con el cual se guardarán las métricas en InfluxDB.
    - tag_keys: Las claves de las etiquetas que se añadirán a las métricas.
- outputs.influxdb_v2: Configura la salida de datos hacia InfluxDB 2.x, incluyendo URL, token de autenticación, organización y bucket de destino.

Con esta configuración, Telegraf recolecta datos de los sensores Sonoff, DHT11 y Raspy, y los envía a InfluxDB para su almacenamiento y posterior visualización y análisis en Grafana.