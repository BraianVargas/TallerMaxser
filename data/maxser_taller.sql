-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 20-09-2021 a las 15:59:03
-- Versión del servidor: 10.4.19-MariaDB
-- Versión de PHP: 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `maxser_taller`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `equipos`
--

CREATE TABLE `equipos` (
  `id` int(9) NOT NULL,
  `Marca` varchar(15) NOT NULL,
  `Problema` varchar(100) NOT NULL,
  `Tipo` varchar(16) NOT NULL,
  `Accesorios` varchar(20) NOT NULL,
  `Estado` varchar(20) DEFAULT NULL,
  `Password` varchar(50) DEFAULT NULL,
  `Backup` varchar(10) DEFAULT NULL,
  `Fecha` date NOT NULL DEFAULT current_timestamp(),
  `Owner` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`Owner`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `equipos`
--

INSERT INTO `equipos` (`id`, `Marca`, `Problema`, `Tipo`, `Accesorios`, `Estado`, `Password`, `Backup`, `Fecha`, `Owner`) VALUES
(88, 'Lenovo', 'No enciende', 'Notebook', 'Bateria', 'En espera', 'maxser2021', 'Si', '2021-08-22', '41830596'),
(89, 'Lenovo', 'No enciende', 'Notebook', 'Cargador', 'En espera', 'maxser2021', 'Si', '2021-08-22', '41830596'),
(90, 'Lenovo', 'No enciende', 'Netbook', 'Bateria', 'En espera', '12345', 'Si', '2021-08-22', '41830597'),
(91, 'Lenovo', 'No enciende', 'Notebook', 'Cargador', 'En espera', 'maxser2021', 'Si', '2021-08-22', '41830596'),
(92, 'Bangho', 'ad', 'Notebook', 'Bateria', 'En espera', '12345', 'No', '2021-09-15', '41830596'),
(93, 'MSI', 'No enciende', 'Netbook', 'Ninguno', 'En espera', '', 'No', '2021-09-16', '41830598'),
(94, 'Lenovo', 'No carga', 'Notebook', 'Cargador', 'En espera', '', 'No', '2021-09-18', '41830596');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `Nombre` varchar(80) NOT NULL,
  `Password` varchar(100) DEFAULT NULL,
  `DNI` int(55) NOT NULL,
  `Telefono` int(45) NOT NULL,
  `Equipos` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`Equipos`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Tabla de usuarios';

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`Nombre`, `Password`, `DNI`, `Telefono`, `Equipos`) VALUES
('maxsersj', 'b185beabbb33578cdd4936c78384b20d', 1111, 1111, NULL),
('Braian Alberto Vargas', NULL, 41830596, 0, NULL),
('Braian Alberto', NULL, 41830597, 0, NULL),
('juanma herrrero', NULL, 41830598, 2147483647, NULL);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `equipos`
--
ALTER TABLE `equipos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`DNI`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `equipos`
--
ALTER TABLE `equipos`
  MODIFY `id` int(9) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=95;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
