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

El firmware original de Sonoff no incluye soporte configurable para MQTT, una característica esencial para nuestro proyecto. Flashear Tasmota en el Sonoff POW V1 nos permite:

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

Lo primero que debemos hacer es configurar en base a todos los templates que tiene cargado el firmware de Tasmota, escoger el nuestro. en este caso debemos ir a "Configuration" donde observaremos lo siguiente:

<p align="center">
  <img src="/images/sonoff_configurationpanel.png" alt="Tasmota" width="200"/>
</p>

Ingresamos a **Configure Module** y luego elegimos nuestro dispositivo, en este caso: "Sonoff Pow (6)"

<p align="center">
  <img src="/images/sonoff_moduleparameters.png" alt="Tasmota" width="200"/>
</p>

Luego, debemos configurar los parámetros de mqtt.

<p align="center">
  <img src="/images/sonoff_configure_mqtt.png" alt="Tasmota" width="200"/>
</p>

Opcionalmente, en el apartado logging podemos configurar cada cuanto tiempo enviamos la información al servidor en la parte del Telemetry period (como mínimo Tasmota permite 5).

<p align="center">
  <img src="/images/sonoff_logging.png" alt="Tasmota" width="200"/>
</p>

Si configuramos todo correctamente, debemos ver lo siguiente en el menú principal del Tasmota y en la parte de Console podemos ver los logs de cómo se envian los datos.

<p align="center">
  <div style="display: inline-block; margin: 0 10px;">
    <img src="/images/sonoff_console.png" alt="Conexión" width="500"/>
  </div>
  <div style="display: inline-block; margin: 0 10px;">
    <img src="/images/sonoff_configured.png" alt="TipodeConexión" width="150"/>
  </div>
</p>

## Calibración

### Preparativos

**Requisitos:**

1. 2 multímetros AC calibrados.
2. Una carga de potencia conocida con un factor de potencia cercano a 1 (por ejemplo, una bombilla incandescente de 60W).

**Advertencias:**

- No usar dispositivos de conmutación como lámparas LED o equipos de computadora.
- No usar dispositivos inductivos o capacitivos como motores.

### Configuración

Conecta la carga (por ejemplo, una bombilla incandescente de 60W) al dispositivo Sonoff y conecta en paralelo un voltímetro y en continuo un amperímetro. Abre dos ventanas del navegador con la interfaz web de Tasmota: una ventana en la consola y otra en la página principal para ver los datos de telemetría de energía. Enciende el dispositivo y asegúrate de que la carga también esté encendida. Espera unos segundos para que las lecturas se estabilicen.

### Procedimiento de Calibración

**Lectura de Potencia**

Indicar al Sonoff la potencia que tendría que estar consumiendo, por ejemplo 60W (por eso es super importante realizar esta calibración en un entorno donde no haya cargas inductivas para que sea lo más preciso posible.)

```
PowerSet <valor de potencia>
```

Ejemplo para una bombilla de 60W:

```
PowerSet 60
```

**Lectura de Voltaje**

-Verifica la lectura de voltaje.

-Ajusta el offset de voltaje si es necesario usando el comando:

```
VoltageSet <valor de voltaje>
```

Sustituye `<valor de voltaje>` por el valor leído en el multímetro.

**Lectura de Corriente**:

-Verifica la lectura de corriente.

-Ajusta el offset de corriente si es necesario usando el comando:

```
CurrentSet <valor de corriente>
```

Sustituye `<valor de corriente>` por el valor leído en el multímetro.

Con esto, el Sonoff debería mostrar valores muy cercanos a los medidos por el amperímetro y el voltímetro, indicando que ha sido calibrado correctamente.
