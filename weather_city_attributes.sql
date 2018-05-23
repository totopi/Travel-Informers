-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: weather
-- ------------------------------------------------------
-- Server version	5.7.21-log

USE `x5t20wxo8nmqqxfz`;

--
-- Table structure for table `city_attributes`
--

DROP TABLE IF EXISTS city_attributes;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `city_attributes` (
  `city` text,
  `abbr` text,
  `country` text,
  `latitude` double DEFAULT NULL,
  `longitude` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `city_attributes`
--

LOCK TABLES `city_attributes` WRITE;
INSERT INTO `city_attributes` VALUES ('Vancouver', 'van','Canada',49.24966,-123.119339),('Portland','por','United States',45.523449,-122.676208),('San Francisco','sfran','United States',37.774929,-122.419418),('Seattle','sea','United States',47.606209,-122.332069),('Los Angeles',"la",'United States',34.052231,-118.243683),('San Diego','sand','United States',32.715328,-117.157257),('Las Vegas','laveg','United States',36.174969,-115.137222),('Phoenix','pho','United States',33.44838,-112.074043),('Albuquerque','alb','United States',35.084492,-106.651138),('Denver','den','United States',39.739151,-104.984703),('SanAntonio','sant','United States',29.42412,-98.493629),('Dallas','dal','United States',32.783058,-96.806671),('Houston','hou','United States',29.763281,-95.363274),('Kansas City','ksc','United States',39.099731,-94.578568),('Minneapolis','min','United States',44.979969,-93.26384),('Saint Louis','stlo','United States',38.62727,-90.197891),('Chicago','chi','United States',41.850029,-87.650047),('Nashville','nash','United States',36.16589,-86.784439),('Indianapolis','ind','United States',39.768379,-86.158043),('Atlanta','atl','United States',33.749001,-84.387978),('Detroit','det','United States',42.331429,-83.045753),('Jacksonville','jac','United States',30.33218,-81.655647),('Charlotte','char','United States',35.227089,-80.843132),('Miami','mai','United States',25.774269,-80.193657),('Pittsburgh','pit','United States',40.44062,-79.995888),('Toronto','tor','Canada',43.700111,-79.416298),('Philadelphia','phi','United States',39.952339,-75.163788),('New York','nyc','United States',40.714272,-74.005966),('Montreal','mon','Canada',45.508839,-73.587807),('Boston','bos','United States',42.358429,-71.059769),('Beersheba','bee','Israel',31.25181,34.791302),('Tel Aviv','tel','Israel',32.083328,34.799999),('Eilat','eil','Israel',29.55805,34.948212),('Haifa','hai','Israel',32.815559,34.98917),('Nahariyya','nah','Israel',33.005859,35.09409),('Jerusalem','jer','Israel',31.769039,35.216331);

UNLOCK TABLES;


-- Dump completed on 2018-05-20 20:35:11
