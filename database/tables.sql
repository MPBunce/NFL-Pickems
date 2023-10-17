CREATE TABLE public."users-regular-season-picks" (
  "pickId" integer NOT NULL,
  "userId" integer NULL,
  year integer NULL,
  team_name character varying NULL,
  team_division character varying NULL,
  division_position integer NULL
);
ALTER TABLE public."users-regular-season-picks" ADD CONSTRAINT "users-regular-season-picks_pkey" PRIMARY KEY (pickId);


CREATE TABLE public."users" (
  id integer NOT NULL,
  username character varying NULL,
  email character varying NULL,
  hashed_password character varying NULL
);
ALTER TABLE public.users ADD CONSTRAINT users_pkey PRIMARY KEY (id);


CREATE TABLE public."nfl-seasons" (
  id integer NOT NULL,
  team_name character varying(255) NOT NULL,
  wins integer NULL,
  losses integer NULL,
  ties integer NULL,
  team_division character varying(255) NULL,
  year integer NULL,
  divisional_position integer NULL
);
ALTER TABLE public."nfl-seasons" ADD CONSTRAINT "nfl-seasons_pkey" PRIMARY KEY (id);


CREATE TABLE public."users-scores" (
  id integer NOT NULL,
  username character varying NULL,
  year integer NULL,
  regular_season_score integer NULL,
  playoff_score integer NULL
);
ALTER TABLE public."users-scores" ADD CONSTRAINT "users-scores_pkey" PRIMARY KEY (id);