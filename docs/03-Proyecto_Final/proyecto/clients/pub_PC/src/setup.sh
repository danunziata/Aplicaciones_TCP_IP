#!/bin/bash

# Nombre del servicio systemd
SERVICE_NAME=mqtt_service

# Archivo de servicio systemd
SERVICE_FILE=/etc/systemd/system/${SERVICE_NAME}.service

# Ruta al script Python
SCRIPT_PATH=$(realpath lmsensors.py)

# Directorio de trabajo del script Python
WORKING_DIR=$(dirname $SCRIPT_PATH)

# Usuario actual
USER=$(whoami)

# Crea el archivo de servicio systemd
sudo bash -c "cat > ${SERVICE_FILE}" <<EOL
[Unit]
Description=MQTT Publisher Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 ${SCRIPT_PATH}
WorkingDirectory=${WORKING_DIR}
StandardOutput=inherit
StandardError=inherit
Restart=always
User=${USER}

[Install]
WantedBy=multi-user.target
EOL

# Añadir un retraso antes de ejecutar el script Python en el servicio
sudo sed -i 's/ExecStart=\/usr\/bin\/python3/ExecStartPre=\/bin\/sleep 10\nExecStart=\/usr\/bin\/python3/' ${SERVICE_PATH}

# Recarga systemd y habilita el servicio
sudo systemctl daemon-reload
sudo systemctl enable ${SERVICE_NAME}
sudo systemctl start ${SERVICE_NAME}

echo "Servicio ${SERVICE_NAME} configurado y iniciado."
