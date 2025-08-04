-- Tipi di dato

create domain stringa as varchar(100);

create domain intgez as integer
        check (value >=0);

create domain codicefiscale as char(16)
        check (value ~'^[A-Za-z]{6}[0-9]{2}[A-Za-z]{1}[0-9]{2}[A-Za-z]{1}[0-9]{3}[A-Za-z]{1}$');

create domain partitaiva as char(11)
        check (value ~'^\d{11}$');

create domain telefono as varchar(13)
        check (value ~'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$');        
        
create domain email as varchar(100)
        check (value ~'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$');

create type statoordine as enum (
        'in preparazione',  'inviato',  'da saldare',
        'saldato');

create domain real01 as real
        check (value > 0 and value < 1);

create domain realgez as real
        check (value >= 0);

-- creo i dati per indirizzo

create domain via as varchar(100)
        check(value is not null);

create domain civico as varchar(100)
        check (value is not null);

create domain cap as char(5)
        check (value ~'^[0-9]{5}$');

create type indirizzo as (
        via via ,
        civico civico,
        cap cap);

-- tabelle

create table nazione (
        nome stringa primary key);

create table regione (
        nome stringa not null,
        -- accorpo  reg_naz,
        nazione stringa not null,
        foreign key (nazione)
                references nazione(nome),

        primary key (nome, nazione)
);

create table citta (
        -- visto che l'accorpamento senno mi diventa enorme creo un id come primary key 
        -- per rendere piu comodo la FK verso questa tabella
        id integer primary key, -- posso usare un serial
        nome stringa not null,
        regione stringa not null,
        nazione stringa not null,
        -- accorpo reg_naz e cit_reg
        foreign key (regione, nazione)
                references regione(nome, nazione),
                -- comunque le lascio come unique
                        unique (nome, regione, nazione)
);

create table direttore (
        nome stringa not null,
        cognome stringa not null,
        data_nascita date not null,
        anni_servizio intgez not null,
        cf codicefiscale not null,

        primary key (cf),

        -- accorpo dir_nasc
        citta integer not null,
        foreign key (citta)
                references citta(id)
);

create table fornitore (
        ragione_sociale stringa not null,
        partita_iva partitaiva not null,
        indirizzo indirizzo not null,
        telefono telefono not null,
        email email not null,
        id integer not null, -- potrei usare serial

        primary key (id),

        -- accorpo cit_forn
        citta integer not null,
        foreign key (citta)
                references citta(id)
);

create table dipartimento (
        nome stringa not null,
        indirizzo indirizzo not null,

        primary key (nome),

        -- accorpo dip_sede
        citta integer not null,
        foreign key (citta)
                references citta(id),
        -- accorpo dip_dir
        direttore codicefiscale not null,
        foreign key (direttore)
                references direttore(cf)
);

create table ordine (
        data_stipula date not null,
        imponibile realgez not null,
        aliquota_iva real01 not null,
        stato statoordine not null,
        id integer not null,

        primary key (id),

        -- accorpo fond_ord
        fornitore integer not null,
        foreign key (fornitore)
                references fornitore(id),

        -- accorpo dip_ord
        dipartimento stringa not null,
        foreign key (dipartimento)
                references dipartimento(nome)
);

