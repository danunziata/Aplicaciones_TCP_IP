# Visualización de datos IoT con Streamlit

Esta aplicación de Streamlit permite visualizar datos de temperatura, uso de CPU, humedad, voltaje y corriente desde una base de datos InfluxDB. También muestra estadísticas relevantes para cada tipo de dato.

## Características

- Visualización interactiva de datos de sensores IoT.
- Soporte para múltiples tipos de datos: Temperatura (Raspberry Pi), Uso de CPU, Humedad, Temperatura de ambiente, Voltaje y Corriente.
- Cálculo y visualización de estadísticas: Media, Mediana, Máximo, Mínimo y Desviación estándar.

## Uso de la Aplicación

1. **Acceder a la Aplicación:**
   - Abre tu navegador web y ve a `http://localhost:8501` si la aplicación está ejecutándose localmente.
   - Si la aplicación está desplegada en un servidor, reemplaza `localhost` con la dirección IP o el nombre del dominio del servidor.

2. **Seleccionar Tipo de Dato:**
   - En la barra lateral de la aplicación, utiliza el menú desplegable para seleccionar el tipo de dato que deseas visualizar (e.g., Temperatura de CPU, Humedad de Ambiente, etc.).

3. **Visualización de Datos:**
   - Una vez seleccionado el tipo de dato, la aplicación mostrará un gráfico interactivo con los datos correspondientes.
   - Desplázate hacia abajo para ver las estadísticas básicas del tipo de dato seleccionado, incluyendo media, mediana, máximo, mínimo y desviación estándar.

4. **Cambiar Tipo de Dato:**
   - Puedes cambiar el tipo de dato seleccionado en cualquier momento utilizando el menú desplegable en la barra lateral.
   - La visualización y las estadísticas se actualizarán automáticamente para reflejar el nuevo tipo de dato seleccionado.

## Personalización del Código

El archivo `app.py` es el núcleo de la aplicación. A continuación, se explica cómo puedes modificarlo para personalizar la aplicación según tus necesidades.

### Configuración de la Conexión a InfluxDB

Modifica las variables de configuración en la parte superior del archivo `app.py` para que apunten a tu instancia de InfluxDB:

```python
url = "http://<INFLUXDB_URL>:8086"
token = "<INFLUXDB_TOKEN>"
org = "<YOUR_ORG>"
bucket = "<YOUR_BUCKET>"

Personalización de la Consulta de Datos

Las consultas a InfluxDB se realizan utilizando Flux. Puedes modificar estas consultas según 
los tipos de datos específicos que estés utilizando. Si los sensores utilizados son diferentes, asegúrate de 
ajustar las medidas y los campos en la consulta: