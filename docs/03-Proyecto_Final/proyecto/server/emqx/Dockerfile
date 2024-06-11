FROM emqx:latest

#COPY config/emqx_auth_mysql.conf /opt/emqx/etc/plugins/emqx_auth_mysql.conf

ENV EMQX_DASHBOARD__DEFAULT_USERNAME=labiot
ENV EMQX_DASHBOARD__DEFAULT_PASSWORD=labiot
ENV EMQX_ALLOW_ANONYMOUS=false

# Configurar la autenticación MySQL
ENV EMQX_AUTH__MYSQL__SERVER=127.0.0.1:3306
ENV EMQX_AUTH__MYSQL__USERNAME=labiot
ENV EMQX_AUTH__MYSQL__PASSWORD=labiot2024
ENV EMQX_AUTH__MYSQL__DATABASE=emqx_auth