-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tienda
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `proveedores`
--

DROP TABLE IF EXISTS `proveedores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedores` (
  `nombre` varchar(50) NOT NULL,
  `cif` varchar(10) NOT NULL,
  `categoria` varchar(50) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `telefono` int NOT NULL,
  `email` varchar(100) NOT NULL,
  `id_plantillas` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`cif`),
  KEY `id_unidades_idx` (`id_plantillas`),
  CONSTRAINT `id_plantilla_des` FOREIGN KEY (`id_plantillas`) REFERENCES `plantilla_descripcion` (`id_plantilla_des`),
  CONSTRAINT `id_plantilla_iva` FOREIGN KEY (`id_plantillas`) REFERENCES `plantilla_iva` (`id_plantilla_iva`),
  CONSTRAINT `id_plantilla_precios` FOREIGN KEY (`id_plantillas`) REFERENCES `plantilla_precios` (`id_plantilla_precios`),
  CONSTRAINT `id_plantilla_totales` FOREIGN KEY (`id_plantillas`) REFERENCES `plantilla_totales` (`id_plantilla_totales`),
  CONSTRAINT `id_plantillla_unidades` FOREIGN KEY (`id_plantillas`) REFERENCES `plantilla_unidades` (`id_plantilla_unidades`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedores`
--

LOCK TABLES `proveedores` WRITE;
/*!40000 ALTER TABLE `proveedores` DISABLE KEYS */;
INSERT INTO `proveedores` VALUES ('luis','1','1','1',1,'1',7),('juan','2','1','1',1,'1',8),('coval petrol','awd','adwda','qasd',655,'awda',4);
/*!40000 ALTER TABLE `proveedores` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-11 20:03:01
