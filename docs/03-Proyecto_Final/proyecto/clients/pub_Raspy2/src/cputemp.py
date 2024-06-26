#Temperatura y uso de CPU (JSON + MQTT) 

import psutil
import json
import paho.mqtt.publish as publish
import time

broker_address = "192.168.0.229"
topic = "Server/PC1"

def get_cpu_temp():
    temp = psutil.sensors_temperatures()['nvme'][0]
    return temp.current

while True:
    msg = json.dumps({'id': "PC1", 'cpu_usage': psutil.cpu_percent(), 'cpu_temp': get_cpu_temp()})
    print(msg)
    publish.single(topic, msg, hostname=broker_address, client_id='Raspberry Pi 2')
    time.sleep(5)