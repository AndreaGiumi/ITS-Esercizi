create domain StringaM as varchar(100);

create domain PosInteger as integer check (value >= 0);

create domain codice_IATA as char(3);



create table Compagnia(

        nome StringaM primary key,
        anno_fondazione PosInteger
);


create table Aeroporto(

        codice codice_IATA primary key,
        nome StringaM not null
);


create table LuogoAeroporto(

        aeroporto codice_IATA,
        citta varchar(100),
        nazione varchar(100),
        foreign key (aeroporto)
                references Aeroporto(codice) deferrable,

        primary key (aeroporto)
);


alter table Aeroporto
        add foreign key (codice) references LuogoAeroporto(codice) deferrable;


create table ArrPart(

        codice PosInteger not null, 
        comp StringaM not null,

        arrivo codice_IATA not null,
        foreign key (arrivo)
                references Aeroporto(codice),

        partenza codice_IATA not null,
        foreign key (partenza)
                references Aeroporto(codice),

        primary key (codice, comp)
);


create table Volo(

        codice PosInteger not null,
        durata_minuti PosInteger not null,
        
        -- accorpo compagnia
        comp StringaM not null,
        foreign key (comp)
                references Compagnia(nome),

        foreign key (codice, comp) 
                references ArrPart(codice, comp) deferrable,

        primary key (codice, comp)
);

alter table ArrPart
        add foreign key (codice, comp) references Volo(codice, comp) deferrable;
        
        
-- Query

select codice, comp 
from volo 
where durata_minuti > 180;

select distinct comp 
from volo 
where durata_minuti > 180;

select codice ,comp 
from arrpart 
where partenza = 'CIA';

select distinct comp 
from arrpart 
where arrivo = 'FCO';

select codice, comp 
from arrpart 
where partenza = 'FCO' and arrivo = 'JFK';

select distinct comp
from arrpart
 where partenza = 'FCO' and arrivo = 'JFK';

select distinct comp 
from arrpart
where partenza = 'FCO' or partenza = 'CIA' and arrivo = 'JFK';

select * 
from aeroporto, luogoaeroporto, arrpart
where aeroporto.codice = luogoaeroporto.aeroporto and arrpart.comp = 'MagicFly' and partenza = aeroporto.codice; 

select *
from arrpart
where (arrpart.partenza = 'FCO' or partenza = 'CIA') and arrivo = 'JFK';

