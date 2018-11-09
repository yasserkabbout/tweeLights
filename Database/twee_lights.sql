-- phpMyAdmin SQL Dump
-- version 2.8.0.1
-- http://www.phpmyadmin.net
-- 
-- Host: custsql-ipg62.eigbox.net
-- Generation Time: Nov 08, 2018 at 10:51 PM
-- Server version: 5.6.41
-- PHP Version: 4.4.9
-- 
-- Database: `twee_lights`
-- 

-- --------------------------------------------------------

-- 
-- Table structure for table `Stores`
-- 

CREATE TABLE `Stores` (
  `store_id` int(11) NOT NULL DEFAULT '0',
  `store_name` varchar(255) DEFAULT NULL,
  `store_country` varchar(255) DEFAULT NULL,
  `store_city` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`store_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- 
-- Dumping data for table `Stores`
-- 

INSERT INTO `Stores` VALUES (1, 'Amazon', 'America', 'Ny');
INSERT INTO `Stores` VALUES (2, 'eBay', 'Australia', 'Sydney');

-- --------------------------------------------------------

-- 
-- Table structure for table `winners_colors`
-- 

CREATE TABLE `winners_colors` (
  `record_id` int(11) NOT NULL AUTO_INCREMENT,
  `store_id` int(11) DEFAULT NULL,
  `winner_color` varchar(255) DEFAULT NULL,
  `record_date` varchar(15) NOT NULL,
  PRIMARY KEY (`record_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

-- 
-- Dumping data for table `winners_colors`
-- 

INSERT INTO `winners_colors` VALUES (1, 1, 'RED', '1-01-2018');
INSERT INTO `winners_colors` VALUES (2, 1, 'GREEN', '1-02-2018');
INSERT INTO `winners_colors` VALUES (3, 1, 'YELLOW', '1-03-2018');
INSERT INTO `winners_colors` VALUES (4, 1, 'RED', '1-04-2018');
INSERT INTO `winners_colors` VALUES (5, 1, 'GREEN', '1-05-2018');
INSERT INTO `winners_colors` VALUES (6, 1, 'RED', '1-06-2018');
INSERT INTO `winners_colors` VALUES (7, 1, 'RED', '1-07-2018');
INSERT INTO `winners_colors` VALUES (8, 1, 'RED', '1-08-2018');
INSERT INTO `winners_colors` VALUES (9, 1, 'RED', '1-09-2018');
INSERT INTO `winners_colors` VALUES (10, 1, 'RED', '1-10-2018');
INSERT INTO `winners_colors` VALUES (11, 1, 'GREEN', '1-11-2018');
INSERT INTO `winners_colors` VALUES (12, 1, 'YELLOW', '1-12-2018');
