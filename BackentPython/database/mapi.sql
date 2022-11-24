-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 24-11-2022 a las 05:52:11
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
CREATE DEFINER=`root`@`localhost` PROCEDURE `actualizar_informacion_niño` (`identificacion` VARCHAR(100), `nombre` VARCHAR(100), `apellido` VARCHAR(100), `genero` VARCHAR(100), `fecha_nacimiento` DATE, `parentesco` VARCHAR(100))   UPDATE `niño` SET `nombre`=nombre,`apellido`=apellido,`genero`=genero,`fecha_nacimiento`=fecha_nacimiento,`parentesco`=parentesco WHERE `identificacion`=identificacion$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `actualizar_informacio_acudiente` (IN `cedula_acudiente` VARCHAR(255), IN `nombre` VARCHAR(255), IN `apellido` VARCHAR(255), IN `telefono` VARCHAR(255), IN `telefono_2` VARCHAR(255), IN `acudiente_alternativo` VARCHAR(255))   UPDATE `acudiente` SET `nombre`=nombre,`apellido`=apellido,`telefono`=telefono,`telefono_2`=telefono_2,`acudiente_alternativo`=acudiente_alternativo WHERE `cedula_acudiente`=cedula_acudiente$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `actulizar_clave_acudiente` (`clave` VARCHAR(100), `cedula_acudiente` VARCHAR(100))   UPDATE `acudiente` SET `clave`=clave WHERE `cedula_acudiente`=cedula_acudiente$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `deshabilitar_estado_niño` (`identificacion` VARCHAR(100))   UPDATE `niño` SET `estado`=0 WHERE `identificacion`=identificacion$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `eliminar_acudiente` (`cedula_acudiente` VARCHAR(255))   DELETE FROM `acudiente` WHERE `cedula_acudiente`=cedula_acudiente$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `eliminar_niño` (`identificacion` VARCHAR(100))   DELETE FROM `niño` WHERE `identificacion`=identificacion$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `listar_acudiente` (`cedula_acudiente` VARCHAR(100))   SELECT * FROM `acudiente`  WHERE `cedula_acudiente`=cedula_acudiente$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `listar_acudientes` ()   SELECT * FROM `acudiente`$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `listar_niño` (`identificacion` VARCHAR(100))   SELECT * FROM `niño`  WHERE `identificacion`=identificacion$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `listar_niños` ()   SELECT * FROM `niño`$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `registragrpo` (`Nombre_Grupo` VARCHAR(100), `codigo_grupo` VARCHAR(255), `nombre_Insitucion` VARCHAR(255), `fecha_creacion` DATE, `cedula_docente` VARCHAR(255))   INSERT INTO `grupos`(`Nombre_Grupo`, `codigo_grupo`, `nombre_Insitucion`, `fecha_creacion`, `cedula_docente`) VALUES
  (Nombre_Grupo,codigo_grupo,nombre_Insitucion,fecha_creacion,cedula_docente)$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `registro_acudiente` (`cedula_acudiente` VARCHAR(255), `nombre` VARCHAR(255), `apellido` VARCHAR(255), `telefono` VARCHAR(255), `clave` VARCHAR(255))   INSERT INTO `acudiente`(`cedula_acudiente`, `nombre`, `apellido`, `telefono`, `clave`) VALUES (cedula_acudiente,nombre,apellido,telefono,clave)$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `registro_niño` (`identificacion` VARCHAR(255), `nombre` VARCHAR(255), `apellido` VARCHAR(255), `edad` INT(50), `genero` VARCHAR(255), `fecha_nacimiento` DATE, `parentesco_acudiente` VARCHAR(255), `cedula_acudiente` VARCHAR(255), `codigo_grupo` VARCHAR(255))   INSERT INTO `niño`(`identificacion`, `nombre`, `apellido`, `edad`, `genero`, `fecha_nacimiento`, `parentesco_acudiente`,`cedula_acudiente`,`codigo_grupo`,`estado`) VALUES (identificacion,nombre,apellido,edad,genero,fecha_nacimiento,parentesco_acudiente,cedula_acudiente,codigo_grupo,1)$$

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

--
-- Volcado de datos para la tabla `acudiente`
--

INSERT INTO `acudiente` (`cedula_acudiente`, `nombre`, `apellido`, `telefono`, `telefono_2`, `acudiente_alternativo`, `teléfono_alternativo`, `clave`) VALUES
('1', '1', '1', '1', NULL, NULL, NULL, '1');

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

--
-- Volcado de datos para la tabla `anuncio`
--

INSERT INTO `anuncio` (`codigo_anuncio`, `descripcion`, `fecha_creacion`, `multimedia`) VALUES
('222', 'hika', '2022-11-22', 'nada');

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
-- Estructura de tabla para la tabla `grupos`
--

CREATE TABLE `grupos` (
  `Nombre_Grupo` varchar(100) NOT NULL,
  `codigo_grupo` varchar(255) NOT NULL,
  `nombre_Insitucion` varchar(255) NOT NULL,
  `fecha_creacion` date NOT NULL,
  `cedula_docente` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `grupos`
--

INSERT INTO `grupos` (`Nombre_Grupo`, `codigo_grupo`, `nombre_Insitucion`, `fecha_creacion`, `cedula_docente`) VALUES
('ca', '32323', 'sena', '2022-11-23', '2');

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
  `cedula_acudiente` varchar(100) DEFAULT NULL,
  `codigo_grupo` varchar(100) DEFAULT NULL,
  `estado` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `niño`
--

INSERT INTO `niño` (`identificacion`, `nombre`, `apellido`, `edad`, `genero`, `fecha_nacimiento`, `parentesco_acudiente`, `cedula_acudiente`, `codigo_grupo`, `estado`) VALUES
('1', '1', '1', 12, 'femenino', '2010-01-01', 'padre', '1', '1', 1),
('2', '2', '22', 22, 'maculino', '2022-11-01', 'padre', '1', '1', 1),
('3', '2', '22', 22, 'maculino', '2022-11-01', 'padre', '1', '1', 1),
('4', '4', '4', 12, 'femenino', '2010-01-01', 'tio', '1', '1', 1);

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
-- Indices de la tabla `grupos`
--
ALTER TABLE `grupos`
  ADD PRIMARY KEY (`codigo_grupo`),
  ADD KEY `cedula_docente` (`cedula_docente`);

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
-- Filtros para la tabla `grupos`
--
ALTER TABLE `grupos`
  ADD CONSTRAINT `grupos_ibfk_1` FOREIGN KEY (`cedula_docente`) REFERENCES `docente` (`cedula_docente`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
