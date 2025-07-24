CREATE DOMAIN str as varchar(100);

CREATE DOMAIN IntGEZ as integer
        check(value >= 0);

CREATE DOMAIN Int1900 as integer
        check (value >= 1900);

CREATE DOMAIN IntGZ as integer
        check (value > 0);

CREATE DOMAIN CodiceVolo as varchar(5);

CREATE DOMAIN CodiceIATA as varchar(2);

create table nazione (
    nome str primary key
);

create table citta (
    nome str not null,
    numero_abitanti IntGEZ not null,

    -- accorpo citta_naz
    nome_nazione str not null,

    primary key (nome, nome_nazione),

    foreign key (nome_nazione)
        references nazione(nome)

);

create table aeroporto (
    nome str not null, 
    codice CodiceIATA not null,
    -- accorpo aer_citta
    nome_citta str not null,
    nome_nazione str not null,

    foreign key (nome_citta, nome_nazione)
        references citta(nome, nome_nazione),

    primary key (codice)
);

create table compagnia (
    nome str not null,
    fondazione Int1900 not null,
    id integer not null,

    -- accorpo comp_dirz_citta

    nome_citta str not null,
    nome_nazione str not null,

    foreign key (nome_citta, nome_nazione)
        references citta(nome, nome_nazione),

    primary key (id)

     
);

create table volo (`
    id integer not null,
    durataminuti IntGZ not null,
    codice CodiceVolo not null,

    -- accorpo arrivo
    codarrivo CodiceIATA not null,

    -- accorpo partenza
    codpartenza CodiceIATA not null,

    -- accorpo volo_comp
    compagnia integer not null,

    primary key (id),
    -- arrivo
    foreign key (codarrivo)
        references aeroporto(codice),
    
    -- partenza
    foreign key (codpartenza)
        references aeroporto(codice),
    
    -- compagnia
    foreign key (compagnia)
        references compagnia(id)

);
