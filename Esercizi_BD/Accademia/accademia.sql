create type Strutturato as enum('Ricercatore', 'Professore Associato', 'Professore Ordinario');

create type LavoroProgetto as enum('Ricerca e Sviluppo', 'Dimostrazione', 'Management', 'Altro');

create type LavoroNonProgettuale as enum('Didattica', 'Ricerca', 'Missione', 'Incontro Dipartimentale', 'Incontro Accademico', 'Altro');

create type CausaAssenza as enum('Chiusura Universitaria', 'Maternità', 'Malattia');

create domain PosInteger as integer
	check (value >= 0 and value is not null);

create domain StringaM as varchar(100)
	check(value is not 	null);

create domain NumeroOre as integer
	check(value >= 0 and value <= 8 and value is not null);

create domain Denaro as real
	check(value >= 0 and value is not null);


create table persona(
	id PosInteger primary key,
	nome StringaM not null,
	cogome StringaM not null,
	posizione Strutturato not null,
	stipendio Denaro not null
);


create table progetto(
	id PosInteger primary key,
	nome StringaM not null,
	inizio date not null,
	fine date not null,
	budget Denaro not null,
	unique (nome),
	check(inizio<fine)


);


create table wp(
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
	oreDurata NummeroOne not null,
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
	oreDurata NummeroOne not null,
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




insert into persona(id, nome, cognome, posizione, stipendio)
values
(1, 'Andrea', 'Giumi', 'Professore Associato', 1560);

insert into persona(id, nome, cognome, posizione, stipendio)
values
(2, 'Kristian', 'Lanni', 'Professore Ordinario', 1900);


insert into persona(id, nome, cognome, posizione, stipendio)
values
(3, 'Matteo', 'Azzoli', 'Ricercatore', 1450);


insert into persona(id, nome, cognome, posizione, stipendio)
values
(4, 'Mirko', 'Capraro', 'Professore Associato', 1560


insert into progetto(id, nome, inizio, fine, budget)
values
(1, 'Alpha', '2025-04-15', '2025-07-24', 25000);

insert into progetto(id, nome, inizio, fine, budget)
values
(4, 'Beta', '2025-03-04', '2025-06-29', 25000);

insert into progetto(id, nome, inizio, fine, budget)
values
(3, 'Gamma', '2025-08-04', '2026-04-21', 251000);


insert into progetto(id, nome, inizio, fine, budget)
values
(2, 'Alpha2', '2026-04-04', '2026-07-01', 271000);


insert into wp (progetto, id, nome, inizio, fine)
values
(1, 5, 'Alpha3', '2025-01-01', '2025-05-25');


insert into wp (progetto, id, nome, inizio, fine)
values
(4, 14, 'Beta2', '2025-02-05', '2025-7-15');


insert into wp (progetto, id, nome, inizio, fine)
values
(3, 14, 'Gamma2', '2026-01-05', '2026-12-15');



insert into wp (progetto, id, nome, inizio, fine)
values
(2, 15, 'Beta3', '2026-05-11', '2026-10-8');


insert into AttivitàProgetto(id, persona, progetto, wp, giorno, tipo, oreDurata)
values
(10, 1, 2, 15, '2025-07-07', 'Management', 8);


insert into AttivitàProgetto(id, persona, progetto, wp, giorno, tipo, oreDurata)
values
(11, 4, 4, 14, '2025-07-07', 'Ricerca e Sviluppo', 8);



insert into AttivitàProgetto(id, persona, progetto, wp, giorno, tipo, oreDurata)
values
(11, 3, 1, 5, '2024-02-07', 'Dimostrazione', 5);

insert into AttivitàProgetto(id, persona, progetto, wp, giorno, tipo, oreDurata)
values
(11, 4, 3, 14, '2024-02-07', 'Dimostrazione', 5);



insert into AttivitàNonProgettuale(id, persona, tipo, giorno, oreDurata)
values
(12, 1,'Incontro Dipartimentale', '2025-07-14', 4);


insert into AttivitàNonProgettuale(id, persona, tipo, giorno, oreDurata)
values
(13, 2,'Missione', '2025-07-15', 6);



insert into AttivitàNonProgettuale(id, persona, tipo, giorno, oreDurata)
values
(14, 3,'Incontro Accademico', '2025-06-15', 6);


insert into AttivitàNonProgettuale(id, persona, tipo, giorno, oreDurata)
values
(15, 4,'Ricerca', '2025-07-15', 8);


insert into Assenza(id, persona, tipo, giorno)
values
(16, 1, 'Chiusura Universitaria', '2025-07-30');

insert into Assenza(id, persona, tipo, giorno)
values
(17, 4, 'Chiusura Universitaria', '2025-07-30');

insert into Assenza(id, persona, tipo, giorno)
values
(18, 2, 'Malattia', '2025-07-10');

insert into Assenza(id, persona, tipo, giorno)
values
(19, 3, 'Malattia', '2025-07-19');