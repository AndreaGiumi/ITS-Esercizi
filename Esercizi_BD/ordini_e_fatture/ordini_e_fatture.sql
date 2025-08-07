create type StatoOrdine as enum('In preparazione', 'Inviato', 'Da saldare', 'Saldato');


create domain CAP as char(5)
        check(value ~'^[0-9]{5}$');


create type Indirizzo as (
        via varchar,
        civico varchar,
        CAP CAP
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



create table Nazione(
	nome varchar primary key
);

create table Regione(
	nome varchar,
	nazione varchar,
	primary key(nome, nazione),

	foreign key (nazione)
		references nazione(nome)
);


create table Citta(
	nome varchar,
	id serial primary key,
	regione varchar not null,
	nazione varchar not null,
	unique(nome, regione, nazione),

	foreign key (regione, nazione)
		references regione(nome, nazione)

);



create table Direttore(
	cf CodiceFiscale primary key,
	nome varchar not null,
	cognome varchar not null,
	data_nascita date not null,
	anni_servizio IntGEZ not null,
	citta integer not null,

	foreign key (citta)
		references citta(id)
);


create table Fornitore(
	id serial primary key,
	regione_sociale varchar not null,
	partita_iva PartitaIVA not null,
	indirizzo Indirizzo not null,
	telefono Telefono not null,
	email Email not null,
	citta integer not null,

	foreign key (citta)
		references citta(id)
);

create table Dipartimento(
	nome varchar primary key,
	indirizzo Indirizzo,
	direttore CodiceFiscale,
	citta integer not null,
	foreign key (citta)
		references citta(id),
	foreign key (direttore)
		references Direttore(cf)
);




create table Ordine(
	id serial primary key,
	imponibile RealGEZ not null,
	aliquota_iva Real01 not null,
	stato StatoOrdine not null,
	dipartimento varchar not null,
	fornitore integer not null,

	foreign key (dipartimento)
		references dipartimento(nome),

	 foreign key(fornitore)
		references fornitore(id)

);
