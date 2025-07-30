create domain RealGEZ as real 
	check(value >=0);


create type Indirizzo as (
	
		via varchar,
		civico varchar

	);


create table progetto(
	id integer primary key,
	nome varchar not null,
	budget RealGEZ not null
);


create table impiegato(
	id integer primary key,
	nome varchar not null,
	cognome varchar not null,
	nascita date not null,
	stipendio RealGEZ not null
);

create table coinvolto(
	impiegato integer,
	progetto integer,
	primary key(impiegato, progetto),

	foreign key (impiegato)
		references
			impiegato(id),

	foreign key (progetto)
		references
			progetto(id)
);


create table dipartimento(
	id integer primary key,
	nome varchar not null,
	indirizzo Indirizzo,
	impiegato integer not null,

	foreign key (impiegato)
		references
			impiegato(id)
	-- V.inclu id occorre almeno una volta in dip_tel (dipartimento)
);


create table telefono(
	telefono varchar(12) primary key
	-- V.inclu telefono occorre almeno una volta in dip_tel (telefono)
);


create table dip_tel(
		telefono varchar(12) not null,
		dipartimento integer not null,
		foreign key (telefono)
			references
				telefono(telefono),

		foreign key (dipartimento)
			references
				dipartimento(id),
				
		primary key	(telefono, dipartimento)


);


create table afferenza(
	impiegato integer primary key,
	dipartimento integer not null,
	data_afferenza date not null,
	foreign key (impiegato)
		references
			impiegato(id),

	foreign key (dipartimento)
		references
			dipartimento(id)

);


