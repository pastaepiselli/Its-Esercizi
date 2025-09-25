
-- tipi di dato

CREATE DOMAIN Stringa as varchar(100)
        check(value is not null);

CREATE DOMAIN RealGEZ as Real
        check (value >= 0);
CREATE DOMAIN numerotelefono as varchar(15);

create domain cap as char(5)
        check(value ~ '[0-9]{5}');

create type indirizzo as (
        via Stringa,
        civico Stringa,
        cap cap not null 
);


-- tabelle

create table impiegato (
        id integer primary key,
        nome Stringa not null,
        cognome Stringa not null,
        nascita date not null,
        stipendio RealGEZ not null      
);

-- potevo accorpare afferenza perche 0..1


-- create table impiegato (
--        id integer primary key,
--        nome Stringa not null,
--        cognome Stringa not null,
--        nascita date not null,
--        stipendio RealGEZ not null,
--        dipartimento integer,
--        data_afferenza date,
        -- foreign key verso dipartimento posticipata
--        foreign key (dipartimento)
--                references dipartimento(id),
        -- v.ennupla: (dipartimento is null) == (data_afferenza is null));

create table progetto (
        id integer primary key,
        nome Stringa not null,
        budget RealGEZ not null
);

-- impiegato 0..* <----------> 0..* progetto
create table coinvolto (
        impiegato integer not null,
        progetto integer not null,
        primary key (impiegato, progetto)
        foreign key (impiegato)
                references impiegato(id),
        foreign key (progetto)
                references progetto(id),
        
);

create table telefonodip (
        id integer primary key,
        telefono numerotelefono not null
        -- v.inclusione (id) occorre in tel_dip(telefono)
);

create table dipartimento (
        id integer not null ,
        nome Stringa not null,
        indirizzo indirizzo -- [0..1],
        primary key (id)
        -- v.inclusione dipartimento(id) occorred in tel_dip(dipartimento)
        -- v.inclusione dipartimento(id) occorre in direzione
);

-- alter table impiegato add constraint foreign key (dipartimento) references dipartimento(id); 

-- potevo accorpare direzione perche 1..1

-- create table dipartimento (
--        id integer not null,
--        nome Stringa not null,
--        indirizzo indirizzo,
--        direttore integer not null, -- ogni dipartimento ha un solo impiegato che lo gestisce
--        primary key (id),
--        foreign key (direttore)
--                references impiegato(id)
-- );

-- dipartimento 1..* <---------> 1..* telefono
create table tel_dip (
        numerotelefono integer not null,
        dipartimento integer not null,
        primary key(numerotelefono, dipartimento),
        foreign key (numerotelefono)
                references telefonodip(id),
        foreign key (dipartimento)
                references dipartimento(id)
);

-- impiegato 1..1 <---------> 0..* dipartimento
create table direzione (
        dipartimento integer primary key,
        impiegato integer not null,
        foreign key (dipartimento)
                references dipartimento(id),
        foreign key (impiegato)
                references impiegato(id)
);
-- impiegato 0..* <----------> 0..1 dipartimento
create table afferenza (
        impiegato integer not null,
        dipartimento integer not null,
        data_afferenza date not null,

        primary key (impiegato),

        foreign key (impiegato)   
                references impiegato(id),
        foreign key (dipartimento)
                references dipartimento(id)
);