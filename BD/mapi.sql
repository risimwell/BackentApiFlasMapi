-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-11-2022 a las 12:52:10
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `mapi`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `actualizar_acudiente` (`cedula_acudiente` VARCHAR(255), `nombre` VARCHAR(255), `apellido` VARCHAR(255), `telefono` VARCHAR(255), `telefono_2` VARCHAR(255), `acudiente_alternativo` VARCHAR(255), `clave` VARCHAR(255))   UPDATE `acudiente` SET `nombre`=nombre,`apellido`=apellido,`telefono`=telefono,`telefono_2`=telefono_2,`acudiente_alternativo`=acudiente_alternativo WHERE `cedula_acudiente`=cedula_acudiente$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `eliminar_acudiente` (`cedula_acudiente` VARCHAR(255))   DELETE FROM `acudiente` WHERE `cedula_acudiente`=cedula_acudiente$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `listar_acudiente` ()   SELECT * FROM `acudiente`$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `registrar_niño` (IN `identificacion` VARCHAR(255), IN `nombre` VARCHAR(255), IN `apellido` VARCHAR(255), IN `edad` INT(255), IN `genero` VARCHAR(255), IN `fecha_nacimiento` DATE, IN `parentesco` VARCHAR(255))   INSERT INTO `niño`(`identificacion`, `nombre`, `apellido`, `edad`, `genero`, `fecha_nacimiento`,  `parentesco`) VALUES (identificacion,nombre,apellido,edad,genero,fecha_nacimiento,parentesco)$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `registro_acudiente` (`cedula_acudiente` VARCHAR(255), `nombre` VARCHAR(255), `apellido` VARCHAR(255), `telefono` VARCHAR(255), `clave` VARCHAR(255))   INSERT INTO `acudiente`(`cedula_acudiente`, `nombre`, `apellido`, `telefono`, `clave`) VALUES (cedula_acudiente,nombre,apellido,telefono,clave)$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `acudiente`
--

CREATE TABLE `acudiente` (
  `cedula_acudiente` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `telefono` varchar(100) NOT NULL,
  `telefono_2` varchar(100) DEFAULT NULL,
  `acudiente_alternativo` varchar(100) DEFAULT NULL,
  `teléfono_alternativo` varchar(100) DEFAULT NULL,
  `clave` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `acudiente`
--

INSERT INTO `acudiente` (`cedula_acudiente`, `nombre`, `apellido`, `telefono`, `telefono_2`, `acudiente_alternativo`, `teléfono_alternativo`, `clave`) VALUES
(0, '[value-2]', '[value-3]', '[value-4]', '[value-5]', '[value-6]', '[value-7]', '[value-8]'),
(2, '', '1', '1', NULL, NULL, NULL, '1'),
(3, ' ', '1', '1', NULL, NULL, NULL, '1'),
(8, '4', '1', '1', NULL, NULL, NULL, '1');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuncio`
--

CREATE TABLE `anuncio` (
  `codigo_anuncio` varchar(100) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `fecha_creacion` date NOT NULL,
  `multimedia` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `docente`
--

CREATE TABLE `docente` (
  `cedula_docente` varchar(100) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `telefono` varchar(100) NOT NULL,
  `institucion` varchar(100) NOT NULL,
  `clave` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `docente`
--

INSERT INTO `docente` (`cedula_docente`, `nombre`, `apellido`, `telefono`, `institucion`, `clave`) VALUES
('2', '2', '2', '2', '', '2'),
('4', '4', '4', '4', '', '4');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grupo`
--

CREATE TABLE `grupo` (
  `Codigo_grupo` varchar(30) NOT NULL,
  `Nombre_Insitucion` varchar(30) NOT NULL,
  `Fecha_Creacion` varchar(30) NOT NULL,
  `Codigo_Anuncio` varchar(30) NOT NULL,
  `Cedula_Docente` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `niño`
--

CREATE TABLE `niño` (
  `identificacion` varchar(100) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `edad` int(11) NOT NULL,
  `genero` varchar(100) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `cedula_acudiente` int(11) DEFAULT NULL,
  `parentesco` varchar(100) NOT NULL,
  `codigo_grupo` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `acudiente`
--
ALTER TABLE `acudiente`
  ADD PRIMARY KEY (`cedula_acudiente`);

--
-- Indices de la tabla `anuncio`
--
ALTER TABLE `anuncio`
  ADD PRIMARY KEY (`codigo_anuncio`);

--
-- Indices de la tabla `docente`
--
ALTER TABLE `docente`
  ADD PRIMARY KEY (`cedula_docente`);

--
-- Indices de la tabla `grupo`
--
ALTER TABLE `grupo`
  ADD PRIMARY KEY (`Codigo_grupo`),
  ADD KEY `Codigo_Anuncio` (`Codigo_Anuncio`),
  ADD KEY `Cedula_Docente` (`Cedula_Docente`);

--
-- Indices de la tabla `niño`
--
ALTER TABLE `niño`
  ADD PRIMARY KEY (`identificacion`),
  ADD KEY `cedula_acudiente` (`cedula_acudiente`),
  ADD KEY `codigo_grupo` (`codigo_grupo`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `grupo`
--
ALTER TABLE `grupo`
  ADD CONSTRAINT `grupo_ibfk_1` FOREIGN KEY (`Codigo_Anuncio`) REFERENCES `anuncio` (`codigo_anuncio`),
  ADD CONSTRAINT `grupo_ibfk_2` FOREIGN KEY (`Cedula_Docente`) REFERENCES `docente` (`cedula_docente`);

--
-- Filtros para la tabla `niño`
--
ALTER TABLE `niño`
  ADD CONSTRAINT `niño_ibfk_1` FOREIGN KEY (`cedula_acudiente`) REFERENCES `acudiente` (`cedula_acudiente`),
  ADD CONSTRAINT `niño_ibfk_2` FOREIGN KEY (`codigo_grupo`) REFERENCES `grupo` (`Codigo_grupo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
