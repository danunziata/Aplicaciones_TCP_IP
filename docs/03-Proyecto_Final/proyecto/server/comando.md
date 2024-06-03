# Pasos para Conectarte Correctamente a MySQL desde el Contenedor EMQX

Accede al Contenedor EMQX:
sh
docker exec -it server-emqx-1 sh

Instala el cliente mysql:
apt-get update
apt-get install default-mysql-client -y

ingresa a mysql:
mysql -h mysql -u root -p

Una vez conectado como root, verifica los permisos del usuario labiot y asegúrate de que todo está configurado correctamente:
-- Mostrar todos los usuarios y sus hosts
SELECT host, user FROM mysql.user;

-- Mostrar los permisos del usuario labiot
SHOW GRANTS FOR 'labiot'@'%';

-- Asegúrate de que el usuario labiot tiene permisos adecuados
GRANT ALL PRIVILEGES ON emqx_auth.* TO 'labiot'@'%';
FLUSH PRIVILEGES;

aca es donde debemos crear el usuario labiot: Crear el Usuario y Asignar Permisos
dentro de la consola de mysql dentro del contenedor:
CREATE USER 'labiot'@'%' IDENTIFIED BY 'labiot2024';
GRANT ALL PRIVILEGES ON emqx_auth.* TO 'labiot'@'%';
FLUSH PRIVILEGES;

y para verificar:
SELECT host, user FROM mysql.user;
SHOW GRANTS FOR 'labiot'@'%';

Reinicia los contenedores para asegurarte de que los cambios se apliquen:
sh
docker-compose down
docker-compose up -d
