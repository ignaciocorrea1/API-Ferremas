-- FerremasBD

-- DROP DATABSE Ferremas;
CREATE DATABASE Ferremas;
USE  Ferremas;

-- Drops
-- DROP TABLE IF EXISTS Marca;
-- DROP TABLE IF EXISTS Tipo_Producto;
-- DROP TABLE IF EXISTS Producto;
-- DROP TABLE IF EXISTS Tipo_Usuario;
-- DROP TABLE IF EXISTS Usuario;
-- DROP TABLE IF EXISTS Pedido;
-- DROP TABLE IF EXISTS Detalle_Pedido;
-- DROP TABLE IF EXISTS Pago;

-- Tablas
CREATE TABLE Marca (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE Tipo_Producto (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE Producto (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    marca_producto INT NOT NULL,
    tipo_producto_id INT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(300) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    imagen VARCHAR(200) NOT NULL, -- URL
    stock INT NOT NULL,
    FOREIGN KEY (marca_producto) REFERENCES Marca(id),
    FOREIGN KEY (tipo_producto_id) REFERENCES Tipo_Producto(id)
);

CREATE TABLE Tipo_Usuario (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE Usuario (
    rut VARCHAR(12) PRIMARY KEY NOT NULL,
    dv VARCHAR(1) NOT NULL,
    tipo_usuario_id INT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    correo VARCHAR(50) NOT NULL,
    contrasenia VARCHAR(255) NOT NULL,
    direccion VARCHAR(100) NOT NULL,
    telefono VARCHAR(15) NOT NULL,
    FOREIGN KEY (tipo_usuario_id) REFERENCES Tipo_Usuario(id)
);

CREATE TABLE Pedido (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    fecha DATE NOT NULL,
    cliente_id VARCHAR(12) NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES Usuario(rut)
);

CREATE TABLE Detalle_Pedido (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    pedido_id INT NOT NULL,
    producto_id INT NOT NULL,
    cantidad INT NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES Pedido(id),
    FOREIGN KEY (producto_id) REFERENCES Producto(id)
);

CREATE TABLE Pago (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    pedido_id INT NOT NULL,
    cliente_id VARCHAR(12) NOT NULL, 
    total DECIMAL(10, 2) NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado VARCHAR(50) NOT NULL,
    token VARCHAR(255), 
    tipo VARCHAR(50) NOT NULL, 
    FOREIGN KEY (pedido_id) REFERENCES Pedido(id),
    FOREIGN KEY (cliente_id) REFERENCES Usuario(rut)  
);

-- Inserción datos prueba
INSERT INTO Marca (nombre) VALUES
('Bosch'),
('Makita'),
('Stanley');

INSERT INTO Tipo_Producto (nombre) VALUES
('Taladro'),
('Sierra'),
('Lijadora');

INSERT INTO Producto (marca_producto, tipo_producto_id, nombre, descripcion, precio, imagen, stock) VALUES
(1, 1, 'Taladro Inalámbrico Bosch', 'Taladro inalámbrico 18V con batería de litio.', 89990.00, 'url_prueba', 15),
(2, 2, 'Sierra Circular Makita', 'Sierra circular 1200W con disco de 7 pulgadas.', 129990.00, 'url_prueba', 10),
(3, 3, 'Lijadora Orbital Stanley', 'Lijadora orbital para acabados finos y madera.', 54990.00, 'url_prueba', 20),
(1, 2, 'Sierra Caladora Bosch', 'Sierra caladora de precisión para cortes curvos.', 74990.00, 'url_prueba', 12),
(2, 1, 'Taladro Percutor Makita', 'Taladro percutor de alto rendimiento para hormigón.', 99990.00, 'url_prueba', 8);