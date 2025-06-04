#CREATE DATABASE veterinary_db;
USE veterinary_db;

CREATE TABLE Customers (
	dni varchar(9) PRIMARY KEY,
    name varchar(200) NOT NULL,
    surnames varchar(200) NOT NULL,
    mail varchar(200),
    phone int(9)
);

CREATE TABLE Pets (
	num_chip int PRIMARY KEY,
    name varchar(200) NOT NULL,
    birth_date date NOT NULL,
	animal varchar(200) NOT NULL,
    breed varchar(200) NOT NULL,
    customer_id varchar(9) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(dni)
);

# Nuestra tabla de usuarios
CREATE TABLE  Users (
	dni varchar(9) PRIMARY KEY,
    name varchar(200) NOT NULL,
    password varchar(200) NOT NULL,
    surnames varchar(200) NOT NULL,
    rol varchar(200) NOT NULL,
    mail varchar(200) NOT NULL,
    phone varchar(200) NOT NULL,
    admission_date date NOT NULL
);

CREATE TABLE Sessions(
	id varchar(200) PRIMARY KEY NOT NULL,
    user_id varchar(9) NOT NULL,
    created_at date NOT NULL,
	FOREIGN KEY (user_id) REFERENCES Users(dni)
);

CREATE TABLE Appointments (
	id int PRIMARY KEY,
    type varchar(200) NOT NULL,
    description varchar(200) NOT NULL,
    date date NOT NULL,
    user_id varchar(9) NOT NULL,
    pet_id int NOT NULL,
    treatment_id int NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(dni),
	FOREIGN KEY (pet_id) REFERENCES Pets(num_chip)
	# FOREIGN KEY (tratamiento) REFERENCES Tratamiento(id)
);


# NO EJECUTAR TODAVIA # 
#CREATE TABLE Producto (
#	id int PRIMARY KEY,
#    nombre varchar(200) NOT NULL,
#    precio_total float NOT NULL,
#	cantidad int NOT NULL
#);

#CREATE TABLE Tratamiento (
#	id int PRIMARY KEY,
#    descripcion varchar(200) NOT NULL,
#    precio_total float NOT NULL,
#    producto int NOT NULL,
#    FOREIGN KEY (producto) REFERENCES Producto(id)
#);
