-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 13-09-2021 a las 08:01:25
-- Versión del servidor: 10.4.11-MariaDB
-- Versión de PHP: 7.2.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `votaciones`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `barrio`
--

CREATE TABLE `barrio` (
  `idBarrio` int(11) NOT NULL,
  `nombreBarrio` varchar(30) NOT NULL,
  `comunaId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `barrio`
--

INSERT INTO `barrio` (`idBarrio`, `nombreBarrio`, `comunaId`) VALUES
(1, 'chiquinquira', 1),
(2, 'La Pradera', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comuna`
--

CREATE TABLE `comuna` (
  `idComuna` int(11) NOT NULL,
  `nombreComuna` varchar(30) NOT NULL,
  `municipioId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `comuna`
--

INSERT INTO `comuna` (`idComuna`, `nombreComuna`, `municipioId`) VALUES
(1, 'Centro', 1),
(2, 'Olivos', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cordenadas`
--

CREATE TABLE `cordenadas` (
  `idcordenadas` int(11) NOT NULL,
  `latitud` varchar(20) NOT NULL,
  `longitud` varchar(20) NOT NULL,
  `ente` varchar(20) NOT NULL,
  `identidicdor` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `cordenadas`
--

INSERT INTO `cordenadas` (`idcordenadas`, `latitud`, `longitud`, `ente`, `identidicdor`) VALUES
(1, '10.9697484', '-74.78974509999999', 'lider', 18),
(4, '10.9421217', '-74.792118', 'puesto', 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamentos`
--

CREATE TABLE `departamentos` (
  `idDepartamento` int(11) NOT NULL,
  `nombreDepartamento` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `departamentos`
--

INSERT INTO `departamentos` (`idDepartamento`, `nombreDepartamento`) VALUES
(1, 'Atlantico'),
(2, 'Magdalena'),
(10, 'Cesar');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historialvotante`
--

CREATE TABLE `historialvotante` (
  `idhistorial` int(11) NOT NULL,
  `fecha` datetime NOT NULL DEFAULT current_timestamp(),
  `votanteid` bigint(20) NOT NULL,
  `lider` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `historialvotante`
--

INSERT INTO `historialvotante` (`idhistorial`, `fecha`, `votanteid`, `lider`) VALUES
(1, '0000-00-00 00:00:00', 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `municipio`
--

CREATE TABLE `municipio` (
  `idMunicipio` int(11) NOT NULL,
  `nombreMunicipio` varchar(30) NOT NULL,
  `depId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `municipio`
--

INSERT INTO `municipio` (`idMunicipio`, `nombreMunicipio`, `depId`) VALUES
(1, 'Barranquilla', 1),
(2, 'Soledad', 1),
(5, 'Baranoa', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personas`
--

CREATE TABLE `personas` (
  `ccPersona` bigint(20) NOT NULL,
  `nombres` varchar(20) NOT NULL,
  `apellidos` varchar(20) NOT NULL,
  `direccion` varchar(30) NOT NULL,
  `cel` varchar(20) NOT NULL,
  `barrio` int(11) NOT NULL,
  `comuna` int(11) NOT NULL,
  `ciudad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `personas`
--

INSERT INTO `personas` (`ccPersona`, `nombres`, `apellidos`, `direccion`, `cel`, `barrio`, `comuna`, `ciudad`) VALUES
(1111, 'uno', 'ape 1', 'kara 1', '12345678', 1, 1, 1),
(1234, 'usuario 1', 'apellido 1', 'calle 1 kr 1', '12345678', 1, 1, 1),
(4321, 'usuario 3', 'apellido 3', 'calle 1 kr 1', '12345678', 1, 1, 1),
(12345, 'usuario 2', 'apellido 2', 'calle 45 27-30', '12345678', 1, 1, 1),
(77167709, 'roland', 'osorio', 'carrera 27 # 43 06', '2345666', 1, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `puestovotacion`
--

CREATE TABLE `puestovotacion` (
  `idpuesto` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `direccion` varchar(30) NOT NULL,
  `municipioid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `puestovotacion`
--

INSERT INTO `puestovotacion` (`idpuesto`, `nombre`, `direccion`, `municipioid`) VALUES
(1, 'jesus', 'calle a', 2),
(4, 'colegio marco fidel suarez', 'calle 33 ', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `idrol` smallint(6) NOT NULL,
  `nonbrerol` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`idrol`, `nonbrerol`) VALUES
(1, 'lider'),
(2, 'admin');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `idUsuario` int(11) NOT NULL,
  `ccUsuario` bigint(20) NOT NULL,
  `passw` varchar(90) NOT NULL,
  `rolid` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`idUsuario`, `ccUsuario`, `passw`, `rolid`) VALUES
(1, 1234, 'sha256$D1J4Qp7f$cde61b159ab6dd25a527d65e50085b33d8ab5d94300f0bb234112f8095bf626e', 1),
(19, 12345, 'sha256$MYp0rnCV$dcc0b2e949fe8e68b4996e623d51f9007e5f1c668dfb38ead900e939a3640c43', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `votante`
--

CREATE TABLE `votante` (
  `idVonatentes` int(11) NOT NULL,
  `perosonacc` bigint(20) NOT NULL,
  `liderId` bigint(20) NOT NULL,
  `barrioId` int(11) NOT NULL,
  `puestoVotaId` int(11) NOT NULL,
  `mesa` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `votante`
--

INSERT INTO `votante` (`idVonatentes`, `perosonacc`, `liderId`, `barrioId`, `puestoVotaId`, `mesa`) VALUES
(1, 77167709, 1234, 1, 4, 1),
(2, 4321, 1234, 1, 4, 1),
(11, 1111, 1234, 1, 1, 2);

--
-- Disparadores `votante`
--
DELIMITER $$
CREATE TRIGGER `logvotante` AFTER INSERT ON `votante` FOR EACH ROW INSERT INTO `historialvotante` (`idhistorial`, `fecha`, `votanteid`, `lider`) VALUES (NULL, current_timestamp(), NEW.perosonacc,NEW.liderId)
$$
DELIMITER ;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `barrio`
--
ALTER TABLE `barrio`
  ADD PRIMARY KEY (`idBarrio`),
  ADD KEY `comunaId` (`comunaId`);

--
-- Indices de la tabla `comuna`
--
ALTER TABLE `comuna`
  ADD PRIMARY KEY (`idComuna`),
  ADD KEY `municipioId` (`municipioId`);

--
-- Indices de la tabla `cordenadas`
--
ALTER TABLE `cordenadas`
  ADD PRIMARY KEY (`idcordenadas`),
  ADD KEY `identidicdor` (`identidicdor`);

--
-- Indices de la tabla `departamentos`
--
ALTER TABLE `departamentos`
  ADD PRIMARY KEY (`idDepartamento`);

--
-- Indices de la tabla `historialvotante`
--
ALTER TABLE `historialvotante`
  ADD PRIMARY KEY (`idhistorial`);

--
-- Indices de la tabla `municipio`
--
ALTER TABLE `municipio`
  ADD PRIMARY KEY (`idMunicipio`),
  ADD KEY `depId` (`depId`);

--
-- Indices de la tabla `personas`
--
ALTER TABLE `personas`
  ADD PRIMARY KEY (`ccPersona`);

--
-- Indices de la tabla `puestovotacion`
--
ALTER TABLE `puestovotacion`
  ADD PRIMARY KEY (`idpuesto`),
  ADD KEY `municipioid` (`municipioid`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`idrol`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD UNIQUE KEY `idUsuario` (`idUsuario`),
  ADD UNIQUE KEY `ccUsuario` (`ccUsuario`),
  ADD KEY `rolid` (`rolid`);

--
-- Indices de la tabla `votante`
--
ALTER TABLE `votante`
  ADD PRIMARY KEY (`idVonatentes`),
  ADD UNIQUE KEY `perosonacc` (`perosonacc`),
  ADD KEY `liderId` (`liderId`),
  ADD KEY `barrioId` (`barrioId`),
  ADD KEY `puestoVotaId` (`puestoVotaId`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `barrio`
--
ALTER TABLE `barrio`
  MODIFY `idBarrio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `comuna`
--
ALTER TABLE `comuna`
  MODIFY `idComuna` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `cordenadas`
--
ALTER TABLE `cordenadas`
  MODIFY `idcordenadas` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `departamentos`
--
ALTER TABLE `departamentos`
  MODIFY `idDepartamento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `historialvotante`
--
ALTER TABLE `historialvotante`
  MODIFY `idhistorial` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `municipio`
--
ALTER TABLE `municipio`
  MODIFY `idMunicipio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `puestovotacion`
--
ALTER TABLE `puestovotacion`
  MODIFY `idpuesto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `idrol` smallint(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `idUsuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de la tabla `votante`
--
ALTER TABLE `votante`
  MODIFY `idVonatentes` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `barrio`
--
ALTER TABLE `barrio`
  ADD CONSTRAINT `bar-com` FOREIGN KEY (`comunaId`) REFERENCES `comuna` (`idComuna`);

--
-- Filtros para la tabla `comuna`
--
ALTER TABLE `comuna`
  ADD CONSTRAINT `com-mun` FOREIGN KEY (`municipioId`) REFERENCES `municipio` (`idMunicipio`);

--
-- Filtros para la tabla `municipio`
--
ALTER TABLE `municipio`
  ADD CONSTRAINT `mun-dep` FOREIGN KEY (`depId`) REFERENCES `departamentos` (`idDepartamento`);

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `rol-user` FOREIGN KEY (`rolid`) REFERENCES `roles` (`idrol`),
  ADD CONSTRAINT `use-per` FOREIGN KEY (`ccUsuario`) REFERENCES `personas` (`ccPersona`);

--
-- Filtros para la tabla `votante`
--
ALTER TABLE `votante`
  ADD CONSTRAINT `barrio` FOREIGN KEY (`barrioId`) REFERENCES `barrio` (`idBarrio`),
  ADD CONSTRAINT `lider` FOREIGN KEY (`liderId`) REFERENCES `usuarios` (`ccUsuario`),
  ADD CONSTRAINT `pues-per` FOREIGN KEY (`perosonacc`) REFERENCES `personas` (`ccPersona`),
  ADD CONSTRAINT `puuesto` FOREIGN KEY (`puestoVotaId`) REFERENCES `puestovotacion` (`idpuesto`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
