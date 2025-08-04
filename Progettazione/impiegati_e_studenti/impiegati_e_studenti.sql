-- tipi di dato

create domain stringa as varchar(100);

create domain intgez as integer
        check(value >=0);

create domain realgez as real
        check(value >= 0);

create domain intgz as integer
        check(value > 0);

create type tipoprogettista as enum (
        'progettista', 'responsabile');  

create domain codicefiscale as char(16)
        check(value ~'^[A-Za-z]{6}[0-9]{2}[A-Za-z]{1}[0-9]{2}[A-Za-z]{1}[0-9]{3}[A-Za-z]{1}$');    


-- creo le tabelle

create table posizione_militare (
        nome stringa primary key
);

create table persona (
        nome stringa not null,
        cognome stringa not null,
        cf codicefiscale not null,
        nascita date not null,

        primary key (cf)
);

create table uomo(
        -- accorpo uomo_pos_mil
        posizione_militare stringa not null,
        foreign key (posizione_militare)
            references posizione_militare(nome),

        -- accorpo uomo_isa_pers
        cf codicefiscale not null,
        foreign key (cf)
            references persona(cf),

        primary key (cf)
);

create table donna (
        maternita intgez not null,

        -- accorpo donna_isa_pers
        cf codicefiscale not null,
        foreign key (cf)
            references persona(cf),

        primary key (cf)
);

create table impiegato (
        stipendio realgez not null,

        -- accorpo imp_isa_pers
        cf codicefiscale not null,
        foreign key (cf)
            references persona(cf),

        primary key (cf)
);

create table segretario (
        -- accorpo segr_isa_i
        cf codicefiscale not null,
        foreign key (cf)
            references impiegato(cf),

        primary key (cf)
);

create table direttore (
        -- accorpo dir_isa_i
        cf codicefiscale not null,
        foreign key (cf)
            references impiegato(cf),

        primary key (cf)
);


create table progettista (
        tipo tipoprogettista not null,
        -- accorpo prog_isa_i
        cf codicefiscale not null,
        foreign key (cf)
            references impiegato(cf),

        primary key (cf)
);


create table studente (
    matricola intgz not null,

    -- accorpo stud_isa_pers
    cf codicefiscale not null,
    foreign key (cf)
        references persona(cf),

    primary key (cf),
    unique (matricola)
);


create table progetto (
    id integer not null,
    nome stringa not null,

    primary key (id)
);

create table resp_prog (
    progetto integer not null,
    progettista codicefiscale not null,

    foreign key (progetto)
        references progetto(id),
    foreign key (progettista)
        references progettista(cf),

    primary key (progetto, progettista)
);  