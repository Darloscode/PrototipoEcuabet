create database proyecto;
use proyecto;

create table cliente(
id_usuario varchar(5) primary key not null, 
nombre varchar(30) not null, 
apellido varchar(30) not null, 
telefono char (10) not null, 
cedula char(10) not null,
edad int not null check (edad>18), 
ciudad_residencia varchar(25) not null,
provincia_residencia varchar(25) not null, 
email varchar(250) not null
);

create table cuenta_bancaria(
num_cuenta varchar(5) primary key not null, 
tipo_cuenta varchar(25) not null, 
cedula_dueño varchar(10) not null, 
banco varchar(100) not null, 
estado bool default true, 
id_usuario varchar(5) not null,
foreign key (id_usuario) references cliente(id_usuario)
);

create table movimiento_bancario(
num_movimiento varchar(5) not null,
tipo_movimiento varchar(25) not null,
estado bool default true , 
monto float not null, 
fecha_generacion date not null, 
id_usuario varchar(5) not null,
num_cuenta varchar(5) not null, 
foreign key (id_usuario) references cliente(id_usuario),
foreign key (num_cuenta) references cuenta_bancaria(num_cuenta)
);

create table juego_deportivo(
id_juego varchar(5) primary key not null,
categoria varchar(50) not null, 
liga varchar(50) not null, 
tipo_deporte varchar(15) not null
);

create table competidor(
id_competidor varchar(5) primary key not null, 
nombre varchar (25) not null
);

create table enfrentamiento_deportivo(
id_enfrentamiento varchar(5) primary key not null,
resultado varchar(250) default null,
fecha date not null,
id_juego varchar(5) not null,
id_competidora varchar(5) not null,
id_competidorb varchar(5) not null,
foreign key (id_juego) references juego_deportivo(id_juego),
foreign key (id_competidora) references competidor(id_competidor),
foreign key (id_competidorb) references competidor(id_competidor)
);

create table estadistica_deportiva(
id_estadistica varchar(5) primary key not null,
descripcion varchar(250) not null,
marcador varchar(250) not null,
id_enfrentamiento varchar(5) not null,
foreign key (id_enfrentamiento) references enfrentamiento_deportivo(id_enfrentamiento)
);

create table pronostico_deportivo(
id_pronostico varchar(5) primary key not null,
monto_apuesta float not null, 
valor_multiplicativo float not null check(valor_multiplicativo>0), 
ganancia float not null, 
fecha_apuesta float not null , 
id_usuario varchar(5) not null ,
id_enfrentamiento varchar(5) not null,
foreign key (id_usuario) references cliente(id_usuario),
foreign key (id_enfrentamiento) references enfrentamiento_deportivo(id_enfrentamiento)
);

create table sorteo(
    id_sorteo int primary key auto_increment not null,
    nombre varchar(100) not null,
    fechainicio date not null,
    fechafin date not null,
    estado boolean default true,
    cantidad_de_paradas int not null
);

create table cupones(
    id_cupon int primary key auto_increment not null,
    precio float not null,
    nombreDeUsuario varchar(5) not null,
    id_sorteo int not null,
    foreign key (nombreDeUsuario) references cliente(id_usuario),
    foreign key (id_sorteo) references sorteo(id_sorteo)
);

create table paradas(
    id_parada int primary key auto_increment not null,
    id_sorteo int not null,
    cupon_ganador int,
    fechasorteo date not null,
    premio varchar(100) not null,
    foreign key (id_sorteo) references sorteo(id_sorteo),
    foreign key (cupon_ganador) references cupones(id_cupon)
);


#Insertando datos en tabla Cliente
INSERT INTO cliente (id_usuario, nombre, apellido, telefono, cedula, edad, ciudad_residencia, provincia_residencia, email) VALUES 
    ('10001', 'Juan', 'Pérez', '5551234567', '1234567890', 25, 'Madrid', 'Madrid', 'juan.perez@example.com'),
    ('10002', 'María', 'Gómez', '4449876543', '0987654321', 30, 'Barcelona', 'Barcelona', 'maria.gomez@example.com'),
    ('10003', 'Carlos', 'Rodríguez', '3336549870', '1357924680', 22, 'Valencia', 'Valencia', 'carlos.rodriguez@example.com'),
    ('10004', 'Laura', 'López', '2225678901', '8642097531', 28, 'Sevilla', 'Sevilla', 'laura.lopez@example.com'),
    ('10005', 'Pedro', 'Martínez', '7772345678', '2468135790', 32, 'Málaga', 'Málaga', 'pedro.martinez@example.com'),
    ('10006', 'Ana', 'Fernández', '6667890123', '0246813579', 20, 'Bilbao', 'Vizcaya', 'ana.fernandez@example.com'),
    ('10007', 'Isabel', 'Ramírez', '8889012345', '9876543210', 27, 'Zaragoza', 'Zaragoza', 'isabel.ramirez@example.com'),
    ('10008', 'David', 'Sánchez', '9993456789', '0123456789', 24, 'Alicante', 'Alicante', 'david.sanchez@example.com'),
    ('10009', 'Paula', 'Torres', '1115678901', '9876543210', 29, 'Palma de Mallorca', 'Islas Baleares', 'paula.torres@example.com'),
    ('10010', 'Sergio', 'Ortega', '2228901234', '1234567890', 26, 'Córdoba', 'Córdoba', 'sergio.ortega@example.com');

#Insertando datos en tabla cuenta_bancaria
INSERT INTO cuenta_bancaria (num_cuenta, tipo_cuenta, cedula_dueño, banco, estado, id_usuario) VALUES 
    ('C001', 'Ahorros', '1234567890', 'Banco Pichincha', true, '10001'),
    ('C002', 'Corriente', '0987654321', 'Banco del Pacifico', true, '10002'),
    ('C003', 'Ahorros', '1357924680', 'Banco Guayaquil', true, '10003'),
    ('C004', 'Corriente', '8642097531', 'PRODUBANCO', true, '10004'),
    ('C005', 'Ahorros', '2468135790', 'BANCO AMAZONAS', true, '10005'),
    ('C006', 'Corriente', '0246813579', 'BANCO NACIONAL DE FOMENTO', true, '10006'),
    ('C007', 'Ahorros', '9876543210', 'BANCO CENTRAL DEL ECUADOR', true, '10007'),
    ('C008', 'Corriente', '0123456789', 'Banco Pichincha', true, '10008'),
    ('C009', 'Ahorros', '9876543210', 'Banco Guayaquil', true, '10009'),
    ('C010', 'Corriente', '1234567890', 'PRODUBANCO', true, '10010');

#Insertando datos en tabla movimiento_bancario
INSERT INTO movimiento_bancario (num_movimiento, tipo_movimiento, estado, monto, fecha_generacion, id_usuario, num_cuenta) VALUES 
    ('M001', 'Depósito', true, 1000.00, '2023-07-31', '10001', 'C001'),
    ('M002', 'Retiro', true, 500.00, '2023-07-31', '10002', 'C002'),
    ('M003', 'Depósito', true, 750.00, '2023-07-31', '10003', 'C003'),
    ('M004', 'Retiro', true, 300.00, '2023-07-31', '10004', 'C004'),
    ('M005', 'Transferencia', true, 200.00, '2023-07-31', '10005', 'C005'),
    ('M006', 'Transferencia', true, 150.00, '2023-07-31', '10006', 'C006'),
    ('M007', 'Depósito', true, 800.00, '2023-07-31', '10007', 'C007'),
    ('M008', 'Retiro', true, 100.00, '2023-07-31', '10008', 'C008'),
    ('M009', 'Depósito', true, 1200.00, '2023-07-31', '10009', 'C009'),
    ('M010', 'Retiro', true, 400.00, '2023-07-31', '10010', 'C010');
    
#Insertando datos en tabla juego_deportivo
INSERT INTO juego_deportivo (id_juego, categoria, liga, tipo_deporte) VALUES 
    ('JD001', 'Fútbol', 'Liga A', 'Fútbol Sala'),
    ('JD002', 'Baloncesto', 'Liga B', 'Baloncesto'),
    ('JD003', 'Tenis', 'Liga C', 'Individual'),
    ('JD004', 'Fútbol', 'Liga A', 'Fútbol 11'),
    ('JD005', 'Voleibol', 'Liga D', 'Voleibol Playa'),
    ('JD006', 'Baloncesto', 'Liga B', 'Baloncesto'),
    ('JD007', 'Atletismo', 'Liga E', 'Carrera'),
    ('JD008', 'Fútbol', 'Liga A', 'Fútbol Sala'),
    ('JD009', 'Tenis', 'Liga C', 'Dobles'),
    ('JD010', 'Voleibol', 'Liga D', 'Voleibol Sala');

#Insertar registros en la tabla "competidor"
INSERT INTO competidor (id_competidor, nombre) VALUES 
    ('C001', 'Competidor 1'),
    ('C002', 'Competidor 2'),
    ('C003', 'Competidor 3'),
    ('C004', 'Competidor 4'),
    ('C005', 'Competidor 5'),
    ('C006', 'Competidor 6'),
    ('C007', 'Competidor 7'),
    ('C008', 'Competidor 8'),
    ('C009', 'Competidor 9'),
    ('C010', 'Competidor 10');

#Insertar registros en la tabla "enfrentamiento_deportivo"
INSERT INTO enfrentamiento_deportivo (id_enfrentamiento, resultado, fecha, id_juego, id_competidora, id_competidorb) VALUES 
    ('E001', '3-2', '2023-07-31', 'JD001', 'C001', 'C002'),
    ('E002', '90-85', '2023-07-31', 'JD002', 'C003', 'C004'),
    ('E003', '6-4, 6-3', '2023-07-31', 'JD003', 'C005', 'C006'),
    ('E004', '2-1', '2023-07-31', 'JD004', 'C007', 'C008'),
    ('E005', '21-18, 16-21, 15-10', '2023-07-31', 'JD005', 'C009', 'C010'),
    ('E006', '100m: 10.32s', '2023-07-31', 'JD006', 'C001', 'C002'),
    ('E007', '800m: 1:54.67', '2023-07-31', 'JD007', 'C003', 'C004'),
    ('E008', '5-0', '2023-07-31', 'JD008', 'C005', 'C006'),
    ('E009', '6-1, 6-3', '2023-07-31', 'JD009', 'C007', 'C008'),
    ('E010', '25-20, 18-25, 15-13', '2023-07-31', 'JD010', 'C009', 'C010');

-- Insertar registros en la tabla "estadistica_deportiva"
INSERT INTO estadistica_deportiva (id_estadistica, descripcion, marcador, id_enfrentamiento) VALUES 
    ('ES001', 'Puntos anotados por jugador A', '28 puntos', 'E001'),
    ('ES002', 'Puntos anotados por jugador B', '25 puntos', 'E001'),
    ('ES003', 'Rebotes totales del equipo A', '42 rebotes', 'E001'),
    ('ES004', 'Rebotes totales del equipo B', '37 rebotes', 'E001'),
    ('ES005', 'Aciertos de triples equipo A', '6 triples', 'E001'),
    ('ES006', 'Aciertos de triples equipo B', '5 triples', 'E001'),
    ('ES007', 'Juegos de saque directo de jugadora A', '2 saques directos', 'E002'),
    ('ES008', 'Juegos de saque directo de jugadora B', '1 saque directo', 'E002'),
    ('ES009', 'Errores no forzados jugador A', '20 errores', 'E002'),
    ('ES010', 'Errores no forzados jugador B', '15 errores', 'E002');
    
-- Insertar registros en la tabla "pronostico_deportivo"
INSERT INTO pronostico_deportivo (id_pronostico, monto_apuesta, valor_multiplicativo, ganancia, fecha_apuesta, id_usuario, id_enfrentamiento) VALUES 
    ('P001', 50.00, 1.75, 87.50, '2023-07-31', '10001', 'E001'),
    ('P002', 30.00, 2.25, 67.50, '2023-07-31', '10002', 'E001'),
    ('P003', 25.00, 1.90, 47.50, '2023-07-31', '10003', 'E001'),
    ('P004', 40.00, 1.50, 60.00, '2023-07-31', '10004', 'E001'),
    ('P005', 20.00, 2.10, 42.00, '2023-07-31', '10005', 'E002'),
    ('P006', 35.00, 1.80, 63.00, '2023-07-31', '10006', 'E002'),
    ('P007', 15.00, 2.50, 37.50, '2023-07-31', '10007', 'E002'),
    ('P008', 60.00, 1.40, 84.00, '2023-07-31', '10008', 'E003'),
    ('P009', 75.00, 1.30, 97.50, '2023-07-31', '10009', 'E003'),
    ('P010', 100.00, 1.20, 120.00, '2023-07-31', '10010', 'E004');
   
#Insertando datos en tabla Sorteo
INSERT INTO sorteo (nombre, fechainicio, fechafin, estado, cantidad_de_paradas) VALUES
    ('Sorteo 1', '2023-07-05', '2023-09-03', false, 5),
    ('Sorteo 2', '2023-07-10', '2023-09-08', false, 6),
    ('Sorteo 3', '2023-07-15', '2023-09-13', false, 5),
    ('Sorteo 4', '2023-07-20', '2023-09-18', false, 6),
    ('Sorteo 5', '2023-07-25', '2023-09-23', false, 5),
    ('Sorteo 6', '2023-07-25', '2023-09-23', false, 5),
    ('Sorteo 7', '2023-07-25', '2023-09-23', false, 5),
    ('Sorteo 8', '2023-07-25', '2023-09-23', false, 5),
    ('Sorteo 9', '2023-07-25', '2023-09-23', false, 5),
    ('Sorteo 10', '2023-07-25', '2023-09-23', false, 5);
    
    
#Insertando datos en tabla Cupones
INSERT INTO cupones (precio, nombredeusuario, id_sorteo) VALUES 
-- Sorteo 1
    (2, '10001', 1),
    (2, '10002', 1),
    (2, '10003', 1),
    (2, '10004', 1),
    (2, '10005', 1),
    (2, '10006', 1),
    (2, '10007', 1),
    (2, '10008', 1),
    (2, '10009', 1),
    (2, '10010', 1),
    -- Sorteo 2
    (2, '10001', 2),
    (2, '10002', 2),
    (2, '10003', 2),
    (2, '10004', 2),
    (2, '10005', 2),
    (2, '10006', 2),
    (2, '10007', 2),
    (2, '10008', 2),
    (2, '10009', 2),
    (2, '10010', 2),
    -- Sorteo 3
    (4, '10001', 3),
    (4, '10002', 3),
    (4, '10003', 3),
    (4, '10004', 3),
    (4, '10005', 3),
    (4, '10006', 3),
    (4, '10007', 3),
    (4, '10008', 3),
    (4, '10009', 3),
    (4, '10010', 3),
    -- Sorteo 4
    (2, '10001', 4),
    (2, '10002', 4),
    (2, '10003', 4),
    (2, '10004', 4),
    (2, '10005', 4),
    (2, '10006', 4),
    (2, '10007', 4),
    (2, '10008', 4),
    (2, '10009', 4),
    (2, '10010', 4),
    -- Sorteo 5
    (2, '10001', 5),
    (2, '10002', 5),
    (2, '10003', 5),
    (2, '10004', 5),
    (2, '10005', 5),
    (2, '10006', 5),
    (2, '10007', 5),
    (2, '10008', 5),
    (2, '10009', 5),
    (2, '10010', 5);

#Insertando datos en tabla Parada
INSERT INTO paradas (ID_SORTEO, cupon_ganador,fechasorteo, premio) VALUES
-- Sorteo 1
    (1,6,'2023-07-05','camiseta de ecuador'),
    (1,3,'2023-07-20','camiseta de ecuador'),
    (1,1,'2023-08-04','camiseta de ecuador'),
    (1,7,'2023-08-19','camiseta de ecuador'),
    (1,10,'2023-09-03','viaje a galápagos'),
-- Sorteo 2
	(2,6,'2023-07-10','camiseta de ecuador'),
    (2,5,'2023-07-20','camiseta de barcelona/emelec/liga de quito o independiente del valle'),
    (2,3,'2023-08-04','camiseta de ecuador'),
    (2,4,'2023-08-19','10 dolares'),
    (2,1,'2023-09-03','50 dolares de bono sin rollOver'),
    (2,2,'2023-09-08','meet and great con chito vera'),
-- Sorteo 3
    (3,6,'2023-07-15','10 dolares en bono'),
    (3,3,'2023-07-20','camiseta autografíada por chito vera'),
    (3,1,'2023-08-04','camiseta de barcelona/emelec/liga de quito o independiente del valle'),
    (3,7,'2023-08-19','camiseta de ecuador'),
    (3,10,'2023-09-13','entrada y viaje (todo incluido) 2 personas a la ufc300'),
-- Sorteo 4
	(4,6,'2023-07-20','camiseta de ecuador'),
    (4,5,'2023-07-26','camiseta de barcelona/emelec/liga de quito o independiente del valle'),
    (4,3,'2023-08-04','camiseta de ecuador'),
    (4,4,'2023-08-19','10 dolares'),
    (4,1,'2023-09-03','50 dolares de bono sin rollOver'),
    (4,2,'2023-09-18','1 suit en el monumental para el partido barcelona-emelec'),
-- Sorteo 5
    (5,6,'2023-07-25','camiseta de ecuador'),
    (5,3,'2023-08-1','camiseta de argentina'),
    (5,1,'2023-08-17','camiseta de portugal'),
    (5,7,'2023-09-1','camiseta de brasil'),
    (5,10,'2023-09-23','meet and great con messi');