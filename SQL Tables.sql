-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: minor
-- ------------------------------------------------------
-- Server version	8.0.26

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
-- Table structure for table `call_center_details`
--

DROP TABLE IF EXISTS `call_center_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `call_center_details` (
  `call_center_ID` varchar(20) DEFAULT NULL,
  `call_center_name` varchar(30) DEFAULT NULL,
  `call_center_add` varchar(40) DEFAULT NULL,
  `call_center_phone` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `call_center_details`
--

LOCK TABLES `call_center_details` WRITE;
/*!40000 ALTER TABLE `call_center_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `call_center_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `calldata_details`
--

DROP TABLE IF EXISTS `calldata_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `calldata_details` (
  `call_ID` varchar(20) DEFAULT NULL,
  `productID` varchar(20) DEFAULT NULL,
  `ServiceId` varchar(20) DEFAULT NULL,
  `engineer_ID` varchar(20) DEFAULT NULL,
  `assign_date` varchar(20) DEFAULT NULL,
  `total_amount` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `calldata_details`
--

LOCK TABLES `calldata_details` WRITE;
/*!40000 ALTER TABLE `calldata_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `calldata_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_details`
--

DROP TABLE IF EXISTS `customer_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer_details` (
  `customer_ID` varchar(20) DEFAULT NULL,
  `customer_name` varchar(50) DEFAULT NULL,
  `customer_add` varchar(50) DEFAULT NULL,
  `customer_phone` varchar(20) DEFAULT NULL,
  `customer_city` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_details`
--

LOCK TABLES `customer_details` WRITE;
/*!40000 ALTER TABLE `customer_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `customer_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `engineer_details`
--

DROP TABLE IF EXISTS `engineer_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `engineer_details` (
  `engineer_ID` varchar(20) DEFAULT NULL,
  `engineer_name` varchar(20) DEFAULT NULL,
  `engineer_add` varchar(50) DEFAULT NULL,
  `engineer_phone` varchar(10) DEFAULT NULL,
  `engineer_city` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `engineer_details`
--

LOCK TABLES `engineer_details` WRITE;
/*!40000 ALTER TABLE `engineer_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `engineer_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_details`
--

DROP TABLE IF EXISTS `product_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_details` (
  `productID` varchar(20) DEFAULT NULL,
  `productName` varchar(40) DEFAULT NULL,
  `VARIANT` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_details`
--

LOCK TABLES `product_details` WRITE;
/*!40000 ALTER TABLE `product_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `product_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `service_cntr_details`
--

DROP TABLE IF EXISTS `service_cntr_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `service_cntr_details` (
  `ServiceID` varchar(20) DEFAULT NULL,
  `Servicename` varchar(50) DEFAULT NULL,
  `Address` varchar(50) DEFAULT NULL,
  `owner` varchar(30) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL,
  `State` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `service_cntr_details`
--

LOCK TABLES `service_cntr_details` WRITE;
/*!40000 ALTER TABLE `service_cntr_details` DISABLE KEYS */;
INSERT INTO `service_cntr_details` VALUES ('','','','','','','');
/*!40000 ALTER TABLE `service_cntr_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `service_type_details`
--

DROP TABLE IF EXISTS `service_type_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `service_type_details` (
  `ServiceId` varchar(20) DEFAULT NULL,
  `ProductID` varchar(40) DEFAULT NULL,
  `ServiceName` varchar(50) DEFAULT NULL,
  `ServiceCharges` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `service_type_details`
--

LOCK TABLES `service_type_details` WRITE;
/*!40000 ALTER TABLE `service_type_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `service_type_details` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-08-25 22:31:36
