-- 1. Quali sono i voli (codice e nome della compagnia) la cui durata supera le 3 ore?
select volo.codice, volo.comp
from volo
where durataminuti > 180;

-- 2. Quali sono le compagnie che hanno voli che superano le 3 ore?
select distinct volo.comp 
from volo
where volo.durataminuti > 180;

-- 3. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto con
-- codice ‘CIA’?
select arrpart.codice, arrpart.comp
from arrpart
where partenza = 'CIA';

-- 4. Quali sono le compagnie che hanno voli che arrivano all’aeroporto con codice
-- ‘FCO’?
select distinct comp
from arrpart
where arrivo = 'FCO';
-- 5. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto ‘FCO’
-- e arrivano all’aeroporto ‘JFK’?
select distinct codice, comp
from arrpart
where partenza = 'FCO'
and arrivo = 'JFK'

-- 6. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’ e atterrano all’aeroporto ‘JFK’?
select distinct comp
from arrpart
where partenza = 'FCO'
and arrivo = 'JFK'


-- 7. Quali sono i nomi delle compagnie che hanno voli diretti dalla città di ‘Roma’ alla
-- città di ‘New York’?
select distinct comp
from arrpart
where partenza = 'FCO' and arrivo = 'JFK' 
or partenza = 'CIA' and arrivo = 'JFK';

-- 8. Quali sono gli aeroporti (con codice IATA, nome e luogo) nei quali partono voli
-- della compagnia di nome ‘MagicFly’?
select distinct aeroporto.codice, aeroporto.nome, luogoaeroporto.citta	
from luogoaeroporto, aeroporto, arrpart
where arrpart.comp = 'MagicFly'
and aeroporto.codice = luogoaeroporto.aeroporto
and arrpart.partenza = aeroporto.codice;

-- 9. Quali sono i voli che partono da un qualunque aeroporto della città di ‘Roma’ e
-- atterrano ad un qualunque aeroporto della città di ‘New York’? Restituire: codice
-- del volo, nome della compagnia, e aeroporti di partenza e arrivo.
select arrpart.codice, arrpart.comp, arrpart.partenza, arrpart.arrivo
from arrpart
where arrpart.partenza in ('FCO', 'CIA') 
and arrpart.arrivo = 'JFK'

-- 10. Quali sono i possibili piani di volo con esattamente un cambio (utilizzando solo
-- voli della stessa compagnia) da un qualunque aeroporto della città di ‘Roma’ ad un
-- qualunque aeroporto della città di ‘New York’? Restituire: nome della compagnia,
-- codici dei voli, e aeroporti di partenza, scalo e arrivo.

select ap1.comp, ap1.codice as codice_volo1, ap1.partenza as partenza, ap1.arrivo as scalo, ap2.codice as codice_volo2, ap2 as arrivo
from arrpart as ap1, arrpart as ap2
where (ap1.partenza = 'CIA' or ap1.partenza = 'FCO')
and ap1.arrivo = ap2.partenza
and ap1.comp = ap2.comp
and ap2.arrivo = 'JFK'
-- 11. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’, atterrano all’aeroporto ‘JFK’, e di cui si conosce l’anno di fondazione?

select comp
from arrpart, compagnia
where arrpart.partenza = 'FCO'
and  arrpart.arrivo = 'JFK'
and compagnia.anno_fondazione is not null

-- esercizi fatti in classe


select count(*)
from volo,luogoaeroporto, arrpart
where volo.durataminuti >= 180
and luogoaeroporto.aeroporto = arrpart.partenza
and luogoaeroporto.citta = 'Roma'
and volo.codice = arrpart.codice


select round(avg(durataminuti), 2)
from volo
where comp = 'Apitalia';