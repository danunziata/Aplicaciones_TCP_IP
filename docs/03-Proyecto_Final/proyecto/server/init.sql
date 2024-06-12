CREATE DATABASE IF NOT EXISTS emqx_auth;

USE emqx_auth;

CREATE TABLE `mqtt_user` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password_hash` varchar(100) NOT NULL,
  `salt` varchar(35) DEFAULT NULL,
  `is_superuser` tinyint(1) DEFAULT 0,
  `created` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mqtt_username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Insertar los usuarios con sus contraseñas en texto plano
-- INSERT INTO mqtt_user (username, password_hash) VALUES ('sonoff', 'tcpip2024');
-- INSERT INTO mqtt_user (username, password_hash) VALUES ('dht11', 'sebacrack');
-- INSERT INTO mqtt_user (username, password_hash) VALUES ('raspy', 'tcpip2024');
INSERT INTO mqtt_user (username, password_hash, salt) VALUES ('sonoff', SHA2(CONCAT('tcpip2024', 'slat_foo123'), 256), 'slat_foo123');
INSERT INTO mqtt_user (username, password_hash, salt) VALUES ('dht11', SHA2(CONCAT('sebacrack', 'slat_foo123'), 256), 'slat_foo123');
INSERT INTO mqtt_user (username, password_hash, salt) VALUES ('raspy', SHA2(CONCAT('labiot2024', 'slat_foo123'), 256), 'slat_foo123');

-- Crear el usuario de base de datos y concederle permisos
CREATE USER 'labiot'@'%' IDENTIFIED BY 'labiot2024';
GRANT ALL PRIVILEGES ON emqx_auth.* TO 'labiot'@'%';
FLUSH PRIVILEGES;
