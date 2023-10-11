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
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(250) NOT NULL,
  `unidades` int NOT NULL,
  `precio` float NOT NULL,
  `iva` float NOT NULL,
  `cif_proveedor` varchar(15) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=142 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (111,'LLAVE CRUZ AUTOMOVIL',20,12.28,0,'1'),(112,'TRIANGULO DE EMERGENCIA',20,6.8,0,'1'),(113,'FUNDA VOLANTE 37-38cm DUNLOP NEG/NEGRO',12,8.59,0,'1'),(114,'PARASOL FRONTAL 150X70cm PLATA',20,10.96,0,'1'),(115,'JUEGO ABRAZADERAS DE TUBOS 6PZAS',25,16.4,0,'1'),(116,'CHALECO REFLECTANTE AMARILLO',20,8.58,0,'1'),(117,'CABLES ARRANQUE CAMION 4,5M 35mm',12,32.7,0,'1'),(118,'CABLES ARRANQUE 400A 3M',12,12.18,0,'1'),(119,'GUANTE PIEL GRIS T/9',120,33.48,0,'1'),(120,'RASQUETA 60cm CON ESPONJA',30,18.33,0,'1'),(121,'LIMPIA SALPICADEROS 500m! AIRE FRESCO',30,15.33,0,'1'),(122,'LIMPIA SALPICADEROS 500m!I COCHE NUEVO',30,15.33,0,'1'),(123,'LIMPIA SALPICADEROS 500mI FRESA',30,15.33,0,'1'),(124,'LIMPIA SALPICADEROS 500m! LIMON',30,15.33,0,'1'),(125,'LIMPIA SALPICADEROS 500m! VAINILLA',30,15.33,0,'1'),(126,'BIDON 5L ROJO HOMOLOGADO',50,9.82,21,'1'),(127,'BIDON 10L ROJO HOMOLOGADO',22,10.94,0,'1'),(128,'ALICATES DE CORTE LATERAL',12,5.26,0,'1'),(129,'ALICATE UNIVERSAL 150mm 6Pg',13,4.25,0,'1'),(130,'LLAVE INGLESA 20cm 8Pg',20,13.82,0,'1'),(131,'LLAVES COMBINADAS 8-19 8Pzas',12,6.99,0,'1'),(132,'GOMA ELASTICA 100cm 2uds BL',20,6.36,0,'1'),(133,'CABLE CARGADOR TIPO-C A TIPO-C 3A 1M.',50,18.95,0,'1'),(134,'CARGADOR 12V LIGHTNING DOBLE USB 2,4A 1M',50,26,0,'1'),(135,'AURICULAR + MICRO JACK 3.5MM CABLE 1M',40,11.44,0,'1'),(136,'ADAPTADOR DOBLE 240V CARGA SMARTPHONE TIPO-C / USB',40,24.64,0,'1'),(137,'Frazen Brontosaurus Ribs',2,100,19,'1'),(138,'helado',3,20,21,'1'),(139,'pajitas',100,1,21,'1'),(140,'helade.',3,20,21,'1'),(141,'pajites',100,1,21,'1');
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
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