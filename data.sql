-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.7.18-log - MySQL Community Server (GPL)
-- Server OS:                    Win64
-- HeidiSQL Version:             9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for n2_bookstore
DROP DATABASE IF EXISTS `n2_bookstore`;
CREATE DATABASE IF NOT EXISTS `n2_bookstore` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `n2_bookstore`;

-- Dumping structure for table n2_bookstore.author
DROP TABLE IF EXISTS `author`;
CREATE TABLE IF NOT EXISTS `author` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(512) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `email` varchar(128) DEFAULT NULL,
  `address` varchar(256) DEFAULT NULL,
  `country` varchar(128) DEFAULT NULL,
  `bio` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- Dumping data for table n2_bookstore.author: ~2 rows (approximately)
DELETE FROM `author`;
/*!40000 ALTER TABLE `author` DISABLE KEYS */;
INSERT INTO `author` (`id`, `name`, `birthday`, `email`, `address`, `country`, `bio`) VALUES
	(1, 'J. K. Rowling', '1965-09-30', 'info@jkrowling.com', 'Yate, United Kingdom', 'United Kingdom', 'Joanne Rowling, CH, OBE, FRSL, who writes under the pen names J. K. Rowling and Robert Galbraith, is a British novelist, film and television producer, screenwriter and philanthropist, best known as the author of the Harry Potter fantasy series'),
	(2, 'Stephen King', '1947-09-21', 'info@stephening.com', 'Portland, Maine, United States', 'United States', 'Stephen Edwin King is an American author of horror, supernatural fiction, suspense, science fiction, and fantasy.'),
	(3, 'Dan Brown', '1964-06-22', 'info@danbrown.com', 'Exeter, New Hampshire, United States', 'United States', 'Daniel Gerhard "Dan" Brown is an American author of thriller fiction who wrote the 2003 bestselling novel The Da Vinci Code.');
/*!40000 ALTER TABLE `author` ENABLE KEYS */;

-- Dumping structure for table n2_bookstore.book
DROP TABLE IF EXISTS `book`;
CREATE TABLE IF NOT EXISTS `book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(1024) DEFAULT NULL,
  `isbn` varchar(25) DEFAULT NULL,
  `year` year(4) DEFAULT NULL,
  `cover` text NOT NULL,
  `author` int(11) NOT NULL,
  `publisher` int(11),
  PRIMARY KEY (`id`),
  KEY `book_publisher` (`publisher`),
  KEY `book_author` (`author`),
  CONSTRAINT `book_author` FOREIGN KEY (`author`) REFERENCES `author` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `book_publisher` FOREIGN KEY (`publisher`) REFERENCES `publisher` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- Dumping data for table n2_bookstore.book: ~0 rows (approximately)
DELETE FROM `book`;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` (`id`, `title`, `isbn`, `year`, `cover`, `author`, `publisher`) VALUES
	(1, 'Inferno', '978-0-385-53785-8', '2013', 'https://upload.wikimedia.org/wikipedia/en/thumb/b/bb/Inferno-cover.jpg/200px-Inferno-cover.jpg', 3, 1),
	(2, 'The Lost Symbol', '978-0-385-50422-5', '2009', 'https://upload.wikimedia.org/wikipedia/en/0/07/LostSymbol.jpg', 3, 1),
	(3, 'The Davinci Code', '0-385-50420-9', '2003', 'https://upload.wikimedia.org/wikipedia/en/thumb/6/6b/DaVinciCode.jpg/220px-DaVinciCode.jpg', 3, 1);
/*!40000 ALTER TABLE `book` ENABLE KEYS */;

-- Dumping structure for table n2_bookstore.publisher
DROP TABLE IF EXISTS `publisher`;
CREATE TABLE IF NOT EXISTS `publisher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL DEFAULT '0',
  `address` varchar(512) NOT NULL DEFAULT '0',
  `country` varchar(128) NOT NULL DEFAULT '0',
  `phone_number` varchar(20) NOT NULL DEFAULT '0',
  `email` varchar(128) NOT NULL DEFAULT '0',
  `web` varchar(2048) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- Dumping data for table n2_bookstore.publisher: ~0 rows (approximately)
DELETE FROM `publisher`;
/*!40000 ALTER TABLE `publisher` DISABLE KEYS */;
INSERT INTO `publisher` (`id`, `name`, `address`, `country`, `phone_number`, `email`, `web`) VALUES
	(1, 'DoubleDay', 'New York City', 'New York', '1-800-815-9387', 'info@doubleday.knopfdoubleday.com', 'doubleday.knopfdoubleday.com');
/*!40000 ALTER TABLE `publisher` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
