# Sobre este proyecto

<p align="center">
  <img src="/images/diaginicial.png" alt="Diagrama" width="600"/>
</p>
(esto es la parte del servidor, todavía no está terminado)
## Introducción

El presente proyecto tiene como objetivo construir un entorno de trabajo integrado para la recolección, almacenamiento, análisis y visualización de datos provenientes de dispositivos IoT (Internet of Things). Utilizando una arquitectura basada en contenedores y tecnologías de código abierto, se busca facilitar la gestión eficiente y segura de grandes volúmenes de datos en tiempo real. A continuación, se presenta una descripción detallada de cada componente utilizado en este proyecto y su papel dentro del sistema.

## Marco Teórico

### Internet of Things (IoT)

<div align="center">
   <img src="/images/iot.png" alt="Logo" width="200" height="200">
</div>
<br />

El Internet de las Cosas (IoT) se refiere a la interconexión de dispositivos físicos a través de internet, permitiendo que estos recopilen y compartan datos. Estos dispositivos incluyen sensores, actuadores y otros sistemas integrados que pueden comunicarse entre sí y con sistemas centrales para automatizar y optimizar diversos procesos en aplicaciones industriales, domésticas, de salud, entre otras.

### MQTT (Message Queuing Telemetry Transport)

<div align="center">
   <img src="/images/mqtt.png" alt="Logo" width="500" height="500">
</div>
<br />

MQTT es un protocolo de mensajería ligero y de bajo ancho de banda ideal para la comunicación M2M (Machine-to-Machine) y IoT. Utiliza un modelo de publicación/suscripción que permite una transmisión eficiente de datos entre dispositivos y servidores, siendo especialmente útil en redes con ancho de banda limitado y alta latencia.

## Componentes del Proyecto

- **EMQX**
  <div align="center">
     <img src="/images/emqx_log.png" alt="Logo" width="200" height="200">
  </div>
  <br />

  EMQX es un broker de mensajes MQTT de alto rendimiento, escalable y distribuido. Está diseñado para manejar millones de conexiones concurrentes, proporcionando una plataforma robusta para la comunicación IoT.

  En este proyecto, EMQX se encarga de gestionar la comunicación entre los dispositivos IoT y el sistema central. Actúa como intermediario para la transmisión de mensajes, garantizando que los datos enviados por los dispositivos lleguen de manera eficiente y segura a los servidores y aplicaciones correspondientes.

- **Telegraf**
  <div align="center">
     <img src="/images/telegraf.png" alt="Logo" width="200" height="200">
  </div>
  <br />
  Telegraf es un agente de recopilación de métricas desarrollado por la empresa InfluxData. Es parte del conjunto de herramientas de InfluxDB, que también incluye InfluxDB (base de datos de series temporales), Chronograf (interfaz de usuario para la visualización) y Kapacitor (procesamiento de datos en tiempo real).
  
  La configuración de Telegraf se realiza a través de un archivo de configuración (generalmente telegraf.conf), lo que permite una fácil personalización.

  Tiene un alto grado de compatibilidad, ya que puede integrarse con varios sistemas de almacenamiento y visualización de datos, como InfluxDB, Graphite, OpenTSDB, Prometheus, Datadog, AWS CloudWatch, entre otros.

- **InfluxDB**
  <div align="center">
     <img src="/images/influxdb.png" alt="Logo" width="200" height="200">
  </div>
  <br />

  InfluxDB es una base de datos de series temporales optimizada para manejar grandes volúmenes de datos generados por sensores y dispositivos IoT. Está diseñada para la ingestión rápida de datos, consulta de series temporales y retención de datos.

- **MySQL**
  <div align="center">
     <img src="/images/mysql.png" alt="Logo" width="200" height="200">
  </div>
  <br />

  MySQL es una base de datos relacional ampliamente utilizada para almacenar datos estructurados. Su popularidad y soporte para múltiples lenguajes de programación lo convierten en una opción sólida para muchas aplicaciones.

  En este proyecto, MySQL se utiliza para almacenar datos relacionados con la autenticación y autorización de usuarios y dispositivos. Esto incluye información sobre usuarios, contraseñas hasheadas y permisos de acceso, facilitando la gestión segura del acceso al sistema.

- **Grafana**
  <div align="center">
     <img src="/images/grafana.png" alt="Logo" width="200" height="200">
  </div>
  <br />

  Grafana es una plataforma de análisis y monitoreo que permite la creación de paneles interactivos y visualizaciones en tiempo real. Soporta una amplia variedad de fuentes de datos, incluyendo InfluxDB, y proporciona herramientas avanzadas para el análisis de datos.
  
  Esto permite a los usuarios monitorear el rendimiento y el estado de los dispositivos IoT, así como realizar análisis detallados de los datos recolectados.

- **Streamlit**
  <div align="center">
     <img src="/images/streamlit.png" alt="Logo" width="200" height="200">
  </div>
  <br />

  Streamlit es una biblioteca de Python que permite la creación de aplicaciones web interactivas de manera rápida y sencilla. Está diseñada para el desarrollo de aplicaciones de análisis de datos y es ideal para la creación de herramientas personalizadas de visualización y procesamiento de datos.

  En este proyecto, Streamlit se utiliza para desarrollar aplicaciones web que capturan y procesan datos de los dispositivos IoT. Estas aplicaciones permiten a los usuarios interactuar con los datos de manera intuitiva y realizar análisis personalizados según sus necesidades.

## Finalidad del Proyecto

El propósito de este proyecto es proporcionar una solución completa y escalable para la gestión de datos de dispositivos IoT, abarcando desde la recolección y almacenamiento hasta el análisis y visualización de los datos. Este entorno integrado facilita la automatización y optimización de procesos en diversas aplicaciones IoT, proporcionando una plataforma robusta y flexible para la gestión eficiente de grandes volúmenes de datos en tiempo real.

## Arquitectura del Sistema

<div align="center">
   <img src="/images/conteiner.png" alt="contenedores" width="300" height="300">
</div>
<br />
El sistema está diseñado utilizando una arquitectura basada en contenedores, lo que permite una fácil implementación y escalabilidad. Cada componente del sistema se despliega en un contenedor independiente utilizando Docker, y se gestionan colectivamente utilizando Docker Compose.

## Estructura del Proyecto

La estructura de directorios del proyecto es la siguiente:

```plaintext
├── docker-compose.yaml
├── emqx
│   ├── config
│   │   └── emqx_auth_mysql.conf
│   └── Dockerfile
├── grafana
│   ├── Dockerfile
│   ├── grafana.conf
│   └── secrets
│       └── grafana_admin_password
├── influxdb
│   └── Dockerfile
├── mysql
│   ├── Dockerfile
│   └── init.sql
├── seguridad
│   └── certs
│       ├── ca.key
│       ├── ca.pem
│       ├── client.csr
│       ├── client.key
│       ├── client.pem
│       ├── emqx.csr
│       ├── emqx.key
│       ├── emqx.pem
│       └── openssl.cnf
├── streamlitapp
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
└── telegraf
    ├── data
    │   └── telegraf.conf
    └── Dockerfile
```

Use the `getting_started.md` to get started.
