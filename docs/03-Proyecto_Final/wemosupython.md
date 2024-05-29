# Wemos with micropython

## Instalar paquetes necesarios

```bash
sudo apt install python3-setuptools

sudo apt install picocom

sudo apt install python3-pip

python3 -m pip install --upgrade pip

pip install esptool
pip install adafruit-ampy

sudo usermod -aG dialout $USER

sudo usermod -aG tty $USER

reboot
```

## Ver si conecta el wemos

sudo dmesg # dmesg - print or control the kernel ring buffer

# si aparece brltty desinstalarlo

sudo apt remove brltty

## Erase flash and charge new flash

```bash
# erase flash
esptool.py  -p /dev/ttyUSB0 --baud 115200 erase_flash

#download bin
wget https://micropython.org/resources/firmware/ESP8266_GENERIC-FLASH_1M-20240222-v1.22.2.bin

#write flash
esptool.py --port /dev/ttyUSB0 --baud 115200 write_flash --flash_size=detect -fm dio 0 ESP8266_GENERIC-FLASH_1M-20240222-v1.22.2.bin

#Probar conexion serial
picocom /dev/ttyUSB0 -b115200
```

## Crear script python

[main.py](http://main.py) 

```python
from machine import Pin
import time

# Configurar el pin D4 (GPIO2) como salida
led = Pin(2, Pin.OUT)

# Encender y apagar el LED en un bucle
while True:
    led.on()
    time.sleep(1)  # Mantener encendido 1 segundo
    led.off()
    time.sleep(1)  # Mantener apagado 1 segundo
```

## Correr script  en wemos

```bash
ampy --port /dev/ttyUSB0 run main.pỳ
```

## Cargar script  en wemos

```bash
ampy --port /dev/ttyUSB0 put main.pỳ
```
