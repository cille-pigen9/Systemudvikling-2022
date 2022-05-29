-- MySQL dump 10.13  Distrib 8.0.28, for macos11 (x86_64)
--
-- Host: localhost    Database: studynet
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `Administrationssekretær`
--

DROP TABLE IF EXISTS `Administrationssekretær`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Administrationssekretær` (
  `idAdministrationssekretær` int NOT NULL AUTO_INCREMENT,
  `medarbejderNummer` int DEFAULT NULL,
  `afdeling` varchar(45) DEFAULT NULL,
  `Administrationssekretær_kurser` int DEFAULT NULL,
  PRIMARY KEY (`idAdministrationssekretær`),
  KEY `fk_administrationssekretær_kurser_idx` (`Administrationssekretær_kurser`),
  CONSTRAINT `fk_administrationssekretær_kurser` FOREIGN KEY (`Administrationssekretær_kurser`) REFERENCES `Administrationssekretær_kurser` (`idRelation`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Administrationssekretær`
--

LOCK TABLES `Administrationssekretær` WRITE;
/*!40000 ALTER TABLE `Administrationssekretær` DISABLE KEYS */;
/*!40000 ALTER TABLE `Administrationssekretær` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Administrationssekretær_kurser`
--

DROP TABLE IF EXISTS `Administrationssekretær_kurser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Administrationssekretær_kurser` (
  `idRelation` int NOT NULL,
  `idAdministrationsekretær` int DEFAULT NULL,
  `idkurser` int DEFAULT NULL,
  PRIMARY KEY (`idRelation`),
  KEY `fk_administrationssekretærkurser_idx` (`idkurser`),
  CONSTRAINT `fk_administrationssekretærkurser` FOREIGN KEY (`idkurser`) REFERENCES `kurser` (`idkurser`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Administrationssekretær_kurser`
--

LOCK TABLES `Administrationssekretær_kurser` WRITE;
/*!40000 ALTER TABLE `Administrationssekretær_kurser` DISABLE KEYS */;
/*!40000 ALTER TABLE `Administrationssekretær_kurser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kurser`
--

DROP TABLE IF EXISTS `kurser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kurser` (
  `idkurser` int NOT NULL AUTO_INCREMENT,
  `kursusnavn` varchar(45) NOT NULL,
  `kursusId` int DEFAULT NULL,
  `ETSCpoint` float DEFAULT NULL,
  `skema` varchar(45) DEFAULT NULL,
  `kursusAnsvarlig` varchar(45) DEFAULT NULL,
  `placering` varchar(45) DEFAULT NULL,
  `fakultet` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idkurser`),
  UNIQUE KEY `kursusnavn_UNIQUE` (`kursusnavn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kurser`
--

LOCK TABLES `kurser` WRITE;
/*!40000 ALTER TABLE `kurser` DISABLE KEYS */;
/*!40000 ALTER TABLE `kurser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `idstudent` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `age` int DEFAULT NULL,
  `idTeacher` int DEFAULT NULL,
  `student_kurser` int DEFAULT NULL,
  PRIMARY KEY (`idstudent`),
  KEY `idteacher_idx` (`idTeacher`),
  KEY `student_kurser_idx` (`student_kurser`),
  CONSTRAINT `student_kurser` FOREIGN KEY (`student_kurser`) REFERENCES `student_kurser` (`idRelation`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_kurser`
--

DROP TABLE IF EXISTS `student_kurser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_kurser` (
  `idRelation` int NOT NULL,
  `idStudent` int DEFAULT NULL,
  `idkurser` int DEFAULT NULL,
  PRIMARY KEY (`idRelation`),
  KEY `fk_kurserkursus_idx` (`idkurser`,`idStudent`),
  CONSTRAINT `fk_kurser` FOREIGN KEY (`idkurser`) REFERENCES `kurser` (`idkurser`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_kurser`
--

LOCK TABLES `student_kurser` WRITE;
/*!40000 ALTER TABLE `student_kurser` DISABLE KEYS */;
/*!40000 ALTER TABLE `student_kurser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Teacher`
--

DROP TABLE IF EXISTS `Teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Teacher` (
  `idTeacher` int NOT NULL,
  `medarbejderNummer` int NOT NULL,
  `kursus` varchar(45) NOT NULL,
  `teacher_kurser` int DEFAULT NULL,
  PRIMARY KEY (`idTeacher`),
  KEY `fk_idx` (`kursus`),
  KEY `teacher_kurser_idx` (`teacher_kurser`),
  CONSTRAINT `teacher_kurser` FOREIGN KEY (`teacher_kurser`) REFERENCES `teacher_kurser` (`idRelation`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Teacher`
--

LOCK TABLES `Teacher` WRITE;
/*!40000 ALTER TABLE `Teacher` DISABLE KEYS */;
/*!40000 ALTER TABLE `Teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher_kurser`
--

DROP TABLE IF EXISTS `teacher_kurser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teacher_kurser` (
  `idRelation` int NOT NULL,
  `idTeacher` int DEFAULT NULL,
  `idkurser` int DEFAULT NULL,
  PRIMARY KEY (`idRelation`),
  KEY `fk_kursuskurser _idx` (`idkurser`),
  CONSTRAINT `fk_kursuskurser ` FOREIGN KEY (`idkurser`) REFERENCES `kurser` (`idkurser`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher_kurser`
--

LOCK TABLES `teacher_kurser` WRITE;
/*!40000 ALTER TABLE `teacher_kurser` DISABLE KEYS */;
/*!40000 ALTER TABLE `teacher_kurser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `iduser` int NOT NULL AUTO_INCREMENT,
  `navn` varchar(45) NOT NULL,
  `adresse` varchar(255) DEFAULT NULL,
  `cprNummer` int NOT NULL,
  `telefonNr` int DEFAULT NULL,
  `idStudent` int DEFAULT NULL,
  `idTeacher` int DEFAULT NULL,
  `idAdministrationssekretær` int DEFAULT NULL,
  PRIMARY KEY (`iduser`),
  KEY `idstudent_idx` (`idStudent`),
  KEY `idteacher_idx` (`idTeacher`),
  KEY `idaministrationssekretær_idx` (`idAdministrationssekretær`),
  CONSTRAINT `idaministrationssekretær` FOREIGN KEY (`idAdministrationssekretær`) REFERENCES `Administrationssekretær` (`idAdministrationssekretær`),
  CONSTRAINT `idstudent` FOREIGN KEY (`idStudent`) REFERENCES `student` (`idstudent`),
  CONSTRAINT `idteacher` FOREIGN KEY (`idTeacher`) REFERENCES `Teacher` (`idTeacher`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-25 10:33:03
