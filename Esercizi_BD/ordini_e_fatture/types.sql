create type StatoOrdine as enum('In preparazione', 'Inviato', 'Da saldare', 'Saldato');


create domain CAP as char(5)
        check(value ~'^[0-9]{5})$');


create type Indirizzo as (
        via varchar,
        civico varchar,
        CAP type(CAP)
);

create domain IntGEZ as integer
        check(value >= 0);


create domain RealGEZ as real
        check(value >= 0);


create domain Real01 as real
        check(value >= 0 and value <= 1);


create domain CodiceFiscale as varchar(16)
        check (value ~ '^[A-Z]{6}[0-9]{2}[A-EHLMPRST]{1}[0-9]{2}[A-Z]{1}[0-9]{3}[A-Z]{1}$');


create domain PartitaIVA as varchar(11)
        check (value ~ '^[0-9]{11}$');


create domain Email as text
        check(value ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$');


create domain Telefono as varchar(15)
        check(value ~'^\+?[0-9]{6,15}$');







