# Grafana
## Descripción
Grafana es una plataforma de análisis y visualización de código abierto que permite crear, explorar y compartir dashboards interactivos. En este proyecto, Grafana se utiliza para visualizar los datos de los sensores almacenados en InfluxDB, proporcionando una interfaz amigable para el monitoreo y análisis de las métricas en tiempo real.

## Dockerfile
El siguiente `Dockerfile` se utiliza para construir la imagen de Grafana, configurando las variables de entorno necesarias para la autenticación y configuración inicial:

```dockerfile
# grafana/Dockerfile
FROM grafana/grafana:8.5.3

# Configuración de las variables de entorno
ENV GF_SECURITY_ADMIN_PASSWORD__FILE=/run/secrets/admin_password

# Opcional: Si necesitas hacer alguna configuración adicional, puedes agregar más comandos aquí
```
Este archivo se encuentra en: [Dockerfile](https://github.com/danunziata/Aplicaciones_TCP_IP/blob/develop/docs/03-Proyecto_Final/proyecto/server/grafana/Dockerfile)

## docker-compose.yaml
La configuración de `docker-compose.yaml` para el servicio de Grafana se detalla a continuación. Este servicio se construye a partir del Dockerfile y utiliza volúmenes para persistir los datos y la configuración.

```yaml
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
```
Este archivo se encuentra en: [docker-compose.yaml](https://github.com/danunziata/Aplicaciones_TCP_IP/blob/develop/docs/03-Proyecto_Final/proyecto/server/docker-compose.yaml)
### Explicación de la Configuración
- user: Especifica que el contenedor se ejecuta como root.
- build: Especifica la ruta al directorio que contiene el Dockerfile de Grafana.
- ports: Expone el puerto 3000 del contenedor para que Grafana sea accesible desde el host.
- volumes: Monta el volumen necesario para persistir los datos y la configuración de Grafana.
- secrets: Utiliza un secreto para la contraseña del administrador, especificado en un archivo separado.

## Archivo de Secretos
El archivo de secretos [grafana_admin_password](https://github.com/danunziata/Aplicaciones_TCP_IP/blob/develop/docs/03-Proyecto_Final/proyecto/server/grafana/secrets/grafana_admin_password) contiene la contraseña del administrador de Grafana. Este archivo es referenciado en el `docker-compose.yaml` para configurar la contraseña del administrador de manera segura.

## Integración con InfluxDB
Grafana se conecta a InfluxDB como fuente de datos para crear dashboards y gráficos interactivos. La configuración para agregar InfluxDB como una fuente de datos se realiza a través de la interfaz de usuario de Grafana, proporcionando la URL del servicio de InfluxDB, junto con el token de autenticación, la organización y el bucket configurados en InfluxDB.

Una vez que ya se tiene el contenedor de Grafana corriendo, se debe dirigir a la dirección `localhost:3000`. Iniciamos sesión con usuario y contraseña que hayan sido declarados en el `docker-compose.yaml` y el `grafana_admin_password`respectivamente.

<div align="center">
   <img src="/images/grafana_auth.png" alt="Logo" width="500" height="500">
</div>
<br />

Luego, nos situamos en "Data Sources" en las configuraciones para cargar una base de datos de donde Grafana pueda tomar los datos. En nuestro caso es InfluxDB. Los parametros seleccionados son como se muestra en las siguientes capturas:
<div align="center">
   <img src="/images/grafana_ds1.png" alt="Logo" width="700" height="700">
</div>
<div align="center">
   <img src="/images/grafana_ds2.png" alt="Logo" width="700" height="700">
</div>
<br />

La direccion URL corresponde a la direccion IP asignada al contenedor de InfluxDB. Si no sabes cual es, puedes usar Portainer para ver cada una de las direcciones y demas caracteristicas de cada uno de los contenedores. En el siguiente link, tienes mas información: [Install Portainer](https://unrc.gitlab.io/labredes/Docker/portainer/instalacion/)

Una vez que configuras todo, das click en "Save & test" y verificas que este todo correctamente.

El siguiente paso es añadir un dashboard. En la parte izquierda de la interfaz de Grafana puedes hacerlo. Debes crear un panel nuevo donde visualizar las graficas deseadas. Se mostrara el ejemplo para monitoreo de temperatura del sensor DHT11. Despues de añadir el panel, debes editar la configuración del mismo añadiendo el código para realizar las consultas a la base de datos y generar la gráfica. En el ejemplo, se tiene lo siguiente:

```flux
from(bucket: "iotdata")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "dht11_measurement" and r._field == "DHT11_Temperature")
  |> aggregateWindow(every: 10s, fn: mean, createEmpty: false)
  |> yield(name: "mean")
```

### Explicación paso a paso
1. `from(bucket: "iotdata")`
    - Esta línea especifica el bucket de InfluxDB desde el cual se leerán los datos. En este caso, el bucket se llama iotdata.

2. `|> range(start: -1h)`
    - Este operador `|>` canaliza los datos a través de varias transformaciones.
    - `range(start: -1h)` selecciona los datos de la última hora. Esto significa que solo se considerarán los datos generados en la última hora desde el momento actual.

3. `|> filter(fn: (r) => r._measurement == "dht11_measurement" and r._field == "DHT11_Temperature")`
    - `filter` aplica un filtro a los datos seleccionados.
    - Esta línea filtra los datos para incluir solo aquellos que tienen `_measurement` igual a "dht11_measurement" y `_field` igual a "DHT11_Temperature". En otras palabras, selecciona únicamente las mediciones de temperatura del sensor DHT11.

4. `|> aggregateWindow(every: 10s, fn: mean, createEmpty: false)`
    - `aggregateWindow` agrupa los datos en ventanas de tiempo de 10 segundos (every: 10s).
    - `fn: mean` aplica la función de agregación mean (media) a cada ventana de 10 segundos.
    - `createEmpty: false` significa que no se crearán ventanas vacías si no hay datos en ese intervalo de tiempo específico.

5. `|> yield(name: "mean")`
    - `yield` devuelve el resultado de la consulta.
    - `name: "mean"` especifica el nombre de la salida, en este caso, "mean".

### ¿Qué hace en conjunto?
Esta consulta extrae las lecturas de temperatura del sensor DHT11 del bucket iotdata de InfluxDB, solo para los datos de la última hora. Luego, agrupa estos datos en intervalos de 10 segundos y calcula la media de las lecturas de temperatura en cada uno de esos intervalos de tiempo. Finalmente, la consulta devuelve estos valores medios, que pueden ser utilizados en Grafana para crear gráficos y visualizar cómo varía la temperatura medida por el sensor DHT11 a lo largo del tiempo.

De manera adicional se puede editar la estética de la gráfica para suavizar las curvas, añadir titulos a los ejes, visualizar puntos, cambiar colores y muchas otros parámetros.

La gráfica resultante es la siguiente:

<div align="center">
   <img src="/images/grafana_tempdht11.png" alt="Logo" width="500" height="500">
</div>
<br />

Para las demas mediciones es muy similar con la diferencia de que cambia `_measurement` y `_field`. Cada una de las opciones esta en "Explore" de InfluxDB.

Así es como se ve el Dashboard completo:

<div align="center">
   <img src="/images/grafana_dashboard.png" alt="Logo" width="700" height="700">
</div>
<br />


## Resumen
Esta configuración asegura que Grafana esté correctamente preparado para visualizar y analizar los datos almacenados en InfluxDB. La combinación de Docker y Docker Compose permite desplegar fácilmente el entorno completo, facilitando la gestión y escalabilidad del sistema. Con Grafana, se pueden crear dashboards detallados que permiten monitorear las métricas en tiempo real, mejorando la capacidad de análisis y toma de decisiones basada en los datos recolectados.





