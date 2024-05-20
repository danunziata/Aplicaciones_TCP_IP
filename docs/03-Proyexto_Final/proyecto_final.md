# Proyecto Final Aplicaiciones TCP IP 2024 -  "Despliegue de una Plataforma IoT para la Gestión y Visualización de Datos de Series Temporales"

## Resumen
Este proyecto se centra en el desarrollo de la plataforma del lado del servidor para la gestión y visualización de datos de series temporales en entornos IoT. La implementación de referencia proporcionará una base sólida para la expansión futura de la plataforma hacia proyectos más específicos en ambientes productivos. Se enfocará en la captura, almacenamiento y presentación eficientes de datos clave, como temperatura, humedad, corriente y tensión, utilizando tecnologías específicas para garantizar su funcionamiento óptimo en tiempo real. Este enfoque permitirá construir sobre una base sólida y escalable, facilitando la adaptación a diferentes casos de uso y requisitos en el futuro.

## Introducción
El desarrollo de este prototipo tiene como objetivo validar la viabilidad técnica y funcional de una solución IoT para la gestión de datos de series temporales. Se busca capturar datos relevantes de sensores y dispositivos, almacenarlos de manera eficiente en una base de datos de series temporales y visualizarlos en tiempo real mediante paneles interactivos. El prototipo servirá como experiencia inicial para futuras implementaciones en entornos reales.

## Fases del Proyecto:

### Requerimientos
En esta fase se identifican y documentan los requerimientos del prototipo. Se establecen los siguientes requerimientos:

- Captura de datos de temperatura, humedad, corriente y tensión.
- Almacenamiento eficiente de datos en una base de datos de series temporales.
- Visualización en tiempo real de datos mediante dashboards interactivos.
- Seguridad en la comunicación MQTT entre dispositivos y la plataforma.

### Diseño
En esta fase se especifica la arquitectura de la solución y se diseñan los paneles de visualización. Aspectos clave del diseño incluyen:

- Arquitectura de comunicación entre dispositivos y plataforma.
- Especificación de la base de datos InfluxDB y el broker MQTT EMQX.
- Diseño de los dashboards interactivos en Grafana y Streamlit.
- Planificación de la seguridad en la comunicación MQTT.

### Implementación o Desarrollo
Durante esta fase se lleva a cabo la implementación del prototipo según el diseño establecido. Se realizan las siguientes tareas:

- Configuración del broker MQTT EMQX y la base de datos InfluxDB.
- Desarrollo de scripts en Python y MicroPython para la captura y envío de datos.
- Integración de Telegraf para la recolección y almacenamiento de datos en InfluxDB.
- Creación de los dashboards interactivos en Streamlit y Grafana.

### Pruebas o Ensayos
Se realizan pruebas exhaustivas para validar el funcionamiento del prototipo. Se llevan a cabo las siguientes actividades:

- Pruebas de integración entre los componentes del sistema.
- Verificación de la captura y almacenamiento correcto de datos.
- Validación de la visualización de datos en los dashboards.
- Evaluación de la seguridad en la comunicación MQTT.

### Mantenimiento
La fase de mantenimiento asegura el funcionamiento óptimo del prototipo a lo largo del tiempo. Se incluyen las siguientes acciones:

- Implementación de métricas de monitoreo para detectar posibles fallos.
- Monitoreo continuo del rendimiento y la disponibilidad de los servicios.
- Actualización y mejora de los componentes del prototipo según sea necesario.

## Consideracines
El proyecto se realizará utilizando contenedores, lo que permitirá una fácil portabilidad y escalabilidad del entorno de desarrollo. Se implementará el despliegue del stack con Docker Compose para simplificar el proceso de configuración y gestión de los servicios. Además, toda la documentación del proyecto se realizará en formato Markdown (Markdown Documentation), proporcionando una forma clara y concisa de documentar el proceso de desarrollo y facilitando la colaboración entre los miembros del equipo.

### Referencia de estructura del repositorio



```sh
proyecto/
├── docs/
│   ├── file.md
│   ├── file2.md
│   └── folder/
│       ├── file.md
│       └── file2.md
├── server/
│   ├── README.md
│   ├── docker-compose.yml
│   ├── influxdb/
│   │   ├── Dockerfile
│   │   └── influxdb.conf
│   ├── emqx/
│   │   ├── Dockerfile
│   │   └── emqx.conf
│   ├── telegraf/
│   │   ├── telegraf.conf
│   │   └── Dockerfile
│   ├── grafana/
│   │   ├── grafana.conf
│   │   └── Dockerfile
│   └── streamlitapp/
│       ├── data_capture.py
│       └── data_processing.py
├── clients/
│   ├── client1/
│   │   ├── README.md
│   │   └── src/
│   │       ├── main.py
│   │       └── utils.py
│   └── client2/
│       ├── README.md
│       └── src/
│           ├── main.py
│           └── utils.py
├── .gitignore
├── LICENSE
└── README.md
```