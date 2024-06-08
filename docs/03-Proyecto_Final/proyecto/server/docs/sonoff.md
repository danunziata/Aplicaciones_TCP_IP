# Documentación para Flasheo de Sonoff POW V1 con Tasmota

## Introducción

Aquí, documentaremos el proceso de flasheo de un dispositivo Sonoff POW V1 con Tasmota para que pueda enviar datos al servidor mediante MQTT.

## ¿Qué es un Sonoff?

Sonoff es una línea de dispositivos de automatización del hogar fabricada por ITEAD. Estos dispositivos permiten controlar electrodomésticos y otros dispositivos eléctricos de manera remota. El Sonoff POW V1 es un interruptor inteligente que también mide el consumo de energía.

<p align="center">
  <img src="/images/sonoff.jpg" alt="Sonoff" width="400"/>
</p>

## ¿Qué es Tasmota?

Tasmota es un firmware de código abierto para dispositivos basados ​​en chipset Espressif ESP8266, ESP32, ESP32-S o ESP32-C3 fue creados y es mantenidos por Theo Arends.

<p align="center">
  <img src="/images/tasmotalogo.svg" alt="Tasmota" width="200"/>
</p>

Proporciona soporte para MQTT, automatización, reglas y una interfaz web para controlar dispositivos. Utilizar Tasmota en lugar del firmware original de Sonoff permite integrar el dispositivo en nuestro entorno IoT de manera eficiente y flexible.

## ¿Por qué utilizar Tasmota?

El firmware original de Sonoff no incluye soporte para MQTT, una característica esencial para nuestro proyecto. Flashear Tasmota en el Sonoff POW V1 nos permite:

- Integrar el dispositivo con nuestro servidor MQTT.
- Utilizar funciones avanzadas de control y monitoreo.
- Acceder a una interfaz web para configuración y control.

## Pasos para Flashear Tasmota

### 1. Conexión Física con el Dispositivo

Para flashear Tasmota en el Sonoff POW V1, primero debemos conectarnos al ESP8266 de manera serial. La forma más sencilla es utilizando un adaptador USB a TTL. A continuación, se muestra el esquema de conexión.

**IMPORTANTE:** No conectar el dispositivo a 220V durante este proceso.

<p align="center">
  <div style="display: inline-block; margin: 0 10px;">
    <img src="/images/conexion.png" alt="Conexión" width="300"/>
  </div>
  <div style="display: inline-block; margin: 0 10px;">
    <img src="/images/tipodeconexion.png" alt="TipodeConexión" width="300"/>
  </div>
</p>

1. Conectar los cables según el esquema.
2. Mantener presionado el botón del Sonoff mientras se conecta el USB a la PC para iniciar en modo booteo. La luz del Sonoff debe permanecer apagada si está en modo booteo correctamente.

### 2. Aprovisionamiento de la Computadora

En la computadora que se va a utilizar para flashear el dispositivo, instalar los siguientes paquetes:

```bash
sudo apt install pipx
pipx install tasmotizer
```

Asegurarse de que el usuario tenga los permisos necesarios para utilizar los puertos seriales:

```bash
cat /etc/group | grep ${USER}
cat /etc/group | grep tty
```

Si el usuario no aparece en el grupo `tty`, agregarlo:

```bash
sudo usermod -a -G tty ${USER}
```

Verificar nuevamente:

```bash
cat /etc/group | grep tty
```

### 3. Ejecución de Tasmotizer

Ejecutar Tasmotizer con el siguiente comando:

```bash
tasmotizer.py
```

Se necesitará el archivo `tasmotiza.bin`, que es el firmware a instalar. Este puede descargarse de la [página oficial de Tasmota](https://github.com/tasmota/install/tree/firmware/firmware/release) (se recomienda instalar `tasmotiza.bin`).

<p align="center">
  <img src="/images/tasmotizerdashboard.png" alt="Tasmota" width="300"/>
</p>

Importar el firmware en Tasmotizer y, una vez reconocido y elegido el USB, hacer clic en "TASMOTIZE!".

Sí está funcionando correctamente, aparecerá algo similar a lo siguiente.

<p align="center">
  <img src="/images/comandostasmotizer.png" alt="Tasmota" width="400"/>
</p>

Una vez completado este proceso, el dispositivo estará correctamente flasheado.

### 4. Configuración del Sonoff

Una vez flasheado, el dispositivo creará una red WiFi. Conectarse a esta red (por ejemplo, "tasmota-161167916") con un dispositivo móvil y acceder a la IP `192.168.4.1`. Configurar la red WiFi a la que el dispositivo debe conectarse. Una vez conectado correctamente, el dispositivo mostrará la IP asignada por el router.

<p align="center">
  <img src="/images/config_red.jpeg" alt="tasmotaprimerconfiguracion" width="200"/>
</p>

Conectarse a la red configurada y acceder a la IP proporcionada por Tasmota para ver el dashboard principal.

<p align="center">
  <img src="/images/dashboardprincipal.png" alt="Tasmota" width="700"/>
</p>

FALTA AGREGAR CONFIGURACIÓN MÓDULO SONOFF, MQTT Y TIMER
