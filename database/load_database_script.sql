--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: admin; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO admin;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO admin;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: admin; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO admin;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO admin;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: admin; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO admin;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO admin;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: admin; Tablespace: 
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(75) NOT NULL,
    password character varying(128) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    is_superuser boolean NOT NULL,
    last_login timestamp with time zone NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO admin;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: admin; Tablespace: 
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO admin;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO admin;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO admin;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: admin; Tablespace: 
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO admin;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO admin;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: admin; Tablespace: 
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    content_type_id integer,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO admin;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO admin;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: admin; Tablespace: 
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO admin;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO admin;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: admin; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO admin;

--
-- Name: django_site; Type: TABLE; Schema: public; Owner: admin; Tablespace: 
--

CREATE TABLE django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.django_site OWNER TO admin;

--
-- Name: django_site_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE django_site_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_site_id_seq OWNER TO admin;

--
-- Name: django_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE django_site_id_seq OWNED BY django_site.id;


--
-- Name: main_group; Type: TABLE; Schema: public; Owner: admin; Tablespace: 
--

CREATE TABLE main_group (
    id integer NOT NULL,
    name character varying(30) NOT NULL,
    description text NOT NULL,
    logo_url text NOT NULL,
    web_site_url text NOT NULL,
    created date NOT NULL,
    entity_status smallint NOT NULL
);


ALTER TABLE public.main_group OWNER TO admin;

--
-- Name: main_group_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE main_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.main_group_id_seq OWNER TO admin;

--
-- Name: main_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE main_group_id_seq OWNED BY main_group.id;


--
-- Name: main_group_user; Type: TABLE; Schema: public; Owner: admin; Tablespace: 
--

CREATE TABLE main_group_user (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL,
    role_id integer NOT NULL
);


ALTER TABLE public.main_group_user OWNER TO admin;

--
-- Name: main_group_user_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE main_group_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.main_group_user_id_seq OWNER TO admin;

--
-- Name: main_group_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE main_group_user_id_seq OWNED BY main_group_user.id;


--
-- Name: main_log; Type: TABLE; Schema: public; Owner: admin; Tablespace: 
--

CREATE TABLE main_log (
    id integer NOT NULL,
    activity text NOT NULL,
    "time" smallint NOT NULL,
    date date NOT NULL,
    user_id integer NOT NULL,
    project_id integer NOT NULL,
    group_id integer NOT NULL,
    entity_status smallint NOT NULL
);


ALTER TABLE public.main_log OWNER TO admin;

--
-- Name: main_log_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE main_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.main_log_id_seq OWNER TO admin;

--
-- Name: main_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE main_log_id_seq OWNED BY main_log.id;


--
-- Name: main_permission; Type: TABLE; Schema: public; Owner: admin; Tablespace: 
--

CREATE TABLE main_permission (
    id integer NOT NULL,
    name character varying(10) NOT NULL,
    description character varying(255) NOT NULL,
    entity_status smallint NOT NULL
);


ALTER TABLE public.main_permission OWNER TO admin;

--
-- Name: main_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE main_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.main_permission_id_seq OWNER TO admin;

--
-- Name: main_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE main_permission_id_seq OWNED BY main_permission.id;


--
-- Name: main_permission_roles; Type: TABLE; Schema: public; Owner: admin; Tablespace: 
--

CREATE TABLE main_permission_roles (
    id integer NOT NULL,
    permission_id integer NOT NULL,
    role_id integer NOT NULL
);


ALTER TABLE public.main_permission_roles OWNER TO admin;

--
-- Name: main_permission_roles_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE main_permission_roles_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.main_permission_roles_id_seq OWNER TO admin;

--
-- Name: main_permission_roles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE main_permission_roles_id_seq OWNED BY main_permission_roles.id;


--
-- Name: main_project; Type: TABLE; Schema: public; Owner: admin; Tablespace: 
--

CREATE TABLE main_project (
    id integer NOT NULL,
    name character varying(30) NOT NULL,
    description text NOT NULL,
    created date NOT NULL,
    entity_status smallint NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.main_project OWNER TO admin;

--
-- Name: main_project_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE main_project_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.main_project_id_seq OWNER TO admin;

--
-- Name: main_project_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE main_project_id_seq OWNED BY main_project.id;


--
-- Name: main_project_user; Type: TABLE; Schema: public; Owner: admin; Tablespace: 
--

CREATE TABLE main_project_user (
    id integer NOT NULL,
    user_id integer NOT NULL,
    project_id integer NOT NULL,
    role_id integer NOT NULL
);


ALTER TABLE public.main_project_user OWNER TO admin;

--
-- Name: main_project_user_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE main_project_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.main_project_user_id_seq OWNER TO admin;

--
-- Name: main_project_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE main_project_user_id_seq OWNED BY main_project_user.id;


--
-- Name: main_role; Type: TABLE; Schema: public; Owner: admin; Tablespace: 
--

CREATE TABLE main_role (
    id integer NOT NULL,
    name character varying(10) NOT NULL,
    description character varying(255) NOT NULL,
    entity_status smallint NOT NULL
);


ALTER TABLE public.main_role OWNER TO admin;

--
-- Name: main_role_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE main_role_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.main_role_id_seq OWNER TO admin;

--
-- Name: main_role_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE main_role_id_seq OWNED BY main_role.id;


--
-- Name: main_user; Type: TABLE; Schema: public; Owner: admin; Tablespace: 
--

CREATE TABLE main_user (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    email character varying(50) NOT NULL,
    password character varying(40) NOT NULL,
    entity_status smallint DEFAULT 0 NOT NULL,
    session_key character varying(50)
);


ALTER TABLE public.main_user OWNER TO admin;

--
-- Name: main_user_forgot_password; Type: TABLE; Schema: public; Owner: admin; Tablespace: 
--

CREATE TABLE main_user_forgot_password (
    id integer NOT NULL,
    user_id integer NOT NULL,
    token character varying(128) NOT NULL
);


ALTER TABLE public.main_user_forgot_password OWNER TO admin;

--
-- Name: main_user_forgot_password_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE main_user_forgot_password_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.main_user_forgot_password_id_seq OWNER TO admin;

--
-- Name: main_user_forgot_password_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE main_user_forgot_password_id_seq OWNED BY main_user_forgot_password.id;


--
-- Name: main_user_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE main_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.main_user_id_seq OWNER TO admin;

--
-- Name: main_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE main_user_id_seq OWNED BY main_user.id;


--
-- Name: tastypie_apiaccess; Type: TABLE; Schema: public; Owner: admin; Tablespace: 
--

CREATE TABLE tastypie_apiaccess (
    id integer NOT NULL,
    identifier character varying(255) NOT NULL,
    url character varying(255) NOT NULL,
    request_method character varying(10) NOT NULL,
    accessed integer NOT NULL,
    CONSTRAINT tastypie_apiaccess_accessed_check CHECK ((accessed >= 0))
);


ALTER TABLE public.tastypie_apiaccess OWNER TO admin;

--
-- Name: tastypie_apiaccess_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE tastypie_apiaccess_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tastypie_apiaccess_id_seq OWNER TO admin;

--
-- Name: tastypie_apiaccess_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE tastypie_apiaccess_id_seq OWNED BY tastypie_apiaccess.id;


--
-- Name: tastypie_apikey; Type: TABLE; Schema: public; Owner: admin; Tablespace: 
--

CREATE TABLE tastypie_apikey (
    id integer NOT NULL,
    user_id integer NOT NULL,
    key character varying(256) NOT NULL,
    created timestamp with time zone NOT NULL
);


ALTER TABLE public.tastypie_apikey OWNER TO admin;

--
-- Name: tastypie_apikey_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE tastypie_apikey_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tastypie_apikey_id_seq OWNER TO admin;

--
-- Name: tastypie_apikey_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE tastypie_apikey_id_seq OWNED BY tastypie_apikey.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY django_site ALTER COLUMN id SET DEFAULT nextval('django_site_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY main_group ALTER COLUMN id SET DEFAULT nextval('main_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY main_group_user ALTER COLUMN id SET DEFAULT nextval('main_group_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY main_log ALTER COLUMN id SET DEFAULT nextval('main_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY main_permission ALTER COLUMN id SET DEFAULT nextval('main_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY main_permission_roles ALTER COLUMN id SET DEFAULT nextval('main_permission_roles_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY main_project ALTER COLUMN id SET DEFAULT nextval('main_project_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY main_project_user ALTER COLUMN id SET DEFAULT nextval('main_project_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY main_role ALTER COLUMN id SET DEFAULT nextval('main_role_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY main_user ALTER COLUMN id SET DEFAULT nextval('main_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY main_user_forgot_password ALTER COLUMN id SET DEFAULT nextval('main_user_forgot_password_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY tastypie_apiaccess ALTER COLUMN id SET DEFAULT nextval('tastypie_apiaccess_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY tastypie_apikey ALTER COLUMN id SET DEFAULT nextval('tastypie_apikey_id_seq'::regclass);


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_key; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_group_id_key; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_model_key; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_key UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- Name: main_group_pkey; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY main_group
    ADD CONSTRAINT main_group_pkey PRIMARY KEY (id);


--
-- Name: main_group_user_pkey; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY main_group_user
    ADD CONSTRAINT main_group_user_pkey PRIMARY KEY (id);


--
-- Name: main_log_pkey; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY main_log
    ADD CONSTRAINT main_log_pkey PRIMARY KEY (id);


--
-- Name: main_permission_name_key; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY main_permission
    ADD CONSTRAINT main_permission_name_key UNIQUE (name);


--
-- Name: main_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY main_permission
    ADD CONSTRAINT main_permission_pkey PRIMARY KEY (id);


--
-- Name: main_permission_roles_permission_id_role_id_key; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY main_permission_roles
    ADD CONSTRAINT main_permission_roles_permission_id_role_id_key UNIQUE (permission_id, role_id);


--
-- Name: main_permission_roles_pkey; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY main_permission_roles
    ADD CONSTRAINT main_permission_roles_pkey PRIMARY KEY (id);


--
-- Name: main_project_pkey; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY main_project
    ADD CONSTRAINT main_project_pkey PRIMARY KEY (id);


--
-- Name: main_project_user_pkey; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY main_project_user
    ADD CONSTRAINT main_project_user_pkey PRIMARY KEY (id);


--
-- Name: main_role_name_key; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY main_role
    ADD CONSTRAINT main_role_name_key UNIQUE (name);


--
-- Name: main_role_pkey; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY main_role
    ADD CONSTRAINT main_role_pkey PRIMARY KEY (id);


--
-- Name: main_user_email_key; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY main_user
    ADD CONSTRAINT main_user_email_key UNIQUE (email);


--
-- Name: main_user_forgot_password_pkey; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY main_user_forgot_password
    ADD CONSTRAINT main_user_forgot_password_pkey PRIMARY KEY (id);


--
-- Name: main_user_pkey; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY main_user
    ADD CONSTRAINT main_user_pkey PRIMARY KEY (id);


--
-- Name: tastypie_apiaccess_pkey; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY tastypie_apiaccess
    ADD CONSTRAINT tastypie_apiaccess_pkey PRIMARY KEY (id);


--
-- Name: tastypie_apikey_pkey; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY tastypie_apikey
    ADD CONSTRAINT tastypie_apikey_pkey PRIMARY KEY (id);


--
-- Name: tastypie_apikey_user_id_key; Type: CONSTRAINT; Schema: public; Owner: admin; Tablespace: 
--

ALTER TABLE ONLY tastypie_apikey
    ADD CONSTRAINT tastypie_apikey_user_id_key UNIQUE (user_id);


--
-- Name: auth_group_permissions_group_id; Type: INDEX; Schema: public; Owner: admin; Tablespace: 
--

CREATE INDEX auth_group_permissions_group_id ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id; Type: INDEX; Schema: public; Owner: admin; Tablespace: 
--

CREATE INDEX auth_group_permissions_permission_id ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id; Type: INDEX; Schema: public; Owner: admin; Tablespace: 
--

CREATE INDEX auth_permission_content_type_id ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id; Type: INDEX; Schema: public; Owner: admin; Tablespace: 
--

CREATE INDEX auth_user_groups_group_id ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id; Type: INDEX; Schema: public; Owner: admin; Tablespace: 
--

CREATE INDEX auth_user_groups_user_id ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id; Type: INDEX; Schema: public; Owner: admin; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_permission_id ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id; Type: INDEX; Schema: public; Owner: admin; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_user_id ON auth_user_user_permissions USING btree (user_id);


--
-- Name: django_admin_log_content_type_id; Type: INDEX; Schema: public; Owner: admin; Tablespace: 
--

CREATE INDEX django_admin_log_content_type_id ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id; Type: INDEX; Schema: public; Owner: admin; Tablespace: 
--

CREATE INDEX django_admin_log_user_id ON django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date; Type: INDEX; Schema: public; Owner: admin; Tablespace: 
--

CREATE INDEX django_session_expire_date ON django_session USING btree (expire_date);


--
-- Name: main_group_user_group_id; Type: INDEX; Schema: public; Owner: admin; Tablespace: 
--

CREATE INDEX main_group_user_group_id ON main_group_user USING btree (group_id);


--
-- Name: main_group_user_role_id; Type: INDEX; Schema: public; Owner: admin; Tablespace: 
--

CREATE INDEX main_group_user_role_id ON main_group_user USING btree (role_id);


--
-- Name: main_group_user_user_id; Type: INDEX; Schema: public; Owner: admin; Tablespace: 
--

CREATE INDEX main_group_user_user_id ON main_group_user USING btree (user_id);


--
-- Name: main_log_group_id; Type: INDEX; Schema: public; Owner: admin; Tablespace: 
--

CREATE INDEX main_log_group_id ON main_log USING btree (group_id);


--
-- Name: main_log_project_id; Type: INDEX; Schema: public; Owner: admin; Tablespace: 
--

CREATE INDEX main_log_project_id ON main_log USING btree (project_id);


--
-- Name: main_log_user_id; Type: INDEX; Schema: public; Owner: admin; Tablespace: 
--

CREATE INDEX main_log_user_id ON main_log USING btree (user_id);


--
-- Name: main_permission_roles_permission_id; Type: INDEX; Schema: public; Owner: admin; Tablespace: 
--

CREATE INDEX main_permission_roles_permission_id ON main_permission_roles USING btree (permission_id);


--
-- Name: main_permission_roles_role_id; Type: INDEX; Schema: public; Owner: admin; Tablespace: 
--

CREATE INDEX main_permission_roles_role_id ON main_permission_roles USING btree (role_id);


--
-- Name: main_project_group_id; Type: INDEX; Schema: public; Owner: admin; Tablespace: 
--

CREATE INDEX main_project_group_id ON main_project USING btree (group_id);


--
-- Name: main_project_user_project_id; Type: INDEX; Schema: public; Owner: admin; Tablespace: 
--

CREATE INDEX main_project_user_project_id ON main_project_user USING btree (project_id);


--
-- Name: main_project_user_role_id; Type: INDEX; Schema: public; Owner: admin; Tablespace: 
--

CREATE INDEX main_project_user_role_id ON main_project_user USING btree (role_id);


--
-- Name: main_project_user_user_id; Type: INDEX; Schema: public; Owner: admin; Tablespace: 
--

CREATE INDEX main_project_user_user_id ON main_project_user USING btree (user_id);


--
-- Name: main_user_forgot_password_user_id; Type: INDEX; Schema: public; Owner: admin; Tablespace: 
--

CREATE INDEX main_user_forgot_password_user_id ON main_user_forgot_password USING btree (user_id);


--
-- Name: tastypie_apikey_key; Type: INDEX; Schema: public; Owner: admin; Tablespace: 
--

CREATE INDEX tastypie_apikey_key ON tastypie_apikey USING btree (key);


--
-- Name: tastypie_apikey_key_like; Type: INDEX; Schema: public; Owner: admin; Tablespace: 
--

CREATE INDEX tastypie_apikey_key_like ON tastypie_apikey USING btree (key varchar_pattern_ops);


--
-- Name: auth_group_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_fkey FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: content_type_id_refs_id_728de91f; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT content_type_id_refs_id_728de91f FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_content_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_fkey FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: group_id_refs_id_3cea63fe; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT group_id_refs_id_3cea63fe FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: main_group_user_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY main_group_user
    ADD CONSTRAINT main_group_user_group_id_fkey FOREIGN KEY (group_id) REFERENCES main_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: main_group_user_role_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY main_group_user
    ADD CONSTRAINT main_group_user_role_id_fkey FOREIGN KEY (role_id) REFERENCES main_role(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: main_group_user_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY main_group_user
    ADD CONSTRAINT main_group_user_user_id_fkey FOREIGN KEY (user_id) REFERENCES main_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: main_log_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY main_log
    ADD CONSTRAINT main_log_group_id_fkey FOREIGN KEY (group_id) REFERENCES main_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: main_log_project_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY main_log
    ADD CONSTRAINT main_log_project_id_fkey FOREIGN KEY (project_id) REFERENCES main_project(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: main_log_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY main_log
    ADD CONSTRAINT main_log_user_id_fkey FOREIGN KEY (user_id) REFERENCES main_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: main_permission_roles_role_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY main_permission_roles
    ADD CONSTRAINT main_permission_roles_role_id_fkey FOREIGN KEY (role_id) REFERENCES main_role(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: main_project_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY main_project
    ADD CONSTRAINT main_project_group_id_fkey FOREIGN KEY (group_id) REFERENCES main_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: main_project_user_project_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY main_project_user
    ADD CONSTRAINT main_project_user_project_id_fkey FOREIGN KEY (project_id) REFERENCES main_project(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: main_project_user_role_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY main_project_user
    ADD CONSTRAINT main_project_user_role_id_fkey FOREIGN KEY (role_id) REFERENCES main_role(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: main_project_user_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY main_project_user
    ADD CONSTRAINT main_project_user_user_id_fkey FOREIGN KEY (user_id) REFERENCES main_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: main_user_forgot_password_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY main_user_forgot_password
    ADD CONSTRAINT main_user_forgot_password_user_id_fkey FOREIGN KEY (user_id) REFERENCES main_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: permission_id_refs_id_6ceb9b3; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY main_permission_roles
    ADD CONSTRAINT permission_id_refs_id_6ceb9b3 FOREIGN KEY (permission_id) REFERENCES main_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tastypie_apikey_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY tastypie_apikey
    ADD CONSTRAINT tastypie_apikey_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_7ceef80f; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT user_id_refs_id_7ceef80f FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_dfbab7d; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT user_id_refs_id_dfbab7d FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

--
-- Add basic data
--

INSERT INTO main_role(
            id, name, description, entity_status)
    VALUES 
    (1, 'admin', 'Administrator role', 0),
    (2, 'dev', 'Developer role', 0),
    (3, 'qa', 'Quality Assurance role', 0);    

INSERT INTO main_permission(
            id, name, description, entity_status)
    VALUES 
    (1, 'read/write', '', 0),
    (2, 'readonly', '', 0);

INSERT INTO main_permission_roles(
            id, permission_id, role_id)
    VALUES
    (1, 1, 1),
    (2, 2, 2),
    (3, 2, 3);