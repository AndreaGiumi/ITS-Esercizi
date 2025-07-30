create type Strutturato as enum('Ricercatore', 'Professore Associato', 'Professore Ordinario');

create type LavoroProgetto as enum('Ricerca e Sviluppo', 'Dimostrazione', 'Management', 'Altro');

create type LavoroNonProgettuale as enum('Didattica', 'Ricerca', 'Missione', 'Incontro Dipartimentale', 'Incontro Accademico', 'Altro');

create type CausaAssenza as enum('Chiusura Universitaria', 'Maternità', 'Malattia');

create domain PosInteger as integer
	check (value >= 0);

create domain StringaM as varchar(100);

create domain NumeroOre as integer
	check(value >= 0 and value <= 8);

create domain Denaro as real
	check(value >= 0);



create table Persona(
	id PosInteger primary key,
	nome StringaM not null,
	cognome StringaM not null,
	posizione Strutturato not null,
	stipendio Denaro not null
);


create table Progetto(
	id PosInteger primary key,
	nome StringaM not null,
	inizio date not null,
	fine date not null,
	budget Denaro not null,
	unique (nome),
	check(inizio<fine)


);


create table WP(
	progetto PosInteger not null,
	id PosInteger not null,
	nome StringaM not null,
	inizio date not null,
	fine date not null,
	primary key ( progetto, id),
	unique(progetto, nome),
	check(inizio<fine),

	foreign key (progetto)
		references
			progetto(id)
);


create table AttivitàProgetto(
	id PosInteger not null,
	persona PosInteger not null,
	progetto PosInteger not null,
	wp PosInteger not null,
	giorno date not null,
	tipo LavoroProgetto not null,
	oreDurata NumeroOre not null,
	foreign key (persona)
		references
			persona(id),

	foreign key (progetto, wp)
		references
			wp(progetto, id)
);



create table AttivitàNonProgettuale(
	id PosInteger not null,
	persona PosInteger not null,
	tipo LavoroNonProgettuale not null,
	giorno date not null,
	oreDurata NumeroOre not null,
	foreign key (persona)
		references
			persona(id)
);


create table Assenza(
	id PosInteger not null,
	persona PosInteger not null,
	tipo CausaAssenza not null,
	giorno date not null,
	unique(persona, giorno),
	foreign key (persona)
		references
			persona(id)

);



-- Query


-- 1

select count(distinct(cognome))
from persona;


-- 2

select nome, cognome
from persona
where posizione = 'Ricercatore';


-- 3

select id, nome, cognome
from persona
where posizione = 'Professore Associato' and cognome like 'V%';



-- 4 

select *
from persona
where (posizione = 'Professore Associato' or posizione = 'Professore Ordinario')and cognome like 'V%';


-- 5 

select *
from progetto
where fine < '2025-07-22';

-- 6

select nome
from progetto
order by inizio desc;

-- select *
-- from progetto
-- order by inizio asc;


-- 7

select *
from wp
order by nome asc;

-- 8

select distinct(tipo)
from assenza;


-- 9

select distinct(tipo)
from attivitàprogetto;


-- 10


select distinct(giorno) asc 
from attivitànonprogettuale
where tipo = 'Didattica' ;