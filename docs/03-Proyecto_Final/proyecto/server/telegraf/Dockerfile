# Utiliza la imagen base de Telegraf
FROM telegraf:1.22.4

# Copia el archivo de configuración de Telegraf en el contenedor
COPY ./data/telegraf.conf /etc/telegraf/telegraf.conf

# Comando para iniciar Telegraf
CMD ["telegraf"]