-- Quali sono i cognomi distinti di tutti gli strutturati?
select  distinct cognome
from persona

-- Quali sono i Ricercatori (con nome e cognome)?

select  nome, cognome
from persona
where posizione = 'Ricercatore'

-- Quali sono i Professori Associati il cui cognome comincia con la lettera ‘V’?

select nome, cognome
from persona
where posizione = 'Professore Associato'
and cognome like'V%'

-- Quali sono i Professori (sia Associati che Ordinari) il cui cognome comincia con la
-- lettera ‘V’?

select nome, cognome
from persona
where posizione = 'Professore Associato' 
and cognome like'V%'
or posizione = 'Professore Ordinario'
and cognome like'V%'

-- Quali sono i Progetti già terminati alla data odierna?

select nome
from progetto
where fine < current_date

-- Quali sono i nomi di tutti i Progetti ordinati in ordine crescente di data di inizio?
select nome 
from progetto
order by inizio

-- Quali sono i nomi dei WP ordinati in ordine crescente (per nome)?
select nome
from wp
order by nome

-- Quali sono (distinte) le cause di assenza di tutti gli strutturati?
select distinct tipo
from assenza 

-- Quali sono (distinte) le tipologie di attività di progetto di tutti gli strutturati?
select distinct tipo
from attivitaprogetto;


-- Quali sono i giorni distinti nei quali del personale ha effettuato attività non progettuali di tipo ‘Didattica’? Dare il risultato in ordine crescente
select distinct giorno
from attivitanonprogettuale
where tipo = 'Didattica'



