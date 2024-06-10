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

CREATE TABLE IF NOT EXISTS `mqtt_acl` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ipaddress` varchar(60),
  `username` varchar(100),
  `clientid` varchar(100),
  `access` int(1) NOT NULL,
  `topic` varchar(100) NOT NULL,
  `created` datetime DEFAULT CURRENT_TIMESTAMP,
  `modified` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Insertar los usuarios con sus contraseñas en texto plano
INSERT INTO mqtt_user (username, password_hash) VALUES ('sonoff', 'tcpip2024');
INSERT INTO mqtt_user (username, password_hash) VALUES ('dht11', 'sebacrack');

-- Crear el usuario de base de datos y concederle permisos
CREATE USER 'labiot'@'%' IDENTIFIED BY 'labiot2024';
GRANT ALL PRIVILEGES ON emqx_auth.* TO 'labiot'@'%';
FLUSH PRIVILEGES;
