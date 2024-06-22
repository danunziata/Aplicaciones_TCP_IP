# <p align=center> Raspberry 2 Pi - Medicion de temperatura y uso de CPU <p>

<p align="center">
  <img src="./images/raspy2logo.png" width="200"/>
</p>

## Introduccion

A continuacion se detalla brevemente como realizar mediciones de la temperatura y el uso (%) del CPU del dispositivo Raspberry Pi 2 utilizando un script de Python junto con sus librerias y luego publicar dichos datos en un servidor MQTT.

## Que es Raspberry Pi?

Raspberry Pi es una computadora compacta, util si se necesita planificar e implementar un "smart home". La Raspberry Pi cuenta con todos los beneficios que posee una computadora de escritorio: conexion inalambrica a internet, puertos HDMI para conectar monitores, y puertos USB para conectar todo tipo de accesorios, asi como tambien una amplia capacidad de procesamiento y memoria RAM para utilizar en actividades cotidianas. 

## El sistema operativo Raspberry Pi OS

Para poder funcionar, las Raspberry Pi requieren un sistema operativo previamente instalado en su memoria microSD. El sistema operativo funcional utilizado en estos dispositivos es el Raspberry Pi OS (previamente Raspbian). Para instalar el sistema operativo, se puede utilizar el software oficial Raspberry Pi Imager, junto con su imagen oficial. [(Descargar Raspberry Pi OS)](https://www.raspberrypi.com/software/) 

## Realizar mediciones de temperatura y uso (%) de CPU en Raspberry Pi 2

*(El resumen de pasos y comandos necesarios para implementar y realizar mediciones se encuentra detallado en el Anexo, al final de este documento)*

Para poder realizar mediciones de temperatura y porcentaje de uso de CPU, es necesario contar con python3 instalado dentro de la Raspberry Pi 2. Este viene instalado por defecto al instalar el sistema operativo dentro de la memora microSD. 
Por otro lado, las liberias de Python  necesarias para poder ejecutar el script  son las siguientes:

- psutil
- json
- paho MQTT

#### Libreria "psutil"

La libreria psutil (python system and process utilities) es una libreria multiplataforma utilizada para recolectar informacion sobre procesos en ejecucion y sobre utilizacion del sistema (CPU, memoria, discos, redes, sensores) en Python. Es util principalmente para realizar monitoreo, perfilado, limitacion de recursos y administracion de procesos en ejecucion del sistema.

#### Libreria "JSON"

JSON (JavaScript Object Notation) es un formato ligero de sintaxis utilizado para el intercambio de datos inspirado en la notacion literal de objetos de JavaScript. A pesar de que este formato proviene de JavaScript, su notacion y sintaxis no esta limitada a este lenguaje unicamente. Mediante la libreria JSON se podra estructurar el formato de la informacion para luego enviarla a travez de una publicacion MQTT, lo que facilita su interpretacion y posterior procesado del lado del receptor. 

#### Libreria "paho MQTT"

Mediante la libreria paho MQTT se permite la conexion de un cliente a un broker MQTT para publicar mensajes y para subscribirse a distintos temas o "topics" los cuales permiten recibir informacion sobre mensajes publicados en estos temas. Tambien otorga funciones adicionales para permitir publicaciones a un servidor MQTT de manera directa y sencilla. 

### Descripcion del codigo utilizado para la obtencion de las metricas

Tras importar las librerias necesarias para el funcionamiento del script, se definen las siguientes constantes, que se utilizaran para realizar la conexion al servidor MQTT:

`broker`: Direccion IP en la que se encuentra el broker
`port`: Puerto en el que se encuentra el servicio del broker MQTT
`topic`: Nombre del topic al que se conectara y se realizaran las publicaciones
`client_id`: Nombre identificador del dispositivo
`username`: Nombre de usuario utilizado para la autentificacion dentro del servidor MQTT
`password`: Contraseña utilizada para la autentificacion dentro del servidor MQTT

Ademas, se deben especificar la ruta completa en la cual se encuentran los tres certificados necesarios para realizar una encriptacion SSL en el contenido de la comunicacion entre el dispositivo y el servidor MQTT. Para ello, modificar las variables `key`, `ca` y `cert` con las ubicaciones correspondientes de cada certificado.

###### Conexion al servidor MQTT:

Para realizar la conexion al servidor MQTT se define la funcion `connect_mqtt()` la cual realizara un intento de conexion al servidor utilizando la informacion proporcionada al comienzo del script, tal como direccion IP, puerto, usuario, contraseña y certificacion. En caso de fallar se imprime el mensaje de error correspondiente. En caso de que la conexion se realiza de manera exitosa, se regresa el objeto `client` el cual contiene toda la informacion del cliente.

*(Nota: en caso de contar con una version de paho-mqtt inferior a la version 2.0.0, la asignacion al objeto `client` debe contener el `client_id` unicamente, no se debe especificar el metodo `mqtt.CallbackAPIVersion.VERSION1`)*

```bash
def connect_mqtt():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1,client_id)
    client.username_pw_set(username, password)
    
    client.tls_set(certfile=cert, ca_certs=ca, keyfile=key, cert_reqs=ssl.CERT_REQUIRED)
    client.on_connect = on_connect
    
    client.connect(broker, port)
    
    client.callback_connect = on_connect
    
    return client
```

##### Lectura de datos dentro de la Raspberry Pi 2

Mediante la funcion `get_cpu_temp()` se realiza la lectura de la temperatura del CPU de la Raspberry Pi 2. Para ello se utiliza el metodo `sensor_temperatures()` de la libreria psutil y se lo regresa como un valor entero.

```bash
def get_cpu_temp():
    temp = psutil.sensors_temperatures()['cpu_thermal'][0].current
    return temp
```

##### Publicacion de mensajes al servidor MQTT

Mediante la funcion `publish()` se realiza una publicacion periodica de datos dentro del servidor MQTT. El periodo se encuentra especificado en segundos dentro de la funcion `time.sleep(#)`. Luego, utilizando el metodo `dumps` de la libreria json, se forma el mensaje en formato JSON que luego sera publicado en el servidor MQTT. Para obtener las metricas que seran publicadas en el mensaje se utiliza el metodo `cpu_percent()` de la libreria psutil y la funcion `get_cpu_temp()` descripta anteriormente. En caso de fallar la publicacion en el servidor, se imprime el mensaje de error correspondiente. 

```bash
def publish(client):
    msg_count = 0
    while True:
        #Publicaciones cada 3 segundos
        time.sleep(3)
        msg = json.dumps({'id': client_id, 'cpu_usage': psutil.cpu_percent(), 'cpu_temp': get_cpu_temp()})
        result = client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print(msg)
        else:
            print("Error al publicar el mensaje")
        msg_count += 1
```        

##### Funcion Wrapper

Dentro de la funcion `run()` se ejecutan todas las funciones mencionadas anteriormente. Aqui se realiza la conexion del cliente al servidor, y se realizan publicaciones periodicas con los datos de la Raspberry Pi 2

```bash
def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
```

---

## Anexo - Monitoreo de temperatura y uso de CPU dentro de Raspberry Pi 2

Para poder compilar y ejecutar el codigo anteriormente explicado, es necesario contar con una Raspberry Pi 2 que utilize un sistema operativo Raspberry PI OS. Ademas, esta debe contar con Python instalado (Se instala por defecto al instalar Raspberry PI OS). 

## Requisitos previos

- Instalar python3 en caso de que sea neceasrio, utilizando el siguiente comando dentro de la terminal:

`sudo apt install python3`

- Instalar la libreria de python **psutil** utilizando el siguiente comando dentro de la terminal:

`sudo apt install python3-psutil`

- Instalar la libreria de python **paho-MQTT** utilizando el siguiente comando dentro de la terminal:

`sudo apt install python3-paho-mqtt`

## Implementacion y ejecucion

Modificar los valores de las variables `broker`, `port`, `topic`, `client_id`, `username` y `password` dentro del archivo python `raspymain.py` con los valores correspondientes. Agregar ademas la ruta completa de los certificados en las variables `key`, `ca` y `cert`.
Para ejecutar el script, dentro de una terminal, situarse en la misma direccion en la que se encuentra el archivo antes mencionado. Luego, ejecutar el script utilizando el siguiente comando:

`python3 raspymain.py`