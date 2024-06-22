import time
import psutil
import json
import ssl
import paho.mqtt.client as mqtt

broker = '172.26.0.2'
port = 8883
topic = "test/topic"
client_id = 'Raspy1'
username = 'emqx'
password = '**********'

key = "/home/ejemplo/Desktop/raspymain/client.key"
ca = "/home/ejemplo/Desktop/raspymain/ca.pem"
cert = "/home/ejemplo/Desktop/raspymain/client.pem"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado al Broker MQTT")
    else:
        print(f"Error al realizar la conexión, código {rc}")

def connect_mqtt():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1,client_id)
    client.username_pw_set(username, password)
    
    client.tls_set(certfile=cert, ca_certs=ca, keyfile=key, cert_reqs=ssl.CERT_REQUIRED)
    client.on_connect = on_connect
    
    client.connect(broker, port)
    
    client.callback_connect = on_connect
    
    return client


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = json.dumps({'id': client_id, 'cpu_usage': psutil.cpu_percent(), 'cpu_temp': get_cpu_temp()})
        result = client.publish(topic, msg)
        status = result[0]
        if status == mqtt.MQTT_ERR_SUCCESS:
            print(f"Mensaje publicado: {msg}")
        else:
            print(f"Error al publicar el mensaje: {status}")
        msg_count += 1

def get_cpu_temp():
    temp = psutil.sensors_temperatures()['cpu_thermal'][0].current
    return temp

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()
