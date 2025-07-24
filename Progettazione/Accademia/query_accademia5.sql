-- Quali sono il nome, la data di inizio e la data di fine dei WP del progetto di nome
-- ‘Pegasus’?

select *
from wp, progetto as p
where p.nome = 'Pegasus'
and wp.progetto = p.id

-- Quali sono il nome, il cognome e la posizione degli strutturati che hanno almeno
-- una attività nel progetto ‘Pegasus’, ordinati per cognome decrescente?

select  distinct persona.nome, persona.cognome, persona.posizione
from persona, attivitaprogetto as ap, progetto as p
where ap.progetto = p.id
and p.nome = 'Pegasus'
and ap.persona = persona.id

-- 	Quali sono il nome, il cognome e la posizione degli strutturati che hanno più di
-- una attività nel progetto ‘Pegasus’?

select distinct persona.id, persona.nome, persona.cognome, persona.posizione
from attivitaprogetto ap1, attivitaprogetto ap2, persona , progetto 
where ap1.id <> ap2.id 
	and ap1.progetto = ap2.progetto
	and ap1.persona = ap2.persona
	and ap1.persona = persona.id
	and ap1.progetto = progetto.id
	and progetto.nome = 'Pegasus';

-- Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno
-- fatto almeno una assenza per malattia?

select distinct persona.nome, persona.cognome
from assenza, persona
where assenza.persona = persona.id
and persona.posizione = 'Professore Ordinario'
and assenza.tipo = 'Malattia'


-- Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno
-- fatto più di una assenza per malattia?

select distinct p.nome, p.cognome
from assenza a1, assenza a2, persona p
where p.posizione = 'Professore Ordinario'
and a1.tipo = 'Malattia'
and a2.tipo = 'Malattia'
and a1.persona = p.id
and a2.persona = p.id
and a1.id <> a2.id

-- Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno almeno
-- un impegno per didattica?

select distinct p.nome, p.cognome
from persona as p, attivitanonprogettuale as anp
where anp.tipo = 'Didattica'
and anp.persona = p.id
and p.posizione = 'Ricercatore'

-- Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno più di un
-- impegno per didattica?

select distinct p.nome, p.cognome
from persona as p, attivitanonprogettuale as anp1, attivitanonprogettuale as anp2
where anp1.tipo = 'Didattica'
and anp2.tipo = 'Didattica'
and anp1.persona = p.id
and anp2.persona = p.id
and p.posizione = 'Ricercatore'
and anp1.id <> anp2.id

-- Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia
-- attività progettuali che attività non progettuali?
select p.nome, p.cognome
from attivitaprogetto as ap, attivitanonprogettuale as anp, persona as p
where ap.persona = p.id
and anp.persona = p.id
and ap.giorno = anp.giorno

-- Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia
-- attività progettuali che attività non progettuali? Si richiede anche di proiettare il
-- giorno, il nome del progetto, il tipo di attività non progettuali e la durata in ore di
-- entrambe le attività.

select p.nome, p.cognome, ap.giorno as giorno, progetto.nome, ap.oredurata, anp.tipo, anp.oredurata
from attivitaprogetto as ap, attivitanonprogettuale as anp, persona as p, progetto
where ap.persona = p.id
and anp.persona = p.id
and ap.giorno = anp.giorno
and progetto.id = ap.progetto

-- Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono
-- assenti e hanno attività progettuali?

select p.nome, p.cognome
from persona as p, assenza as a, attivitaprogetto as ap
where a.persona = p.id
and ap.persona = p.id
and a.giorno = ap.giorno

-- Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono
-- assenti e hanno attività progettuali? Si richiede anche di proiettare il giorno, il
-- nome del progetto, la causa di assenza e la durata in ore della attività progettuale.
select p.nome, p.cognome, a.giorno as giorno, progetto.nome, a.tipo as causa_assenza, ap.oredurata
from persona as p, assenza as a, attivitaprogetto as ap, progetto
where a.persona = p.id
and ap.persona = p.id
and a.giorno = ap.giorno
and ap.progetto = progetto.id



-- Quali sono i WP che hanno lo stesso nome, ma appartengono a progetti diversi?
select distinct wp1.nome
from wp as wp1, wp as wp2, progetto as p
where wp1.nome = wp2.nome
and wp1.progetto <> wp2.progetto