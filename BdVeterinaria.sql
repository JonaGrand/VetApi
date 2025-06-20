create table Customers(
    dni      varchar(9)   not null primary key,
    name     varchar(200) not null,
    surnames varchar(200) not null,
    mail     varchar(200) not null,
    phone    varchar(9)   not null
);

create table Pets(
    num_chip    varchar(10)  not null primary key,
    name        varchar(200) not null,
    birth_date  date         not null,
    animal      varchar(200) not null,
    breed       varchar(200) not null,
    customer_id varchar(9)   not null,
    constraint pets_ibfk_1 foreign key (customer_id) references Customers (dni)
);

create index customer_id on Pets (customer_id);

create table Users(
    dni            varchar(9)                    not null primary key,
    name           varchar(200)                  not null,
    password       varchar(200)                  not null,
    surnames       varchar(200)                  not null,
    rol            enum ('vet', 'admin', 'gest') not null,
    mail           varchar(200)                  not null,
    phone          varchar(9)                    not null,
    admission_date date                          not null
);

create table Appointments(
    id          integer  not null primary key auto_increment,
    type        varchar(200) not null,
    description varchar(200) not null,
    date        datetime     not null,
    user_id     varchar(9)   not null,
    pet_id      varchar(10)  not null,
    constraint appointments_fk_user foreign key (user_id) references Users (dni) on delete cascade,
    constraint appointments_ibfk_1 foreign key (user_id) references Users (dni),
    constraint appointments_ibfk_2 foreign key (pet_id) references Pets (num_chip)
);

create index pet_id on Appointments (pet_id);

create index user_id on Appointments (user_id);

create table Sessions(
    id         varchar(200) not null primary key,
    user_id    varchar(9)   not null,
    expires_at datetime     not null,
    constraint sessions_ibfk_1 foreign key (user_id) references Users (dni) on delete cascade
);


# PROCEDIMIENTO PARA LIMPIAR LOS JWT PERIODICAMENTE (8horas)

# Habilitar el programador de eventos:
SET GLOBAL event_scheduler = ON;

# Crear el procedimiento
DELIMITER //

CREATE PROCEDURE CleanExpiredSessions()
BEGIN
    DELETE FROM Sessions
    WHERE expires_at < NOW();
END //

DELIMITER ;

# Creas el evento
CREATE EVENT IF NOT EXISTS DailyCleanExpiredSessions
ON SCHEDULE EVERY 1 DAY
STARTS CURRENT_TIMESTAMP
DO
  CALL CleanExpiredSessions();

# ver los eventos creados
SHOW EVENTS;