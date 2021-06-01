CREATE DATABASE IF NOT EXISTS smarttbot_crypto;
USE smarttbot_crypto;

CREATE TABLE IF NOT EXISTS `crypto` (
  `name` varchar(50) NOT NULL,
  `period` int NOT NULL,
  `date_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `open` double NOT NULL,
  `low` double NOT NULL,
  `high` double NOT NULL,
  `close` double NOT NULL,
  PRIMARY KEY (`name`,`period`,`date_time`)
)ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;