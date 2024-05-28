import psutil
import json
import paho.mqtt.publish as publish
import time

def get_cpu_temp():
    temp = psutil.sensors_temperatures()['nvme'][0]
    return temp.current

broker_address = "192.168.5.168"
topic = "Server/PC1"
msg = json.dumps({'id': "PC1", 'cpu_usage': psutil.cpu_percent(), 'cpu_temp': get_cpu_temp()})
print(msg)


while True:
    publish.single(topic, msg, hostname=broker_address, client_id='bocha_pub.py') 
    time.sleep(5)   #Esperamos 5s entre dato
