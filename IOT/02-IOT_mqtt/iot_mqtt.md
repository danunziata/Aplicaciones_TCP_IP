
# MQTT (Message Queue Telemetry Transport)

Inicialmente, MQTT fue inventado y desarrollado por IBM a finales de los 90. Su aplicación original era vincular sensores en oleoductos de petróleo a satélites. Tal como sugiere su nombre, se trata de un protocolo de mensajería con soporte para la comunicación asíncrona entre las partes. Un protocolo de sistema de mensajes asíncrono separa al emisor y al receptor del mensaje tanto en el tiempo como en el espacio y, por lo tanto, es escalable en ambientes de red que no sean de confianza. Pese a su nombre, no tiene nada que ver con colas de mensajes; en realidad, utiliza un modelo de publicación y suscripción. A final de 2014, se convirtió oficialmente en un patrón abierto OASIS, con soporte en los lenguajes de programación populares, usando diversas implementaciones de software libre.

## Características:
- Protocolo de comunicación asincrónico.
- Baja cantidad de bist en los encabezados
- Modelo de Publish/Subscribe (PubSub model)
- Corre sobre protocolo orientado a la comunicación (TCP)

Los objetivos del protocolo MQTT es minimizar el ancho de banda, comunicación bidireccional entre dispositivos, minimizar los requerimientos de los dispositivos tanto recursos como consumo y garantizar la fiabilidad y cierto grado de seguridad.

Se puede utilizar cifrado SSL el cual añade una sobrecarga debido a un extra en la cantidad de datos, los microcontroladores que se selecciones deben poder implementar el protocolo SSL para garantizar cifrado de extremo a extremo.

## ESTRUCTURA DE UN MENSAJE MQTT
Lo más importante dentro del protocolo MQTT son los mensajes. Se envían de forma asíncrona, es decir, no hay un reloj indicando una base de tiempo para sincronizar la llegada y salida de información y no hay que esperar respuesta una vez que se envía un mensaje.

### Cada mensaje consta de 3 partes:
- Encabezado fijo. Ocupa sólo 2 bytes y es obligatorio enviar esta parte en todos los mensajes.
- Encabezado variable. Ocupa 4 bits y no es obligatorio que esté en todos los mensajes.
- Mensaje o carga útil (payload). Puede tener un máximo de 256 Mb, aunque en implementaciones reales el máximo es de 2 a 4 kB.


## MQTT SERVER - BROKER
Es quien corre los topics , recibe pedidos de suscripción de los clientes a los topics, recibe mensajes desde los clientes y redireccionan , basado en la subscripción de los clientes

## MQTT CLIENT - PUBLISHER, SUBSCRIBER
Los clientes se subscriben a los topics, para publicar y recibir mensajes.

### SINTAXIS DE LOS TOPIC
El símbolo / es un separador de niveles (jerarquias). Siempre se pone para separar cada uno de los niveles. Por ejemplo, podríamos tener algo como esto para medir la temperatura y/o humedad:

/casa/comedor/temperatura
/casa/comedor/humedad
/casa/cocina/temperatura
/casa/cocina/ humedad
/casa/dormitorio/temperatura
/casa/dormitorio/humedad

Es un protocolo intuitivo desde la escritura. Existen comodines como el símbolo + y #

- El símbolo + se sustituye por cualquier nivel. Si por ejemplo nos queremos suscribir a todos los topic de temperatura podemos hacerlo de la siguiente manera:

/casa/+/temperatura

El símbolo + se sustituirá por cada nivel que tenga como nivel superior casa y como nivel inferior temperatura.

El símbolo # también es un comodín. Este símbolo cubre los niveles que estén por debajo.

Por ejemplo, si quieres suscribirte a todos los mensajes que se envían a casa sólo tienes que hacer lo siguiente:

/casa/#

El topic anterior nos enviará cualquier mensaje que se envíe a casa o a cualquier nivel que esté por debajo.

Es recomendable utilizar topics, del formato anterior ya que nos permite escalabilidad.

## ¿CÓMO FUNCIONA LA ARQUITECTURA MQTT?
Una de las características más importantes es que los clientes o nodos no dependen unos de otros ya que no tienen conocimiento de quién está al otro lado. Puede incluso que no haya nadie en el otro extremo.

Esto permite algo muy importante en proyectos de este tipo: la escalabilidad.

Al contrario de lo que ocurre con el protocolo HTTP, no hay que hacer una petición para recibir información desde un cliente. Cada cliente MQTT abre una conexión permanente TCP con el broker.

El Broker tiene la capacidad de hacer que los mensajes sean persistentes, guardando el mensaje hasta que se conecte el cliente al que va dirigido.

El broker es el único que sabe quién está suscrito a un topic.



## Calidad de servicio O QOS
La calidad de servicio en MQTT determina cómo se entrega el mensaje a los receptores.

El QoS se especifica en cada mensaje que se envía y puede haber 3 grados de calidad:

- QoS 0: como máximo una vez. Esto implica que puede que no se entregue.
- QoS 1: al menos una vez. Se garantiza la entrega, pero puede que duplicados.
- QoS 2: exactamente una vez. Se garantiza que llegará una vez el mensaje.

Utilizar un grado de calidad u otro dependerá de la fiabilidad que queramos tener en nuestro sistema.

## Ejemplo Mosquitto

```bash
sudo apt install mosquitto mosquitto-clients
mosquitto_pub -h localhost -t test -m "{\"value1\":20,\"value2\":40}"
mosquitto_sub -h localhost -t test
```

## Referencias

- https://mqtt.org/
- https://eclipse.dev/paho/
- https://mosquitto.org/
- https://www.hivemq.com/blog/mqtt-essentials-part-5-mqtt-topics-best-practices/
- https://mqttx.app/web
- https://github.com/emqx/MQTT-Client-Examples/tree/master/mqtt-client-Python3



