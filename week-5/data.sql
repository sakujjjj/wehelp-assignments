-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: website
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
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '獨立編號',
  `name` varchar(255) NOT NULL COMMENT '姓名',
  `username` varchar(255) NOT NULL COMMENT '帳戶名稱',
  `password` varchar(255) NOT NULL COMMENT '帳戶密碼',
  `follower_count` int NOT NULL DEFAULT '0' COMMENT '追蹤者數量',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '註冊時間',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'test2','test','test',0,'2022-01-29 01:44:14'),(2,'test2','test','test',0,'2022-01-29 01:45:36'),(3,'test2','test2','test',0,'2022-01-29 01:46:12'),(4,'test2','test','test',0,'2022-01-29 01:46:21'),(5,'Lin','test3','test',99,'2022-01-29 02:22:45'),(6,'J','test','test',50,'2022-01-29 02:23:16');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '獨立編號',
  `member_id` bigint NOT NULL COMMENT '留言者會員編號',
  `content` varchar(255) NOT NULL COMMENT '留言內容',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '留言時間',
  PRIMARY KEY (`id`),
  KEY `id_idx` (`member_id`),
  CONSTRAINT `id` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,6,'安安','2022-01-29 03:15:06'),(2,5,'你好','2022-01-29 03:15:31'),(4,1,'hiiiiiiiii','2022-01-29 03:23:08'),(5,1,'hiiiiiiiii','2022-01-29 03:23:12'),(6,1,'hiiiiiiiiiiiiiiiiiiiii','2022-01-29 03:23:18'),(7,2,'OMG','2022-01-29 03:23:59'),(8,3,'@@@@@@@','2022-01-29 03:24:10');
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-29  3:27:01
