CREATE DATABASE andamios;
use andamios;

CREATE TABLE detallesAndamios
(codigo int primary key auto_increment not null,
peso int,
modulos int,
garantia varchar(255),
material varchar(255),
ancho float,
uso varchar(255),
cubrimientoGarantia varchar(255),
cargaMaxima float,
altura float,	
color varchar(255),
capacidadCarga float,
largo float,
caracteristicas text,
observacionesAdicionales varchar(255),
recomendaciones varchar(255),
origen varchar(50)
);

CREATE TABLE empresas
(rut float primary key not null,
nombreEmpresa varchar(255),
ubicacion varchar(255),
telefonoEmpresa int,
añosDeServicio float,
nombreAdministrador varchar(255),
telefonoAdministrador float,
cedulaAdministrador float,
correoAdministrador varchar(120) unique key,
contraseñaAdministrador varchar(100)
);

CREATE TABLE particulares
(cedulaParticular float primary key not null,
nombreParticular varchar(255),
telefonoParticular float,
residenciaParticular varchar(255)
);

CREATE TABLE descuentosCategoria
(identificacion float primary key not null,
categoria varchar(1)
);

CREATE TABLE facturas
(codigoFactura int primary key auto_increment not null,
nombreEmpresa varchar(255),
categoriaAdministradorOParticular varchar(1),
nombreAdministradorEmpresaOParticular varchar(255),
ubicacionEmpresa varchar(255),
fechaFactura datetime,
telefonoAdministrador float,
descripcionCompra varchar(255),
estadoAndamio varchar(50),
cantidadAndamios int,
cantidadModulos int,
totalAPagar float
);

CREATE TABLE alquiler
(codigoEmpresa int primary key auto_increment not null,
rut float not null,
nombreEmpresa varchar(150),
telefonoEmpresa float,
cantidadModulos int,
tiempoAlquiler varchar(100),
ubicacion varchar(150),
hora time,
transporte varchar(2)
);

ALTER TABLE alquiler add constraint alq_RUT
foreign key alquiler_rut(rut)
references empresas (rut);

alter table alquiler modify column tiempoAlquiler varchar(100);

Create table alquiler_Particulares(
codigoParticular int primary key auto_increment not null,
nombreParticular varchar(255),
residenciaParticular varchar(255),
telefonoParticular int,
solicitudAlquilerP varchar(100),
cantidadModulos int,
tiempoAlquiler varchar(100),
transporte varchar(10),
hora varchar(100)
);

Create table administrador(
codigoAdministrador int primary key auto_increment not null,
contraseñaAdministrador int,
correoAdministrador varchar(155),
nombreAdministrador varchar(155)
);

