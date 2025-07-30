create domain CodiceVolo as varchar(3);


create domain CodiceIATA as varchar(6);


create domain IntGZ as integer
        check(value > 0);

create domain RealGEZ as real
        check(value >= 0);


create domain Anno as varchar(4)
        check(value >= 1900);


create table nazione(

nome varchar primary key
);


create table città(

nome_città varchar not null,
n_abitanti IntGEZ not null,

-- accorpo  nazione 
nome_nazione varchar not null,

foreign key (nome_nazione)
        references nazione(nome),

primary key(nome_nazione, nome_città)
);


create table aereoporto(

id serial primary key,
codice_IATA CodiceIATA not null,
nome varchar not null,

-- accorop aer_città
nome_città varchar not null,
nome_nazione varchar not null,

foreign key (nome_nazione, nome_città)
        references città(nome_nazione, nome_città)
);


create table compagnia(

id serial primary key,
nome varchar not null,
fondazione Anno not null,

-- accorop comp_cit
nome_città varchar not null,
nome_nazione varchar not null,

foreign key (nome_nazione, nome_città)
        references città(nome_nazione, nome_città)
);


create table volo(

id serial primary key,
id_volo CodiceVolo not null,
durata_minuti IntGZ,

-- accorpo arrivo
arrivo integer not null,

foreign key (arrivo)
        references aereoporto(id),

-- accorpo partenza
partenza integer not null,

foreign key (partenza)
        references aereoporto(id),

-- accorpo volo_comp
codice_compagnia integer,

foreign key (codice_compagnia)
        references compagnia(id)
);