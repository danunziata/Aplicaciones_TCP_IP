#raspymain
#Publicaciones periodicas al broker EMQX utilizando autentificacion 

import time

import psutil
import json

from paho.mqtt import client as mqtt_client


broker = '192.168.xxx.xxx'      #IP Broker
port = 1883                     #Puerto MQTT
topic = "python/mqtt"           #Nombre del Topic
client_id = 'Raspy1'            #ID de Cliente
username = 'user'               #Usuario para publicar
password = '12345'              #Password para publicar


#Funcion para conectarse al broker tras autentificarse
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Conectado al Broker MQTT")
        else:
            print("Error al realizar la conexion, codigo %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.tls_set(ca_certs='./server-ca.crt')
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


#Funcion para realizar publicaciones
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


#Funcion para obtener metricas del dispositivo:
def get_cpu_temp():
    temp = psutil.sensors_temperatures()['cpu_thermal'][0].current
    return temp


#Funcion Wrapper
def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
