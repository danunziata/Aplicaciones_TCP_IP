import time
import psutil
import json
import paho.mqtt.client as mqtt
import subprocess
import ssl

# Configuración del broker MQTT
broker = '192.168.5.101'
port = 8883  # Puerto estándar sin TLS
topic = "sensor/raspy/pc"
client_id = 'Labredes_PC1'
username = 'raspy'
password = 'tcpip2024'

#Certificados
key = "./certs/client.key"
ca = "./certs/ca.pem"
cert = "./certs/client.pem"

# Función de conexión al broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado al Broker MQTT")
    else:
        print(f"Error al realizar la conexión, código {rc}")

def connect_mqtt():
    client = mqtt.Client(client_id=client_id)
    client.username_pw_set(username, password)
    
    client.tls_set(certfile=cert, ca_certs=ca, keyfile=key, cert_reqs=ssl.CERT_REQUIRED)
    client.on_connect = on_connect
    
    client.connect(broker, port)
    return client

# Función para publicar los datos
def publish(client):
    while True:
        time.sleep(1)
        msg = json.dumps({'id': client_id, 'cpu_usage': psutil.cpu_percent(), 'cpu_temp': get_cpu_temp()})
        result = client.publish(topic, msg)
        status = result.rc
        if status == mqtt.MQTT_ERR_SUCCESS:
            print(f"Mensaje publicado: {msg}")
        else:
            print(f"Error al publicar el mensaje: {status}")

# Función para obtener la temperatura del CPU usando lmsensors
def get_cpu_temp():
    try:
        # Ejecuta el comando sensors y obtiene la salida
        output = subprocess.check_output(['sensors'], encoding='utf-8')
        # Divide la salida por líneas
        lines = output.split('\n')
        for line in lines:
            # Busca líneas que contienen 'Core' y extrae la temperatura
            if 'Core 0' in line:  # Asegúrate de que 'Core 0' se ajusta a tu configuración
                temp_str = line.split()[2]  # Obtiene la tercera palabra (ej: +45.0°C)
                return float(temp_str.strip('+°C'))
    except Exception as e:
        print(f"Error al obtener la temperatura del CPU: {e}")
        return None

# Función principal
def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()
