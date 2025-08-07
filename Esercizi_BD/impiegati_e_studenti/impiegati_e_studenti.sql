create table PosizioneMilitare(
        nome_posizione varchar primary key

);


create table Persona(
        cf CodiceFiscale primary key,
        nome varchar not null,
        cognome varchar not null,
        nascita date not null

);

create table Uomo(
        cf CodiceFiscale primary key,
        nome_posizione varchar not null,

        foreign key (cf)
                references Persona(cf)

        foreign key (nome_posizione)
                references PosizioneMilitare(nome_posizione)

);


 create table Donna(
        cf CodiceFiscale primary key,
        maternità IntGEZ not null,

        foreign key (cf)
                references Persona(cf)
);


create table Studente(
        cf CodiceFiscale,
        matrcola Matricola,

        foreign key (cf)
                references Persona(cf),

        primary key (cf, matrcola)
);


create table Impiegato(
        cf CodiceFiscale primary key,
        stipendio Denaro not null,

        foreign key (cf)
                references Persona(cf)
);


create table Segretario(
        cf CodiceFiscale primary key,

        foreign key(cf)
                references Impiegato(cf)
);



create table Direttore(
        cf CodiceFiscale primary key,

        foreign key(cf)
                references Impiegato(cf)
);



create table Progettista(
        cf CodiceFiscale primary key,

        foreign key(cf)
                references Impiegato(cf)
);


create table Responsabile(
        cf CodiceFiscale primary key,
        tipo TipoProg not null,

        foreign key (cf)
                references Progettista(cf)
);



create table Progetto(
        id serial primary key,
        nome varchar not null
);



