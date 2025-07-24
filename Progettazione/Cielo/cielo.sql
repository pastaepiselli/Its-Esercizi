create domain posinteger as integer
    check(value >= 0);

create domain stringam as varchar(100);

create domain codiata as char(3);

-- prima tabella che inserisco nel database non avendo foreign key non da errori

create table compagnia (
    nome stringam not null,
    anno_fondazione posinteger,

    primary key (nome)
);

-- creo la tabella volo solo con una foreign key visto che non ho ancora definito e arrpart, aggiungo dopo i constraint

create table volo (
    codice posinteger not null,
    comp stringam not null,
    durataminuti posinteger not null,

    primary key (codice, comp),

    foreign key (comp) 
        references compagnia(nome) deferrable
    -- foreign key (codice, comp)
    --     references arrpart(codice, comp)
);

-- creo arr part con solo la foreign key con volo visto che lho appena creata

create table arrpart (
    codice posinteger not null, 
    comp stringam not null, 
    arrivo codiata not null,
    partenza codiata not null,

    primary key (codice, comp),

    foreign key (codice, comp)
        references volo(codice, comp) deferrable
    -- foreign key (arrivo)
    --     references aeroporto(codice) deferrable,
    -- foreign key (partenza)
    --     references aeroporto(codice) deferrable  
);

-- adesso posso aggiungere la fk in volo
alter table volo add constraint fk_codicomp_arrpart foreign key (codice, comp) references arrpart(codice, comp) deferrable;

-- creo la tabella aeroporto, ha una sola fk ma devo andarla ad inserire dopo

create table aeroporto (
    codice codiata not null,
    nome stringam not null,

    primary key (codice)

    -- foreign key (codice),
    --     references luogoaeroporto(aeroporto)     
);

-- dopo che ho creato aeroporto posso aggiungere le 2 fk mancanti di arrpart

alter table arrpart add constraint fk_arrivo_aeroporto_codice foreign key (arrivo) references aeroporto(codice) deferrable;

alter table arrpart add constraint fk_partenza_aeroporto_codice foreign key (partenza) references aeroporto(codice) deferrable;

-- la tabella aeroporto la creo senza problemi in piu mi servira per definire le ultime fk

create table luogoaeroporto (
    aeroporto codiata not null,
    citta stringam not null,
    nazione stringam not null,

    primary key (aeroporto),

    foreign key (aeroporto)
        references aeroporto(codice) deferrable
);

-- fk su aeroporto

alter table aeroporto add constraint fk_codice_luogoaeroporto_aeroporto foreign key (codice) references luogoaeroporto(aeroporto) deferrable;


