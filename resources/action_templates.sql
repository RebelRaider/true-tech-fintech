--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2 (Debian 16.2-1.pgdg120+2)
-- Dumped by pg_dump version 16.2 (Ubuntu 16.2-1.pgdg22.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: action_template; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.action_template (
    id uuid NOT NULL,
    is_head boolean NOT NULL,
    name character varying NOT NULL,
    path public.ltree NOT NULL,
    import_path character varying,
    import_func character varying
);


ALTER TABLE public.action_template OWNER TO postgres;

--
-- Data for Name: action_template; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.action_template (id, is_head, name, path, import_path, import_func) FROM stdin;
54006a24-f039-4478-bc91-eb3dc8bf7429	t	узнать баланс	54006a24.f039.4478.bc91.eb3dc8bf7429	action_tasks.bank_account	check_balance
d3bae2a5-a188-4418-a629-4374d7e66d39	f	Назовите счет, баланс, которого вы хотите просмотреть 	54006a24.f039.4478.bc91.eb3dc8bf7429.9b3ff574.5e46.4927.9001.e854da239b91	\N	\N
\.


--
-- Name: action_template action_template_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.action_template
    ADD CONSTRAINT action_template_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

