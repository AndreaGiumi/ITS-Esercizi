create domain IntGEZ as integer
        check( value >= 0);

create domain Denaro as real
        check ( value >= 0);

create domain CodiceFiscale as varchar(16)
        check (value ~ '^[A-Z]{6}[0-9]{2}[A-EHLMPRST]{1}[0-9]{2}[A-Z]{1}[0-9]{3}[A-Z]{1}$');

create domain Matricola as varchar(6)
        check ( value ~ '^[A-Z]{2}\d{2}-\d{4}$');

create type TipoProg as enum
        ('Progettista', 'Responsabile');
