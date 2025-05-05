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

CREATE TABLE Tipo_Usuario (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE Producto (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(300) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    imagen VARCHAR(200) NOT NULL, -- URL
    stock INT NOT NULL,
    garantia INT NOT NULL,
    marca_producto INT NOT NULL,
    tipo_producto_id INT NOT NULL,
    FOREIGN KEY (marca_producto) REFERENCES Marca(id),
    FOREIGN KEY (tipo_producto_id) REFERENCES Tipo_Producto(id)
);

CREATE TABLE Usuario (
    rut VARCHAR(12) PRIMARY KEY NOT NULL,
    dv VARCHAR(1) NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    correo VARCHAR(50) NOT NULL,
    contrasenia VARCHAR(255) NOT NULL,
    direccion VARCHAR(100) NOT NULL,
    telefono VARCHAR(15) NOT NULL,
    tipo_usuario_id INT NOT NULL,
    FOREIGN KEY (tipo_usuario_id) REFERENCES Tipo_Usuario(id)
);

CREATE TABLE Pedido (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    fecha DATE NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    cliente_id VARCHAR(12) NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES Usuario(rut)
);

CREATE TABLE Detalle_Pedido (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    cantidad INT NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    pedido_id INT NOT NULL,
    producto_id INT NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES Pedido(id),
    FOREIGN KEY (producto_id) REFERENCES Producto(id)
);

CREATE TABLE Pago (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    pedido_id INT NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado VARCHAR(50) NOT NULL,
    token VARCHAR(255), 
    tipo VARCHAR(50) NOT NULL, 
    cliente_id VARCHAR(12) NOT NULL, 
    FOREIGN KEY (pedido_id) REFERENCES Pedido(id),
    FOREIGN KEY (cliente_id) REFERENCES Usuario(rut)  
);

-- Inserción datos prueba
INSERT INTO Marca (nombre) VALUES
("Bosch"),
("Makita"),
("Stanley");

INSERT INTO Tipo_Producto (nombre) VALUES
("Taladro"),
("Sierra"),
("Lijadora");

INSERT INTO Producto (nombre, descripcion, precio, imagen, stock, garantia, marca_producto, tipo_producto_id) VALUES
("Taladro Inalámbrico Bosch", "Taladro inalámbrico 18V con batería de litio.", 89990.00, "https://inalambricoschile.vtexassets.com/arquivos/ids/163840-800-auto?v=638087858680030000&width=800&height=auto&aspect=true", 15, 6, 1, 1),
("Sierra Circular Makita", "Sierra circular 1200W con disco de 7 pulgadas.", 129990.00, "https://www.dimarsa.cl/media/catalog/product/1/_/1_13.jpg", 10, 6, 2, 2),
("Lijadora Orbital Stanley", "Lijadora orbital para acabados finos y madera.", 54990.00, "https://easycl.vteximg.com.br/arquivos/ids/4973288/1279178-0000-001.jpg?v=638742015718900000", 20, 6, 3, 3),
("Sierra Caladora Bosch", "Sierra caladora de precisión para cortes curvos.", 74990.00, "https://rimage.ripley.cl/home.ripley/Attachment/MKP/7947/MPM10002083191/full_image-1.jpeg", 12, 6, 1, 2),
("Taladro Percutor Makita", "Taladro percutor de alto rendimiento para hormigón.", 99990.00, "https://makitaonline.vtexassets.com/arquivos/ids/157169-800-800?v=638254837474870000&width=800&height=800&aspect=true", 8, 6, 2, 1);