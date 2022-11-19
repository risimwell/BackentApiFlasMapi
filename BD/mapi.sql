-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-11-2022 a las 17:19:17
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 7.4.29

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
CREATE DEFINER=`root`@`localhost` PROCEDURE `actualizar_informacion_niño` (`nombre` VARCHAR(255), `apellido` VARCHAR(255), `genero` VARCHAR(255), `fecha_nacimiento` DATE, `parentesco` VARCHAR(255))   UPDATE `niño` SET `nombre`=nombre,`apellido`=apellido,`genero`=genero,`fecha_nacimiento`=fecha_nacimiento,`parentesco`=parentesco WHERE `identificacion`=identificacion$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `actualizar_informacio_acudiente` (IN `cedula_acudiente` VARCHAR(255), IN `nombre` VARCHAR(255), IN `apellido` VARCHAR(255), IN `telefono` VARCHAR(255), IN `telefono_2` VARCHAR(255), IN `acudiente_alternativo` VARCHAR(255))   UPDATE `acudiente` SET `nombre`=nombre,`apellido`=apellido,`telefono`=telefono,`telefono_2`=telefono_2,`acudiente_alternativo`=acudiente_alternativo WHERE `cedula_acudiente`=cedula_acudiente$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `eliminar_acudiente` (`cedula_acudiente` VARCHAR(255))   DELETE FROM `acudiente` WHERE `cedula_acudiente`=cedula_acudiente$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `listar_acudiente` ()   SELECT * FROM `acudiente`$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `registrar_niño` (IN `identificacion` VARCHAR(255), IN `nombre` VARCHAR(255), IN `apellido` VARCHAR(255), IN `edad` INT(255), IN `genero` VARCHAR(255), IN `fecha_nacimiento` DATE, IN `parentesco_acudiente` VARCHAR(255))   INSERT INTO `niño`(`identificacion`, `nombre`, `apellido`, `edad`, `genero`, `fecha_nacimiento`,  `parentesco_acudiente`,`cedula_acudiente`,`codigo_grupo`,`estado`) VALUES (identificacion,nombre,apellido,edad,genero,fecha_nacimiento,parentesco_acudiente,cedula_acudiente,codigo_grupo,1)$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `registro_acudiente` (`cedula_acudiente` VARCHAR(255), `nombre` VARCHAR(255), `apellido` VARCHAR(255), `telefono` VARCHAR(255), `clave` VARCHAR(255))   INSERT INTO `acudiente`(`cedula_acudiente`, `nombre`, `apellido`, `telefono`, `clave`) VALUES (cedula_acudiente,nombre,apellido,telefono,clave)$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `registro_niño` (IN `idenficacion` VARCHAR(255), IN `nombre` VARCHAR(255), IN `apellido` VARCHAR(255), IN `genero` VARCHAR(255), IN `fecha_nacimiento` DATE, IN `parentesco_acudiente` VARCHAR(255), IN `cedula_acudiente` VARCHAR(255), IN `codigo_gurpo` VARCHAR(255))   INSERT INTO `niño`(`identificacion`, `nombre`, `apellido`, `edad`, `genero`, `fecha_nacimiento`,  `parentesco_acudiente`,`cedula_acudiente`,`codigo_grupo`,`estado`) VALUES (identificacion,nombre,apellido,fecha_nacimiento-now(),genero,fecha_nacimiento,parentesco_acudiente,cedula_acudiente,codigo_grupo,1)$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `acudiente`
--

CREATE TABLE `acudiente` (
  `cedula_acudiente` varchar(100) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `telefono` varchar(100) NOT NULL,
  `telefono_2` varchar(100) DEFAULT NULL,
  `acudiente_alternativo` varchar(100) DEFAULT NULL,
  `teléfono_alternativo` varchar(100) DEFAULT NULL,
  `clave` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
  `codigo_grupo` varchar(255) NOT NULL,
  `nombre_Insitucion` varchar(255) NOT NULL,
  `fecha_creacion` date NOT NULL,
  `codigo_anuncio` varchar(255) DEFAULT NULL,
  `cedula_docente` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `grupo`
--

INSERT INTO `grupo` (`codigo_grupo`, `nombre_Insitucion`, `fecha_creacion`, `codigo_anuncio`, `cedula_docente`) VALUES
('1', 'mapi', '2020-03-10', NULL, '2');

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
  `parentesco_acudiente` varchar(100) NOT NULL,
  `cedula_acudiente` varchar(100) NOT NULL,
  `codigo_grupo` varchar(100) NOT NULL
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
  ADD PRIMARY KEY (`codigo_grupo`),
  ADD KEY `Codigo_Anuncio` (`codigo_anuncio`),
  ADD KEY `Cedula_Docente` (`cedula_docente`);

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
  ADD CONSTRAINT `grupo_ibfk_1` FOREIGN KEY (`codigo_anuncio`) REFERENCES `anuncio` (`codigo_anuncio`),
  ADD CONSTRAINT `grupo_ibfk_2` FOREIGN KEY (`Cedula_Docente`) REFERENCES `docente` (`cedula_docente`),
  ADD CONSTRAINT `grupo_ibfk_3` FOREIGN KEY (`cedula_docente`) REFERENCES `docente` (`cedula_docente`),
  ADD CONSTRAINT `grupo_ibfk_4` FOREIGN KEY (`codigo_anuncio`) REFERENCES `anuncio` (`codigo_anuncio`);

--
-- Filtros para la tabla `niño`
--
ALTER TABLE `niño`
  ADD CONSTRAINT `niño_ibfk_1` FOREIGN KEY (`cedula_acudiente`) REFERENCES `acudiente` (`cedula_acudiente`),
  ADD CONSTRAINT `niño_ibfk_2` FOREIGN KEY (`codigo_grupo`) REFERENCES `grupo` (`codigo_grupo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
