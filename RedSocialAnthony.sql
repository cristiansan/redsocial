-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.1.39-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             10.1.0.5464
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for red_social
CREATE DATABASE IF NOT EXISTS `red_social` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `red_social`;

-- Dumping structure for table red_social.amistad
CREATE TABLE IF NOT EXISTS `amistad` (
  `ID_AMISTAD` int(11) NOT NULL AUTO_INCREMENT,
  `ID_USUARIO1` int(11) DEFAULT NULL,
  `ID_USUARIO2` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID_AMISTAD`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

-- Dumping data for table red_social.amistad: ~19 rows (approximately)
/*!40000 ALTER TABLE `amistad` DISABLE KEYS */;
INSERT INTO `amistad` (`ID_AMISTAD`, `ID_USUARIO1`, `ID_USUARIO2`) VALUES
	(1, 1, 2),
	(2, 1, 3),
	(3, 2, 1),
	(4, 2, 4),
	(5, 3, 1),
	(6, 4, 2),
	(7, 5, 3),
	(8, 5, 1),
	(9, 1, 5),
	(10, 9, 1),
	(11, 1, 2),
	(12, 1, 1),
	(13, 1, 2),
	(14, 1, 4),
	(18, 10, 1),
	(19, 11, 1),
	(20, 11, 7),
	(21, 11, 1),
	(26, 8, 7);
/*!40000 ALTER TABLE `amistad` ENABLE KEYS */;

-- Dumping structure for table red_social.categoria
CREATE TABLE IF NOT EXISTS `categoria` (
  `ID_CATEGORIA` int(11) NOT NULL AUTO_INCREMENT,
  `NOMBRE_CATEGORIA` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`ID_CATEGORIA`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- Dumping data for table red_social.categoria: ~5 rows (approximately)
/*!40000 ALTER TABLE `categoria` DISABLE KEYS */;
INSERT INTO `categoria` (`ID_CATEGORIA`, `NOMBRE_CATEGORIA`) VALUES
	(1, 'Humor'),
	(2, 'Noticias'),
	(3, 'Tecnologia'),
	(4, 'Ventas'),
	(5, 'xxx');
/*!40000 ALTER TABLE `categoria` ENABLE KEYS */;

-- Dumping structure for table red_social.ciudad
CREATE TABLE IF NOT EXISTS `ciudad` (
  `IDCiudad` int(11) NOT NULL,
  `NombreCiudad` varchar(30) DEFAULT NULL,
  `IDProvincia` int(11) NOT NULL,
  PRIMARY KEY (`IDCiudad`),
  KEY `IDProvincia` (`IDProvincia`),
  CONSTRAINT `ciudad_ibfk_1` FOREIGN KEY (`IDProvincia`) REFERENCES `provincia` (`IDProvincia`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table red_social.ciudad: ~12 rows (approximately)
/*!40000 ALTER TABLE `ciudad` DISABLE KEYS */;
INSERT INTO `ciudad` (`IDCiudad`, `NombreCiudad`, `IDProvincia`) VALUES
	(1, 'La Plata', 1),
	(2, 'Bahia Blanca', 1),
	(3, 'Mar del Plata', 1),
	(4, 'Olavarría', 1),
	(5, 'Necochea', 1),
	(6, 'Pergamino', 1),
	(7, 'Agua Santa', 27),
	(8, 'Buena Vista', 27),
	(9, 'Caja Seca', 27),
	(10, 'Dividive', 27),
	(11, 'Escuque', 27),
	(12, 'Niquitao', 27);
/*!40000 ALTER TABLE `ciudad` ENABLE KEYS */;

-- Dumping structure for table red_social.pais
CREATE TABLE IF NOT EXISTS `pais` (
  `IDPais` int(11) NOT NULL,
  `NombrePais` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`IDPais`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table red_social.pais: ~7 rows (approximately)
/*!40000 ALTER TABLE `pais` DISABLE KEYS */;
INSERT INTO `pais` (`IDPais`, `NombrePais`) VALUES
	(0, 'ARGENTINA'),
	(1, 'Bolivia'),
	(2, 'CHILE'),
	(3, 'BRASIL'),
	(4, 'VENEZUELA'),
	(5, 'PERU'),
	(6, 'MEXICO');
/*!40000 ALTER TABLE `pais` ENABLE KEYS */;

-- Dumping structure for table red_social.posteo
CREATE TABLE IF NOT EXISTS `posteo` (
  `ID_POSTEO` int(11) NOT NULL AUTO_INCREMENT,
  `MENSAJE` varchar(200) DEFAULT NULL,
  `ID_USUARIO` int(11) DEFAULT NULL,
  `ID_CATEGORIA` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID_POSTEO`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

-- Dumping data for table red_social.posteo: ~24 rows (approximately)
/*!40000 ALTER TABLE `posteo` DISABLE KEYS */;
INSERT INTO `posteo` (`ID_POSTEO`, `MENSAJE`, `ID_USUARIO`, `ID_CATEGORIA`) VALUES
	(1, 'mensaje1', 1, 1),
	(3, 'mensaje3', 3, 2),
	(4, 'mensaje4', 4, 4),
	(5, 'mensaje5', 5, 1),
	(6, 'mensaje6', 1, 5),
	(7, 'mensaje7', 3, 5),
	(8, 'mensaje8', 4, 3),
	(9, 'mensaje9', 2, 1),
	(10, 'mensaje10', 2, 1),
	(11, 'MENSAJE tp', 5, 3),
	(13, 'test feriado', 1, 1),
	(14, 'test usuario "A"', 8, 1),
	(15, 'trtdrtdrtd', 8, 1),
	(16, 'tdrtdrtdtd', 8, 1),
	(18, 'testtesttest', 8, 1),
	(19, 'testtesttest', 8, 1),
	(20, 'testeststestset', 8, 1),
	(21, 'testetsetest', 8, 1),
	(22, 'esto es un post porno', 1, 5),
	(23, 'test', 1, 5),
	(24, 'Esto es un chiste, ajajaj', 8, 1),
	(25, 'Noticia de último momento!!! :o', 8, 2),
	(26, 'Post Tecnología!!', 8, 3),
	(27, 'post hot', 8, 5);
/*!40000 ALTER TABLE `posteo` ENABLE KEYS */;

-- Dumping structure for table red_social.provincia
CREATE TABLE IF NOT EXISTS `provincia` (
  `IDProvincia` int(11) NOT NULL,
  `NombreProvincia` varchar(30) DEFAULT NULL,
  `IDPais` int(11) DEFAULT NULL,
  PRIMARY KEY (`IDProvincia`),
  KEY `IDPais` (`IDPais`),
  CONSTRAINT `provincia_ibfk_1` FOREIGN KEY (`IDPais`) REFERENCES `pais` (`IDPais`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table red_social.provincia: ~42 rows (approximately)
/*!40000 ALTER TABLE `provincia` DISABLE KEYS */;
INSERT INTO `provincia` (`IDProvincia`, `NombreProvincia`, `IDPais`) VALUES
	(1, 'BUENOS AIRES', 0),
	(2, 'CORDOBA', 0),
	(3, 'MENDOZA', 0),
	(4, 'SANTA FE', 0),
	(5, 'JUJUY', 0),
	(6, 'CHUBUT', 0),
	(7, 'ATACAMA', 2),
	(8, 'MULUE', 2),
	(9, 'LOS LAGOS', 2),
	(10, 'LOS RIOS', 2),
	(11, 'COQUIMBO', 2),
	(12, 'TARAPACA', 2),
	(13, 'LA PAZ', 1),
	(14, 'COCHABAMBA', 1),
	(15, 'ORURO', 1),
	(16, 'POTOSI', 1),
	(17, 'TARIJA', 1),
	(18, 'SANTA CRUZ', 1),
	(19, 'RIO DE JANEIRO', 3),
	(20, 'SAN PABLO', 3),
	(21, 'AMAZONAS', 3),
	(22, 'PARA', 3),
	(23, 'RORAIMA', 3),
	(24, 'PARANA', 3),
	(25, 'MERIDA', 4),
	(26, 'MONAGAS', 4),
	(27, 'TRUJILLO', 4),
	(28, 'LARA', 4),
	(29, 'ZULIA', 4),
	(30, 'CARABOBO', 4),
	(31, 'LIMA', 5),
	(32, 'JUNIN', 5),
	(33, 'ICA', 5),
	(34, 'LORETO', 5),
	(35, 'PASCO', 5),
	(36, 'PIURA', 5),
	(37, 'CHIAPAS', 6),
	(38, 'CHIHUAHUA', 6),
	(39, 'DURANGO', 6),
	(40, 'MORELOS', 6),
	(41, 'SINALOA', 6),
	(42, 'TABASCO', 6);
/*!40000 ALTER TABLE `provincia` ENABLE KEYS */;

-- Dumping structure for table red_social.usuario
CREATE TABLE IF NOT EXISTS `usuario` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `NOMBRE` varchar(40) DEFAULT NULL,
  `APELLIDO` varchar(40) DEFAULT NULL,
  `CLAVE` varchar(40) DEFAULT NULL,
  `EMAIL` varchar(40) DEFAULT NULL,
  `Ciudad` int(11) DEFAULT NULL,
  `edad` int(11) DEFAULT NULL,
  `sexo` varchar(1) DEFAULT NULL,
  `fecha_nac` date DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `Ciudad` (`Ciudad`),
  CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`Ciudad`) REFERENCES `ciudad` (`IDCiudad`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

-- Dumping data for table red_social.usuario: ~10 rows (approximately)
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` (`ID`, `NOMBRE`, `APELLIDO`, `CLAVE`, `EMAIL`, `Ciudad`, `edad`, `sexo`, `fecha_nac`) VALUES
	(1, 'Cristian', 'San Emeterio', '1234', 'cs@gmail.com', 5, 25, 'M', '1977-01-12'),
	(2, 'Jorge', 'Guanare', '456', 'jg@gmail.com', 3, 22, 'M', '1980-10-10'),
	(3, 'Lucas', 'Lezcano', '789', 'll@gmail.com', 4, 30, 'M', '1999-09-21'),
	(4, 'Laura', 'Ingalls', 'lauingalls123', 'lau@gmail.com', 4, 35, 'F', '1982-07-02'),
	(5, 'Monica', 'Lopez', 'Moni1', 'monica@gmail.com', 3, 38, 'F', '1945-02-12'),
	(7, 'jorge', 'caseros', '4321', 'jocaseros@gmail.com', 3, 44, 'M', '1980-09-09'),
	(8, 'aa', 'aa', 'aa', 'aa', 1, 11, 'F', '1980-12-12'),
	(9, 'a', 'a', 'a', 'a@a.com', 1, 33, 'F', '2000-01-01'),
	(10, 'Anthony', 'Lunar', '1234', 'an@gmail.com', 1, 34, 'M', '1985-08-16'),
	(11, 'Matias', 'Acuna', '12345', 'matias_22@gmail.com', 4, 27, 'M', '0000-00-00');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
