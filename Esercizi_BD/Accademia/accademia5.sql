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

select nome, inizio, fine
from wp
where progetto = 1;

-- 2

select p.id , p.nome, p.cognome, p.posizione 
from persona p, attivitàprogetto ap, progetto pg
where p.id = ap.persona and pg.id = ap.progetto and pg.nome = 'Pegasus'
group by (p.id)
order by p.id desc;

-- 3

select p.id , p.nome, p.cognome, p.posizione
from persona p, attivitàprogetto ap, attivitàprogetto ap2, progetto pg
where p.id = ap.persona
and pg.id = ap.progetto
and pg.nome = 'Pegasus'
and ap.id <> ap2.id
and ap.persona = ap2.persona
group by (p.id);


-- 4

select p.id , p.nome, p.cognome, p.posizione
from persona p, assenza a, assenza a2
where p.id = a.persona
and a.id <> a2.id
and p.posizione = 'Professore Ordinario'
and a.tipo = 'Malattia'
group by (p.id);


-- 5
select p.id , p.nome, p.cognome, p.posizione
from persona p, assenza a, assenza a2
where p.id = a.persona
and a.id <> a2.id
and a.persona = a2.persona
and p.posizione = 'Professore Ordinario'
and a.tipo = 'Malattia'
group by (p.id);


-- 6

select p.id , p.nome, p.cognome
from persona p, attivitànonprogettuale anp
where p.id = anp.persona
and p.posizione = 'Ricercatore'
group by (p.id);


-- 7

select p.id , p.nome, p.cognome
from persona p, attivitànonprogettuale anp, attivitànonprogettuale anp2
where p.id = anp.persona
and anp.id <> anp2.id
and anp.persona = anp2.persona
and p.posizione = 'Ricercatore'
group by (p.id);


-- 8 


select nome, cognome
from persona p, attivitàprogetto ap, attivitànonprogettuale anp
where p.id = ap.persona 
and p.id = anp.persona
and ap.giorno = anp.giorno;



-- 9 

select p.nome, p.cognome, ap.giorno, pg.nome, ap.oredurata,anp.tipo,anp.oredurata
from persona p, progetto pg, attivitàprogetto ap, attivitànonprogettuale anp
where p.id = ap.persona 
and p.id = anp.persona
and ap.giorno = anp.giorno
and pg.id = ap.progetto;


-- 10

select p.nome, p.cognome
from persona p, attivitàprogetto ap, assenza a
where p.id = ap.persona
and ap.giorno = a.giorno;


-- 11

select p.nome, p.cognome, ap.giorno, a.tipo as causa_assenza, pg.nome as progetto, ap.oredurata 
from persona p, attivitàprogetto ap, assenza a, progetto pg
where p.id = ap.persona
and ap.giorno = a.giorno
and ap.progetto = pg.id;


-- 12

select wp1.nome
from wp wp1, wp wp2
where wp1.nome = wp2.nome
and wp1.progetto <> wp2.progetto
group by (wp1.nome);
