CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS embeddings (
  id SERIAL,
  embedding vector(4096),
  text text,
  created_at timestamptz DEFAULT now(),
  PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS competence (
  id SERIAL,
  name text,
  description text,
  embedding_id SERIAL,
  PRIMARY KEY(id),
  FOREIGN KEY(id) REFERENCES embeddings(id)
);

CREATE TABLE IF NOT EXISTS auth_user (
  id SERIAL,
  username text,
  PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS user_competence (
  id_u SERIAL REFERENCES auth_user(id),
  id_c SERIAL REFERENCES competence(id),
  PRIMARY KEY(id_u, id_c)
);