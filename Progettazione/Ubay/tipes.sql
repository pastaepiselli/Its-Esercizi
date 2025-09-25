create domain voto as integer
	check (value BETWEEN 0 and 5);

create domain IntGEZ as integer:
	check (value >= 0);

create domain stringa as varchar;

create domain RealGEZ as real
	check (value >= 0);

create domain IntG1 as integer
	check (value > 1);

create domain RealGZ as Real
	check (value > 0);

create type Condizione as enum
	('Ottimo', 'Buono', 'Discreto', 'Da sistemare');

create type Popolarita as enum
	('Bassa', 'Media', 'Alta')

create domain URL as varchar
	check (value ~'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)');

create table categoria (
	nome stringa primary key,
	-- super sarebbe il nome della categoria sopra
	super stringa
);

alter table categoria add foreign key (super) references categoria(nome);

create table utente (
	username stringa primary key,
	registrazione timestamp not null
);

create table venditoreprof (
	-- accorpo vp_isa_u
	utente stringa primary key,
	foreign key (utente)
		references utente(username),
	vetrina URL not null,
	unique(vetrina)
);

create table privato (
	-- accorpo pr_isa_u
	utente stringa primary key,
	foreign key (utente)
		references utente(username));

create table postoggetto (
	descrizione stringa not null,
	pubblicazione timestamp not null,
	ha_feedback boolean not null,
	voto voto,
	istante_feedback timestamp,
	commento stringa,
	
	-- accorpo cat_post	
	categoria stringa not null,
	foreign key (categoria)
		references categoria(nome),

	-- accorpo pubblica
	utente stringa not null,
	foreign key (utente)
		references utente(username),

	-- v.inclusione postoggetto(id) occorre in met_post(postoggetto)
	-- v.ennupla
	check ((ha_feedback = true and voto is not null and istante_feedback is not null)
		or (ha_feedback = false and voto is null and istante_feedback is null and commento is null)),
	id serial primary key
);

create table asta (
	prezzo_base RealGEZ not null,
	prezzo_bid RealGZ not null,
	scadenza timestamp not null,

	-- accorpo asta_isa_po
	postoggetto integer primary key,
	foreign key (postoggetto)
		references postoggetto(id)
);

create table compralosubito (
	prezzo RealGZ not null,

	-- accorpo cs_isa_po
	postoggetto RealGZ primary key,
	foreign key (postoggetto)
		references postoggetto(id),

	-- accorpo cs_ut
	istante timestamp, -- puo essere null 0..1
	privato stringa,
	foreign key (privato)
		references privato(utente),

	-- v.ennupla: (privato is null) = (istante is null)
	check ((privato is null) = (istante is null))
);

create table postoggettonuovo (
	anni_garanzia IntG1 not null,

	-- accorpo pon_isa_po
	postoggetto integer primary key,
	foreign key (postoggetto)
		references postoggetto(id)

	-- accorpo pubblica_nuovo
	venditoreprof stringa not null,
	foreign key (venditoreprof)
		references venditoreprof(utente)
);

create table postoggettousato (
	condizione Condizione not null,
	anni_garanzia IntGEZ not null,

	-- accorpo pou_isa_po
	postoggetto integer primary key,
	foreign key (postoggetto)
		references postoggetto(id)
);

create table metododipagamento (
	nome stringa primary key
);

create table met_post (
	postoggetto integer not null,
	metododipagamento stringa not null,

	primary key (postoggetto, metododipagamento),

	foreign key (postoggetto)
		references postoggetto(id),

	foreign key (metododipagamento)
		references metododipagamento(nome)
);

create table bid (
	istante timestamp not null,
	codice id primary key,

	-- accorpo bid_ut
	privato stringa not null,
	foreign key (privato)
		references privato(utente),

	-- accorpo asta_bid
	asta integer not null,
	unique(asta, istante),
	foreign key (asta)
		references asta(postoggetto)
);	