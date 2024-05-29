# influxdb/Dockerfile
FROM influxdb:2.2.0-alpine

ENV DOCKER_INFLUXDB_INIT_MODE=setup
ENV DOCKER_INFLUXDB_INIT_USERNAME=labiot
ENV DOCKER_INFLUXDB_INIT_PASSWORD=labiot
ENV DOCKER_INFLUXDB_INIT_ORG=atcpip
ENV DOCKER_INFLUXDB_INIT_BUCKET=iotdata
ENV DOCKER_INFLUXDB_INIT_RETENTION=1w
ENV DOCKER_INFLUXDB_INIT_ADMIN_TOKEN=labiot-iotdata-auth-token

# Opcional: Si necesitas hacer alguna configuración adicional, puedes agregar más comandos aquí
