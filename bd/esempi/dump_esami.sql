--
-- PostgreSQL database dump
--

-- Dumped from database version 17.3
-- Dumped by pg_dump version 17.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: varchar_not_null; Type: DOMAIN; Schema: public; Owner: postgres
--

CREATE DOMAIN public.varchar_not_null AS character varying
	CONSTRAINT varchar_not_nul_check CHECK ((VALUE IS NOT NULL));


ALTER DOMAIN public.varchar_not_null OWNER TO postgres;

--
-- Name: indirizzo; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.indirizzo AS (
	via public.varchar_not_null,
	civico public.varchar_not_null,
	cap character(5)
);


ALTER TYPE public.indirizzo OWNER TO postgres;

--
-- Name: intgez; Type: DOMAIN; Schema: public; Owner: postgres
--

CREATE DOMAIN public.intgez AS integer
	CONSTRAINT intgez_check CHECK ((VALUE >= 0));


ALTER DOMAIN public.intgez OWNER TO postgres;

--
-- Name: intgz; Type: DOMAIN; Schema: public; Owner: postgres
--

CREATE DOMAIN public.intgz AS integer
	CONSTRAINT intgz_check CHECK ((VALUE > 0));


ALTER DOMAIN public.intgz OWNER TO postgres;

--
-- Name: stringa; Type: DOMAIN; Schema: public; Owner: postgres
--

CREATE DOMAIN public.stringa AS character varying;


ALTER DOMAIN public.stringa OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: corso; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.corso (
    nome character varying NOT NULL,
    crediti public.intgz NOT NULL
);


ALTER TABLE public.corso OWNER TO postgres;

--
-- Name: esame; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.esame (
    studente integer NOT NULL,
    corso character varying NOT NULL,
    data date NOT NULL,
    voto integer NOT NULL,
    lode boolean NOT NULL,
    CONSTRAINT esame_check CHECK (((lode = false) OR (voto = 30))),
    CONSTRAINT esame_voto_check CHECK ((voto >= 18))
);


ALTER TABLE public.esame OWNER TO postgres;

--
-- Name: studente; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.studente (
    matricola integer NOT NULL,
    nome character varying(100) NOT NULL
);


ALTER TABLE public.studente OWNER TO postgres;

--
-- Data for Name: corso; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.corso (nome, crediti) FROM stdin;
\.


--
-- Data for Name: esame; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.esame (studente, corso, data, voto, lode) FROM stdin;
\.


--
-- Data for Name: studente; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.studente (matricola, nome) FROM stdin;
234	Lorenzo
\.


--
-- Name: corso corso_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.corso
    ADD CONSTRAINT corso_pkey PRIMARY KEY (nome);


--
-- Name: esame esame_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.esame
    ADD CONSTRAINT esame_pkey PRIMARY KEY (studente, corso);


--
-- Name: studente studente_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.studente
    ADD CONSTRAINT studente_pkey PRIMARY KEY (matricola);


--
-- Name: esame esame_corso_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.esame
    ADD CONSTRAINT esame_corso_fkey FOREIGN KEY (corso) REFERENCES public.corso(nome);


--
-- Name: esame esame_studente_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.esame
    ADD CONSTRAINT esame_studente_fkey FOREIGN KEY (studente) REFERENCES public.studente(matricola);


--
-- PostgreSQL database dump complete
--

